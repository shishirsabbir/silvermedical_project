import { notFound } from 'next/navigation';
import Link from 'next/link';
import { guides } from '../../../features/home/guides';
import { StoreBreadcrumb } from '../../../features/shell/breadcrumb';

type Props = { params: Promise<{ slug: string }> };
export const dynamicParams = false;
export function generateStaticParams() { return guides.map(g => ({ slug: g.id })); }
export async function generateMetadata({ params }: Props) {
  const { slug } = await params;
  const guide = guides.find(g => g.id === slug);
  if (!guide) notFound();
  return { title: guide.title, description: guide.summary, alternates: { canonical: '/journal/' + guide.id } };
}
export default async function GuidePage({ params }: Props) {
  const { slug } = await params;
  const guide = guides.find(g => g.id === slug);
  if (!guide) notFound();
  return <main id="main" className="store-page store-article"><StoreBreadcrumb current={guide.label} parent={{title:'Journal',href:'/journal'}}/><article>
    <h1>{guide.title}</h1><p className="lede">{guide.summary}</p>
    {guide.sections.map(s => <section key={s.title}><h2>{s.title}</h2><p>{s.body}</p></section>)}
    <Link href="/shop" className="store-action">Explore the catalogue</Link>
  </article></main>;
}

