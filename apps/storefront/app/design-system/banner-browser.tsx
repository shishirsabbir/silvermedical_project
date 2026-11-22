'use client';

import { useState } from 'react';
import { Download, Monitor, Smartphone } from 'lucide-react';
import { Button, LinkButton, Select } from '@silver-medical/ui/controls';
import { banners, type BannerAsset } from '../../features/assets/banners';

const bannerKinds: readonly BannerAsset['kind'][] = ['Homepage', 'Department', 'Collection'];
const crops = [{ id: 'desktop', label: 'Desktop', Icon: Monitor }, { id: 'mobile', label: 'Mobile', Icon: Smartphone }] as const;

export function BannerBrowser() {
  const [bannerId, setBannerId] = useState<string>(banners[0].id);
  const [crop, setCrop] = useState<'desktop' | 'mobile'>('desktop');
  const selected = banners.find(banner => banner.id === bannerId) ?? banners[0];
  const image = selected[crop];

  return <div className="asset-banner">
    <div className="asset-banner-tools">
      <Select label="Banner artwork" value={selected.id} onChange={event => setBannerId(event.target.value)}>
        {bannerKinds.map(kind => <optgroup key={kind} label={kind}>
          {banners.filter(banner => banner.kind === kind).map(banner => <option key={banner.id} value={banner.id}>{banner.title}</option>)}
        </optgroup>)}
      </Select>
      <div role="group" aria-label="Preview crop" className="asset-crop">
        {crops.map(({ id, label, Icon }) => <Button key={id} size="sm" variant="ghost" aria-pressed={id === crop} onClick={() => setCrop(id)}>
          <Icon size={15} aria-hidden="true" />{label}
        </Button>)}
      </div>
    </div>
    <figure>
      <div className={'asset-banner-stage asset-banner-stage--' + crop}>
        <img key={image.src} src={image.src} alt={selected.alt} width={image.width} height={image.height} />
      </div>
      <figcaption>
        <span><strong>{selected.title}</strong><small>{image.width} × {image.height} · WebP</small></span>
        <LinkButton variant="secondary" size="sm" href={image.src} download aria-label={'Download ' + selected.title + ' ' + crop + ' crop as WebP'}>
          <Download size={15} aria-hidden="true" />Download crop
        </LinkButton>
      </figcaption>
    </figure>
  </div>;
}
