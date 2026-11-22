import { catalogue, getProduct } from '../../../../features/catalogue/catalogue';

export const generateStaticParams = () => catalogue.map(({ slug }) => ({ slug }));

export async function GET(_request: Request, { params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const item = getProduct(slug);
  if (!item) return new Response('Product unavailable', { status: 404 });
  const text = [
    'SILVER MEDICAL UK', 'Sample purchasing record', '', item.name,
    'Catalogue SKU: ' + item.sku, 'Department: ' + item.category, 'Pack: ' + item.pack,
    'Variant: ' + item.variant, 'Sample pack price including demo VAT: £' + item.price.toFixed(2),
    'Buyer access: ' + (item.professional ? 'Verified professional demo account' : 'General purchase'),
    'Manufacturer reference: Awaiting supplier record',
    '', 'Illustrative catalogue data for the Silver Medical storefront demo.',
  ].join('\r\n');
  return new Response(text, { headers: {
    'Content-Type': 'text/plain; charset=utf-8', 'Content-Disposition': 'attachment; filename="' + item.sku + '.txt"',
    'X-Robots-Tag': 'noindex',
  } });
}
