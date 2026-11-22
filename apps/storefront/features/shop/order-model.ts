import { catalogue } from '../catalogue/catalogue';

export type Delivery = 'standard' | 'express';
export type Payment = 'card' | 'paypal' | 'apple' | 'google' | 'revolut';
export const paymentLabels: Record<Payment, string> = {
  card: 'Demo card', paypal: 'PayPal', apple: 'Apple Pay', google: 'Google Pay', revolut: 'Revolut Pay',
};
export const orderStatusLabels = {
  confirmed: 'Order confirmed', preparing: 'Being prepared', dispatched: 'Dispatched',
  delivered: 'Delivered', 'return-requested': 'Return requested', refunded: 'Refunded',
} as const;
export type OrderStatus = keyof typeof orderStatusLabels;
export interface ShippingDetails {
  name: string; email: string; line1: string; line2: string; city: string; postcode: string;
}
export interface OrderLine {
  id: string; name: string; pack: string; sku: string; quantity: number; unitPence: number; art: number; image?: string;
}
export interface ShopOrder {
  id: string; reference: string; ownerId: string | null; createdAt: string; status: OrderStatus;
  events: { status: OrderStatus; at: string }[]; lines: OrderLine[]; address: ShippingDetails;
  delivery: Delivery; payment: Payment; subtotalPence: number; deliveryPence: number; totalPence: number; vatPence: number;
}
export const sampleAddress: ShippingDetails = {
  name: 'Alex Taylor', email: 'alex@example.test', line1: '14 Example Lane', line2: '', city: 'London', postcode: 'SW1A 1AA',
};
export const sampleOrderId = 'sample-shipment';
export const demoCard = { approved: '4242 4242 4242 4242', declined: '4000 0000 0000 0002', expiry: '12/30', cvc: '123' };
export const deliveryMethods: Record<Delivery, { label: string; estimate: string }> = {
  standard: { label: 'Standard delivery', estimate: '3–5 working days' },
  express: { label: 'Express delivery', estimate: '1–2 working days' },
};
const gbp = new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP' });
export const money = (pence: number) => gbp.format(pence / 100);
export const formatPostcode = (postcode: string) => postcode.toUpperCase().replace(/\s/g, '');
export function deliverablePostcode(value: string) {
  const postcode = formatPostcode(value);
  return !/^(BT|GY|JE|IM)/.test(postcode)
    && /^(?:GIR0AA|(?:[A-PR-UWYZ][0-9][0-9A-HJKPSTUW]?|[A-PR-UWYZ][A-HK-Y][0-9][0-9ABEHMNPRVWXY]?)[0-9][ABD-HJLNP-UW-Z]{2})$/.test(postcode);
}
export function validAddress(value: ShippingDetails) {
  return Boolean(value.name.trim() && value.line1.trim() && value.city.trim() && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.email.trim())
    && deliverablePostcode(value.postcode));
}
export function orderLines(cart: Record<string, number>): OrderLine[] {
  return catalogue.filter(item => cart[item.id] > 0).map(item => ({
    id: item.id, name: item.name, sku: item.sku, unitPence: Math.round(item.price * 100),
    quantity: cart[item.id], pack: item.pack, art: item.art, image: item.image,
  }));
}
export function totals(lines: OrderLine[], delivery: Delivery) {
  const subtotalPence = lines.reduce((sum, item) => sum + item.quantity * item.unitPence, 0);
  const deliveryPence = !lines.length ? 0 : delivery === 'express' ? 695 : subtotalPence >= 5000 ? 0 : 395;
  const totalPence = subtotalPence + deliveryPence;
  // The fixture uses a single illustrative inclusive rate for the entire order.
  return { subtotalPence, deliveryPence, totalPence, vatPence: Math.round(totalPence / 6) };
}
export function basketStamp(cart: Record<string, number>) {
  return JSON.stringify(orderLines(cart).map(line => [line.id, line.quantity, line.unitPence]));
}
export function allowedNext(status: OrderStatus): OrderStatus | undefined {
  const progression: Partial<Record<OrderStatus, OrderStatus>> = {
    confirmed: 'preparing', preparing: 'dispatched', dispatched: 'delivered', delivered: 'return-requested', 'return-requested': 'refunded',
  };
  return progression[status];
}
export function createSampleOrder(): ShopOrder {
  const lines = orderLines({ stethoscope: 1 });
  const ago = (hours: number) => new Date(Date.now() - hours * 3600000).toISOString();
  return { id: sampleOrderId, reference: 'SM-DEMO-2601', ownerId: null, createdAt: ago(48), status: 'dispatched',
    events: [{ status: 'confirmed', at: ago(48) }, { status: 'preparing', at: ago(32) }, { status: 'dispatched', at: ago(8) }],
    lines, address: { ...sampleAddress }, delivery: 'standard', payment: 'card', ...totals(lines, 'standard') };
}
