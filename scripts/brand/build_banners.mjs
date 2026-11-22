import { mkdir, readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import sharp from 'sharp';

const project = fileURLToPath(new URL('../../', import.meta.url));
const images = path.join(project, 'apps/storefront/public/images');
const masters = path.join(project, 'assets/branding/banner-masters');
const output = path.join(images, 'banners');
const direction = JSON.parse(await readFile(
  path.join(project, 'apps/storefront/features/assets/art-direction.json'), 'utf8'
));

await mkdir(output, { recursive: true });

for (const [id, shot] of Object.entries(direction.shots)) {
  const source = shot.source ? path.join(images, shot.source) : path.join(masters, id + '.webp');
  const original = await sharp(source).metadata();
  for (const [crop, [width, height]] of Object.entries(direction.profiles[shot.profile])) {
    // Align within the excess image area after fitting the crop. Optional zoom tightens the subject.
    const [alignX, alignY, zoom = 1] = shot[crop];
    const scale = Math.min(original.width / width, original.height / height) / zoom;
    const cropWidth = Math.round(width * scale);
    const cropHeight = Math.round(height * scale);
    const left = Math.round((original.width - cropWidth) * alignX);
    const top = Math.round((original.height - cropHeight) * alignY);
    await sharp(source)
      .extract({ left, top, width: cropWidth, height: cropHeight })
      .resize(width, height)
      .webp({ quality: 85, effort: 5 })
      .toFile(path.join(output, id + '-' + crop + '.webp'));
  }
}
