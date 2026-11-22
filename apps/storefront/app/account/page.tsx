import type { Metadata } from 'next';
import { AccountHub } from '../../features/account/account-hub';
import '../../features/support/service.css';

export const metadata: Metadata = { title: 'Your account', description: 'Manage your Silver Medical profile, orders, addresses and professional access.', robots: { index: false, follow: false } };
export default async function AccountPage({ searchParams }: { searchParams: Promise<{ view?: string | string[]; next?: string | string[] }> }) {
  const query = await searchParams;
  return <AccountHub view={typeof query.view === 'string' ? query.view : 'profile'} returnToCheckout={query.next === '/checkout'}/>;
}
