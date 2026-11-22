import Link from 'next/link';
import type { Metadata } from 'next';
import { DemoStart } from '../../features/shell/demo-start';
import { StoreBreadcrumb } from '../../features/shell/breadcrumb';
import { WorkflowIcon, type WorkflowIconName } from '../../features/shell/workflow-icon';

export const metadata: Metadata = {
  title: 'Try the store demo', description: 'Explore a sample purchase, demo account and delivery timeline.',
  openGraph: { title: 'From basket to doorstep · The Silver Edit', url:'/demo', images:[{url:'/brand/identity/shopping-demo-social.jpg',width:1200,height:630,alt:'Silver Medical demo store and emerald parcel'}] },
  twitter: { card:'summary_large_image', images:['/brand/identity/shopping-demo-social.jpg'] },
};
const journeys: { icon: WorkflowIconName; title: string; body: string; label: string; href: string }[] = [
  { icon: 'basket', title: 'Build a basket', body: 'Compare packs and prices, save items and set quantities.', label: 'Browse products', href: '/shop' },
  { icon: 'card', title: 'Try a payment', body: 'At checkout, choose a test card or a simulated wallet. Try a decline and retry the same basket.', label: 'Open your basket', href: '/cart' },
  { icon: 'parcel', title: 'Follow a delivery', body: 'Open the sample shipment or find an order you placed. Advance the delivery timeline in demo controls.', label: 'Track an order', href: '/track' },
  { icon: 'account', title: 'Open an account', body: 'Try registration and verification, save an address or request professional access.', label: 'Visit your account', href: '/account' },
  { icon: 'receipt', title: 'Read order updates', body: 'Preview the confirmation, dispatch and refund messages a customer would receive.', label: 'Preview messages', href: '/demo/messages' },
  { icon: 'return', title: 'Try a return', body: 'Use a delivered sample order to request a return and follow the refund.', label: 'See returns', href: '/help/returns' },
];
export default function DemoPage() {
  return <main id="main" className="store-page"><StoreBreadcrumb current="Store demo"/>
    <section className="store-demo-hero"><div><p className="edit-eyebrow">The Silver Edit</p><h1>From basket<br/>to doorstep.</h1><p>Try a complete order with sample details. Orders stay in this browser and payments are simulated.</p><DemoStart/></div>
      <img src="/images/dispatch.webp" alt="An emerald parcel with ivory tissue and a packing insert." width={960} height={720} fetchPriority="high"/></section>
    <section aria-label="Demo journeys" className="store-workflows">{journeys.map(j => <article key={j.icon} className="store-workflow"><WorkflowIcon name={j.icon}/><h2>{j.title}</h2><p>{j.body}</p><Link href={j.href}>{j.label}</Link></article>)}</section>
  </main>;
}

