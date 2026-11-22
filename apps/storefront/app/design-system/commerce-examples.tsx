'use client';

import { useState } from 'react';
import { ShoppingBag } from 'lucide-react';
import { Button, EmptyState } from '@silver-medical/ui/controls';
import { BasketRow, CatalogueControls, CollectionTile, PackInfo, Price, ProductArt, ProductCard, ProductListItem, type SortOrder } from '@silver-medical/ui/commerce';
import { Dialog, useToast } from '@silver-medical/ui/overlays';
import { products } from '../../features/home/products';
import { Specimen } from './specimen';

const samples = products.slice(0, 3);

export function CommerceExamples() {
  const { toast } = useToast();
  const [category, setCategory] = useState('All');
  const [sort, setSort] = useState<SortOrder>('featured');
  const [quickId, setQuickId] = useState<string | null>(null);
  const [saved, setSaved] = useState<string[]>([]);
  const [basket, setBasket] = useState<Record<string,number>>({ stethoscope: 1 });
  const filtered = samples.filter(p => category === 'All' || p.category === category);
  if (sort === 'low') filtered.sort((a,b) => a.price-b.price);
  if (sort === 'high') filtered.sort((a,b) => b.price-a.price);
  if (sort === 'az') filtered.sort((a,b) => a.name.localeCompare(b.name));
  const lines = products.filter(p => (basket[p.id] ?? 0) > 0);
  const quick = products.find(p => p.id === quickId);
  function addItem(id: string) {
    setBasket(current => ({ ...current, [id]: Math.min(99, (current[id] ?? 0) + 1) }));
    toast({ title: 'Added to sample basket', tone: 'success' });
  }
  const actions = {
    onQuickView: setQuickId,
    onSave: (id: string) => setSaved(items => items.includes(id) ? items.filter(item => item !== id) : [...items, id]),
    onAdd: addItem,
  };
  return <>
    <Specimen title="Product cards & catalogue controls" description="Filter, sort, save or add one of the sample products. The basket below reflects your changes." usage={'<ProductCard product={product} saved={isSaved} onSave={save} onQuickView={showDetails} onAdd={addToBasket} />'}>
      <CatalogueControls categories={['All','Diagnostics','Consumables']} category={category} onCategoryChange={setCategory} sort={sort} onSortChange={setSort}/>
      <div className="lib-products">{filtered.map(p => <ProductCard product={p} {...actions} key={p.id} saved={saved.includes(p.id)}/>)}</div>
    </Specimen>
    <Specimen title="List item" description="A compact presentation for saved items or search results." usage={'<ProductListItem product={product} saved={isSaved} {...actions} />'}>
      <ProductListItem product={products[1]} {...actions} saved={saved.includes(products[1].id)}/>
    </Specimen>
    <Specimen title="Basket rows" usage={'<BasketRow product={product} quantity={quantity} onQuantityChange={updateQuantity} onRemove={remove} />'}>
      {lines.length ? <>{lines.map(p => <BasketRow key={p.id} product={p} quantity={basket[p.id]} onQuantityChange={quantity => setBasket(current => ({...current, [p.id]:quantity}))} onRemove={() => setBasket(current => ({...current, [p.id]:0}))}/>)}<div className="lib-total"><span>Sample subtotal</span><Price amount={lines.reduce((sum,p) => sum + p.price * basket[p.id], 0)}/></div></>
      : <EmptyState title="Your sample basket is empty" icon={<ShoppingBag/>} action={<Button onClick={() => addItem(products[0].id)}>Add a sample</Button>}/>}
    </Specimen>
    <Specimen title="Collection tile" description="A photographic entry point to a storefront collection." usage={'<CollectionTile variant="feature" title="Explore diagnostics" eyebrow="Collection" action="Shop diagnostics" href="/#browse" image="/images/diagnostics.webp" />'}>
      <div className="lib-collection"><CollectionTile variant="feature" title="Explore diagnostics" eyebrow="Collection" action="View collection" href="/#browse" image="/images/diagnostics.webp" imageAlt="Stethoscope and penlight"/></div>
    </Specimen>
    <Dialog open={Boolean(quick)} onOpenChange={open => {if (!open) setQuickId(null);}} title={quick?.name ?? 'Product details'} description="Sample product details.">
      {quick && <div className="lib-quick"><ProductArt index={quick.art}/><div className="lib-stack"><PackInfo>{quick.pack}</PackInfo><Price amount={quick.price} caption="Sample price"/><Button onClick={() => {addItem(quick.id); setQuickId(null);}}>Add to basket</Button></div></div>}
    </Dialog>
  </>;
}
