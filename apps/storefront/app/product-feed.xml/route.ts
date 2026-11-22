import { catalogue } from '../../features/catalogue/catalogue';

export const dynamic = 'force-static';

function xml(text: string) {
  return text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
}
const origin = 'https://silvermedical.co.uk';

export function GET() {
  const items = catalogue.filter(p => p.publication === 'approved' && p.shoppingFeedApproved && !p.professional);
  const contents = items.map(p => [
    '<item>',
    '<g:id>' + xml(p.sku) + '</g:id>',
    '<g:title>' + xml(p.name) + '</g:title>',
    '<g:description>' + xml(p.description ?? '') + '</g:description>',
    '<g:link>' + origin + '/products/' + encodeURIComponent(p.slug) + '</g:link>',
    '<g:image_link>' + xml(new URL(p.image, origin).href) + '</g:image_link>',
    '<g:availability>' + (p.stock > 0 ? 'in_stock' : 'out_of_stock') + '</g:availability>',
    '<g:price>' + p.price.toFixed(2) + ' GBP</g:price>',
    '</item>',
  ].join('')).join('\n');
  const feed = '<?xml version="1.0" encoding="UTF-8"?>\n' +
    '<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0"><channel><title>Silver Medical UK</title>' +
    '<link>https://silvermedical.co.uk/</link><description>Products approved for the UK shopping feed.</description>' + contents + '</channel></rss>';
  return new Response(feed, { headers: { 'Content-Type': 'application/rss+xml; charset=utf-8', 'X-Robots-Tag': 'noindex' } });
}

