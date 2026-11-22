'use client';

import Link from 'next/link';
import { ArrowRight, Heart, ShieldCheck, Trash2 } from 'lucide-react';
import { Button, IconButton, QuantityControl } from '@silver-medical/ui/controls';
import { ProductArt } from '@silver-medical/ui/commerce';
import { useToast } from '@silver-medical/ui/overlays';
import { catalogue } from '../catalogue/catalogue';
import { EmptyBag, JourneyPage, ShopLinkButton, LoadingShop, Summary } from './journey-ui';
import { money, orderLines } from './order-model';
import { useShop } from './shop-provider';

export function BasketPage({ savedOnly = false }: { savedOnly?: boolean }) {
  const shop = useShop(), { toast } = useToast();
  const items = catalogue.filter(item => savedOnly ? shop.saved.includes(item.id) : shop.cart[item.id] > 0);
  const lines = orderLines(shop.cart);
  const unavailable = items.some(item => (item.professional && !shop.professionalApproved) || shop.cart[item.id] > shop.stockFor(item.id));
  return <JourneyPage label={savedOnly ? 'Saved products' : 'Basket'} title={savedOnly ? <>Your <em>shortlist.</em></> : <>Your <em>basket.</em></>}>
    {!shop.ready ? <LoadingShop/> : !items.length ? <EmptyBag saved={savedOnly}/> : <div className={'order-columns' + (savedOnly ? ' order-columns--single' : '')}>
      <section className="order-bag" aria-label={savedOnly ? 'Saved products' : 'Basket contents'}>
        <div className="order-section-bar"><h2>{savedOnly ? 'Saved products' : 'Your selection'}</h2><span>{items.length} {items.length === 1 ? 'product' : 'products'}</span></div>
        <ul className="order-bag-lines">{items.map(item => {
          const stock = shop.stockFor(item.id);
          const canBuy = stock > 0 && (!item.professional || shop.professionalApproved);
          const quantity = shop.cart[item.id] ?? 0;
          return <li key={item.id} className="order-bag-line">
            <Link href={'/products/' + item.slug} className="order-product-image" aria-label={'View ' + item.name}><ProductArt index={item.art} image={item.image}/></Link>
            <div className="order-bag-detail"><small>{item.category}</small><h3><Link href={'/products/' + item.slug}>{item.name}</Link></h3>
              <p>{item.pack} · {item.sku}</p>
              {!canBuy && <p className="order-alert-inline">{stock === 0 ? 'Currently out of stock' : 'Professional approval required'}</p>}
              {!savedOnly && quantity > stock && <p className="order-alert-inline">Only {stock} available. Update your quantity.</p>}
              {savedOnly ? <Button size="sm" variant="secondary" disabled={!canBuy || quantity >= stock} onClick={() => {
                const added = shop.addItem(item.id);
                toast({ title: added ? item.name + ' added to your basket' : 'Available quantity reached' });
              }}>Add to basket</Button> : <QuantityControl label={'Quantity of ' + item.name} value={quantity} min={1} max={Math.max(1, stock)} onValueChange={value => shop.setQuantity(item.id, value)}/>}
            </div>
            <div className="order-bag-actions"><strong>{money(Math.round(item.price * 100) * (savedOnly ? 1 : quantity))}</strong>
              <div>{!savedOnly && <IconButton label={(shop.saved.includes(item.id) ? 'Unsave ' : 'Save ') + item.name} size="sm" aria-pressed={shop.saved.includes(item.id)} onClick={() => shop.toggleSaved(item.id)}><Heart size={17} fill={shop.saved.includes(item.id) ? 'currentColor' : 'none'}/></IconButton>}
              <IconButton size="sm" label={'Remove ' + item.name + (savedOnly ? ' from saved products' : ' from basket')} onClick={() => savedOnly ? shop.toggleSaved(item.id) : shop.setQuantity(item.id, 0)}><Trash2 size={17}/></IconButton></div>
            </div>
          </li>;
        })}</ul><Link className="order-textlink" href="/shop">Continue shopping <ArrowRight size={15} aria-hidden/></Link>
        {savedOnly && <Link className="order-textlink" href="/cart">View basket <ArrowRight size={15} aria-hidden/></Link>}
      </section>
      {!savedOnly && <Summary lines={lines}>
        {unavailable ? <p role="alert" className="order-error">Update unavailable items before checkout.</p> : <ShopLinkButton href="/checkout" className="order-wide">Continue to checkout <ArrowRight aria-hidden size={17}/></ShopLinkButton>}
        <div className="order-summary-note"><ShieldCheck aria-hidden size={17}/><span>Demo checkout with sample payment details.</span></div>
      </Summary>}
    </div>}
    {!shop.storageAvailable && <p className="order-note" role="status">Browser storage is unavailable. This demo session lasts until the page reloads.</p>}
  </JourneyPage>;
}
