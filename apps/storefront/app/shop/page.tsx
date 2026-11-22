import type { Metadata } from 'next';
import { CataloguePage } from '../../features/catalogue/catalogue-page';
import type { SearchValues } from '../../features/catalogue/filters';

export const metadata: Metadata = {
  title: 'Shop the practice catalogue', description: 'Browse Silver Medical instruments and everyday practice supplies by department, pack, availability and SKU.',
  alternates: { canonical: '/shop' },
};

export default async function Page({ searchParams }: { searchParams: Promise<SearchValues> }) {
  return <CataloguePage values={await searchParams} />;
}
