import Link from 'next/link';
import { ArrowRight, CheckCheck, ChevronRight, Layers3, MousePointer2, SlidersHorizontal, PanelsTopLeft, ShoppingBag, Waypoints } from 'lucide-react';
import { sections, sectionPath, type Section } from './library';

export const metadata = { title: 'Design system · The Silver Edit' };

const indexIcons = { actions: MousePointer2, forms: SlidersHorizontal, navigation: Waypoints, overlays: Layers3, feedback: CheckCheck, products: ShoppingBag } as const;

export default function LibraryOverview() {
  return <>
    <section className="lib-cover" aria-labelledby="overview-title">
      <img className="lib-cover-photo" src="/images/editorial.webp" alt="" width="1536" height="1024" fetchPriority="high"/>
      <div className="lib-cover-copy">
        <p className="lib-kicker">Silver Medical design system</p>
        <h1 id="overview-title">The <em>Silver</em> Edit.</h1>
        <p>Deep emerald and silver set the palette. Cormorant Garamond headlines pair with Manrope for product names, prices and controls.</p>
        <Link className="lib-cover-link" href="#component-index">Explore components <ArrowRight size={16} aria-hidden="true"/></Link>
      </div>
    </section>
    <section aria-labelledby="foundations-title" className="lib-overview-section">
      <div className="lib-section-heading"><h2 id="foundations-title">Foundations</h2><Link href="/design-system/assets" className="lib-assets-entry">Browse assets <ArrowRight size={15} aria-hidden="true"/></Link></div>
      <div className="lib-foundations">
        <Link href="/design-system/brand" className="lib-foundation">
          <div className="lib-spectrum" aria-hidden="true"><i/><i/><i/><i/><i/></div>
          <div className="lib-card-foot"><div><h3>Brand &amp; colour</h3><p>Logo artwork and the storefront palette</p></div><ChevronRight size={18} aria-hidden="true"/></div>
        </Link>
        <Link href="/design-system/typography" className="lib-foundation">
          <div className="lib-type-sample" aria-hidden="true"><i>Aa</i><span>Ag</span><small>Cormorant Garamond<br/>Manrope</small></div>
          <div className="lib-card-foot"><div><h3>Type &amp; spacing</h3><p>Type specimens, rhythm and scale</p></div><ChevronRight size={18}/></div>
        </Link>
      </div>
    </section>
    <section id="component-index" aria-labelledby="index-title" className="lib-overview-section">
      <div className="lib-section-heading"><h2 id="index-title">Component index</h2></div>
      <div className="lib-index">{sections.filter(s => s.group !== 'Foundations').map(s => {
        const Icon = indexIcons[s.slug as keyof typeof indexIcons] ?? PanelsTopLeft;
        return <Link href={sectionPath(s.slug as Section)} key={s.slug}><span className="lib-index-icon"><Icon size={19} strokeWidth={1.65}/></span><span><strong>{s.title}</strong><small>{s.summary}</small></span><ChevronRight size={16} aria-hidden="true"/></Link>;
      })}</div>
    </section>
  </>;
}
