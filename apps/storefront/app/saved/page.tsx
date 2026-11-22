import { BasketPage } from '../../features/shop/basket';

export const metadata = { title: 'Saved products', robots: { index: false, follow: false } };
export default function Page() { return <BasketPage savedOnly/>; }
