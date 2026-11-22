# Silver Medical storefront

The storefront implements **The Silver Edit** in the Next.js App Router. The homepage and design gallery import the same buttons, fields, product cards, catalogue filters, dialogs and basket rows from [`@silver-medical/ui`](../../packages/ui/README.md).

## Run locally

Run these commands from the repository root using Node.js 20.9 or newer and npm:

```powershell
npm install
npm run dev
```

| Route | What you can try |
|---|---|
| [Homepage](http://localhost:3000/) | Browse departments, search, sort, switch between product cards and a list, inspect products, save items and adjust a sample basket. |
| [Design system](http://localhost:3000/design-system) | Explore brand foundations and live examples of forms, menus, overlays, feedback and commerce components. Each gallery section has its own URL. |
| [Shopping demo](http://localhost:3000/demo) | Start a basket, preview service messages, or walk through a sample shipment. |
| [Catalogue](http://localhost:3000/shop) | Search by name or SKU, filter by department, availability and professional access, choose a variant and download its sample record. Try `SM-DG-101` or `SM-CS-201-S`. |
| [Account](http://localhost:3000/account) | Open the sample account or register a fictional one. Try the local verification inbox, sign-in, password reset, address book, professional application and order history. |
| [Basket](http://localhost:3000/cart) and [checkout](http://localhost:3000/checkout) | Change quantities, choose guest or account checkout, select delivery and review a sample payment. |
| [Tracking](http://localhost:3000/track) | Look up an order using its reference and delivery postcode. The sample shipment can be opened immediately. Advance delivery, request a return, complete a demo refund or print a receipt. |
| [Help](http://localhost:3000/help) and [preferences](http://localhost:3000/cookies) | Read delivery, returns and demo service information, prepare a sample enquiry, and update consent preferences. |

For a production-mode check, stop the development server, then run:

```powershell
npm run typecheck
npm run build
npm run start
```

## Cloudflare Workers client preview

The storefront and design system share one Worker named `silvermedical-project`. Open `/` for the storefront, select **Design system** to explore the shared colours, fonts and components, and use **View storefront** to return. The gallery also supports direct links such as `/design-system/brand` and `/design-system/overlays`. The demo keeps account, basket and order data in the visitor’s browser.

From the repository root, use Node.js 24 LTS and the workspace lockfile. Build once, check the deployment bundle, then start the local Workers runtime.

```sh
npm ci
npm run cf:build
npm run cf:check
npm run cf:preview
```

Open the local URL printed by Wrangler, normally `http://localhost:8787`. To exercise the design system and checkout in Chromium at mobile and desktop sizes, run `python scripts/qa/check_shopping_journey.py http://localhost:8787` in another terminal. Rebuild after source changes.

**Publishing to your Cloudflare account.** After testing the built bundle, run the following from the repository root. Select the intended account during sign-in. The deployment command publishes the Worker and prints the shareable `workers.dev` URL. Append `/design-system` to that URL to take the client directly to the gallery.

```sh
npx wrangler login
npm run cf:deploy
```

For a Git-connected deployment in the Cloudflare dashboard, use the repository root as the build directory so npm can resolve the shared UI workspace. The connected Worker, the Wrangler `name`, and the `service` for `WORKER_SELF_REFERENCE` must all use `silvermedical-project`. Set the build command to `npm run cf:build` and the deploy command to `npm run cf:deploy`. For branch previews, use `cd apps/storefront && npx wrangler preview` so Wrangler loads the storefront configuration. [Workers Builds configuration](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/).

The [Wrangler configuration](wrangler.jsonc) targets the preview subdomain. The [OpenNext configuration](open-next.config.ts) uses Workers Static Assets for the prerendered pages and their cache. The same Worker handles dynamic catalogue and order routes. The preview requires no database, payment credentials or R2 bucket. Its pages include `noindex` metadata. Anyone with the published preview URL can open it.

## Components and data

- The [shop provider](features/shop/shop-provider.tsx) keeps baskets, saved items and local orders across page loads. Signing into a demo account merges the guest basket. Account order history is scoped to the signed-in profile.
- The [catalogue](features/catalogue/catalogue.ts) supplies ten sample SKUs, including two glove sizes, an unavailable otoscope and a professional-only instrument set. Each product page has a canonical URL and descriptive product and breadcrumb data. The whole demo uses `noindex`. The [shopping feed](app/product-feed.xml/route.ts) excludes sample and unapproved records. [Google RSS product feed format](https://support.google.com/merchants/answer/14987622?hl=en-uk).
- The [gallery](app/design-system/library.ts) documents the public UI components. Edit shared behaviour and styles in `packages/ui/src/` so both the gallery and the storefront pick up a change.
- The [root layout](app/layout.tsx) loads the UI styles and mounts one `ToastProvider` for both routes. The local preview uses `noindex,nofollow` metadata.

## Demo and release handoff

### Test a complete purchase

Start at `/demo`, choose **Start a sample basket**, then **Continue to checkout**. Use **Fill sample details** or enter a fictional address. Demo shipping covers England, Scotland and Wales. Standard costs £3.95 or is free at £50. Express costs £6.95. Totals use integer pence and a single illustrative inclusive VAT rate.

| Card outcome | Test number | Expiry | Security code |
|---|---|---|---|
| Approved | 4242 4242 4242 4242 | 12/30 | 123 |
| Declined | 4000 0000 0000 0002 | 12/30 | 123 |

The payment form also has autofill buttons. Simulated Revolut Pay, PayPal, Apple Pay and Google Pay support approved, declined and cancelled outcomes. A successful payment creates one local order. The account area uses an in-browser verification inbox. Use fictional credentials and personal details.

Run `python scripts/qa/check_shopping_journey.py http://127.0.0.1:3141` from the root against a running preview. Adjust the port if needed. The check uses Playwright for Python and Chromium in isolated contexts. It covers navigation between the store and gallery, an interactive dialog, basket persistence, decline and retry, totals, delivery, return, refund and message previews at mobile and desktop sizes.

### Release boundaries from the 25-day plan

| Plan features | Implemented in the frontend | Required for live selling |
|---|---|---|
| F01–F03 | Responsive branded storefront, product discovery and SKU detail screens | Owner-reviewed product data, imagery, tax and sale eligibility for the actual warehouse assortment |
| F04–F05 | Guest and account journeys, address book, sample verification, professional application and demo approval | Server sessions, email verification and staff-reviewed buyer entitlements |
| F06–F08 | Basket, delivery totals, checkout, simulated card and wallet payments, retry and confirmation | Authoritative pricing/stock and approved payment providers with server-verified settlement |
| F09–F10 | Order messages, tracking and returns, service pages, consent, product metadata, sitemap and gated feed | Seller details, reviewed policies, actual dispatch and refund events, email delivery and publication approval |

The [dispatch artwork source](../../assets/branding/dispatch-master.png) and [export script](../../scripts/brand/build_shopping_assets.mjs) produce the shopping-demo photograph, sharing card and email header. The six shopping icons are in [the SVG sprite](public/icons/shopping.svg).

## Original logo artwork

The interlocking mark and **SilverMedical UK** lockup were redrawn as transparent SVGs with square canvases from the client-supplied mockup on 19 November 2026. The lettering is outlined, so the logo does not need a font download.

| Public URL | Use |
|---|---|
| `/brand/silver-medical.svg` | Horizontal lockup for light headers |
| `/brand/silver-medical-reversed.svg` | Horizontal silver lockup for dark green or charcoal backgrounds |
| `/brand/silver-medical-stacked.svg` | Stacked silver lockup from the reference for dark splash screens |
| `/brand/silver-medical-mark.svg` | Symbol-only silver SVG for compact placements on dark backgrounds |

Render the logo through the shared component to preserve the approved artwork and fit the horizontal lockup:

```tsx
import { BrandLogo } from '@silver-medical/ui/brand';

<BrandLogo variant="reversed" size={180} alt="Silver Medical UK" />
```

## Photographs and fonts

The [asset library](http://localhost:3000/design-system/assets) previews and downloads the homepage hero, three collection banners, eight department banners, eight SVG department icons, original logo variants, app icons and homepage sharing card. The [banner catalogue](features/assets/banners.ts) supplies the same images to the storefront. The browser selects the mobile composition at 768px and below. Banner headings and actions are HTML.

Ten new illustrative photo masters are in `assets/branding/banner-masters/`. Two collections reuse photography from the selected Silver Edit concept. To adjust a composition, edit the [crop settings](features/assets/art-direction.json) and run `node scripts/brand/build_banners.mjs` from the repository root. The script exports 24 optimised WebP files under `public/images/banners/`. The product grid still uses the original six-photo `products.webp` sheet. [Original concept photography notes](../../dev/designs/homepage-concepts/assets/prompts.json).

The browser and sharing files use the client mark. Regenerate these with `python scripts/brand/build_identity.py` from the repository root using Pillow and Playwright Chromium.

Manrope and Cormorant Garamond are served locally from `public/fonts/`. Include the original SIL Open Font License files when redistributing the fonts. [Manrope license](public/fonts/manrope-LICENSE.txt) and [Cormorant Garamond license](public/fonts/cormorantgaramond-LICENSE.txt).
