import { notFound } from 'next/navigation';
import { sections } from '../library';
import { Examples } from '../examples';

type Params = { params: Promise<{ section: string }> };

export function generateStaticParams() {
  return sections.filter(s => s.slug !== 'overview').map(s => ({ section: s.slug }));
}
export const dynamicParams = false;

export async function generateMetadata({ params }: Params) {
  const { section } = await params;
  const entry = sections.find(s => s.slug === section);
  return { title: entry ? entry.title + ' · Design system' : 'Design system' };
}

export default async function ComponentPage({ params }: Params) {
  const { section } = await params;
  const entry = sections.find(s => s.slug === section && s.slug !== 'overview');
  if (!entry) notFound();
  return <>
    <div className="lib-page-heading"><p className="lib-kicker">{entry.group}</p><h1>{entry.title}</h1><p>{entry.summary}</p></div>
    <Examples section={entry.slug}/>
  </>;
}
