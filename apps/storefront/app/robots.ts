import type { MetadataRoute } from 'next';

// The current catalogue and payment environment are illustrative.
export default function robots(): MetadataRoute.Robots {
  return { rules: { userAgent: '*', disallow: '/' } };
}

