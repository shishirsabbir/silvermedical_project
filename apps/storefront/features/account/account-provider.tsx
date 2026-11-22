'use client';

import { createContext, useContext, useEffect, useState, type ReactNode } from 'react';

export interface DemoAddress {
  id: string;
  label: string;
  name: string;
  line1: string;
  line2: string;
  city: string;
  postcode: string;
  country: 'GB';
}
export type ProfessionalStatus = 'none' | 'pending' | 'approved' | 'declined';
export interface DemoAccount {
  id: string;
  email: string;
  name: string;
  addresses: DemoAddress[];
  professionalStatus: ProfessionalStatus;
  organisation: string;
  profession: string;
  reviewerNote: string;
}
interface StoredAccount extends DemoAccount {
  verified: boolean;
  salt: string;
  digest: string;
}
interface Challenge {
  accountId: string;
  kind: 'verify' | 'reset';
  code: string;
  expires: number;
}
interface AccountContextValue {
  account: DemoAccount | null;
  ready: boolean;
  storageAvailable: boolean;
  professionalApproved: boolean;
  challenge: Challenge | null;
  register: (name: string, email: string, password: string) => Promise<void>;
  signIn: (email: string, password: string) => Promise<void>;
  signOut: () => void;
  useSampleAccount: () => Promise<void>;
  startReset: (email: string) => void;
  completeChallenge: (code: string, password?: string) => Promise<void>;
  cancelChallenge: () => void;
  setName: (name: string) => void;
  saveAddress: (address: DemoAddress) => void;
  removeAddress: (id: string) => void;
  applyProfessional: (organisation: string, profession: string) => void;
  simulateReview: (status: 'approved' | 'declined', note: string) => void;
}

const DB = 'silver-edit.demo.accounts.v1';
const SESSION = 'silver-edit.demo.session.v1';
const INBOX = 'silver-edit.demo.inbox.v1';
const DEMO_ID = 'silver-edit-sample-account';
const SAMPLE_EMAIL = 'alex.taylor@example.test';
const Context = createContext<AccountContextValue | null>(null);

function isObject(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}
function isText(value: unknown): value is string { return typeof value === 'string' && Boolean(value.trim()); }
function uniqueById<T extends { id: string }>(values: T[]): T[] {
  return [...new Map(values.map(value => [value.id, value])).values()];
}
function parseAddress(value: unknown): DemoAddress[] {
  if (!isObject(value) || value.country !== 'GB' || !isText(value.id) || !isText(value.name) || !isText(value.label)
    || !isText(value.line1) || !isText(value.city) || !isText(value.postcode)) return [];
  return [{ id: value.id, label: value.label, name: value.name, line1: value.line1,
    line2: typeof value.line2 === 'string' ? value.line2 : '', city: value.city, postcode: value.postcode, country: 'GB' }];
}
function parseAccount(value: unknown): StoredAccount[] {
  if (!isObject(value) || !isText(value.id) || !isText(value.name) || !isText(value.email)
    || typeof value.salt !== 'string' || typeof value.digest !== 'string') return [];
  if (value.id === DEMO_ID) {
    if (value.email !== SAMPLE_EMAIL || value.verified !== true) return [];
  } else if (!/^[a-f0-9]{32}$/.test(value.salt) || !/^[a-f0-9]{64}$/.test(value.digest)) return [];
  const status = value.professionalStatus;
  const addresses = Array.isArray(value.addresses) ? uniqueById(value.addresses.flatMap(parseAddress)) : [];
  return [{ id: value.id, name: value.name, email: normaliseEmail(value.email), verified: value.verified === true,
    digest: value.digest, salt: value.salt, addresses, professionalStatus: status === 'pending' || status === 'approved' || status === 'declined' ? status : 'none',
    organisation: typeof value.organisation === 'string' ? value.organisation : '', profession: typeof value.profession === 'string' ? value.profession : '',
    reviewerNote: typeof value.reviewerNote === 'string' ? value.reviewerNote : '' }];
}
function accounts(): StoredAccount[] {
  const raw = localStorage.getItem(DB);
  if (!raw) return [];
  try {
    const data: unknown = JSON.parse(raw);
    return Array.isArray(data) ? uniqueById(data.flatMap(parseAccount)) : [];
  } catch { return []; }
}

function normaliseEmail(value: string) { return value.trim().toLowerCase(); }
function validatePassword(password: string) {
  if (password.length < 8 || password.length > 128) throw new Error('Use a test password of 8 to 128 characters.');
}
const toHex = (value: Uint8Array) => Array.from(value, byte => byte.toString(16).padStart(2, '0')).join('');

async function hashPassword(password: string, salt: string) {
  const material = await crypto.subtle.importKey('raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveBits']);
  const digest = await crypto.subtle.deriveBits({
    name: 'PBKDF2', salt: Uint8Array.from(salt.match(/../g) ?? [], pair => parseInt(pair, 16)), iterations: 180000, hash: 'SHA-256',
  }, material, 256);
  return toHex(new Uint8Array(digest));
}

async function credentials(password: string) {
  validatePassword(password);
  const salt = toHex(crypto.getRandomValues(new Uint8Array(16)));
  return { salt, digest: await hashPassword(password, salt) };
}

function readChallenge(): Challenge | null {
  try {
    const value = JSON.parse(sessionStorage.getItem(INBOX) || 'null');
    return value && ['verify', 'reset'].includes(value.kind) && typeof value.code === 'string' && /^\d{6}$/.test(value.code)
      && typeof value.accountId === 'string' && Number.isFinite(value.expires) ? value : null;
  } catch { return null; }
}
function publicAccount(stored?: StoredAccount): DemoAccount | null {
  if (!stored?.verified) return null;
  const { id, name, email, addresses, professionalStatus, organisation, profession, reviewerNote = '' } = stored;
  return { id, name, email, addresses, professionalStatus, organisation, profession, reviewerNote };
}
function blankAccount(id: string, name: string, email: string): DemoAccount {
  return { id, name, email, addresses: [], professionalStatus: 'none', organisation: '', profession: '', reviewerNote: '' };
}

export function AccountProvider({ children }: { children: ReactNode }) {
  const [account, setAccount] = useState<DemoAccount | null>(null);
  const [challenge, setChallenge] = useState<Challenge | null>(null);
  const [ready, setReady] = useState(false);
  const [storageAvailable, setStorageAvailable] = useState(true);
  function syncSession() {
    try { setAccount(publicAccount(accounts().find(row => row.id === sessionStorage.getItem(SESSION)))); }
    catch { setAccount(null); }
  }

  useEffect(() => {
    try {
      const probe = 'silver-edit.demo.storage-check';
      for (const storage of [localStorage, sessionStorage]) { storage.setItem(probe, '1'); storage.removeItem(probe); }
    } catch { setStorageAvailable(false); }
    syncSession();
    setChallenge(readChallenge());
    setReady(true);
    function refresh(event: StorageEvent) { if (event.key === DB || event.key === null) syncSession(); }
    window.addEventListener('storage', refresh);
    return () => window.removeEventListener('storage', refresh);
  }, []);

  function commit(rows: StoredAccount[]) {
    localStorage.setItem(DB, JSON.stringify(rows));
    syncSession();
  }
  function activate(id: string) {
    sessionStorage.setItem(SESSION, id);
    syncSession();
  }
  function cancelChallenge() {
    sessionStorage.removeItem(INBOX);
    setChallenge(null);
  }
  function issue(accountId: string, kind: Challenge['kind']) {
    const value: Challenge = { accountId, kind, code: String(crypto.getRandomValues(new Uint32Array(1))[0] % 1000000).padStart(6, '0'), expires: Date.now() + 600000 };
    sessionStorage.setItem(INBOX, JSON.stringify(value));
    setChallenge(value);
  }
  async function register(name: string, input: string, password: string) {
    const email = normaliseEmail(input);
    if (!name.trim() || !email) throw new Error('Enter a name and email for this demo account.');
    const auth = await credentials(password);
    const rows = accounts();
    if (email === SAMPLE_EMAIL || rows.some(row => row.email === email)) throw new Error('This email already has a demo account. Sign in or reset its password.');
    const record = { ...blankAccount(crypto.randomUUID(), name.trim(), email), ...auth, verified: false };
    commit([...rows, record]);
    issue(record.id, 'verify');
  }
  async function signIn(input: string, password: string) {
    const email = normaliseEmail(input);
    const row = accounts().find(record => record.email === email);
    if (!row || row.id === DEMO_ID || await hashPassword(password, row.salt) !== row.digest)
      throw new Error('The email or test password does not match this browser’s account records.');
    if (!row.verified) { issue(row.id, 'verify'); return; }
    cancelChallenge();
    activate(row.id);
  }
  function signOut() {
    sessionStorage.removeItem(SESSION);
    cancelChallenge();
    setAccount(null);
  }
  async function useSampleAccount() {
    const rows = accounts();
    if (!rows.some(row => row.id === DEMO_ID)) {
      const row: StoredAccount = { ...blankAccount(DEMO_ID, 'Alex Taylor', SAMPLE_EMAIL), verified: true,
        salt: '', digest: '', addresses: [{ id: 'sample-practice', label: 'Practice', name: 'Alex Taylor', line1: '10 Example Lane', line2: '', city: 'London', postcode: 'SW1A 1AA', country: 'GB' }] };
      commit([...rows, row]);
    }
    cancelChallenge();
    activate(DEMO_ID);
  }
  function startReset(input: string) {
    const row = accounts().find(record => record.email === normaliseEmail(input));
    if (!row || row.id === DEMO_ID) throw new Error('Use an account you created in this browser. Open the sample account with the demo button.');
    issue(row.id, 'reset');
  }
  async function completeChallenge(code: string, password?: string) {
    const current = readChallenge();
    if (!current || current.expires <= Date.now()) throw new Error('This demo code expired. Request another code.');
    if (current.code !== code.trim()) throw new Error('Enter the six digits shown in the demo inbox.');
    const auth = current.kind === 'reset' ? await credentials(password || '') : {};
    const rows = accounts();
    const row = rows.find(record => record.id === current.accountId);
    if (!row) throw new Error('This demo account is no longer available.');
    commit(rows.map(record => record.id === row.id ? { ...record, ...auth, verified: true } : record));
    cancelChallenge();
    if (current.kind === 'verify') activate(row.id);
  }
  function change(update: (record: StoredAccount) => StoredAccount) {
    const currentId = sessionStorage.getItem(SESSION);
    if (!account || account.id !== currentId) throw new Error('Sign in to update your account.');
    const rows = accounts();
    if (!rows.some(row => row.id === currentId && row.verified)) throw new Error('This account is unavailable.');
    commit(rows.map(record => record.id === currentId ? update(record) : record));
  }
  function setName(name: string) {
    if (!name.trim()) throw new Error('Enter a name.');
    change(row => ({ ...row, name: name.trim() }));
  }
  function saveAddress(address: DemoAddress) {
    if (![address.label, address.name, address.line1, address.city].every(value => value.trim())) throw new Error('Complete the address fields.');
    const raw = address.postcode.toUpperCase().replace(/\s/g, '');
    if (!/^(GIR0AA|[A-Z]{1,2}\d[A-Z\d]?\d[A-Z]{2})$/.test(raw)) throw new Error('Enter a UK postcode, for example SW1A 1AA.');
    const value = { ...address, postcode: raw.slice(0, -3) + ' ' + raw.slice(-3) };
    change(row => ({ ...row, addresses: row.addresses.some(item => item.id === value.id) ? row.addresses.map(item => item.id === value.id ? value : item) : [...row.addresses, value] }));
  }
  function applyProfessional(organisation: string, profession: string) {
    if (!organisation.trim() || !profession.trim()) throw new Error('Enter an example organisation and select a role.');
    change(row => ({ ...row, profession, organisation: organisation.trim(), reviewerNote: '', professionalStatus: 'pending' }));
  }
  function simulateReview(status: 'approved' | 'declined', note: string) {
    change(row => {
      if (row.professionalStatus !== 'pending') throw new Error('Submit an application first.');
      return { ...row, professionalStatus: status, reviewerNote: note.trim().slice(0, 240) };
    });
  }
  return <Context.Provider value={{ account, challenge, ready, storageAvailable, professionalApproved: account?.professionalStatus === 'approved',
    register, signIn, signOut, useSampleAccount, startReset, completeChallenge, cancelChallenge, setName,
    saveAddress, removeAddress: id => change(row => ({ ...row, addresses: row.addresses.filter(x => x.id !== id) })), applyProfessional, simulateReview }}>
    {children}
  </Context.Provider>;
}

export function useAccount() {
  const value = useContext(Context);
  if (!value) throw new Error('AccountProvider is required.');
  return value;
}
