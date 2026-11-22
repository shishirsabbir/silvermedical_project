import Link from 'next/link';
import type { ReactNode } from 'react';
import { ArrowRight, ChevronRight, ShoppingBag } from 'lucide-react';
import { buttonClass, type LinkButtonProps } from '@silver-medical/ui/controls';
import { ProductArt } from '@silver-medical/ui/commerce';
import { deliveryMethods, money, totals, type Delivery, type OrderLine } from './order-model';
import './journey.css';

export function ShopLinkButton({ variant = 'primary', size = 'md', className, ...props }: LinkButtonProps) {
  return <Link {...props} className={buttonClass(variant, size, className)}/>;
}

export function JourneyPage({ label, title, intro, children }: { label: string; title: ReactNode; intro?: string; children: ReactNode }) {
  return <main id="main" className="order-page">
    <div className="order-shell">
      <nav className="order-crumbs" aria-label="Breadcrumb"><Link href="/">Home</Link><ChevronRight size={14} aria-hidden/><span aria-current="page">{label}</span></nav>
      <header className="order-heading"><h1>{title}</h1>{intro && <p>{intro}</p>}</header>
      {children}
    </div>
  </main>;
}
export function EmptyBag({ saved = false }: { saved?: boolean }) {
  return <section className="order-empty"><div className="order-symbol"><ShoppingBag size={30} aria-hidden strokeWidth={1.4}/></div>
    <h2>{saved ? 'Your shortlist starts here.' : 'Your basket is empty.'}</h2>
    <p>{saved ? 'Select the heart on a product to keep your practice essentials together.' : 'Explore the collection and choose the supplies you would like to order.'}</p>
    <ShopLinkButton href="/shop">Explore the catalogue <ArrowRight size={16} aria-hidden/></ShopLinkButton>
  </section>;
}
export function LoadingShop() { return <p role="status" className="order-loading">Loading your shopping details…</p>; }
export function Finance({ subtotalPence, deliveryPence, totalPence, vatPence }: ReturnType<typeof totals>) {
  return <dl className="order-finance">
    <div><dt>Items</dt><dd>{money(subtotalPence)}</dd></div>
    <div><dt>Delivery</dt><dd>{deliveryPence ? money(deliveryPence) : 'Free'}</dd></div>
    <div className="order-total"><dt>Total</dt><dd>{money(totalPence)}</dd></div>
    <div className="order-vat"><dt>Includes illustrative VAT</dt><dd>{money(vatPence)}</dd></div>
  </dl>;
}
export function Summary({ lines, delivery = 'standard', previews, children }: { lines: OrderLine[]; delivery?: Delivery; previews?: boolean; children?: ReactNode }) {
  return <aside className="order-summary" aria-label="Order summary"><h2>Order summary</h2>
    {previews && <ul className="order-mini-lines">{lines.map(line => <li key={line.id}>
      <span className="order-thumb"><ProductArt index={line.art} image={line.image}/></span>
      <span><strong>{line.name}</strong><small>{line.quantity} × {money(line.unitPence)}</small></span>
    </li>)}</ul>}
    <Finance {...totals(lines, delivery)}/>
    <p className="order-note">{deliveryMethods[delivery].label} · {deliveryMethods[delivery].estimate}</p>
    {children}
  </aside>;
}
