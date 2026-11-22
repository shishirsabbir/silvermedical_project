'use client';

import { useState } from 'react';
import { BookOpen, ChevronDown, Heart, Info, SlidersHorizontal } from 'lucide-react';
import { Button, IconButton, Select, Switch, TextInput } from '@silver-medical/ui/controls';
import { Accordion, Breadcrumbs, DropdownMenu, Pagination, Tabs } from '@silver-medical/ui/navigation';
import { Dialog, Drawer, Popover, Tooltip, useToast } from '@silver-medical/ui/overlays';
import { Specimen } from './specimen';

export function NavigationExamples() {
  const [page, setPage] = useState(1);
  return <>
    <Specimen title="Breadcrumbs" description="Link each ancestor and identify the current page." usage={'<Breadcrumbs items={[{ label: "Library", href: "/design-system" }, { label: "Navigation" }]} />'}>
      <Breadcrumbs items={[{label:'Design system',href:'/design-system'},{label:'Navigation'}]}/>
    </Specimen>
    <Specimen title="Tabs" description="Use the arrow keys to move between related panels." usage={'<Tabs label="Product information" items={panels} />'}>
      <Tabs label="Product information" items={[
        {value:'details',label:'Details',content:'A dual-head stethoscope with a forest green finish.'},
        {value:'pack',label:'Pack information',content:'One instrument per pack. Sample price £38.50.'},
        {value:'care',label:'Care notes',content:'Use the documentation supplied with the selected model.'}
      ]}/>
    </Specimen>
    <Specimen title="Accordion" usage={'<Accordion items={[{ value: "pack", title: "What is included?", content: "One instrument." }]} />'}>
      <Accordion items={[{value:'packs',title:'Where can I find pack information?',content:'Check the pack description below the product name, or open its quick view.'},{value:'saved',title:'How do I shortlist a product?',content:'Select the heart on a product card to save it.'}]}/>
    </Specimen>
    <Specimen title="Pagination" usage={'<Pagination page={page} totalPages={12} onPageChange={setPage} />'}>
      <Pagination page={page} totalPages={12} onPageChange={setPage}/>
      <p className="lib-status-line" aria-live="polite">Showing items {(page - 1) * 10 + 1}–{page * 10} of 120</p>
    </Specimen>
  </>;
}

export function OverlayExamples() {
  const { toast } = useToast();
  const [sort, setSort] = useState('Featured');
  const [marked, setMarked] = useState(false);
  const [saved, setSaved] = useState('');
  const [name, setName] = useState('Practice essentials');
  const [dialogOpen, setDialogOpen] = useState(false);
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [view, setView] = useState('Grid');
  const [prices, setPrices] = useState(true);
  return <>
    <Specimen title="Dropdown menu" description="A menu groups actions. Open it and use the arrow keys to make a selection." usage={'<DropdownMenu label="Sort products" trigger={<Button>Sort by</Button>} items={actions} />'}>
      <div className="lib-row"><DropdownMenu label="Sort products" trigger={<Button variant="secondary">Sort by <ChevronDown size={15}/></Button>} items={['Featured','Price: low to high','Price: high to low'].map(label => ({label,onSelect:() => setSort(label)}))}/><span className="lib-help" aria-live="polite">{sort}</span></div>
    </Specimen>
    <Specimen title="Tooltip & popover" description="Hover or focus the heart for a label. Open pack details for information you can read at your own pace." usage={'<Tooltip content="Save product"><IconButton label="Save product"><Heart /></IconButton></Tooltip>\n<Popover title="Pack details" trigger={<Button>Pack details</Button>}>One instrument per pack.</Popover>'}>
      <div className="lib-row"><Tooltip content={marked ? 'Remove from shortlist' : 'Save to shortlist'}><IconButton label={marked ? 'Remove from shortlist' : 'Save to shortlist'} variant="secondary" aria-pressed={marked} onClick={() => setMarked(!marked)}><Heart size={18} fill={marked ? 'currentColor' : 'none'}/></IconButton></Tooltip>
      <Popover title="Pack details" trigger={<Button variant="secondary"><Info size={16}/>Pack details</Button>}><p>One instrument per pack. Use the quantity control to add more packs to your basket.</p></Popover></div>
    </Specimen>
    <Specimen title="Modal dialog" description="A dialog keeps focus on a short task. Escape closes it and returns focus to its trigger." usage={'<Dialog title="Name your selection" trigger={<Button>Open dialog</Button>}>…</Dialog>'}>
      <div className="lib-row"><Dialog title="Name your selection" description="Give this sample shortlist a name." open={dialogOpen} onOpenChange={setDialogOpen}
        trigger={<Button variant="secondary"><BookOpen size={16}/>Open dialog</Button>}
        footer={<><Button variant="ghost" onClick={() => setDialogOpen(false)}>Cancel</Button><Button disabled={!name.trim()} onClick={() => {setSaved(name.trim()); setDialogOpen(false);}}>Save name</Button></>}>
        <TextInput label="Selection name" value={name} onChange={e => setName(e.target.value)} maxLength={80}/>
      </Dialog>{saved && <span className="lib-help" aria-live="polite">Saved as {saved}</span>}</div>
    </Specimen>
    <Specimen title="Drawer" description="Use a side panel for a basket or a task that benefits from keeping the page in view." usage={'<Drawer title="Display options" trigger={<Button>Open drawer</Button>}>…</Drawer>'}>
      <Drawer title="Display options" description="Try the controls inside a side panel." open={drawerOpen} onOpenChange={setDrawerOpen}
        trigger={<Button variant="secondary"><SlidersHorizontal size={16}/>Open drawer</Button>}
        footer={<Button onClick={() => {setDrawerOpen(false); toast({title:'Display options applied', description:view + ' view · ' + (prices ? 'prices visible' : 'prices hidden'),tone:'success'});}}>Apply options</Button>}>
        <div className="lib-stack"><Select label="Product layout" options={['Grid','List'].map(label=>({label,value:label}))} value={view} onChange={e => setView(e.target.value)}/><Switch label="Show prices" checked={prices} onCheckedChange={setPrices}/></div>
      </Drawer>
    </Specimen>
  </>;
}
