'use client';

import Link from 'next/link';
import { ArrowLeft, ArrowRight, SearchX } from 'lucide-react';
import { Button, EmptyState, LinkButton, Select, TextInput } from '@silver-medical/ui/controls';
import { useShop } from '../shop/shop-provider';
import { catalogue } from './catalogue';
import { CatalogueCard } from './product-actions';
import { accessOptions, listingUrl, matchingProducts, sortOptions, stockOptions, type CatalogueFilters } from './filters';

const pageSize = 6;

export function CatalogueResults({ filters, path, department }: { filters: CatalogueFilters; path: string; department?: string }) {
  const shop = useShop();
  const eligible = department ? catalogue.filter(item => item.department === department) : catalogue;
  const matches = matchingProducts(eligible, filters, item => shop.ready ? shop.stockFor(item.id) : item.stock);
  const pages = Math.max(1, Math.ceil(matches.length / pageSize));
  const page = Math.min(pages, filters.page);
  const start = (page - 1) * pageSize;
  const visible = matches.slice(start, start + pageSize);
  const active = Boolean(filters.q || filters.stock || filters.access || filters.sort);
  const pageHref = (n: number) => listingUrl(path, filters, n) + '#catalogue-results';

  return <section className="cat-results" id="catalogue-results" aria-label="Catalogue results">
    <form className="cat-filters" action={path + '#catalogue-results'} method="get" key={listingUrl(path, filters)}>
      <TextInput name="q" label="Search this selection" placeholder="Product name or SKU" type="search" maxLength={120} defaultValue={filters.q} />
      <Select label="Availability" name="stock" defaultValue={filters.stock} options={stockOptions} />
      <Select label="Purchase access" name="access" defaultValue={filters.access} options={accessOptions} />
      <Select label="Sort by" name="sort" defaultValue={filters.sort} options={sortOptions} />
      <Button type="submit" variant="secondary">Apply filters</Button>
    </form>
    <div className="cat-result-summary">
      <h2 id="catalogue-products" tabIndex={-1}>{filters.q ? 'Search results' : 'Products'}</h2>
      <p aria-live="polite">{matches.length > 0 ? (start + 1) + '–' + (start + visible.length) + ' of ' + matches.length : '0'} products
        {filters.q && <> for “{filters.q}”</>}</p>
      {active && <Link href={path + '#catalogue-results'}>Clear filters</Link>}
    </div>
    {visible.length ? <div className="cat-grid">{visible.map(product => <CatalogueCard key={product.id} product={product} />)}</div> :
      <EmptyState title="No products match this selection" description="Check the SKU or try fewer filters."
        icon={<SearchX />} action={<LinkButton href={path + '#catalogue-results'}>See all products in this selection</LinkButton>} />}
    {pages > 1 && <nav className="cat-pagination" aria-label="Catalogue pages">
      {page > 1 && <Link href={pageHref(page - 1)} aria-label="Previous page"><ArrowLeft size={17} aria-hidden="true" /></Link>}
      {Array.from({ length: pages }, (_, i) =>
        <Link key={i} href={pageHref(i + 1)} aria-label={'Page ' + (i + 1)} aria-current={page === i + 1 ? 'page' : undefined}>{i + 1}</Link>
      )}
      {page < pages && <Link href={pageHref(page + 1)} aria-label="Next page"><ArrowRight size={17} aria-hidden="true" /></Link>}
    </nav>}
  </section>;
}
