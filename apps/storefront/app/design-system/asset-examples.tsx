import { ArrowDown, Download, Grid2X2, Heart, List, Search, ShoppingBag, X } from 'lucide-react';
import { BrandLogo, type BrandLogoProps } from '@silver-medical/ui/brand';
import { departmentIcons, DepartmentIcon } from '@silver-medical/ui/icons';
import { BannerBrowser } from './banner-browser';
import './assets.css';

const logoArtwork = [
  { variant: 'light', label: 'Primary wordmark', file: 'silver-medical.svg', size: 157 },
  { variant: 'reversed', label: 'Reversed wordmark', file: 'silver-medical-reversed.svg', size: 157 },
  { variant: 'mark', label: 'Silver emblem', file: 'silver-medical-mark.svg', size: 66 },
  { variant: 'stacked', label: 'Stacked signature', file: 'silver-medical-stacked.svg', size: 88 },
] as const satisfies readonly { variant: BrandLogoProps['variant']; label: string; file: string; size: number }[];

const deviceArtwork = [
  { title: 'Order message header', format: '900 × 150 · PNG', href: '/brand/identity/service-email-header.png' },
  { title: 'Shopping demo sharing card', format: '1200 × 630 · JPEG', href: '/brand/identity/shopping-demo-social.jpg' },
  { title: 'Dispatch photograph', format: '960 × 720 · WebP', href: '/images/dispatch.webp' },
  { title: 'Shopping journey symbols', format: 'Six symbols · SVG sprite', href: '/icons/shopping.svg' },
  { title: 'Scalable favicon', format: 'SVG', href: '/brand/identity/favicon.svg' },
  { title: 'Browser favicon', format: '16, 32, 48 px · ICO', href: '/favicon.ico' },
  { title: 'Apple touch icon', format: '180 × 180 · PNG', href: '/brand/identity/apple-touch-icon.png' },
  { title: 'App icon', format: '192 × 192 · PNG', href: '/brand/identity/app-icon-192.png' },
  { title: 'App icon', format: '512 × 512 · PNG', href: '/brand/identity/app-icon-512.png' },
  { title: 'Maskable app icon', format: '512 × 512 · PNG', href: '/brand/identity/app-icon-maskable-512.png' },
  { title: 'Web app manifest', format: 'Webmanifest', href: '/manifest.webmanifest' },
];

const interfaceIcons = [
  { label: 'Search', Icon: Search }, { label: 'Saved', Icon: Heart },
  { label: 'Basket', Icon: ShoppingBag }, { label: 'Grid view', Icon: Grid2X2 },
  { label: 'List view', Icon: List }, { label: 'Close', Icon: X },
];

export function AssetExamples() {
  return <>
    <nav className="asset-jump" aria-label="Asset types">
      <a href="#banners">Banners <ArrowDown aria-hidden="true" size={13} /></a>
      <a href="#department-icons">Department icons <ArrowDown aria-hidden="true" size={13} /></a>
      <a href="#brand-exports">Brand exports <ArrowDown aria-hidden="true" size={13} /></a>
    </nav>

    <section className="asset-section" id="banners" aria-labelledby="banner-heading">
      <div className="lib-specimen-head">
        <h2 id="banner-heading">Banners</h2>
        <p>Keep headings and links in the page. When the photograph is decorative and the heading gives the full context, use an empty alt attribute.</p>
      </div>
      <BannerBrowser />
    </section>

    <section className="asset-section" id="department-icons" aria-labelledby="department-icon-heading">
      <div className="lib-specimen-head">
        <h2 id="department-icon-heading">Department icons</h2>
        <p>Use each symbol beside its department name. When an icon is the only content in a control, give the control an accessible name.</p>
      </div>
      <div className="asset-icons">
        {departmentIcons.map(icon => (
          <a key={icon.id} href={icon.src} download aria-label={'Download ' + icon.label + ' icon as SVG'}>
            <span className="asset-icon-glyph"><DepartmentIcon name={icon.id} size={46} /></span>
            <span className="asset-icon-caption"><strong>{icon.label}</strong><Download aria-hidden="true" size={15} /></span>
          </a>
        ))}
      </div>
      <div className="asset-interface">
        <h3>Interface icons</h3>
        <p>Storefront controls use the outlined Lucide set.</p>
        <ul>{interfaceIcons.map(({ label, Icon }) => <li key={label}><Icon size={19} aria-hidden="true" />{label}</li>)}</ul>
      </div>
    </section>

    <section className="asset-section" id="brand-exports" aria-labelledby="brand-export-heading">
      <div className="lib-specimen-head">
        <h2 id="brand-export-heading">Brand exports</h2>
        <p>Download the original Silver Medical signatures, sharing card and browser artwork.</p>
      </div>
      <div className="asset-logos">
        {logoArtwork.map(logo => (
          <a key={logo.variant} href={'/brand/' + logo.file} download aria-label={'Download ' + logo.label + ' as SVG'}>
            <span className={'asset-logo-stage asset-logo-stage--' + logo.variant}><BrandLogo variant={logo.variant} size={logo.size} alt="" /></span>
            <span className="asset-logo-caption"><strong>{logo.label}</strong><span>SVG <Download size={13} aria-hidden="true" /></span></span>
          </a>
        ))}
      </div>
      <div className="asset-delivery">
        <article>
          <h3>Social sharing card</h3>
          <a className="asset-social" href="/brand/identity/silver-edit-social.png" download aria-label="Download the social sharing card as PNG">
            <img src="/brand/identity/silver-edit-social.png" alt="" width={1200} height={630} loading="lazy" />
            <span className="asset-file"><span><strong>Homepage link preview</strong><small>1200 × 630 · PNG</small></span><Download size={16} aria-hidden="true" /></span>
          </a>
        </article>
        <article>
          <h3>Browser &amp; app icons</h3>
          <ul className="asset-files">
            {deviceArtwork.map(file => <li key={file.href}>
              <a href={file.href} download className="asset-file" aria-label={'Download ' + file.title + ', ' + file.format}>
                {file.href.endsWith('.webmanifest') ? <span className="asset-manifest-icon" aria-hidden="true">{'{ }'}</span>
                  : <img src={file.href} alt="" width={29} height={29} loading="lazy" />}
                <span><strong>{file.title}</strong><small>{file.format}</small></span><Download aria-hidden="true" size={16} />
              </a>
            </li>)}
          </ul>
        </article>
      </div>
    </section>
  </>;
}
