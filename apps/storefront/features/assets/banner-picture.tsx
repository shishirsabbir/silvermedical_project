import type { BannerAsset } from './banners';

interface BannerPictureProps {
  asset: BannerAsset;
  /** Use an empty alternative when the heading already conveys the same information. */
  alt?: string;
  priority?: boolean;
  className?: string;
}

export function BannerPicture({ asset, alt = asset.alt, priority, className }: BannerPictureProps) {
  return (
    <picture className={className}>
      <source media="(max-width: 48rem)" srcSet={asset.mobile.src} width={asset.mobile.width} height={asset.mobile.height} />
      <img src={asset.desktop.src} alt={alt} width={asset.desktop.width} height={asset.desktop.height}
        loading={priority ? 'eager' : 'lazy'} fetchPriority={priority ? 'high' : undefined} />
    </picture>
  );
}
