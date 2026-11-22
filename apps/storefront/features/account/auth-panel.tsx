'use client';

import Link from 'next/link';
import { useEffect, useRef, useState, type FormEvent } from 'react';
import { ArrowRight, MailOpen } from 'lucide-react';
import { Button, TextInput, StatusMessage } from '@silver-medical/ui/controls';
import { useAccount } from './account-provider';

export type AuthMode = 'signin' | 'register' | 'reset';

export function AuthPanel({ initialMode, professional, returnToCheckout }: { initialMode: AuthMode; professional: boolean; returnToCheckout: boolean }) {
  const auth = useAccount();
  const [mode, setMode] = useState<AuthMode>(initialMode);
  const [error, setError] = useState('');
  const [notice, setNotice] = useState('');
  const [busy, setBusy] = useState(false);
  const [openInbox, setOpenInbox] = useState(false);
  const [password, setPassword] = useState('');
  const formHeading = useRef<HTMLHeadingElement>(null);
  const challenge = auth.challenge;
  const challengeKind = challenge?.kind;
  useEffect(() => { if (challengeKind) formHeading.current?.focus(); }, [challengeKind]);

  function changeMode(next: AuthMode) {
    setMode(next); setError(''); setNotice(''); setPassword(''); setOpenInbox(false);
    if (auth.challenge) auth.cancelChallenge();
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const email = String(data.get('email') || '');
    setError(''); setNotice(''); setBusy(true);
    try {
      if (challenge) {
        await auth.completeChallenge(String(data.get('code') || ''), password);
        if (challenge.kind === 'reset') { changeMode('signin'); setNotice('Password updated. You can sign in with the new test password.'); }
      } else if (mode === 'reset') {
        auth.startReset(email);
      } else if (mode === 'register') {
        await auth.register(String(data.get('name') || ''), email, password);
      } else {
        await auth.signIn(email, password);
      }
      setPassword('');
    } catch (cause) { setError(cause instanceof Error ? cause.message : 'Please try again.'); }
    finally { setBusy(false); }
  }
  async function openSample() {
    setBusy(true); setError('');
    try { await auth.useSampleAccount(); }
    catch { setError('The sample account needs browser storage. Enable it and try again.'); }
    finally { setBusy(false); }
  }

  const title = challenge ? (challenge.kind === 'verify' ? 'Verify your email' : 'Choose a new password')
    : mode === 'register' ? 'Create an account' : mode === 'reset' ? 'Reset your password' : 'Sign in';
  return <div className="se-account-entry">
    <section className="se-service-card se-auth-form" aria-labelledby="sign-heading">
      <h2 id="sign-heading" ref={formHeading} tabIndex={-1}>{title}</h2>
      <p>{challenge ? 'Open the simulated inbox below to find your six-digit code. Codes expire in ten minutes.'
        : mode === 'reset' ? 'Enter the email you used for a demo account in this browser.'
        : mode === 'register' ? 'Use an example email and a password made just for this demo.'
        : 'Use a demo account you created on this browser.'}</p>
      <form onSubmit={submit} key={challenge ? challenge.kind + challenge.accountId : mode}>
        {challenge ? <>
          <div className="se-inbox"><Button size="sm" variant="secondary" aria-expanded={openInbox} aria-controls="se-demo-code" onClick={() => setOpenInbox(!openInbox)}><MailOpen size={16}/> {openInbox ? 'Close demo inbox' : 'Open demo inbox'}</Button>
            {openInbox && <p id="se-demo-code">Demo code <strong>{challenge.code}</strong></p>}</div>
          <TextInput name="code" label="Verification code" autoComplete="one-time-code" inputMode="numeric" pattern="[0-9]{6}" maxLength={6} placeholder="Six digits" required/>
        </> : <>
          {mode === 'register' && <TextInput name="name" label="Name" autoComplete="off" placeholder="Alex Taylor" maxLength={80} required/>}
          <TextInput type="email" name="email" label="Email address" autoComplete="off" placeholder="alex@example.test" maxLength={160} required/>
        </>}
        {((!challenge && mode !== 'reset') || challenge?.kind === 'reset') && <TextInput label={challenge ? 'New test password' : 'Test password'} type="password"
          autoComplete="off" value={password} onChange={event => setPassword(event.target.value)} required minLength={mode === 'signin' && !challenge ? 1 : 8} maxLength={128}
          hint={(mode === 'register' || challenge?.kind === 'reset') ? 'Use at least 8 characters.' : undefined}/>}
        {error && <StatusMessage tone="error">{error}</StatusMessage>}
        {notice && <StatusMessage tone="success">{notice}</StatusMessage>}
        <Button type="submit" loading={busy}>{challenge ? (challenge.kind === 'verify' ? 'Verify and sign in' : 'Update password') : mode === 'register' ? 'Create demo account' : mode === 'reset' ? 'Request reset code' : 'Sign in'} <ArrowRight size={17}/></Button>
      </form>
      <div className="se-auth-switch">
        {challenge ? <button onClick={() => changeMode(challenge.kind === 'reset' ? 'reset' : 'signin')}>Request another code</button> : <>
          {mode !== 'register' && <button onClick={() => changeMode('register')}>Create an account</button>}
          {mode !== 'signin' && <button onClick={() => changeMode('signin')}>Back to sign in</button>}
          {mode === 'signin' && <button onClick={() => changeMode('reset')}>Forgotten password?</button>}
        </>}
      </div>
    </section>
    <aside className="se-sample">
      <img src="/images/banners/clinical-workspace-mobile.webp" alt="" width={704} height={640}/>
      <div><h2>Explore a sample account.</h2>
        <p>{professional ? 'Open the practice account to try applying for professional purchasing access.' : 'Try the address book, professional application and order history with a fictional practice profile.'}</p>
        <Button variant="light" onClick={openSample} loading={busy}>Open sample account <ArrowRight size={16}/></Button>
        <Link href={returnToCheckout ? '/checkout' : '/shop'}>{returnToCheckout ? 'Continue checkout as a guest' : 'Continue shopping as a guest'}</Link>
      </div>
    </aside>
  </div>;
}
