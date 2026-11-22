'use client';

import { useState } from 'react';
import { Grid2X2, List } from 'lucide-react';
import { CatalogueControls, type SortOrder } from '@silver-medical/ui/commerce';
import { IconButton, LinkButton } from '@silver-medical/ui/controls';
import { CatalogueCard } from '../catalogue/product-actions';
import { catalogue } from '../catalogue/catalogue';
import { Collections, Help, Hero, Journal, PracticeStory, SectionHeading } from './editorial';

const categories = ['All', 'Diagnostics', 'Consumables', 'Wound care', 'Equipment'];

export function SilverEditStorefront() {
  const [category, setCategory] = useState('All');
  const [sort, setSort] = useState<SortOrder>('featured');
  const [list, setList] = useState(false);
  const selection = catalogue.filter(p => category === 'All' || p.category === category);
  if (sort === 'low') selection.sort((a,b) => a.price - b.price);
  if (sort === 'high') selection.sort((a,b) => b.price - a.price);
  if (sort === 'az') selection.sort((a,b) => a.name.localeCompare(b.name, 'en-GB'));
  const featured = selection.slice(0, 4);
  return <main id="main" className="edit-home">
    <Hero/><Collections/>
    <section id="products" className="edit-shell edit-section edit-products" aria-label="Selected essentials">
      <SectionHeading eyebrow="Selected essentials" title="Considered down to the detail.">Explore the range, compare packs and build your list.</SectionHeading>
      <CatalogueControls categories={categories} category={category} onCategoryChange={setCategory} sort={sort} onSortChange={setSort}/>
      <div className="edit-result-bar"><p aria-live="polite">Showing {featured.length} of {selection.length} essentials</p>
        <div className="edit-layout-controls" role="group" aria-label="Product layout">
          <IconButton label="Grid view" size="sm" variant="ghost" aria-pressed={!list} onClick={() => setList(false)}><Grid2X2 size={16}/></IconButton>
          <IconButton label="List view" size="sm" variant="ghost" aria-pressed={list} onClick={() => setList(true)}><List size={16}/></IconButton>
        </div>
      </div>
      <div className={list ? 'edit-product-list' : 'edit-product-grid'}>{featured.map(p => <CatalogueCard key={p.id} product={p} list={list} />)}</div>
      <div className="edit-show-all"><LinkButton variant="secondary" href="/shop">Explore all essentials</LinkButton></div>
    </section>
    <PracticeStory/><Journal/><Help/>
    <section className="edit-cta"><div className="edit-shell"><h2>Find the essentials.<br/><em>Focus on the care.</em></h2><LinkButton href="/shop">Explore the catalogue</LinkButton></div></section>
  </main>;
}

