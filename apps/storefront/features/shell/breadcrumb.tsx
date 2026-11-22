import Link from 'next/link';

export function StoreBreadcrumb({ current, parent }: { current: string; parent?: { title: string; href: string } }) {
  return <nav className="store-crumb" aria-label="Breadcrumb"><Link href="/">Home</Link><span aria-hidden>/</span>{parent && <><Link href={parent.href}>{parent.title}</Link><span aria-hidden>/</span></>}<span aria-current="page">{current}</span></nav>;
}

