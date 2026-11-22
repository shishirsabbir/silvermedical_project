import type { Metadata } from 'next';
import Link from 'next/link';
import { guides } from '../../features/home/guides';
import { StoreBreadcrumb } from '../../features/shell/breadcrumb';

export const metadata: Metadata = { title: 'Practice journal and buying guides', alternates: { canonical: '/journal' } };
export default function JournalPage() {
  return <main id="main" className="store-page"><StoreBreadcrumb current="Practice journal"/><h1>The practice journal.</h1><p className="lede">Practical buying guides for organising a workspace, comparing pack sizes and planning the next restock.</p>
    <div className="store-guides">{guides.map(g => <article className="store-guide" key={g.id}><p className="edit-eyebrow">{g.label}</p><h2>{g.title}</h2><p>{g.summary}</p><Link href={'/journal/'+g.id} className="store-action" aria-label={'Read ' + g.title}>Read the guide</Link></article>)}</div></main>;
}

