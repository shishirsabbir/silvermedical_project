import type { MetadataRoute } from 'next';
import { guides } from '../features/home/guides';

// Public editorial URLs only. Sample SKUs, accounts and transaction links are excluded.
export default function sitemap(): MetadataRoute.Sitemap {
  return ['/', '/departments', '/journal', ...guides.map(g => '/journal/' + g.id)]
    .map(path => ({ url: new URL(path, 'https://silvermedical.co.uk').href }));
}

