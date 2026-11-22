'use client';

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useEffect, useRef, useState, type FormEvent } from 'react';
import { ArrowLeft, ArrowRight, Check, CreditCard, Package, Truck, Wallet } from 'lucide-react';
import { Button, Select, TextInput } from '@silver-medical/ui/controls';
import { useAccount } from '../account/account-provider';
import { catalogue } from '../catalogue/catalogue';
import { EmptyBag, JourneyPage, ShopLinkButton, LoadingShop, Summary } from './journey-ui';
import {
  basketStamp, deliverablePostcode, deliveryMethods, demoCard, money, orderLines, paymentLabels, sampleAddress, totals, validAddress,
  type Delivery, type Payment, type ShippingDetails,
} from './order-model';
import { useShop } from './shop-provider';

const blankAddress: ShippingDetails = { name: '', email: '', line1: '', line2: '', city: '', postcode: '' };
const fields = [
  { key: 'email', label: 'Email address', type: 'email' }, { key: 'name', label: 'Recipient name' },
  { key: 'line1', label: 'Address line 1' }, { key: 'line2', label: 'Address line 2 (optional)' },
  { key: 'city', label: 'Town or city' }, { key: 'postcode', label: 'Delivery postcode' },
] as const;
const methods: Payment[] = ['card', 'revolut', 'apple', 'google', 'paypal'];
const steps = ['Delivery', 'Payment', 'Review'] as const;
function CheckoutForm() {
  const shop = useShop(), { account } = useAccount(), router = useRouter();
  const [step, setStep] = useState(0), [delivery, setDelivery] = useState<Delivery>('standard');
  const [address, setAddress] = useState<ShippingDetails>(() => {
    const first = account?.addresses[0];
    return { ...blankAddress, name: account?.name ?? '', ...(first && { name: first.name, line1: first.line1, line2: first.line2, city: first.city, postcode: first.postcode }), email: account?.email ?? '' };
  });
  const [method, setMethod] = useState<Payment>('card'), [number, setNumber] = useState(''), [expiry, setExpiry] = useState(''), [cvc, setCvc] = useState('');
  const [outcome, setOutcome] = useState<'approved' | 'declined' | 'cancelled'>('approved');
  const [error, setError] = useState(''), [reviewStamp, setReviewStamp] = useState(''), [busy, setBusy] = useState(false);
  const [addressAttempted, setAddressAttempted] = useState(false);
  const postcodeInput = useRef<HTMLInputElement>(null);
  const attempt = useRef(''), submitting = useRef(false), stepHeading = useRef<HTMLHeadingElement>(null), firstMount = useRef(true);
  useEffect(() => {
    if (!firstMount.current) stepHeading.current?.focus();
    firstMount.current = false;
  }, [step]);
  function move(next: number) { setError(''); setStep(next); }
  const lines = orderLines(shop.cart);
  const unavailable = lines.some(line => line.quantity > shop.stockFor(line.id) || (!shop.professionalApproved && catalogue.find(item => item.id === line.id)?.professional));
  function confirmDelivery(event: FormEvent) {
    event.preventDefault();
    setAddressAttempted(true);
    if (!validAddress(address)) {
      setError('Check the address fields and use a delivery postcode in England, Scotland or Wales.');
      if (!deliverablePostcode(address.postcode)) postcodeInput.current?.focus();
      return;
    }
    setAddress({ name: address.name.trim(), email: address.email.trim(), line1: address.line1.trim(), line2: address.line2.trim(), city: address.city.trim(), postcode: address.postcode.trim().toUpperCase() });
    move(1);
  }
  function confirmPayment(event: FormEvent) {
    event.preventDefault();
    if (method === 'card') {
      const digits = number.replace(/\s/g, '');
      const approved = digits === demoCard.approved.replace(/\s/g, '');
      const declined = digits === demoCard.declined.replace(/\s/g, '');
      if ((!approved && !declined) || expiry !== demoCard.expiry || cvc !== demoCard.cvc) {
        setError('Use one of the two demo card numbers with expiry 12/30 and security code 123.'); return;
      }
      setOutcome(approved ? 'approved' : 'declined');
    }
    setNumber(''); setExpiry(''); setCvc('');
    setReviewStamp(basketStamp(shop.cart));
    attempt.current = crypto.randomUUID();
    move(2);
  }
  async function place() {
    if (submitting.current) return;
    if (outcome !== 'approved') {
      setStep(1);
      setError(outcome === 'declined' ? 'Demo payment declined. Your basket is saved. Choose the approved sample to try again.' : 'Demo payment cancelled. Your basket is saved. Choose another outcome or return to your basket.');
      return;
    }
    submitting.current = true; setBusy(true);
    try {
      const result = await shop.placeOrder({ id: attempt.current, basket: reviewStamp, address, delivery, payment: method });
      if (result.ok) { router.replace('/orders/' + result.id); return; }
      setError(result.error);
    } catch { setError('The demo could not complete this order. Please try again.'); }
    submitting.current = false; setBusy(false);
  }
  function fillCard(which: 'approved' | 'declined') { setNumber(demoCard[which]); setExpiry(demoCard.expiry); setCvc(demoCard.cvc); setError(''); }
  if (busy && !lines.length) return <p className="order-loading" role="status">Opening your order confirmation…</p>;
  if (!lines.length) return <EmptyBag/>;
  if (unavailable) return <div className="order-panel"><h2>Review your basket</h2><p>Adjust unavailable quantities or remove products requiring professional approval.</p><ShopLinkButton href="/cart">Return to basket</ShopLinkButton></div>;
  const changed = step === 2 && reviewStamp !== basketStamp(shop.cart);
  return <div className="order-columns">
    <section className="order-flow">
      <ol className="order-steps" aria-label="Checkout progress">{steps.map((text, index) => <li key={text} aria-current={index === step ? 'step' : undefined}>
        <span aria-hidden>{index < step ? <Check size={14}/> : index + 1}</span>{text}
      </li>)}</ol>
      <h2 ref={stepHeading} tabIndex={-1}>{['Delivery details', 'Payment method', 'Review your order'][step]}</h2>
      {error && <p className="order-error" role="alert">{error}</p>}
      {step === 0 && <form onSubmit={confirmDelivery} className="order-form">
        <div className="order-demo-note"><p>Use a fictional name and address for this demo.</p><Button size="sm" variant="secondary" onClick={() => setAddress({ ...sampleAddress, ...(account && { email: account.email, name: account.name }) })}>Fill sample details</Button></div>
        {account ? <p className="order-note">Checking out as {account.name}.</p> : <p className="order-note">Continue as a guest or <Link href="/account?next=/checkout">open your account</Link>.</p>}
        {Boolean(account?.addresses.length) && <Select label="Saved delivery addresses" defaultValue="" onChange={e => {
          const choice = account?.addresses.find(item => item.id === e.target.value);
          if (choice && account) setAddress({ name: choice.name, line1: choice.line1, line2: choice.line2, city: choice.city, postcode: choice.postcode, email: account.email });
        }} options={[{ value: '', label: 'Choose a saved address' }, ...(account?.addresses ?? []).map(item => ({ value: item.id, label: item.label + ' · ' + item.postcode }))]}/>}
        <div className="order-field-grid">{fields.map(field => <TextInput key={field.key} label={field.label}
          type={'type' in field ? field.type : 'text'} required={field.key !== 'line2'} maxLength={field.key === 'postcode' ? 9 : 140}
          ref={field.key === 'postcode' ? postcodeInput : undefined}
          error={field.key === 'postcode' && addressAttempted && !deliverablePostcode(address.postcode) ? 'Enter a Great Britain delivery postcode.' : undefined}
          readOnly={field.key === 'email' && Boolean(account)} value={address[field.key]} onChange={e => setAddress({ ...address, [field.key]: e.target.value })}/>)}</div>
        <fieldset className="order-options"><legend>Delivery service</legend><p>Demo delivery to England, Scotland and Wales.</p>
          {(Object.keys(deliveryMethods) as Delivery[]).map(key => <label key={key} className="order-choice">
            <input type="radio" name="shipping" value={key} checked={key === delivery} onChange={() => setDelivery(key)}/>{key === 'standard' ? <Package aria-hidden size={20}/> : <Truck aria-hidden size={20}/>}
            <span><strong>{deliveryMethods[key].label}</strong><small>{deliveryMethods[key].estimate}</small></span>
            <b>{totals(lines, key).deliveryPence ? money(totals(lines, key).deliveryPence) : 'Free'}</b>
          </label>)}</fieldset>
        <Button type="submit">Continue to payment <ArrowRight size={16} aria-hidden/></Button>
      </form>}
      {step === 1 && <form onSubmit={confirmPayment} className="order-form" autoComplete="off">
        <p className="order-note">This checkout simulates payment locally. Use sample details only.</p>
        <fieldset className="order-methods"><legend>Choose a demo payment method</legend>{methods.map(key => <label key={key}>
          <input type="radio" checked={method === key} name="method" onChange={() => { setMethod(key); setOutcome('approved'); setNumber(''); setExpiry(''); setCvc(''); setError(''); }}/>
          {key === 'card' ? <CreditCard aria-hidden size={18}/> : <Wallet aria-hidden size={18}/>} {paymentLabels[key]}
        </label>)}</fieldset>
        {method === 'card' ? <>
          <div className="order-demo-note"><div><strong>Sample cards</strong><p>Fill an approved or declined card to try either outcome.</p></div>
            <div className="order-buttons"><Button size="sm" variant="secondary" onClick={() => fillCard('approved')}>Use approved card</Button><Button size="sm" variant="ghost" onClick={() => fillCard('declined')}>Use declined card</Button></div></div>
          <TextInput label="Demo card number" inputMode="numeric" autoComplete="off" placeholder={demoCard.approved} value={number} maxLength={19} required onChange={e => setNumber(e.target.value.replace(/[^0-9]/g, '').slice(0,16).replace(/(.{4})/g, '$1 ').trim())}/>
          <div className="order-field-grid"><TextInput label="Expiry (MM/YY)" inputMode="numeric" maxLength={5} placeholder="12/30" required autoComplete="off" value={expiry} onChange={e => { const digits=e.target.value.replace(/\D/g,'').slice(0,4); setExpiry(digits.length > 2 ? digits.slice(0,2)+'/'+digits.slice(2) : digits); }}/>
            <TextInput label="Security code" type="password" inputMode="numeric" maxLength={3} placeholder="123" autoComplete="off" required value={cvc} onChange={e => setCvc(e.target.value.replace(/\D/g,''))}/></div>
        </> : <Select label="Demo payment outcome" options={[{value:'approved',label:'Approved'},{value:'declined',label:'Declined'},{value:'cancelled',label:'Cancelled'}]} value={outcome} onChange={e => setOutcome(e.target.value as typeof outcome)}/>}
        <div className="order-buttons"><Button variant="secondary" onClick={() => move(0)}><ArrowLeft size={15} aria-hidden/>Delivery</Button><Button type="submit">Review order <ArrowRight size={16} aria-hidden/></Button></div>
      </form>}
      {step === 2 && <div className="order-form">
        <div className="order-review"><header><h3>Deliver to</h3><Button size="sm" variant="ghost" onClick={() => move(0)}>Edit delivery</Button></header>
          <p>{address.name}<br/>{address.line1}{address.line2 && <><br/>{address.line2}</>}<br/>{address.city}, {address.postcode}<br/>{address.email}</p>
          <p>{deliveryMethods[delivery].label} · {deliveryMethods[delivery].estimate}</p></div>
        <div className="order-review"><header><h3>Payment</h3><Button size="sm" variant="ghost" onClick={() => move(1)}>Edit payment</Button></header>
          <p>{paymentLabels[method]}{method === 'card' && (outcome === 'declined' ? ' ending in 0002' : ' ending in 4242')}</p></div>
        <p className="order-note">Placing this demo order creates a local receipt and delivery timeline. No money is taken.</p>
        {changed && <p className="order-error" role="alert">Your basket has changed. Review the new contents and total.</p>}
        {changed ? <Button onClick={() => { setReviewStamp(basketStamp(shop.cart)); setError(''); }}>Accept updated basket</Button> :
          <Button onClick={place} loading={busy}>Place demo order · {money(totals(lines, delivery).totalPence)} <ArrowRight size={16} aria-hidden/></Button>}
      </div>}
    </section>
    <Summary lines={lines} delivery={delivery} previews><Link className="order-textlink" href="/cart">Edit basket</Link></Summary>
  </div>;
}
export function CheckoutPage() {
  const { ready, storageAvailable } = useShop(), { account } = useAccount();
  return <JourneyPage label="Checkout" title={<>Your <em>checkout.</em></>}>
    {ready && !storageAvailable && <p className="order-note" role="status">Browser storage is unavailable. Keep this tab open through checkout.</p>}
    {ready ? <CheckoutForm key={account?.id || 'guest'}/> : <LoadingShop/>}
  </JourneyPage>;
}
