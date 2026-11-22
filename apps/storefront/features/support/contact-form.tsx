'use client';

import { useState, type FormEvent } from 'react';
import { Button, Select, Textarea, TextInput, StatusMessage } from '@silver-medical/ui/controls';

export function ContactForm() {
  const [preview, setPreview] = useState<{ reference: string; topic: string; email: string; body: string } | null>(null);
  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    setPreview({ reference: 'ENQ-' + crypto.randomUUID().slice(0, 8).toUpperCase(),
      topic: String(data.get('topic')), email: String(data.get('email')), body: String(data.get('message')) });
  }
  if (preview) return <div className="se-service-form">
    <StatusMessage tone="success" title="Sample enquiry prepared">Reference {preview.reference}. This preview keeps the message on screen and sends no email.</StatusMessage>
    <div><h2>{preview.topic}</h2><p>{preview.email}</p><p style={{ whiteSpace: 'pre-line' }}>{preview.body}</p></div>
    <Button variant="secondary" onClick={() => setPreview(null)}>Prepare another enquiry</Button>
  </div>;
  return <form className="se-service-form" onSubmit={submit}>
    <h2>Prepare an enquiry</h2><p>Use example details. This form previews the support journey and does not contact a live team.</p>
    <div className="se-field-row"><TextInput name="name" label="Name" placeholder="Alex Taylor" maxLength={80} required/>
      <TextInput name="email" label="Email address" type="email" placeholder="alex@example.test" maxLength={160} required/></div>
    <Select name="topic" label="What can we help with?" options={['Order and delivery', 'Product details', 'Professional account', 'Returns and refunds', 'Other enquiry'].map(value => ({ value, label: value }))}/>
    <Textarea name="message" label="Your message" maxLength={1500} hint="Keep medical or personal details out of your example." required/>
    <Button type="submit">Prepare sample enquiry</Button>
  </form>;
}
