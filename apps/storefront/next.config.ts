import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  transpilePackages: ['@silver-medical/ui'],
  devIndicators: false,
};

export default nextConfig;
