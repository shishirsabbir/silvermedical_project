import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Download, Package, Truck } from 'lucide-react';
import { Price } from '@silver-medical/ui/commerce';
import { Accordion, Breadcrumbs } from '@silver-medical/ui/navigation';
import { catalogue, getProduct } from '../../../features/catalogue/catalogue';
import { CatalogueCard, ProductPhoto, PurchasePanel } from '../../../features/catalogue/product-actions';
import { BreadcrumbData, ProductData } from '../../../features/catalogue/structured-data';
import '../../../features/catalogue/catalogue.css';

type Parameters = { params: Promise<{ slug: string }> };
export const dynamicParams = false;
export const generateStaticParams = () => catalogue.map(({ slug }) => ({ slug }));

async function productFor(params: Parameters['params']) {
  const { slug } = await params;
  return getProduct(slug) ?? notFound();
}

export async function generateMetadata({ params }: Parameters): Promise<Metadata> {
  const product = await productFor(params);
  const title = product.name + ' · ' + product.variant;
  const url = '/products/' + product.slug;
  const image = { url: product.image, width: 512, height: 512, alt: product.name };
  return {
    title, description: product.description, alternates: { canonical: url },
    openGraph: { title, description: product.description, url, images: [image] },
    twitter: { card: 'summary', title, description: product.description, images: [image] },
  };
}

export default async function Page({ params }: Parameters) {
  const product = await productFor(params);
  const trail = [
    { label: 'Home', href: '/' }, { label: 'Catalogue', href: '/shop' },
    { label: product.category, href: '/departments/' + product.department },
    { label: product.name, href: '/products/' + product.slug },
  ];
  const variants = catalogue.filter(item => item.family === product.family);
  const similar = catalogue.filter(item => item.department === product.department && item.family !== product.family);
  const recommendations = similar.length ? similar : catalogue.filter(item => item.family !== product.family && item.stock > 0 && !item.professional);

  return <main id="main" className="cat-page cat-wrap">
    <Breadcrumbs items={trail} /><BreadcrumbData items={trail} /><ProductData product={product} />
    <div className="cat-product">
      <ProductPhoto product={product} />
      <section className="cat-product-summary" aria-labelledby="product-name">
        <Link href={'/departments/' + product.department} className="cat-kicker">{product.category}</Link>
        <h1 id="product-name">{product.name}</h1>
        <p className="cat-code">SKU {product.sku}</p>
        <p className="cat-lede">{product.description}</p>
        <div className="cat-product-price"><Price amount={product.price} caption="Per pack, including demo VAT" /></div>
        {variants.length > 1 && <div className="cat-variants">
          <p>Size <strong>{product.variant}</strong></p>
          <nav aria-label="Available sizes">{variants.map(item => <Link key={item.id} href={'/products/' + item.slug}
            aria-current={item.id === product.id ? 'page' : undefined}>{item.variant}</Link>)}</nav>
        </div>}
        <p className="cat-pack"><Package aria-hidden="true" size={17} />{product.pack}</p>
        <PurchasePanel key={product.id} product={product} />
        <div className="cat-ship"><Truck size={18} aria-hidden="true" /><span>GB delivery options and totals at checkout.</span></div>
      </section>
    </div>
    <section className="cat-product-details" aria-labelledby="product-details">
      <div><p className="cat-kicker">Product information</p><h2 id="product-details">The details.</h2></div>
      <Accordion defaultValue="specification" items={[
        { value: 'specification', title: 'Specification and pack', content:
          <dl className="cat-spec">{[['Catalogue SKU', product.sku], ['Department', product.category], ['Pack', product.pack],
            ['Variant', product.variant], ['Manufacturer reference', 'Awaiting supplier record']].map(([name, value]) =>
              <div key={name}><dt>{name}</dt><dd>{value}</dd></div>)}</dl> },
        { value: 'delivery', title: 'Price and delivery', content:
          <p>Displayed prices include illustrative VAT. Standard GB delivery is £3.95, or free on baskets of £50 or more. Express is £6.95. Checkout shows the final demo total.</p> },
        { value: 'documents', title: 'Product documents', content: <div>
          <p>Download the sample purchasing record for the SKU, pack and variant. Manufacturer instructions are awaiting supplier verification.</p>
          <a className="cat-download" href={'/products/' + product.slug + '/record'} download><Download size={16} aria-hidden="true" />Download sample record (TXT)</a>
        </div> },
      ]} />
    </section>
    <section className="cat-recommend" aria-labelledby="cat-more">
      <div className="cat-related-heading"><h2 id="cat-more">{similar.length ? 'More in ' + product.category.toLowerCase() : 'Explore the collection'}</h2><Link href="/shop">View catalogue</Link></div>
      <div className="cat-grid">{recommendations.slice(0, 3).map(item => <CatalogueCard product={item} key={item.id} />)}</div>
    </section>
  </main>;
}
