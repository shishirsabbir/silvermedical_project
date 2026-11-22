'use client';

import Link from 'next/link';
import { useState } from 'react';
import { Select } from '@silver-medical/ui/controls';
import { useShop } from '../shop/shop-provider';
import { createSampleOrder, deliveryMethods, money } from '../shop/order-model';

const messages = {
  confirmed: { title: 'Order confirmation', subject: 'Your order is confirmed.', lead: 'Your order summary is below. You can follow its progress from your order page.' },
  dispatched: { title: 'Dispatch update', subject: 'Your parcel is on its way.', lead: 'Your parcel has reached the dispatch stage. Open tracking to see the latest delivery update.' },
  refunded: { title: 'Refund confirmation', subject: 'Your refund is recorded.', lead: 'The full demo refund has been recorded against the original order.' },
} as const;
type Message = keyof typeof messages;

export function OrderMessages({ orderId }: { orderId?: string }) {
  const shop = useShop();
  const [choice, setChoice] = useState<Message>('confirmed');
  if (!shop.ready) return <p role="status">Loading order messages…</p>;
  const order = orderId ? shop.getOrder(orderId) : createSampleOrder();
  if (!order) return <p>This order is unavailable in the current session. <Link href="/track">Find an order</Link></p>;
  const available = (Object.keys(messages) as Message[]).filter(key => !orderId || order.events.some(e => e.status === key));
  if (!available.length) return <p>No messages are available for this order yet.</p>;
  const selected = available.includes(choice) ? choice : available[0];
  const message = messages[selected];
  return <div className="store-mail">
    <Select label="Message" value={selected} onChange={e => setChoice(e.target.value as Message)}
      options={available.map(value => ({ value, label: messages[value].title }))}/>
    <article><img className="store-mail-banner" src="/brand/identity/service-email-header.png" width={900} height={150} alt="Silver Medical UK"/>
      <div className="store-mail-body"><p className="edit-eyebrow">{order.reference}</p><h2>{message.subject}</h2><p>{message.lead}</p>
        <ul>{order.lines.map(line => <li key={line.id}><span>{line.name} × {line.quantity}</span><strong>{money(line.unitPence * line.quantity)}</strong></li>)}</ul>
        <p>{deliveryMethods[order.delivery].label} · {money(order.deliveryPence)}</p>
        <p className="store-mail-total"><strong>{selected === 'refunded' ? 'Refund total' : 'Order total'}</strong><strong>{money(order.totalPence)}</strong></p>
        <Link className="store-action" href={orderId ? '/orders/' + encodeURIComponent(order.id) : '/track'}>{orderId ? 'View order and tracking' : 'Try order tracking'}</Link>
      </div></article></div>;
}

