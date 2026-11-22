'use client';

import { Fragment, type ReactElement, type ReactNode } from 'react';
import {
  Accordion as AccordionPrimitive,
  DropdownMenu as MenuPrimitive,
  Tabs as TabsPrimitive,
} from 'radix-ui';
import { ChevronDown, ChevronLeft, ChevronRight, MoreHorizontal } from 'lucide-react';
import './navigation.css';

export interface DropdownMenuItem {
  label: string;
  onSelect?: () => void;
  icon?: ReactNode;
  disabled?: boolean;
  destructive?: boolean;
  separatorBefore?: boolean;
}

export interface DropdownMenuProps {
  trigger: ReactElement;
  label: string;
  items: readonly DropdownMenuItem[];
  align?: 'start' | 'center' | 'end';
  onCloseAutoFocus?: (event: Event) => void;
}

export function DropdownMenu({ trigger, label, items, align = 'start', onCloseAutoFocus }: DropdownMenuProps) {
  return (
    <MenuPrimitive.Root>
      <MenuPrimitive.Trigger asChild>{trigger}</MenuPrimitive.Trigger>
      <MenuPrimitive.Portal>
        <MenuPrimitive.Content
          className="sm-dropdown"
          aria-label={label}
          align={align}
          sideOffset={7}
          collisionPadding={10}
          onCloseAutoFocus={onCloseAutoFocus}
          loop
        >
          {items.map((item) => (
            <Fragment key={item.label}>
              {item.separatorBefore && <MenuPrimitive.Separator className="sm-dropdown-separator" />}
              <MenuPrimitive.Item
                className="sm-dropdown-item"
                disabled={item.disabled}
                data-destructive={item.destructive || undefined}
                textValue={item.label}
                onSelect={item.onSelect}
              >
                {item.icon && <span className="sm-dropdown-icon" aria-hidden="true">{item.icon}</span>}
                {item.label}
              </MenuPrimitive.Item>
            </Fragment>
          ))}
        </MenuPrimitive.Content>
      </MenuPrimitive.Portal>
    </MenuPrimitive.Root>
  );
}

export interface TabItem {
  value: string;
  label: string;
  content: ReactNode;
  disabled?: boolean;
}

export interface TabsProps {
  label: string;
  items: readonly TabItem[];
  value?: string;
  defaultValue?: string;
  onValueChange?: (value: string) => void;
}

export function Tabs({ label, items, value, defaultValue, onValueChange }: TabsProps) {
  const initialValue = defaultValue ?? items.find((item) => !item.disabled)?.value;
  return (
    <TabsPrimitive.Root className="sm-tabs" value={value} defaultValue={initialValue} onValueChange={onValueChange}>
      <TabsPrimitive.List className="sm-tab-list" aria-label={label}>
        {items.map((item) => (
          <TabsPrimitive.Trigger className="sm-tab" key={item.value} value={item.value} disabled={item.disabled}>
            {item.label}
          </TabsPrimitive.Trigger>
        ))}
      </TabsPrimitive.List>
      {items.map((item) => (
        <TabsPrimitive.Content key={item.value} value={item.value} className="sm-tab-content">
          {item.content}
        </TabsPrimitive.Content>
      ))}
    </TabsPrimitive.Root>
  );
}

export interface BreadcrumbItem {
  label: string;
  href?: string;
}

export function Breadcrumbs({ items }: { items: readonly BreadcrumbItem[] }) {
  return (
    <nav aria-label="Breadcrumb" className="sm-breadcrumbs">
      <ol>
        {items.map(({ label, href }, index) => (
          <li key={href ?? label}>
            {index > 0 && <ChevronRight aria-hidden="true" size={14} />}
            {href && index < items.length - 1
              ? <a href={href}>{label}</a>
              : <span aria-current={index === items.length - 1 ? 'page' : undefined}>{label}</span>}
          </li>
        ))}
      </ol>
    </nav>
  );
}

export interface PaginationProps {
  page: number;
  totalPages: number;
  onPageChange: (page: number) => void;
  label?: string;
}

export function Pagination({ page, totalPages, onPageChange, label = 'Pagination' }: PaginationProps) {
  if (!Number.isFinite(totalPages) || totalPages < 1) return null;
  const last = Math.floor(totalPages);
  const current = Math.min(last, Math.max(1, Math.floor(page) || 1));
  const nearby = [1, current - 1, current, current + 1, last];
  // Show the second or penultimate page directly when the gap contains just that page.
  if (current <= 2) nearby.push(3);
  if (current >= last - 1) nearby.push(last - 2);
  const numbers = [...new Set(nearby)].filter((n) => n >= 1 && n <= last).sort((a, b) => a - b);

  function pageButton(n: number) {
    return (
      <button
        type="button"
        key={n}
        aria-label={'Page ' + n}
        aria-current={n === current ? 'page' : undefined}
        onClick={() => onPageChange(n)}
      >
        {n}
      </button>
    );
  }

  return (
    <nav className="sm-pagination" aria-label={label}>
      <button type="button" aria-label="Previous page" disabled={current === 1} onClick={() => onPageChange(current - 1)}>
        <ChevronLeft aria-hidden="true" size={18} />
      </button>
      {numbers.map((n, index) => {
        const gap = index ? n - numbers[index - 1] : 0;
        return (
          <Fragment key={n}>
            {gap === 2 && pageButton(n - 1)}
            {gap > 2 && <span className="sm-pagination-gap" aria-hidden="true"><MoreHorizontal size={16} /></span>}
            {pageButton(n)}
          </Fragment>
        );
      })}
      <button type="button" aria-label="Next page" disabled={current === last} onClick={() => onPageChange(current + 1)}>
        <ChevronRight aria-hidden="true" size={18} />
      </button>
    </nav>
  );
}

export interface AccordionItem {
  value: string;
  title: string;
  content: ReactNode;
}

export interface AccordionProps {
  items: readonly AccordionItem[];
  defaultValue?: string;
  value?: string;
  onValueChange?: (value: string) => void;
}

export function Accordion({ items, value, defaultValue, onValueChange }: AccordionProps) {
  return (
    <AccordionPrimitive.Root
      type="single"
      collapsible
      className="sm-accordion"
      value={value}
      defaultValue={defaultValue}
      onValueChange={onValueChange}
    >
      {items.map((item) => (
        <AccordionPrimitive.Item className="sm-accordion-item" key={item.value} value={item.value}>
          <AccordionPrimitive.Header className="sm-accordion-header">
            <AccordionPrimitive.Trigger className="sm-accordion-trigger">
              {item.title}
              <ChevronDown size={18} aria-hidden="true" />
            </AccordionPrimitive.Trigger>
          </AccordionPrimitive.Header>
          <AccordionPrimitive.Content className="sm-accordion-content">
            <div className="sm-accordion-copy">{item.content}</div>
          </AccordionPrimitive.Content>
        </AccordionPrimitive.Item>
      ))}
    </AccordionPrimitive.Root>
  );
}
