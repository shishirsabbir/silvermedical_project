'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Button } from '@silver-medical/ui/controls';
import { useShop } from '../shop/shop-provider';

export function DemoStart() {
  const shop = useShop();
  const router = useRouter();
  const [message, setMessage] = useState('');
  function start() {
    if (!Object.keys(shop.cart).length && !shop.addItem('stethoscope') && !shop.addItem('gauze')) {
      setMessage('The starter items are sold out in this browser. Choose another item in the catalogue.');
      return;
    }
    router.push('/cart');
  }
  return <><Button variant="light" disabled={!shop.ready} onClick={start}>Start a sample basket</Button>
    {message && <p role="status">{message} <a href="/shop">Browse products</a></p>}</>;
}

