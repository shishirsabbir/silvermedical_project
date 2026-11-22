import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { departmentIcons } from '@silver-medical/ui/icons';
import { departmentCopy } from '../../../features/catalogue/catalogue';
import { CataloguePage } from '../../../features/catalogue/catalogue-page';
import type { SearchValues } from '../../../features/catalogue/filters';

type Parameters = { params: Promise<{ slug: string }> };
export const dynamicParams = false;
export const generateStaticParams = () => departmentIcons.map(({ id }) => ({ slug: id }));

async function departmentFor(params: Parameters['params']) {
  const { slug } = await params;
  return departmentIcons.find(item => item.id === slug) ?? notFound();
}

export async function generateMetadata({ params }: Parameters): Promise<Metadata> {
  const { id, label } = await departmentFor(params);
  return {
    title: label + ' supplies', description: departmentCopy[id],
    alternates: { canonical: '/departments/' + id },
    openGraph: { title: label + ' | Silver Medical', description: departmentCopy[id],
      url: '/departments/' + id, images: ['/images/banners/' + id + '-desktop.webp'] },
  };
}

export default async function Page({ params, searchParams }: Parameters & { searchParams: Promise<SearchValues> }) {
  const department = await departmentFor(params);
  return <CataloguePage department={department.id} values={await searchParams} />;
}
