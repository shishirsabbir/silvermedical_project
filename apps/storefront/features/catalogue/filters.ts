import type { CatalogueProduct } from './catalogue';

export type SearchValues = Record<string, string | string[] | undefined>;
export const stockOptions = [
  { value: '', label: 'Any availability' }, { value: 'available', label: 'In stock' },
  { value: 'unavailable', label: 'Out of stock' },
];
export const accessOptions = [
  { value: '', label: 'All buyers' }, { value: 'general', label: 'General purchase' },
  { value: 'professional', label: 'Professional only' },
];
export const sortOptions = [
  { value: '', label: 'Featured' }, { value: 'low', label: 'Price: low to high' },
  { value: 'high', label: 'Price: high to low' }, { value: 'az', label: 'Name: A to Z' },
];

export function parseFilters(values: SearchValues) {
  function read(key: string) {
    const value = values[key];
    return (Array.isArray(value) ? value[0] : value)?.trim() ?? '';
  }
  function option(key: string, options: { value: string }[]) {
    const value = read(key);
    return options.some(choice => choice.value === value) ? value : '';
  }
  const wantedPage = Number(read('page'));
  return {
    q: read('q').slice(0, 120), stock: option('stock', stockOptions),
    access: option('access', accessOptions), sort: option('sort', sortOptions),
    page: Number.isSafeInteger(wantedPage) && wantedPage > 0 ? wantedPage : 1,
  };
}

export type CatalogueFilters = ReturnType<typeof parseFilters>;

export function listingUrl(path: string, filters: CatalogueFilters, page = 1) {
  const query = new URLSearchParams();
  for (const key of ['q', 'stock', 'access', 'sort'] as const) {
    if (filters[key]) query.set(key, filters[key]);
  }
  if (page > 1) query.set('page', String(page));
  return query.size ? path + '?' + query.toString() : path;
}

export function matchingProducts(items: CatalogueProduct[], filters: CatalogueFilters, stockFor: (item: CatalogueProduct) => number) {
  const words = filters.q.toLocaleLowerCase('en-GB').split(/[\s-]+/).filter(Boolean);
  const matches = items.filter(item => {
    const text = [item.name, item.category, item.sku, item.sku.replaceAll('-', ''), item.pack, item.variant].join(' ').toLocaleLowerCase('en-GB');
    const inStock = stockFor(item) > 0;
    return words.every(word => text.includes(word))
      && (filters.stock === '' || (filters.stock === 'available' ? inStock : !inStock))
      && (filters.access === '' || (filters.access === 'professional' ? item.professional : !item.professional));
  });
  if (filters.sort === 'az') matches.sort((a, b) => a.name.localeCompare(b.name, 'en-GB') || a.sku.localeCompare(b.sku));
  if (filters.sort === 'low') matches.sort((a, b) => a.price - b.price);
  if (filters.sort === 'high') matches.sort((a, b) => b.price - a.price);
  return matches;
}
