'use client';

import { useState } from 'react';
import { BrandLogo } from '@silver-medical/ui/brand';
import { Specimen } from './specimen';

const palette = [
  ['Deep emerald', 'deep', '#082F26'], ['Evergreen', 'green', '#123E33'],
  ['Ink', 'ink', '#173A31'], ['Muted text', 'muted', '#56675E'],
  ['Silver', 'silver', '#AAB6B1'], ['Mist', 'mint', '#EAF1E9'], ['Paper', 'paper', '#FAFBF7'],
  ['Border', 'line', '#D5DFD7'], ['Focus', 'focus', '#397A60'],
  ['Success', 'success', '#216442'], ['Warning', 'warning', '#79521B'], ['Error', 'danger', '#A23635'],
];

export function BrandExamples() {
  const [announcement, setAnnouncement] = useState('');
  async function copyToken(token: string) {
    try {
      await navigator.clipboard.writeText('var(--sm-' + token + ')');
      setAnnouncement('Copied var(--sm-' + token + ')');
    } catch {
      setAnnouncement('Select and copy this token: var(--sm-' + token + ')');
    }
  }
  return <>
    <Specimen title="Logo artwork" description="Use the full wordmark in a header and the silver emblem in a compact placement." usage={'<BrandLogo variant="reversed" size={180} />'}>
      <div className="lib-lockups">
        <div><BrandLogo size={188}/><span>Light surfaces</span></div>
        <div><BrandLogo size={188} variant="reversed"/><span>Dark surfaces</span></div>
        <div><BrandLogo size={54} variant="mark"/><span>Compact mark</span></div>
        <div><BrandLogo size={90} variant="stacked"/><span>Stacked signature</span></div>
      </div>
    </Specimen>
    <Specimen title="Colour tokens" description="Select a swatch to copy its CSS custom property.">
      <div className="lib-swatch-grid">{palette.map(([name, token, hex]) => <button key={token} type="button" onClick={() => copyToken(token)} aria-label={'Copy ' + name + ' colour token'}>
        <i style={{background: 'var(--sm-' + token + ')'}}/><strong>{name}</strong><code>{hex}</code><small>--sm-{token}</small>
      </button>)}</div><p className="lib-status-line" role="status">{announcement}</p>
    </Specimen>
  </>;
}
export function TypeExamples() {
  return <>
    <Specimen title="Typography" description="Set editorial headings in Cormorant Garamond. Use Manrope for product names, prices, navigation and forms.">
      <div className="lib-type-table">
        <div><label>Editorial display</label><span className="lib-editorial-type">Behind every moment of <i>care.</i></span><code>--sm-serif</code></div>
        <div><label>Interface heading</label><span className="lib-interface-type">Selected essentials</span><code>--sm-sans</code></div>
        <div><label>Body</label><span>Explore instruments and everyday supplies for your practice.</span><code>--sm-font-body</code></div>
        <div><label>Label</label><strong className="lib-example-label">Add to basket</strong><code>--sm-font-label</code></div>
        <div><label>Caption</label><span className="lib-example-caption">Box of 100 · Medium</span><code>--sm-font-caption</code></div>
      </div>
    </Specimen>
    <Specimen title="Spacing" description="Use the scale for gaps, control padding and section rhythm.">
      <div className="lib-scale">{[1, 2, 3, 4, 6, 8, 12, 16].map(n => <div key={n}><code>--sm-space-{n}</code><i style={{width:'var(--sm-space-' + n + ')'}}/><span>{n * 4}px</span></div>)}</div>
    </Specimen>
    <Specimen title="Corners &amp; focus">
      <div className="lib-shapes">{[['Controls','--sm-radius'],['Cards','--sm-radius-card'],['Round','--sm-radius-round']].map(([name, token]) => <div key={token}><i style={{borderRadius:'var(' + token + ')'}}/><strong>{name}</strong><code>{token}</code></div>)}</div>
      <p className="lib-help">Keyboard focus uses the focus colour and an offset outline. Motion follows the system’s reduced-motion preference.</p>
    </Specimen>
  </>;
}
