import type { Metadata } from 'next';
import { OrderMessages } from '../../../features/shell/order-messages';
import { StoreBreadcrumb } from '../../../features/shell/breadcrumb';

export const metadata: Metadata = { title: 'Order message previews' };
export default async function MessagesPage({ searchParams }: { searchParams: Promise<{ order?: string | string[] }> }) {
  const query = await searchParams;
  const orderId = typeof query.order === 'string' ? query.order : undefined;
  return <main id="main" className="store-page store-article"><StoreBreadcrumb current="Order messages" parent={{ title:'Store demo', href:'/demo' }}/><h1>Order messages.</h1>
    <p className="lede">{orderId ? 'Updates for this browser order.' : 'Explore a sample confirmation, dispatch update and refund.'} These previews are displayed locally.</p>
    <OrderMessages orderId={orderId}/></main>;
}

