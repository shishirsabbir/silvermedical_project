'use client';

import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import { ArrowUpRight, BookOpen, ChevronRight, Component, FormInput, Images, Layers3, LayoutDashboard, MousePointer2, PanelTop, Palette, ShoppingBasket, Smartphone, Type, Waypoints } from 'lucide-react';
import { BrandLogo } from '@silver-medical/ui/brand';
import { Button, Select } from '@silver-medical/ui/controls';
import { Dialog } from '@silver-medical/ui/overlays';
import type { ReactNode } from 'react';
import { sections, sectionPath, type Section } from './library';

const icons = { overview: LayoutDashboard, brand: Palette, assets: Images, typography: Type, actions: MousePointer2, forms: FormInput, navigation: Waypoints, overlays: Layers3, feedback: PanelTop, products: ShoppingBasket };

export function LibraryShell({ children }: { children: ReactNode }) {
  const pathname = usePathname();
  const router = useRouter();
  const active = sections.find(({ slug }) => sectionPath(slug) === pathname.replace(/\/$/, '')) ?? sections[0];

  return <div className="lib">
    <a className="lib-skip" href="#library-content">Skip to examples</a>
    <header className="lib-header">
      <div className="lib-header-inner">
        <div className="lib-identity"><Link href="/" aria-label="Silver Medical homepage"><BrandLogo size={171}/></Link><span className="lib-brand-divider" /><Link className="lib-identity-text" href="/design-system">Design system</Link></div>
        <div className="lib-header-tools">
          <Dialog title="Mobile preview" description="Explore the gallery at a phone width of 390 pixels."
            trigger={<Button size="sm" variant="ghost" className="lib-preview-trigger"><Smartphone size={15}/>Mobile preview</Button>}>
            <iframe className="lib-phone-frame" src={sectionPath(active.slug)} title={'Mobile preview of ' + active.title}/>
          </Dialog>
          <Link className="lib-store-link" href="/">View storefront <ArrowUpRight size={15} aria-hidden="true"/></Link>
        </div>
      </div>
    </header>
    <div className="lib-body">
      <aside className="lib-aside">
        <div className="lib-side-inner">
          <span className="lib-subtitle"><BookOpen size={16} aria-hidden="true"/> Library</span>
          <nav aria-label="Design system sections">{['Foundations', 'Components', 'Storefront'].map(group => (
            <div className="lib-nav-group" key={group}>
              <h2>{group}</h2>
              {sections.filter(section => section.group === group).map(({ slug, title }) => {
                const Icon = icons[slug];
                return <Link key={slug} href={sectionPath(slug)} aria-current={active.slug === slug ? 'page' : undefined}>
                  <Icon size={17} strokeWidth={1.6} aria-hidden="true"/>{title}
                </Link>;
              })}
            </div>
          ))}</nav>
        </div>
      </aside>
      <main id="library-content" className="lib-main" tabIndex={-1}>
        <div className="lib-location"><Component size={14} aria-hidden="true"/><Link href="/design-system">Design system</Link><ChevronRight size={13} aria-hidden="true"/><span>{active.title}</span></div>
        <div className="lib-mobile-menu">
          <Select label="Library section" value={active.slug} onChange={e => router.push(sectionPath(e.target.value as Section))} options={sections.map(s => ({ value: s.slug, label: s.title }))}/>
        </div>
        {children}
        <footer className="lib-footer"><span>Silver Medical UK</span><span>The Silver Edit</span></footer>
      </main>
    </div>
  </div>;
}
