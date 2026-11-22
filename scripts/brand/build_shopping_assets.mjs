import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import sharp from 'sharp';

const root = fileURLToPath(new URL('../../', import.meta.url));
const publicDir = path.join(root, 'apps/storefront/public');
const brand = path.join(publicDir, 'brand');
const generated = path.join(brand, 'identity');
const master = path.join(root, 'assets/branding/dispatch-master.png');
const wordmark = await readFile(path.join(brand, 'silver-medical-reversed.svg'), 'utf8');

function logo(x, y, width, height) {
  return wordmark.replace(/<svg[^>]*>/, '<svg x="' + x + '" y="' + y + '" width="' + width + '" height="' + height + '" viewBox="0 0 300 67">');
}

const header = '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="150"><rect width="900" height="150" fill="#082f26"/>' +
  '<g stroke="#527565" fill="none"><circle cx="840" cy="37" r="159"/><circle cx="840" cy="37" r="140"/><circle cx="840" cy="37" r="122"/></g>' +
  logo(47, 40, 288, 70) + '</svg>';
await sharp(Buffer.from(header)).png().toFile(path.join(generated, 'service-email-header.png'));

await sharp(master).resize(960,720,{ fit:'cover', position:'centre' }).webp({ quality:86 }).toFile(path.join(publicDir, 'images/dispatch.webp'));
const photograph = await sharp(master).resize(580,630,{ fit:'cover', position:'centre' }).png().toBuffer();
const card = '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630"><rect width="1200" height="630" fill="#082f26"/>' +
  logo(52, 44, 236, 54) +
  '<g fill="#f7f6ed" font-family="Georgia, serif"><text x="53" y="290" font-size="80">From basket</text><text x="53" y="376" font-size="80" font-style="italic">to doorstep.</text></g>' +
  '<path d="M56 509H544" stroke="#638376"/><text x="56" y="553" fill="#e2ecdc" font-family="sans-serif" font-size="22">silvermedical.co.uk</text></svg>';
await sharp(Buffer.from(card)).composite([{ input: photograph, left:620, top:0 }]).jpeg({ quality:90 }).toFile(path.join(generated, 'shopping-demo-social.jpg'));

