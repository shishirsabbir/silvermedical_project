import type { Metadata } from 'next';
import Link from 'next/link';
import { DepartmentIcon, departmentIcons } from '@silver-medical/ui/icons';
import { Breadcrumbs } from '@silver-medical/ui/navigation';
import { BannerPicture } from '../../features/assets/banner-picture';
import { departmentBanners } from '../../features/assets/banners';
import { BreadcrumbData } from '../../features/catalogue/structured-data';
import '../../features/catalogue/catalogue.css';

export const metadata: Metadata = {
  title: 'Shop by department', description: 'Explore the eight Silver Medical departments, from diagnostics and consumables to laboratory equipment.',
  alternates: { canonical: '/departments' },
};

export default function Page() {
  const trail = [{ label: 'Home', href: '/' }, { label: 'Departments', href: '/departments' }];
  return <main className="cat-page cat-wrap" id="main">
    <Breadcrumbs items={trail} /><BreadcrumbData items={trail} />
    <header className="cat-directory-intro"><p className="cat-kicker">The Silver Edit</p><h1>Shop by department.</h1>
      <p>Find instruments, equipment and everyday supplies for your practice.</p></header>
    <div className="cat-directory-grid">
      {departmentIcons.map(({ id, label }) => {
        const art = departmentBanners.find(item => item.id === id)!;
        return <Link key={id} href={'/departments/' + id}><BannerPicture asset={art} alt="" />
          <span><DepartmentIcon name={id} size={22} />{label}</span></Link>;
      })}
    </div>
  </main>;
}
