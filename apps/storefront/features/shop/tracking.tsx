'use client';

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useEffect, useState, type FormEvent } from 'react';
import { ArrowRight, Box, Check, CheckCircle2, Mail, MapPin, PackageCheck, Printer, RotateCcw, Truck } from 'lucide-react';
import { Button, TextInput } from '@silver-medical/ui/controls';
import { ProductArt } from '@silver-medical/ui/commerce';
import { Finance, JourneyPage, ShopLinkButton, LoadingShop } from './journey-ui';
import {
  allowedNext, deliveryMethods, money, orderStatusLabels, paymentLabels, sampleOrderId, type OrderStatus,
} from './order-model';
import { useShop } from './shop-provider';

const milestones = [
  { id: 'confirmed', Icon: CheckCircle2 }, { id: 'preparing', Icon: Box },
  { id: 'dispatched', Icon: Truck }, { id: 'delivered', Icon: PackageCheck },
] as const;
const statusCopy: Record<OrderStatus, string> = {
  confirmed: 'Your demo order has been received.',
  preparing: 'Your order is being picked and packed.',
  dispatched: 'Your parcel is on its way to the delivery address.',
  delivered: 'Your parcel has reached its destination.',
  'return-requested': 'Your return request has been recorded.',
  refunded: 'Your full demo refund has been recorded.',
};
const day = (iso: string) => new Intl.DateTimeFormat('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }).format(new Date(iso));
export function TrackPage() {
  const shop = useShop(), router = useRouter();
  const [reference, setReference] = useState(''), [postcode, setPostcode] = useState(''), [error, setError] = useState('');
  function lookup(event: FormEvent) {
    event.preventDefault(); const found = shop.trackOrder(reference, postcode);
    if (found) router.push('/orders/' + found.id);
    else setError('No matching order was found on this browser. Check the reference and delivery postcode, or sign in to the account that placed the order.');
  }
  return <JourneyPage label="Track an order" title={<>Track your <em>order.</em></>} intro="Find your receipt, delivery progress and return options.">
    <div className="order-columns order-track">
      <form onSubmit={lookup} className="order-flow order-form"><h2>Find an order</h2>
        <TextInput label="Order reference" required maxLength={30} placeholder="SM-XXXXXXXX" value={reference} onChange={e => setReference(e.target.value.toUpperCase())}/>
        <TextInput label="Delivery postcode" required maxLength={9} placeholder="SW1A 1AA" value={postcode} onChange={e => setPostcode(e.target.value.toUpperCase())}/>
        {error && <p className="order-error" role="alert">{error}</p>}
        <Button type="submit" disabled={!shop.ready}>Track order <ArrowRight size={16} aria-hidden/></Button>
        <p className="order-note">Demo orders are stored on the browser where you placed them.</p>
      </form>
      <aside className="order-sample"><img src="/images/service/parcel.svg" width={560} height={240} alt=""/>
        <div><h2>Follow a sample shipment</h2><p>Explore a parcel in transit and try the delivery and returns updates.</p>
          <ShopLinkButton href={'/orders/' + sampleOrderId} variant="secondary">Explore a sample shipment <ArrowRight size={15} aria-hidden/></ShopLinkButton></div></aside>
    </div>
  </JourneyPage>;
}
export function OrderPage({ id }: { id: string }) {
  const shop = useShop();
  const order = shop.getOrder(id);
  const [returnOpen, setReturnOpen] = useState(false);
  useEffect(() => { if (shop.ready && id === sampleOrderId && !order) shop.openSample(); }, [id, order, shop]);
  if (!shop.ready || (!order && id === sampleOrderId)) return <JourneyPage label="Order details" title="Order details"><LoadingShop/></JourneyPage>;
  if (!order) return <JourneyPage label="Order details" title={<>Find your <em>order.</em></>}>
    <div className="order-empty"><h2>Order unavailable</h2><p>Open the order on the original browser and sign in if you used an account.</p><ShopLinkButton href="/track">Find an order</ShopLinkButton></div></JourneyPage>;
  const next = allowedNext(order.status);
  const nextLabel: Partial<Record<OrderStatus, string>> = { preparing: 'Mark as preparing', dispatched: 'Mark as dispatched', delivered: 'Mark as delivered', refunded: 'Complete demo refund' };
  const refunded = order.status === 'refunded';
  return <JourneyPage label="Order details" title={order.status === 'confirmed' ? <>Order <em>confirmed.</em></> : <>Your <em>delivery.</em></>}>
    <div className="order-receipt">
      <div className="order-print-brand">Silver Medical UK · Demo receipt</div>
      {!shop.storageAvailable && <p className="order-note order-screen-only">Browser storage is unavailable. Print your receipt before reloading or closing this tab.</p>}
      <div className="order-refbar"><div><span>Order reference</span><strong>{order.reference}</strong></div><div><span>Order date</span><strong>{day(order.createdAt)}</strong></div>
        <Button size="sm" variant="secondary" onClick={() => window.print()}><Printer size={16} aria-hidden/>Print receipt</Button></div>
      <div className="order-columns">
        <div className="order-stack">
          <section className="order-flow order-progress"><div className="order-section-bar"><h2>Delivery status</h2><span className="order-status"><i aria-hidden/>{orderStatusLabels[order.status]}</span></div>
            <p aria-live="polite">{statusCopy[order.status]}</p>
            <ol className="order-milestones">{milestones.map(({ id: stage, Icon }) => {
              const event = order.events.find(item => item.status === stage);
              return <li key={stage} data-done={Boolean(event)} aria-current={order.status === stage ? 'step' : undefined}><span><Icon aria-hidden size={18}/></span>
                <div><strong>{orderStatusLabels[stage]}</strong><small>{event ? day(event.at) : 'Upcoming'}</small></div></li>;
            })}</ol>
            {order.events.filter(event => event.status === 'return-requested' || event.status === 'refunded').map(event => <p className="order-return-event" key={event.status}><Check aria-hidden size={15}/>{orderStatusLabels[event.status]} · {day(event.at)}</p>)}
            {next && next !== 'return-requested' && <div className="order-demo-note order-screen-only"><div><strong>Demo tracking controls</strong><p>Advance this local order to its next status.</p></div>
              <Button size="sm" variant="secondary" onClick={() => shop.advanceOrder(id, next)}>{nextLabel[next]}</Button></div>}
            {next === 'return-requested' && <div className="order-return-actions order-screen-only">{returnOpen ? <><p>Request a return for all items in this demo order?</p><div className="order-buttons">
              <Button size="sm" onClick={() => { shop.advanceOrder(id, next); setReturnOpen(false); }}>Confirm return request</Button><Button variant="ghost" size="sm" onClick={() => setReturnOpen(false)}>Keep order</Button></div></> :
              <Button size="sm" variant="secondary" onClick={() => setReturnOpen(true)}><RotateCcw aria-hidden size={15}/>Request a return</Button>}</div>}
          </section>
          <section className="order-flow"><h2>Items ordered</h2><ul className="order-receipt-items">{order.lines.map(line => <li key={line.id}>
            <span className="order-thumb"><ProductArt index={line.art} image={line.image}/></span><div><Link href={'/products/' + line.id}>{line.name}</Link><small>{line.pack} · Qty {line.quantity}</small></div><b>{money(line.unitPence * line.quantity)}</b>
          </li>)}</ul></section>
        </div>
        <aside className="order-summary"><h2>Order totals</h2><Finance {...order}/>
          {refunded && <p className="order-refund">Demo refund <strong>{money(order.totalPence)}</strong></p>}
          <div className="order-destination"><h3><MapPin size={16} aria-hidden/>Delivery</h3><p>{order.address.name}<br/>{order.address.line1}{order.address.line2 && <><br/>{order.address.line2}</>}<br/>{order.address.city}, {order.address.postcode}</p>
            <small>{deliveryMethods[order.delivery].label} · {deliveryMethods[order.delivery].estimate}</small></div>
          <div className="order-destination"><h3>Payment</h3><p>{paymentLabels[order.payment]} · {refunded ? 'Refunded' : 'Demo payment confirmed'}</p></div>
          <Link className="order-textlink order-screen-only" href={'/demo/messages?order=' + encodeURIComponent(order.id)}><Mail size={16} aria-hidden/>Order messages</Link>
        </aside>
      </div>
      <div className="order-buttons order-followup order-screen-only"><ShopLinkButton href="/shop">Continue shopping <ArrowRight aria-hidden size={15}/></ShopLinkButton><ShopLinkButton href="/track" variant="secondary">Track another order</ShopLinkButton></div>
    </div>
  </JourneyPage>;
}
