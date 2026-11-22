'use client';

import Link from 'next/link';
import { useState, type FormEvent } from 'react';
import { ArrowRight, MapPin, Package, Plus, ShieldCheck, UserRound } from 'lucide-react';
import { Button, EmptyState, Select, StatusMessage, TextInput } from '@silver-medical/ui/controls';
import { useAccount, type DemoAccount, type DemoAddress } from './account-provider';
import { useShop } from '../shop/shop-provider';
import { money, orderStatusLabels } from '../shop/order-model';

type Note = { text: string; error?: boolean } | null;
const message = (error: unknown) => error instanceof Error ? error.message : 'Unable to save this change.';
function Feedback({ note }: { note: Note }) {
  return note ? <StatusMessage tone={note.error ? 'error' : 'success'}>{note.text}</StatusMessage> : null;
}

export function ProfileSection({ account }: { account: DemoAccount }) {
  const { setName } = useAccount();
  const [note, setNote] = useState<Note>(null);
  function save(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    try { setName(String(new FormData(event.currentTarget).get('name') || '')); setNote({ text: 'Profile updated.' }); }
    catch (error) { setNote({ text: message(error), error: true }); }
  }
  return <section className="se-service-card">
    <div className="se-section-title"><UserRound aria-hidden/><h2>Personal details</h2></div>
    <form className="se-service-form" onSubmit={save}>
      <TextInput name="name" label="Display name" defaultValue={account.name} required maxLength={80}/>
      <div className="se-readonly"><strong>Verified demo email</strong><span>{account.email}</span></div>
      <Button type="submit">Save profile</Button><Feedback note={note}/>
    </form>
  </section>;
}

function AddressForm({ original, accountName, onCancel, onSave }: { original: DemoAddress | null; accountName: string; onCancel: () => void; onSave: (address: DemoAddress) => void }) {
  const [error, setError] = useState('');
  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const value = (name: string) => String(data.get(name) || '').trim();
    try {
      onSave({ id: original?.id ?? crypto.randomUUID(), label: value('label'), name: value('name'),
        line1: value('line1'), line2: value('line2'), city: value('city'), postcode: value('postcode'), country: 'GB' });
    } catch (reason) { setError(message(reason)); }
  }
  return <form className="se-service-form se-address-form" onSubmit={submit}>
    <h3>{original ? 'Edit address' : 'New address'}</h3>
    <div className="se-field-row"><TextInput name="label" label="Address label" placeholder="Practice" defaultValue={original?.label} maxLength={50} required/>
      <TextInput name="name" label="Recipient" defaultValue={original?.name ?? accountName} maxLength={100} required/></div>
    <TextInput name="line1" label="Address line 1" defaultValue={original?.line1} placeholder="10 Example Lane" maxLength={120} required/>
    <TextInput name="line2" label="Address line 2 (optional)" defaultValue={original?.line2} maxLength={120}/>
    <div className="se-field-row"><TextInput name="city" label="Town or city" defaultValue={original?.city} maxLength={80} required/>
      <TextInput name="postcode" label="UK postcode" defaultValue={original?.postcode} placeholder="SW1A 1AA" maxLength={10} required/></div>
    {error && <StatusMessage tone="error">{error}</StatusMessage>}
    <div className="se-buttons"><Button type="submit">Save address</Button><Button variant="ghost" onClick={onCancel}>Cancel</Button></div>
  </form>;
}

export function AddressesSection({ account }: { account: DemoAccount }) {
  const { saveAddress, removeAddress } = useAccount();
  const [edit, setEdit] = useState<'new' | DemoAddress | null>(null);
  const [note, setNote] = useState<Note>(null);
  return <section className="se-service-card">
    <div className="se-section-title"><MapPin aria-hidden/><h2>Address book</h2></div>
    <p>Save example UK addresses to use at checkout.</p>
    <Feedback note={note}/>
    {!edit && <Button variant="secondary" onClick={() => { setEdit('new'); setNote(null); }}><Plus size={17}/> Add address</Button>}
    {edit && <AddressForm key={typeof edit === 'string' ? edit : edit.id} original={edit === 'new' ? null : edit} accountName={account.name}
      onCancel={() => setEdit(null)} onSave={value => { saveAddress(value); setEdit(null); setNote({ text: 'Address saved.' }); }}/>}
    {account.addresses.length ? <ul className="se-addresses">{account.addresses.map(item => <li key={item.id}>
      <div><strong>{item.label}</strong><address>{item.name}<br/>{item.line1}{item.line2 && <><br/>{item.line2}</>}<br/>{item.city}, {item.postcode}</address></div>
      <div className="se-buttons"><Button size="sm" variant="secondary" aria-label={'Edit ' + item.label} onClick={() => { setEdit(item); setNote(null); }}>Edit</Button>
        <Button size="sm" variant="ghost" aria-label={'Remove ' + item.label} onClick={() => {
          try { removeAddress(item.id); if (typeof edit === 'object' && edit?.id === item.id) setEdit(null); setNote({ text: 'Address removed.' }); }
          catch (error) { setNote({ text: message(error), error: true }); }
        }}>Remove</Button></div></li>)}</ul> : !edit && <p>Your address book is empty.</p>}
  </section>;
}

export function OrdersSection() {
  const { orders, ready } = useShop();
  return <section className="se-service-card">
    <div className="se-section-title"><Package aria-hidden/><h2>Order history</h2></div>
    {!ready ? <p role="status">Loading orders…</p> : !orders.length ?
      <EmptyState title="No orders yet" description="Orders placed while signed in appear here." action={<Link className="se-arrow-link" href="/shop">Explore the catalogue <ArrowRight size={17}/></Link>}/> :
      <ul className="se-orders">{orders.map(order => <li key={order.id}>
        <Link href={'/orders/' + order.id}><span><strong>{order.reference}</strong>
          <small>{new Date(order.createdAt).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' })} · {orderStatusLabels[order.status]}</small></span>
          <span>{money(order.totalPence)} <ArrowRight size={16}/></span></Link></li>)}</ul>}
    <Link href="/track" className="se-arrow-link">Look up a guest order <ArrowRight size={16}/></Link>
  </section>;
}

const statuses = { none: 'No application', pending: 'Awaiting review', approved: 'Approved for the demo', declined: 'Application declined' };
export function ProfessionalSection({ account }: { account: DemoAccount }) {
  const { applyProfessional, simulateReview } = useAccount();
  const [note, setNote] = useState<Note>(null);
  const [reviewNote, setReviewNote] = useState('');
  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    try { applyProfessional(String(data.get('organisation') || ''), String(data.get('profession') || '')); setReviewNote(''); setNote({ text: 'Application submitted for demo review.' }); }
    catch (error) { setNote({ text: message(error), error: true }); }
  }
  function review(result: 'approved' | 'declined') {
    try { simulateReview(result, reviewNote); setNote({ text: result === 'approved' ? 'Professional access is active for this demo account.' : 'The demo application was declined. You can update and reapply.' }); }
    catch (error) { setNote({ text: message(error), error: true }); }
  }
  return <section className="se-service-card">
    <div className="se-section-title"><ShieldCheck aria-hidden/><h2>Professional access</h2></div>
    <p>Apply with fictional practice details to try products marked for professional buyers.</p>
    <div className="se-account-status"><span>Application status</span><strong>{statuses[account.professionalStatus]}</strong></div>
    {account.organisation && <p>{account.organisation} · {account.profession}</p>}
    {account.reviewerNote && <p><strong>Reviewer note</strong><br/>{account.reviewerNote}</p>}
    {(account.professionalStatus === 'none' || account.professionalStatus === 'declined') && <form className="se-service-form" onSubmit={submit}>
      <TextInput label="Example organisation" name="organisation" placeholder="Example Dental Practice" defaultValue={account.organisation} required maxLength={100}/>
      <Select label="Professional role" name="profession" defaultValue={account.profession} required options={[
        { value: '', label: 'Choose a role', disabled: true }, ...['Dentist', 'Practice manager', 'Clinician', 'Procurement professional', 'Other professional'].map(value => ({ value, label: value }))]}/>
      <Button type="submit">Submit application</Button>
    </form>}
    {account.professionalStatus === 'pending' && <details className="se-review">
      <summary>Simulate a reviewer decision</summary><p>These controls let you try both outcomes on this browser. Live access requires a separate reviewer.</p>
      <div className="se-service-form"><TextInput label="Reviewer note (optional)" maxLength={240} value={reviewNote} onChange={event => setReviewNote(event.target.value)}/>
        <div className="se-buttons"><Button size="sm" onClick={() => review('approved')}>Simulate approval</Button><Button size="sm" variant="secondary" onClick={() => review('declined')}>Simulate decline</Button></div></div>
    </details>}
    {account.professionalStatus === 'approved' && <Link className="se-arrow-link" href="/departments/dental">Explore dental products <ArrowRight size={16}/></Link>}
    <Feedback note={note}/>
  </section>;
}
