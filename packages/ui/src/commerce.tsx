'use client';

import type { ReactNode } from 'react';
import { Heart, Plus } from 'lucide-react';
import { Button, IconButton, QuantityControl, Select } from './controls';
import './commerce.css';

export interface Product {
  id: string;
  name: string;
  category: string;
  pack: string;
  price: number;
  art: number;
  image?: string;
  tag?: string;
  description?: string;
  spec?: string[];
}

export type SortOrder = 'featured' | 'low' | 'high' | 'az';

const currency = new Intl.NumberFormat('en-GB', {
  style: 'currency',
  currency: 'GBP',
});

export function Price({ amount, caption }: { amount: number; caption?: string }) {
  return (
    <span className="sm-price">
      <strong>{currency.format(amount)}</strong>
      {caption && <small>{caption}</small>}
    </span>
  );
}

export function PackInfo({ children }: { children: ReactNode }) {
  return <span className="sm-pack-info">{children}</span>;
}

export function ProductArt({ index, label, image }: { index: number; label?: string; image?: string }) {
  if (image) {
    return <img className="sm-product-photo" src={image} alt={label ?? ''} width={512} height={512} loading="lazy" />;
  }
  const cell = Math.min(5, Math.max(0, Math.floor(index)));
  return (
    <div
      className="sm-product-art"
      role={label ? 'img' : undefined}
      aria-label={label}
      aria-hidden={label ? undefined : true}
      style={{ backgroundPosition: `${(cell % 3) * 50}% ${Math.floor(cell / 3) * 100}%` }}
    />
  );
}

interface ProductActions {
  product: Product;
  saved?: boolean;
  onSave: (id: string) => void;
  onQuickView?: (id: string) => void;
  productHref?: string;
  disabledAdd?: boolean;
  disabledSave?: boolean;
  availability?: string;
  onAdd: (id: string) => void;
}

function ProductListing({
  product, onQuickView, onAdd, onSave, productHref, disabledAdd, disabledSave, availability, saved = false, compact = false,
}: ProductActions & { compact?: boolean }) {
  const art = <ProductArt index={product.art} image={product.image} />;
  const openLabel = 'View details for ' + product.name + ', ' + product.pack;
  return (
    <article className={compact ? 'sm-product sm-product--list' : 'sm-product sm-product--card'}>
      <div className="sm-product__picture">
        {productHref ? <a className="sm-product__open" href={productHref} aria-label={openLabel}>{art}</a> : <button
          type="button"
          className="sm-product__open"
          onClick={() => onQuickView?.(product.id)}
          aria-label={`View details for ${product.name}`}
        >
          {art}
        </button>}
        <IconButton
          className="sm-product__save"
          label={`Save ${product.name}`}
          variant="secondary"
          size="sm"
          aria-pressed={saved}
          disabled={disabledSave}
          onClick={() => onSave(product.id)}
        >
          <Heart size={17} fill={saved ? 'currentColor' : 'none'} aria-hidden />
        </IconButton>
      </div>
      <div className="sm-product__description">
        <p className="sm-product__category">{product.tag ?? product.category}</p>
        <h3>
          {productHref ? <a href={productHref}>{product.name}</a> :
            <button type="button" onClick={() => onQuickView?.(product.id)}>{product.name}</button>}
        </h3>
        <PackInfo>{product.pack}</PackInfo>
        {availability && <span className="sm-product__availability">{availability}</span>}
        <div className="sm-product__purchase">
          <Price amount={product.price} caption="Sample price" />
          <Button
            className="sm-product__add"
            size="sm"
            variant="secondary"
            disabled={disabledAdd}
            onClick={() => onAdd(product.id)}
            aria-label={`Add ${product.name} to basket`}
          >
            Add <Plus size={15} aria-hidden />
          </Button>
        </div>
      </div>
    </article>
  );
}

export function ProductCard(props: ProductActions) {
  return <ProductListing {...props} />;
}

export function ProductListItem(props: ProductActions) {
  return <ProductListing {...props} compact />;
}

interface CollectionTileProps {
  title: string;
  eyebrow: string;
  action: string;
  href: string;
  image?: string;
  imageAlt?: string;
  media?: ReactNode;
  art?: number;
  variant?: 'feature' | 'split' | 'scene';
  onSelect?: () => void;
}

export function CollectionTile({
  title, eyebrow, action, href, image, imageAlt = '', media, art, variant = 'feature', onSelect,
}: CollectionTileProps) {
  return (
    <a className={`sm-collection sm-collection--${variant}`} href={href} onClick={onSelect}>
      {media ? <div className="sm-collection__media">{media}</div>
        : image && <img className="sm-collection__photo" src={image} alt={imageAlt} width={1536} height={1024} loading="lazy" />}
      {art !== undefined && <div className="sm-collection__product"><ProductArt index={art} /></div>}
      <div className="sm-collection__copy">
        <span className="sm-collection__label">{eyebrow}</span>
        <h3>{title}</h3>
        <span className="sm-collection__action">{action}</span>
      </div>
    </a>
  );
}

interface BasketRowProps {
  product: Product;
  quantity: number;
  onQuantityChange: (quantity: number) => void;
  onRemove: () => void;
}

export function BasketRow({ product, quantity, onQuantityChange, onRemove }: BasketRowProps) {
  return (
    <article className="sm-basket-row">
      <ProductArt index={product.art} image={product.image} />
      <div className="sm-basket-row__details">
        <h3>{product.name}</h3>
        <PackInfo>{product.pack}</PackInfo>
        <div className="sm-basket-row__quantity">
          <QuantityControl
            label={`Quantity of ${product.name}`}
            value={quantity}
            min={1}
            max={99}
            onValueChange={onQuantityChange}
          />
          <Price amount={product.price * quantity} />
        </div>
        <Button className="sm-basket-row__remove" size="sm" variant="ghost" onClick={onRemove}
          aria-label={`Remove ${product.name} from basket`}>Remove</Button>
      </div>
    </article>
  );
}

const sortOptions = [
  { value: 'featured', label: 'Featured' },
  { value: 'low', label: 'Price: low to high' },
  { value: 'high', label: 'Price: high to low' },
  { value: 'az', label: 'Name: A to Z' },
];

interface CatalogueControlsProps {
  categories: string[];
  category: string;
  onCategoryChange: (category: string) => void;
  sort: SortOrder;
  onSortChange: (sort: SortOrder) => void;
}

export function CatalogueControls({
  categories, category, onCategoryChange, sort, onSortChange,
}: CatalogueControlsProps) {
  return (
    <div className="sm-catalogue-controls">
      <div className="sm-catalogue-controls__filters" role="group" aria-label="Filter by department">
        {categories.map((item) => (
          <Button
            key={item}
            size="sm"
            variant="ghost"
            aria-pressed={item === category}
            onClick={() => onCategoryChange(item)}
          >
            {item === 'All' ? 'All essentials' : item}
          </Button>
        ))}
      </div>
      <Select
        label="Sort products"
        hideLabel
        options={sortOptions}
        value={sort}
        onChange={(event) => onSortChange(event.target.value as SortOrder)}
      />
    </div>
  );
}
