'use client';

import Link from 'next/link';
import { useEffect, useId, useRef, useState, type KeyboardEvent } from 'react';
import { ChevronDown, Grid2X2 } from 'lucide-react';
import { Button } from '@silver-medical/ui/controls';
import { departmentIcons, type DepartmentIconId } from '@silver-medical/ui/icons';
import './department-menu.css';

const captions: Record<DepartmentIconId, string> = {
  diagnostics: 'Instruments for every examination',
  consumables: 'Everyday supplies for your practice',
  'wound-care': 'Dressings, gauze and instruments',
  equipment: 'Equip your clinical workspace',
  dental: 'Essentials for the treatment room',
  veterinary: 'Supplies for animal care',
  laboratory: 'Sample handling essentials',
  'infection-control': 'Keep your workspace prepared',
};

export function DepartmentMenu() {
  const [open, setOpen] = useState(false);
  const menuId = useId();
  const root = useRef<HTMLDivElement>(null);
  const trigger = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (!open) return;
    function dismissOutside(event: PointerEvent) {
      if (event.target instanceof Node && !root.current?.contains(event.target)) setOpen(false);
    }
    document.addEventListener('pointerdown', dismissOutside);
    return () => document.removeEventListener('pointerdown', dismissOutside);
  }, [open]);

  function handleKey(event: KeyboardEvent<HTMLDivElement>) {
    if (event.key === 'Escape' && open) {
      event.preventDefault();
      setOpen(false);
      trigger.current?.focus();
    }
    if (event.key !== 'ArrowDown' && event.key !== 'ArrowUp') return;
    const links = Array.from(event.currentTarget.querySelectorAll<HTMLAnchorElement>('nav a'));
    const index = links.indexOf(document.activeElement as HTMLAnchorElement);
    const down = event.key === 'ArrowDown';
    const next = index === -1 ? (down ? 0 : links.length - 1) : (index + (down ? 1 : -1) + links.length) % links.length;
    event.preventDefault();
    setOpen(true);
    requestAnimationFrame(() => links[next]?.focus());
  }

  function followLink() {
    trigger.current?.focus({ preventScroll: true });
    setOpen(false);
  }

  return <div className="department-disclosure" ref={root} onKeyDown={handleKey}
    onBlur={event => { if (!event.currentTarget.contains(event.relatedTarget)) setOpen(false); }}>
    <Button ref={trigger} variant="ghost" className="edit-header-button" aria-expanded={open}
      aria-controls={menuId} onClick={() => setOpen(!open)}>
      <Grid2X2 size={17} aria-hidden/>All departments<ChevronDown className="department-chevron" size={15} aria-hidden/>
    </Button>
    <nav id={menuId} className="department-menu" aria-label="Department menu" hidden={!open}>
      <div className="department-menu-intro">
        <p className="edit-eyebrow">Explore the catalogue</p>
        <h2>Find your essentials.</h2>
        <p>From the first examination to the everyday restock.</p>
        <Link href="/shop" onNavigate={followLink} className="sm-button sm-button--secondary sm-button--md department-menu-cta">View all products</Link>
      </div>
      <ul className="department-menu-links">
        {departmentIcons.map(({ id, label }) => <li key={id}>
          <Link href={'/departments/' + id} onNavigate={followLink}>
            <svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><use href={'/icons/catalogue-menu.svg#' + id}/></svg>
            <span><strong>{label}</strong><small>{captions[id]}</small></span>
          </Link>
        </li>)}
      </ul>
    </nav>
  </div>;
}
