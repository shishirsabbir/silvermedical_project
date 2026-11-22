'use client';

import { createContext, useContext, useEffect, useRef, useState, type ReactNode } from 'react';
import { useAccount } from '../account/account-provider';
import { catalogue } from '../catalogue/catalogue';
import {
  allowedNext, basketStamp, createSampleOrder, formatPostcode, orderLines, orderStatusLabels, sampleOrderId, totals, validAddress,
  type Delivery, type OrderStatus, type Payment, type ShippingDetails, type ShopOrder,
} from './order-model';

interface Bag { cart: Record<string, number>; saved: string[] }
interface State { version: 1; bags: Record<string, Bag>; orders: ShopOrder[] }
interface Checkout {
  id: string; basket: string; address: ShippingDetails; delivery: Delivery; payment: Payment;
}
type Outcome = { ok: true; id: string } | { ok: false; error: string };
interface Shop extends Bag {
  ready: boolean; storageAvailable: boolean; professionalApproved: boolean; orders: ShopOrder[];
  addItem: (id: string, quantity?: number) => boolean; setQuantity: (id: string, quantity: number) => void;
  toggleSaved: (id: string) => void; stockFor: (id: string) => number; placeOrder: (input: Checkout) => Promise<Outcome>;
  getOrder: (id: string) => ShopOrder | undefined; trackOrder: (reference: string, postcode: string) => ShopOrder | undefined;
  openSample: () => void; advanceOrder: (id: string, next: OrderStatus) => boolean;
}

const storageKey = 'silver-medical.shop.v1';
const guest = 'guest';
const emptyBag = (): Bag => ({ cart: {}, saved: [] });
const freshState = (): State => ({ version: 1, bags: {}, orders: [] });
const context = createContext<Shop | null>(null);
const knownId = (id: string) => catalogue.some(item => item.id === id);
const isRecord = (value: unknown): value is Record<string, unknown> => Boolean(value && typeof value === 'object' && !Array.isArray(value));
const textField = (value: unknown) => typeof value === 'string';
const count = (value: unknown): value is number => Number.isSafeInteger(value) && Number(value) >= 0;
function validOrder(value: unknown): value is ShopOrder {
  if (!isRecord(value) || !isRecord(value.address) || !Array.isArray(value.lines) || !Array.isArray(value.events)) return false;
  const { address } = value;
  return [value.id, value.reference, value.createdAt].every(textField)
    && Number.isFinite(Date.parse(String(value.createdAt))) && (value.ownerId === null || textField(value.ownerId))
    && ['standard', 'express'].includes(String(value.delivery)) && ['card', 'revolut', 'paypal', 'apple', 'google'].includes(String(value.payment))
    && Object.hasOwn(orderStatusLabels, String(value.status)) && [value.subtotalPence, value.deliveryPence, value.totalPence, value.vatPence].every(count)
    && ['name', 'email', 'line1', 'line2', 'city', 'postcode'].every(key => textField(address[key]))
    && value.lines.length > 0 && value.lines.every(row => isRecord(row) && [row.id, row.sku, row.name, row.pack].every(textField)
      && count(row.art) && count(row.quantity) && row.quantity > 0 && count(row.unitPence) && (!row.image || textField(row.image)))
    && value.events.every(event => isRecord(event) && Object.hasOwn(orderStatusLabels, String(event.status)) && Number.isFinite(Date.parse(String(event.at))));
}
function decode(raw: string | null): State {
  if (!raw) return freshState();
  let value: unknown;
  try { value = JSON.parse(raw); } catch { return freshState(); }
  if (!isRecord(value) || value.version !== 1 || !isRecord(value.bags) || !Array.isArray(value.orders)) return freshState();
  const bags: Record<string, Bag> = {};
  for (const [key, bag] of Object.entries(value.bags)) {
    if ((key !== guest && !key.startsWith('account:')) || !isRecord(bag)) continue;
    const entries = isRecord(bag.cart) ? Object.entries(bag.cart) : [];
    const cart: Record<string, number> = {};
    for (const [id, qty] of entries) if (knownId(id) && count(qty) && qty > 0) cart[id] = Math.min(qty, 99);
    bags[key] = { cart, saved: Array.isArray(bag.saved) ? [...new Set(bag.saved.filter((id): id is string => typeof id === 'string' && knownId(id)))] : [] };
  }
  return { version: 1, bags, orders: value.orders.filter(validOrder) };
}
function remaining(state: State, id: string) {
  const item = catalogue.find(row => row.id === id);
  if (!item) return 0;
  const booked = state.orders.reduce((sum, order) => order.id === sampleOrderId ? sum : sum + (order.lines.find(line => line.id === id)?.quantity ?? 0), 0);
  return Math.max(0, Math.min(99, item.stock - booked));
}
function withBag(state: State, key: string, bag: Bag): State {
  return { ...state, bags: { ...state.bags, [key]: bag } };
}
export function ShopProvider({ children }: { children: ReactNode }) {
  const { account, professionalApproved, ready: accountReady } = useAccount();
  const ownerId = account?.id ?? null;
  const key = ownerId ? 'account:' + ownerId : guest;
  const [state, setState] = useState<State>(freshState);
  const [hydrated, setHydrated] = useState(false);
  const [storageAvailable, setStorageAvailable] = useState(true);
  const volatile = useRef(false);
  const current = useRef(state);
  const mergedOwner = useRef<string | null>(null);
  function read() {
    if (!volatile.current) {
      try { return decode(localStorage.getItem(storageKey)); }
      catch { volatile.current = true; setStorageAvailable(false); }
    }
    return current.current;
  }
  function publish(next: State) {
    current.current = next;
    if (!volatile.current) {
      try { localStorage.setItem(storageKey, JSON.stringify(next)); }
      catch { volatile.current = true; setStorageAvailable(false); }
    }
    setState(next);
  }
  useEffect(() => {
    function refresh() { const latest = read(); current.current = latest; setState(latest); }
    function changed(event: StorageEvent) { if (event.key === storageKey || event.key === null) refresh(); }
    refresh(); setHydrated(true);
    window.addEventListener('storage', changed);
    return () => window.removeEventListener('storage', changed);
  }, []);
  useEffect(() => {
    if (!hydrated || !accountReady) return;
    // A refresh on a signed-in tab must not adopt purchases a guest started in another tab.
    try {
      const marker = storageKey + '.mergedOwner';
      mergedOwner.current = sessionStorage.getItem(marker);
      if (ownerId && mergedOwner.current === ownerId) return;
      if (ownerId) sessionStorage.setItem(marker, ownerId);
      else sessionStorage.removeItem(marker);
    } catch { if (ownerId && mergedOwner.current === ownerId) return; }
    mergedOwner.current = ownerId;
    if (!ownerId) return;
    const data = read();
    const guestBag = data.bags[guest];
    if (!guestBag || (!guestBag.saved.length && !Object.keys(guestBag.cart).length)) return;
    const mine = data.bags[key] ?? emptyBag();
    const cart = { ...mine.cart };
    for (const [id, qty] of Object.entries(guestBag.cart)) {
      const quantity = Math.min(remaining(data, id), (cart[id] ?? 0) + qty);
      if (quantity) cart[id] = quantity;
    }
    publish({ ...data, bags: { ...data.bags, [guest]: emptyBag(), [key]: { cart, saved: [...new Set([...mine.saved, ...guestBag.saved])] } } });
  }, [ownerId, key, hydrated, accountReady]);
  const ready = hydrated && accountReady;
  const bag = state.bags[key] ?? emptyBag();
  function addItem(id: string, quantity = 1) {
    if (!ready || !Number.isInteger(quantity) || quantity <= 0) return false;
    const data = read(), item = catalogue.find(product => product.id === id), active = data.bags[key] ?? emptyBag();
    const after = (active.cart[id] ?? 0) + quantity;
    if (!item || (item.professional && !professionalApproved) || after > remaining(data, id)) return false;
    publish(withBag(data, key, { ...active, cart: { ...active.cart, [id]: after } }));
    return true;
  }
  function setQuantity(id: string, value: number) {
    if (!ready || !Number.isSafeInteger(value) || value < 0) return;
    const data = read(), active = data.bags[key] ?? emptyBag(), cart = { ...active.cart };
    if (!cart[id]) return;
    if (!value) delete cart[id];
    else cart[id] = Math.min(value, remaining(data, id));
    if (!cart[id]) delete cart[id];
    publish(withBag(data, key, { ...active, cart }));
  }
  function toggleSaved(id: string) {
    if (!ready || !knownId(id)) return;
    const data = read(), active = data.bags[key] ?? emptyBag();
    const saved = active.saved.includes(id) ? active.saved.filter(item => item !== id) : [...active.saved, id];
    publish(withBag(data, key, { ...active, saved }));
  }
  const accessible = (order: ShopOrder) => order.ownerId === null || order.ownerId === ownerId;
  async function placeOrder(input: Checkout): Promise<Outcome> {
    function commit(): Outcome {
      const data = read(), active = data.bags[key] ?? emptyBag();
      const previous = data.orders.find(order => order.id === input.id);
      if (previous && accessible(previous)) return { ok: true, id: previous.id };
      if (!ready || !validAddress(input.address)) return { ok: false, error: 'Check the delivery address before placing your order.' };
      const lines = orderLines(active.cart);
      if (!lines.length || basketStamp(active.cart) !== input.basket) return { ok: false, error: 'Your basket changed. Review it again before placing this order.' };
      if (lines.some(line => line.quantity > remaining(data, line.id) || (catalogue.find(item => item.id === line.id)?.professional && !professionalApproved)))
        return { ok: false, error: 'An item is unavailable or requires a professional account. Please update your basket.' };
      const createdAt = new Date().toISOString();
      const order: ShopOrder = { id: input.id, reference: 'SM-' + input.id.slice(0, 8).toUpperCase(), ownerId, createdAt, status: 'confirmed',
        address: { ...input.address }, delivery: input.delivery, payment: input.payment, events: [{ status: 'confirmed', at: createdAt }],
        lines, ...totals(lines, input.delivery) };
      publish({ ...withBag(data, key, { ...active, cart: {} }), orders: [order, ...data.orders] });
      return { ok: true, id: order.id };
    }
    // Serialise commits from two tabs before rechecking the basket and available stock.
    return navigator.locks ? navigator.locks.request(storageKey + '.checkout', commit) : commit();
  }
  function openSample() {
    const data = read();
    if (data.orders.some(order => order.id === sampleOrderId)) return;
    publish({ ...data, orders: [createSampleOrder(), ...data.orders] });
  }
  function advanceOrder(id: string, next: OrderStatus) {
    const data = read(), order = data.orders.find(record => record.id === id && accessible(record));
    if (!order || allowedNext(order.status) !== next) return false;
    publish({ ...data, orders: data.orders.map(record => record.id === id ? { ...order, status: next, events: [...order.events, { status: next, at: new Date().toISOString() }] } : record) });
    return true;
  }
  const value: Shop = { ...bag, ready, storageAvailable, professionalApproved, addItem, setQuantity, toggleSaved, placeOrder, openSample, advanceOrder,
    stockFor: id => remaining(state, id), orders: ownerId ? state.orders.filter(order => order.ownerId === ownerId) : [],
    getOrder: id => state.orders.find(order => order.id === id && accessible(order)),
    trackOrder: (reference, postcode) => state.orders.find(order => accessible(order) && order.reference === reference.trim().toUpperCase() && formatPostcode(order.address.postcode) === formatPostcode(postcode)) };
  return <context.Provider value={value}>{children}</context.Provider>;
}
export function useShop() {
  const shop = useContext(context);
  if (!shop) throw new Error('The shopping routes require ShopProvider.');
  return shop;
}
