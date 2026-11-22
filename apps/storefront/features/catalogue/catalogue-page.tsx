import Link from 'next/link';
import { ArrowDown, LayoutGrid } from 'lucide-react';
import { Breadcrumbs, type BreadcrumbItem } from '@silver-medical/ui/navigation';
import { DepartmentIcon, departmentIcons, type DepartmentIconId } from '@silver-medical/ui/icons';
import { BannerPicture } from '../assets/banner-picture';
import { collectionBanners, departmentBanners } from '../assets/banners';
import { departmentCopy } from './catalogue';
import { CatalogueResults } from './catalogue-results';
import { parseFilters, type SearchValues } from './filters';
import { BreadcrumbData } from './structured-data';
import './catalogue.css';

export function CataloguePage({ department, values }: { department?: DepartmentIconId; values: SearchValues }) {
  const selected = departmentIcons.find(item => item.id === department);
  const art = departmentBanners.find(item => item.id === department) ?? collectionBanners.workspace;
  const path = selected ? '/departments/' + selected.id : '/shop';
  const trail: BreadcrumbItem[] = [{ label: 'Home', href: '/' }, { label: 'Catalogue', href: '/shop' }];
  if (selected) trail.push({ label: selected.label, href: path });
  return <main id="main" className="cat-page">
    <div className="cat-wrap"><Breadcrumbs items={trail} /></div>
    <BreadcrumbData items={trail} />
    <header className="cat-mast">
      <div className="cat-mast-copy">
        <p className="cat-kicker">{selected ? 'Shop by department' : 'The Silver Edit'}</p>
        <h1>{selected?.label ?? 'The practice catalogue.'}</h1>
        <p>{department ? departmentCopy[department] : 'Explore instruments, equipment and everyday essentials across eight departments.'}</p>
        <a className="cat-jump" href="#catalogue-products">Browse products <ArrowDown size={15} aria-hidden="true" /></a>
      </div>
      <BannerPicture asset={art} priority alt="" />
    </header>
    <div className="cat-wrap cat-layout">
      <aside className="cat-departments">
        <h2>Departments</h2>
        <nav aria-label="Catalogue departments">
          <Link href="/shop" aria-current={!selected ? 'page' : undefined}><LayoutGrid size={20} aria-hidden="true" />All departments</Link>
          {departmentIcons.map(({ id, label }) => <Link href={'/departments/' + id} key={id} aria-current={id === department ? 'page' : undefined}>
            <DepartmentIcon name={id} size={21} />{label}
          </Link>)}
        </nav>
      </aside>
      <CatalogueResults filters={parseFilters(values)} path={path} department={department} />
    </div>
  </main>;
}
