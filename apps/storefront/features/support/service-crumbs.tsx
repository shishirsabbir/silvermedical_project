import Link from 'next/link';
import { ChevronRight } from 'lucide-react';

export function ServiceCrumbs({ title, inHelp }: { title: string; inHelp?: boolean }) {
  return <nav className="se-crumbs" aria-label="Breadcrumb">
    <Link href="/">Home</Link><ChevronRight size={14} aria-hidden/>
    {inHelp && <><Link href="/help">Customer care</Link><ChevronRight size={14} aria-hidden/></>}
    <span aria-current="page">{title}</span>
  </nav>;
}
