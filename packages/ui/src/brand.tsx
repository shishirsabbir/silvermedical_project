import type { CSSProperties } from 'react';

const brandFiles = {
  light: 'silver-medical.svg',
  reversed: 'silver-medical-reversed.svg',
  mark: 'silver-medical-mark.svg',
  stacked: 'silver-medical-stacked.svg',
} as const;

export interface BrandLogoProps {
  variant?: keyof typeof brandFiles;
  size?: number;
  alt?: string;
  className?: string;
}

export function BrandLogo({ variant = 'light', size = 176, alt = 'Silver Medical UK', className = '' }: BrandLogoProps) {
  const horizontal = variant === 'light' || variant === 'reversed';
  const style: CSSProperties = { width: size, aspectRatio: horizontal ? '4.65' : '1' };
  return (
    <span className={`sm-brand-logo ${className}`} style={style}>
      <img src={`/brand/${brandFiles[variant]}`} alt={alt} width="300" height="300" />
    </span>
  );
}
