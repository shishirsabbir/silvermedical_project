import type { Metadata } from 'next';
import { SilverEditStorefront } from '../features/home/storefront';

const title = 'The Silver Edit | Silver Medical UK';
const description = 'Explore The Silver Edit, a considered collection of diagnostic instruments, medical supplies and practice essentials from Silver Medical UK.';
const sharingImage = {
  url: '/brand/identity/silver-edit-social.png',
  width: 1200,
  height: 630,
  type: 'image/png',
  alt: 'The Silver Edit by Silver Medical UK. Instruments and practice essentials. The silver interlocking mark on emerald.',
};

export const metadata: Metadata = {
  title: { absolute: title },
  description,
  alternates: { canonical: '/' },
  openGraph: {
    type: 'website', locale: 'en_GB', siteName: 'Silver Medical', url: '/',
    title, description, images: [sharingImage],
  },
  twitter: { card: 'summary_large_image', title, description, images: [sharingImage] },
  robots: { index: false, follow: false },
};

export default function HomePage() {
  return <SilverEditStorefront />;
}
