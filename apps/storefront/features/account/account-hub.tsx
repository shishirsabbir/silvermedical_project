'use client';

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';
import { ArrowRight, BriefcaseMedical, ChevronRight, LogOut, MapPin, Package, UserRound } from 'lucide-react';
import { Button, StatusMessage } from '@silver-medical/ui/controls';
import { useAccount } from './account-provider';
import { AuthPanel } from './auth-panel';
import { AddressesSection, OrdersSection, ProfessionalSection, ProfileSection } from './account-sections';

const sections = [
  { id: 'profile', label: 'Personal details', icon: UserRound },
  { id: 'orders', label: 'Order history', icon: Package },
  { id: 'addresses', label: 'Address book', icon: MapPin },
  { id: 'professional', label: 'Professional access', icon: BriefcaseMedical },
];
export function AccountHub({ view, returnToCheckout }: { view: string; returnToCheckout: boolean }) {
  const { account, ready, signOut, storageAvailable } = useAccount();
  const router = useRouter();
  const continuingCheckout = ready && Boolean(account) && returnToCheckout;
  useEffect(() => {
    if (continuingCheckout) router.replace('/checkout');
  }, [continuingCheckout, router]);
  const active = sections.some(section => section.id === view) ? view : 'profile';
  return <main id="main" className="se-service-shell">
    <nav className="se-crumbs" aria-label="Breadcrumb"><Link href="/">Home</Link><ChevronRight size={14} aria-hidden/><span aria-current="page">Your account</span></nav>
    <header className="se-service-heading"><h1>Your <em>account.</em></h1>
      <p>{account ? 'Welcome back, ' + account.name + '.' : 'Manage orders, delivery addresses and professional access.'}</p>
    </header>
    {!ready || continuingCheckout ? <p className="se-service-card" role="status">{continuingCheckout ? 'Returning to checkout…' : 'Opening your account…'}</p> : !storageAvailable ?
      <section className="se-service-card"><StatusMessage tone="warning" title="Account storage is unavailable">Enable site storage in this browser to use a demo account. You can still browse and try checkout as a guest.</StatusMessage>
        <p><Link className="se-arrow-link" href={returnToCheckout ? '/checkout' : '/shop'}>{returnToCheckout ? 'Continue to checkout as a guest' : 'Continue shopping as a guest'} <ArrowRight size={16}/></Link></p></section> : !account ?
      <AuthPanel key={view} initialMode={view === 'register' || view === 'reset' ? view : 'signin'} professional={view === 'professional'} returnToCheckout={returnToCheckout}/> :
      <div className="se-account-layout">
        <aside className="se-account-nav"><nav aria-label="Account sections">
          {sections.map(({ id, label, icon: Icon }) => <Link href={'/account?view=' + id} key={id} aria-current={id === active ? 'page' : undefined}><Icon size={18} aria-hidden/>{label}</Link>)}
        </nav><Button variant="ghost" size="sm" onClick={signOut}><LogOut size={17} aria-hidden/> Sign out</Button></aside>
        <div key={account.id + active}>{active === 'profile' ? <ProfileSection account={account}/> : active === 'orders' ? <OrdersSection/> : active === 'addresses' ? <AddressesSection account={account}/> : <ProfessionalSection account={account}/>}</div>
      </div>}
    <p className="se-service-footnote">Account details and verification codes stay in this browser. <Link href="/help/privacy">How the demo uses data <ArrowRight size={14}/></Link></p>
  </main>;
}
