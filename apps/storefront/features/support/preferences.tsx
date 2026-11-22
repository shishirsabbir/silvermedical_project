'use client';

import { useEffect, useState } from 'react';
import { Button, StatusMessage, Switch } from '@silver-medical/ui/controls';

const KEY = 'silver-edit.consent.v1';
type Preferences = { analytics: boolean; marketing: boolean };
const essentialOnly: Preferences = { analytics: false, marketing: false };

function readPreferences(): Preferences {
  try {
    const item = JSON.parse(localStorage.getItem(KEY) || 'null');
    return { analytics: item?.analytics === true, marketing: item?.marketing === true };
  } catch { return essentialOnly; }
}

export function Preferences() {
  const [preferences, setPreferences] = useState(essentialOnly);
  const [ready, setReady] = useState(false);
  const [saved, setSaved] = useState('');
  const [error, setError] = useState(false);
  useEffect(() => {
    setPreferences(readPreferences()); setReady(true);
    function sync(event: StorageEvent) { if (event.key === KEY || event.key === null) { setPreferences(readPreferences()); setSaved(''); } }
    window.addEventListener('storage', sync); return () => window.removeEventListener('storage', sync);
  }, []);
  function save(value: Preferences) {
    try {
      localStorage.setItem(KEY, JSON.stringify(value)); setPreferences(value); setError(false);
      setSaved(value.analytics || value.marketing ? 'Your choices have been saved.' : 'Only essential storage is enabled.');
    } catch { setError(true); setSaved('Your browser could not save these preferences.'); }
  }
  return <section className="se-service-card se-preferences">
    <h2>Your choices</h2><p>Optional settings start switched off. This frontend loads no analytics or advertising services.</p>
    <div><h3>Essential storage</h3><p>Keeps items in your basket, remembers the signed-in demo session and saves orders and preferences on this browser.</p></div>
    <div><Switch label="Analytics" checked={preferences.analytics} disabled={!ready} onCheckedChange={analytics => { setPreferences({ ...preferences, analytics }); setSaved(''); }}
      hint="Allow measurement of page visits and shopping journeys when an analytics service is connected."/></div>
    <div><Switch label="Marketing" checked={preferences.marketing} disabled={!ready} onCheckedChange={marketing => { setPreferences({ ...preferences, marketing }); setSaved(''); }}
      hint="Allow marketing technologies when a service is connected."/></div>
    <div className="se-buttons"><Button disabled={!ready} onClick={() => save(preferences)}>Save choices</Button>
      <Button disabled={!ready} variant="secondary" onClick={() => save(essentialOnly)}>Use essential only</Button></div>
    {saved && <StatusMessage tone={error ? 'error' : 'success'}>{saved}</StatusMessage>}
  </section>;
}
