'use client';

import { useState } from 'react';
import { ArrowUpRight, Bookmark, Check, Heart, Package, Plus } from 'lucide-react';
import { Button, Checkbox, Combobox, EmptyState, IconButton, LinkButton, QuantityControl, RadioGroup, SearchField, Select, Skeleton, StatusMessage, Switch, Textarea, TextInput } from '@silver-medical/ui/controls';
import { useToast } from '@silver-medical/ui/overlays';
import { Specimen } from './specimen';

const departments = ['Diagnostics', 'Consumables', 'Wound care', 'Equipment', 'Dental', 'Veterinary', 'Laboratory'].map(label => ({ value: label, label }));

export function ActionExamples() {
  const { toast } = useToast();
  const [saved, setSaved] = useState(false);
  const [quantity, setQuantity] = useState(1);
  const [compact, setCompact] = useState(false);
  function confirm(title: string) { toast({title, tone: 'success'}); }
  return <>
    <Specimen title="Button hierarchy" description="Give the primary action the strongest visual weight. Reserve danger for removing something." usage={'<Button onClick={addToBasket}>Add to basket</Button>\n<Button variant="secondary" onClick={save}>Save selection</Button>'}>
      <div className="lib-row"><Button onClick={() => {setQuantity(q => q + 1); confirm('Sample item added to basket');}}><Plus size={16}/>Add to basket</Button>
        <Button variant="secondary" onClick={() => setSaved(!saved)} aria-pressed={saved}>{saved ? <Check size={16}/> : <Bookmark size={16}/>} {saved ? 'Selection saved' : 'Save selection'}</Button>
        <Button variant="ghost" onClick={() => {setQuantity(1); setSaved(false); confirm('Example reset');}}>Reset</Button>
        <Button variant="danger" disabled={quantity === 0} onClick={() => {setQuantity(0); confirm('Sample basket cleared');}}>Clear basket</Button></div>
      <p className="lib-status-line" aria-live="polite">Sample basket · {quantity} {quantity === 1 ? 'item' : 'items'}</p>
    </Specimen>
    <Specimen title="Sizes & states" usage={'<Button size="sm">Save</Button>\n<Button loading>Saving</Button>\n<Button disabled>Unavailable</Button>'}>
      <div className="lib-row">{(['sm', 'md', 'lg'] as const).map(size => <Button key={size} size={size} variant="secondary" onClick={() => confirm('Size selected: ' + size)}>{({sm:'Small', md:'Medium', lg:'Large'})[size]}</Button>)}</div>
      <div className="lib-row lib-row-gap"><Button loading>Saving</Button><Button disabled>Unavailable</Button></div>
    </Specimen>
    <Specimen title="Icon actions & links" description="Icon buttons have accessible names. Use links for destinations." usage={'<IconButton label="Save product" onClick={save}><Heart /></IconButton>\n<LinkButton href="/">View storefront</LinkButton>'}>
      <div className="lib-row"><IconButton label={compact ? 'Remove from shortlist' : 'Save product'} variant="secondary" aria-pressed={compact} onClick={() => setCompact(!compact)}><Heart size={19} fill={compact ? 'currentColor' : 'none'}/></IconButton><LinkButton href="/" variant="secondary">View storefront <ArrowUpRight size={15}/></LinkButton></div>
      <div className="lib-inverse"><LinkButton href="/#browse" variant="light">Discover the collection</LinkButton></div>
    </Specimen>
  </>;
}

export function FormExamples() {
  const [email, setEmail] = useState('');
  const [checked, setChecked] = useState(false);
  const [validated, setValidated] = useState(false);
  const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  const [department, setDepartment] = useState('');
  const [selected, setSelected] = useState('Diagnostics');
  const [enabled, setEnabled] = useState(true);
  const [pack, setPack] = useState('single');
  const [quantity, setQuantity] = useState(1);
  const [search, setSearch] = useState('');
  const [submitted, setSubmitted] = useState<string | null>(null);
  return <>
    <Specimen title="Inputs & validation" usage={'<TextInput label="Email address" type="email" hint="Use your work email." error={error} />'}>
      <form className="lib-stack" noValidate onSubmit={e => {e.preventDefault(); setValidated(true);}}>
        <div className="lib-pair"><TextInput label="Email address" type="email" autoComplete="off" value={email} onChange={e => setEmail(e.target.value)} placeholder="name@practice.co.uk" hint="Try submitting an empty field." error={validated && !emailOk ? 'Enter an email address such as name@practice.co.uk.' : undefined}/>
        <TextInput label="Country" value="United Kingdom" disabled hint="Disabled field example."/></div>
        <Textarea label="Order note" placeholder="Add a delivery instruction" rows={2}/>
        <div className="lib-row"><Button type="submit" variant="secondary">Check input</Button>{validated && emailOk && <span role="status">Email format accepted.</span>}</div>
      </form>
    </Specimen>
    <Specimen title="Select & searchable combobox" description="Use a native select for a short list and a searchable combobox when the options are harder to scan." usage={'<Select label="Department" options={departments} value={value} onChange={e => setValue(e.target.value)} />\n<Combobox label="Find a department" options={departments} value={value} onValueChange={setValue} />'}>
      <div className="lib-pair"><Select label="Department" options={departments} value={selected} onChange={e => setSelected(e.target.value)}/><Combobox label="Find a department" options={departments} value={department} onValueChange={setDepartment} placeholder="Type to filter departments"/></div>
    </Specimen>
    <Specimen title="Search" usage={'<SearchField label="Search products" value={query} onChange={e => setQuery(e.target.value)} onSearch={search} />'}>
      <SearchField label="Search departments" placeholder="Try Diagnostics" value={search} onChange={e => setSearch(e.target.value)} onSearch={value => setSubmitted(value.trim())}/>
      {submitted !== null && <p className="lib-status-line" role="status">{departments.filter(d => d.label.toLowerCase().includes(submitted.toLowerCase())).map(d => d.label).join(' · ') || 'No matching departments.'}</p>}
    </Specimen>
    <Specimen title="Choices & quantity" usage={'<Switch label="Show pack details" checked={enabled} onCheckedChange={setEnabled} />\n<QuantityControl label="Pack quantity" value={quantity} onValueChange={setQuantity} />'}>
      <div className="lib-pair"><div className="lib-stack"><Checkbox label="Include sample packs" checked={checked} onChange={e => setChecked(e.target.checked)}/><Switch label="Show pack details" checked={enabled} onCheckedChange={setEnabled}/></div>
      <RadioGroup label="Order unit" options={[{value:'single',label:'Single instrument'},{value:'case',label:'Case of six'}]} value={pack} onValueChange={setPack}/></div>
      <div className="lib-row lib-row-gap"><QuantityControl label="Pack quantity" value={quantity} onValueChange={setQuantity} max={12}/>{enabled && <span className="lib-help" aria-live="polite">{quantity * (pack === 'case' ? 6 : 1)} instrument(s){checked ? ' · samples included' : ''}</span>}</div>
    </Specimen>
  </>;
}

export function FeedbackExamples() {
  const { toast } = useToast();
  const [hasItem, setHasItem] = useState(false);
  return <>
    <Specimen title="Inline status" usage={'<StatusMessage tone="success" title="Selection saved">Your shortlist is ready.</StatusMessage>'}>
      <div className="lib-pair"><StatusMessage tone="info" title="Sample catalogue">Prices are illustrative.</StatusMessage><StatusMessage tone="success" title="Selection saved">Your shortlist is ready.</StatusMessage><StatusMessage tone="warning" title="Review quantity">The pack contains six instruments.</StatusMessage><StatusMessage tone="error" title="Check the form">Enter the missing order reference.</StatusMessage></div>
    </Specimen>
    <Specimen title="Toast notifications" description="Use brief feedback for a completed action. Keep information that requires a decision on the page." usage={"const { toast } = useToast();\ntoast({ title: 'Selection saved', tone: 'success' });"}>
      <div className="lib-row"><Button variant="secondary" onClick={() => toast({title:'Selection saved', description:'The item is in your shortlist.', tone:'success'})}>Show success</Button><Button variant="secondary" onClick={() => toast({title:'Unable to save selection', description:'Try the action again.',tone:'error'})}>Show error</Button></div>
    </Specimen>
    <Specimen title="Empty & loading states" usage={'<Skeleton width="65%" height={16} label="Loading product name" />'}>
      <div className="lib-pair"><div>{hasItem ? <div className="lib-stack"><StatusMessage title="Sample added" tone="success">One item in your list.</StatusMessage><Button variant="secondary" onClick={() => setHasItem(false)}>Clear sample</Button></div> : <EmptyState icon={<Package/>} title="Your list is empty" description="Add a sample to start a list." action={<Button onClick={() => setHasItem(true)}>Add sample</Button>}/>}</div>
      <div className="lib-skeleton"><Skeleton width="100%" height={110} label="Loading sample product"/><Skeleton width="70%" height={15}/><Skeleton width="40%" height={12}/></div></div>
    </Specimen>
  </>;
}
