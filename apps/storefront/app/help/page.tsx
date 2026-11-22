import type { Metadata } from 'next';
import Link from 'next/link';
import { ArrowRight, CreditCard, Mail, RotateCcw, Shield, Truck, UserRound } from 'lucide-react';
import { ServiceCrumbs } from '../../features/support/service-crumbs';
import { helpTopics, topicKeys } from '../../features/support/help-topics';
import '../../features/support/service.css';

export const metadata: Metadata = { title: 'Customer care', description: 'Find help with Silver Medical demo orders, tracking, returns and accounts.', alternates: { canonical: '/help' } };
const icons = { delivery: Truck, returns: RotateCcw, contact: Mail, privacy: Shield, terms: CreditCard };
export default function HelpPage() {
  return <main className="se-service-shell" id="main">
    <ServiceCrumbs title="Customer care"/>
    <header className="se-care-header">
      <div><h1>Customer <em>care.</em></h1><p>Help with the details of your order, from choosing a delivery option to following a return.</p>
        <Link href="/track" className="se-arrow-link">Track an order <ArrowRight size={17}/></Link></div>
      <img src="/images/banners/clinical-workspace-desktop.webp" width={1008} height={584} alt=""/>
    </header>
    <section aria-label="Help topics" className="se-help-topics">
      {topicKeys.map(key => { const item = helpTopics[key]; const Icon = icons[key]; return <Link key={key} href={'/help/' + key}>
        <Icon size={24} strokeWidth={1.5} aria-hidden/><h2>{item.title}</h2><p>{item.summary}</p><ArrowRight size={17} aria-hidden/></Link>; })}
      <Link href="/account"><UserRound size={24} strokeWidth={1.5} aria-hidden/><h2>Your account</h2><p>Manage a profile, address book, order history and professional application.</p><ArrowRight size={17} aria-hidden/></Link>
    </section>
  </main>;
}
