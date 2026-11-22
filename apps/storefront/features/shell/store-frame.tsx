'use client';

import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { Heart, Palette, ShoppingBag, UserRound } from 'lucide-react';
import type { ReactNode } from 'react';
import { BrandLogo } from '@silver-medical/ui/brand';
import { SearchField } from '@silver-medical/ui/controls';
import { DepartmentMenu } from './department-menu';
import { useShop } from '../shop/shop-provider';
import '../home/storefront.css';
import './shell.css';

function Header() {
  const router = useRouter();
  const pathname = usePathname();
  const { cart } = useShop();
  const count = Object.values(cart).reduce((total, n) => total + n, 0);
  return <header className="edit-header">
    <div className="edit-utility"><div className="edit-shell">
      <nav className="edit-preview-links" aria-label="Client preview">
        <Link href="/demo" className="sm-demo-entry">Demo store<span className="edit-wide"> · Try a purchase</span></Link>
        <Link href="/design-system" className="edit-design-link"><Palette size={15} aria-hidden="true"/>Design system</Link>
      </nav>
      <div><Link href="/track">Track an order</Link><span>UK · GBP £</span></div>
    </div></div>
    <div className="edit-shell edit-masthead">
      <Link href="/" aria-label="Silver Medical home"><BrandLogo variant="reversed" size={182} /></Link>
      <div className="edit-header-search"><SearchField key={pathname} label="Search the catalogue" hideLabel placeholder="Search products or SKU"
        onSearch={q => router.push(q.trim() ? '/shop?q=' + encodeURIComponent(q.trim()) : '/shop')} /></div>
      <nav className="edit-header-actions" aria-label="Your shopping">
        <Link href="/account" aria-label="Your account"><UserRound aria-hidden="true" size={19}/><span className="edit-wide">Account</span></Link>
        <Link href="/saved" aria-label="Saved products"><Heart aria-hidden="true" size={19}/><span className="edit-wide">Saved</span></Link>
        <Link href="/cart" aria-label={'Basket, ' + count + (count === 1 ? ' item' : ' items')}><ShoppingBag aria-hidden="true" size={19}/><span className="edit-wide">Basket</span><span className="edit-count">{count}</span></Link>
      </nav>
    </div>
    <div className="edit-nav"><div className="edit-shell">
      <DepartmentMenu key={pathname}/>
      <nav aria-label="Main navigation"><Link href="/shop">Shop all</Link><Link href="/#browse">Collections</Link><Link href="/journal">Buying guides</Link><Link href="/help">Help &amp; delivery</Link></nav>
      <Link href="/track" className="edit-nav-help">Order tracking</Link>
    </div></div>
  </header>;
}

const footerColumns = [
  { title: 'Explore', links: [['Shop all', '/shop'], ['Departments', '/departments'], ['Buying guides', '/journal'], ['Store demo', '/demo']] },
  { title: 'Your orders', links: [['Account', '/account'], ['Saved products', '/saved'], ['Basket', '/cart'], ['Track an order', '/track']] },
  { title: 'Customer care', links: [['Help centre', '/help'], ['Delivery', '/help/delivery'], ['Returns', '/help/returns'], ['Contact', '/help/contact']] },
];

function Footer() {
  return <footer className="edit-footer"><div className="edit-shell edit-footer__main">
    <div><Link href="/" aria-label="Silver Medical home"><BrandLogo variant="reversed" size={175}/></Link><p>Medical supplies and equipment.<br/>Thoughtfully brought together.</p><span>silvermedical.co.uk</span></div>
    {footerColumns.map(group => <div key={group.title}><h2>{group.title}</h2>{group.links.map(([label, href]) => <Link key={href} href={href}>{label}</Link>)}</div>)}
  </div><div className="edit-shell edit-footer__legal"><span>© Silver Medical UK</span><Link href="/help/privacy">Privacy</Link><Link href="/help/terms">Terms</Link><Link href="/cookies">Cookie preferences</Link><Link href="/design-system">Design system</Link><a href="#store-top">Back to top</a></div></footer>;
}

export function StoreFrame({ children }: { children: ReactNode }) {
  const path = usePathname();
  if (path?.startsWith('/design-system')) return children;
  return <div id="store-top"><a className="edit-skip" href="#main">Skip to content</a><Header/>{children}<Footer/></div>;
}

