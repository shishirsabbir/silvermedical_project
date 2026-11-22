'use client';

import { useState } from 'react';
import Link from 'next/link';
import { Check, Heart, MinusCircle, Plus, ZoomIn } from 'lucide-react';
import { ProductCard, ProductListItem } from '@silver-medical/ui/commerce';
import { Button, QuantityControl } from '@silver-medical/ui/controls';
import { Dialog, useToast } from '@silver-medical/ui/overlays';
import { useShop } from '../shop/shop-provider';
import type { CatalogueProduct } from './catalogue';

function useProductActions(product: CatalogueProduct) {
  const shop = useShop();
  const { toast } = useToast();
  const stock = shop.ready ? shop.stockFor(product.id) : product.stock;
  const remaining = Math.max(0, stock - (shop.cart[product.id] ?? 0));
  const restricted = product.professional && !shop.professionalApproved;
  const saved = shop.saved.includes(product.id);
  function add(quantity: number) {
    if (shop.addItem(product.id, quantity)) {
      toast({ title: 'Added to basket', description: product.name + ' · ' + product.pack, tone: 'success' });
    } else {
      toast({ title: 'Basket could not be updated', description: 'Check the available quantity and your purchase access.', tone: 'error' });
    }
  }
  function save() {
    shop.toggleSaved(product.id);
    toast({ title: saved ? 'Removed from saved items' : 'Saved for later', description: product.name });
  }
  return { stock, remaining, restricted, saved, add, save, ready: shop.ready };
}

export function CatalogueCard({ product, list = false }: { product: CatalogueProduct; list?: boolean }) {
  const { stock, remaining, restricted, saved, add, save, ready } = useProductActions(product);
  const Card = list ? ProductListItem : ProductCard;
  const availability = stock === 0 ? 'Out of stock' : 'In stock';
  return <Card product={product} productHref={'/products/' + product.slug} saved={saved}
    availability={product.professional ? availability + ' · Professional only' : availability}
    disabledSave={!ready} disabledAdd={!ready || !remaining || restricted} onSave={save} onAdd={() => add(1)} />;
}

export function PurchasePanel({ product }: { product: CatalogueProduct }) {
  const { stock, remaining, restricted, saved, add, save, ready } = useProductActions(product);
  const [quantity, setQuantity] = useState(1);
  const chosen = Math.min(quantity, Math.max(1, remaining));
  return <div className="cat-purchase">
    <div className="cat-stock">
      {stock > 0 ? <Check size={16} aria-hidden="true" /> : <MinusCircle size={16} aria-hidden="true" />}
      <span>{stock > 0 ? 'In stock · ' + stock + ' packs available' : 'Out of stock'}</span>
    </div>
    {product.professional && <p className="cat-access">Professional access {restricted ? 'required.' : 'approved.'}
      {restricted && <> <Link href="/account?view=professional">View application</Link></>}</p>}
    <div className="cat-purchase-row">
      <QuantityControl label="packs" value={chosen} onValueChange={setQuantity} max={Math.max(1, remaining)}
        disabled={!ready || restricted || remaining === 0} />
      <Button size="lg" onClick={() => add(chosen)} disabled={!ready || restricted || remaining === 0}>
        <Plus size={18} aria-hidden="true" />Add to basket
      </Button>
    </div>
    {ready && stock > 0 && remaining === 0 && <p className="cat-note">All available packs are in your basket.</p>}
    <div className="cat-purchase-links">
      <Button variant="ghost" size="sm" aria-pressed={saved} disabled={!ready} onClick={save}>
        <Heart size={17} fill={saved ? 'currentColor' : 'none'} aria-hidden="true" />{saved ? 'Saved' : 'Save for later'}
      </Button>
      <Link href="/cart">View basket</Link>
    </div>
  </div>;
}

export function ProductPhoto({ product }: { product: CatalogueProduct }) {
  return <figure className="cat-product-photo">
    <img src={product.image} alt={product.name + ', ' + product.variant} width={512} height={512} fetchPriority="high" />
    <Dialog title={product.name} description={product.pack} trigger={
      <Button size="sm" variant="secondary" className="cat-zoom"><ZoomIn size={16} aria-hidden="true" />Enlarge</Button>
    }>
      <img className="cat-full-photo" src={product.image} alt={product.name + ', ' + product.variant} width={512} height={512} />
    </Dialog>
  </figure>;
}
