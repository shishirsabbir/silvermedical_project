import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import { ToastProvider } from '@silver-medical/ui/overlays';
import { AccountProvider } from '../features/account/account-provider';
import { ShopProvider } from '../features/shop/shop-provider';
import { StoreFrame } from '../features/shell/store-frame';
import '@silver-medical/ui/tokens.css';
import './globals.css';
import '@silver-medical/ui/controls.css';
import '@silver-medical/ui/navigation.css';
import '@silver-medical/ui/overlays.css';
import '@silver-medical/ui/commerce.css';

export const metadata: Metadata = {
  metadataBase: new URL('https://silvermedical.co.uk'),
  title: { default: 'Silver Medical | The Silver Edit', template: '%s | Silver Medical' },
  description: 'Explore the Silver Medical collection of instruments, practice equipment and everyday medical supplies.',
  icons: {
    icon: [
      { url: '/favicon.ico', type: 'image/x-icon', sizes: '16x16 32x32 48x48' },
      { url: '/brand/identity/favicon.svg', type: 'image/svg+xml', sizes: 'any' },
    ],
    apple: { url: '/brand/identity/apple-touch-icon.png', type: 'image/png', sizes: '180x180' },
  },
  robots: { index: false, follow: false },
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en-GB">
      <body><ToastProvider><AccountProvider><ShopProvider><StoreFrame>{children}</StoreFrame></ShopProvider></AccountProvider></ToastProvider></body>
    </html>
  );
}
