import type { BreadcrumbItem } from '@silver-medical/ui/navigation';
import type { CatalogueProduct } from './catalogue';

const origin = 'https://silvermedical.co.uk';

function JsonLd({ data }: { data: object }) {
  return <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(data).replace(/</g, '\\u003c') }} />;
}

export function BreadcrumbData({ items }: { items: BreadcrumbItem[] }) {
  return <JsonLd data={{
    '@context': 'https://schema.org', '@type': 'BreadcrumbList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem', position: index + 1, name: item.label, item: new URL(item.href ?? '/', origin).href,
    })),
  }} />;
}

export function ProductData({ product }: { product: CatalogueProduct }) {
  return <JsonLd data={{
    '@context': 'https://schema.org', '@type': 'Product',
    name: product.name, sku: product.sku, description: product.description, category: product.category,
    image: new URL(product.image, origin).href, url: new URL('/products/' + product.slug, origin).href,
  }} />;
}
