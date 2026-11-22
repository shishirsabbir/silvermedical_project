# Hosting architecture and Cloudflare cost estimate

Status update, 8 November 2026: frontend hosting has changed to Hostinger. The Cloudflare runtime architecture and estimates below preserve the earlier scenario, not the current deployment choice. Admin/API/PostgreSQL also remain on Hostinger; Cloudflare domain and R2 remain selected. Current costs/capacity require review after the deployment approach is discussed. No infrastructure implementation has started.

Checked: 7 November 2026. This records the user's intended deployment and an assumption-led estimate, not a measured bill or a deployed system.

## Confirmed direction

- Next.js storefront frontend on Cloudflare.
- Admin application, API and PostgreSQL on Hostinger KVM 4.
- Product images are optimised during upload through the admin panel, as confirmed by the user. Pre-generated variants will be served directly; Cloudflare on-demand transformations are not part of the planned cost model. R2 is now selected for image/object storage; processing implementation and delivery/cache configuration are undecided.
- Cost-planning traffic: 10,000 daily visitors assumed. The user's word traffic does not establish whether this means visitors, page views or HTTP requests.

The supplied Hostinger screenshot lists KVM 4 with 4 vCPU cores, 16GB RAM, 200GB NVMe and 16TB bandwidth. It shows GBP9.99/month equivalent, GBP239.76 paid for 24 months, and GBP24.99/month renewal for the same term. These are screenshot observations, not an independently verified current checkout quote; tax, optional services and actual contract must be checked separately.

## Proposed request flow

    Browser → Cloudflare frontend/static assets
    Cloudflare frontend or browser → HTTPS API on KVM 4
    API → PostgreSQL over a private/local connection
    Staff → protected admin application on KVM 4

Keep database credentials server-side and database access private. Use the API for catalogue, search, price, stock, accounts and orders. Exact browser-versus-server API calls, authentication, cross-origin rules and session design remain implementation decisions.

Product/category content can use caching or pre-rendering; account, contract-price, cart and checkout content need appropriate private/session handling. Do not cache one customer's negotiated prices or account data into public responses. The API must revalidate price, stock, permissions and tax at order acceptance.

## Cloudflare hosting choices

Static assets can be served without request charges; invoking application code changes the billing route. Static export on Pages is an option when server-rendered features are unnecessary. [Asset billing](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/), [Static Next.js on Pages](https://developers.cloudflare.com/pages/framework-guides/nextjs/deploy-a-static-nextjs-site/).

For SSR/hybrid rendering, use Workers and validate framework compatibility before choosing the deployment tooling. Cloudflare's current Next.js guide recommends vinext and documents OpenNext as another path for existing applications with compatibility gaps. This research does not select a migration tool or authorise rewriting an existing application. [Current Next.js guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/).

## Core runtime tariff and calculation

Workers Paid starts at USD5/account/month, including 10 million requests and 30 million CPU milliseconds. Overage is USD0.30/million requests and USD0.02/million CPU milliseconds. Ordinary Workers bandwidth has no additional transfer charge. Free has daily/per-invocation limits, so production SSR should not be budgeted from visitor count alone. [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

    R = monthly billable Worker invocations
    C = total monthly billed CPU milliseconds
    Core runtime USD = 5 + max(R - 10,000,000, 0)/1,000,000 * 0.30
                         + max(C - 30,000,000, 0)/1,000,000 * 0.02

Use actual invocations, including framework fetches/prefetches, middleware and bots when they invoke code. A visitor is not a billable request. Cache configuration matters: application invocations and directly served static responses are different paths. API network waiting time is not a substitute for measured CPU use.

## Illustrative scenarios

Assume a 30-day month, 300,000 visits, no other account usage, and one Worker invocation per page view. Extra framework requests are excluded here rather than silently assumed free. CPU values are estimates, not measured Next.js benchmarks.

| Scenario | Pages per visit | Worker requests/month | CPU/request | CPU/month | Core runtime/month |
|---|---:|---:|---:|---:|---:|
| Static-only, no Worker execution | 3 | 0 | 0 | 0 | USD0 on a free static-hosting route |
| Light rendering | 3 | 900,000 | 20ms | 18 million ms | USD5.00 |
| Moderate rendering | 3 | 900,000 | 50ms | 45 million ms | USD5.30 |
| More browsing/rendering | 5 | 1,500,000 | 100ms | 150 million ms | USD7.40 |
| Heavy/bot/prefetch stress illustration | Not inferred | 6,000,000 | 250ms | 1.5 billion ms | USD34.40 |

The last row illustrates why USD5–10 is a scenario estimate rather than a guaranteed upper limit. For the normal scenarios above, plan USD5–10/month for core runtime; USD10–20 is a planning buffer before image/storage/other services and taxes. GBP conversion depends on billing-date FX and payment fees.

## Separate costs

The user clarified that optimisation happens during admin upload. The earlier USD27.50 on-demand transformation illustration is therefore excluded from the active plan: Cloudflare transformation cost is USD0 when the prepared files are delivered without invoking its transformation service. Upload processing still uses resources on the chosen processor; running it on KVM 4 would share the existing VPS capacity.

Generate the required responsive sizes/formats during the upload workflow and record dimensions and URLs. Configure the storefront to select those files without a second on-demand optimisation step. Use versioned filenames for cache invalidation, appropriate cache headers and a retryable processing job. Exact sizes, formats and processing location remain proposed implementation choices; the user selected R2 storage.

R2 object storage is distinct from the Cloudflare Images hosted-image product. The latter's transformation/hosted-delivery fees are not included in the selected prepared-file/R2 route. [Images pricing](https://developers.cloudflare.com/images/pricing/).

R2 is selected; the estimate uses Standard storage. It includes 10GB-month, one million Class A operations and ten million Class B operations monthly. Excess storage is USD0.015/GB-month; excess Class A operations USD4.50/million and Class B USD0.36/million. Internet egress is free. Apply billing-unit rounding and total account usage, including any Worker service separately. The free allowances do not apply to Infrequent Access. [R2 pricing](https://developers.cloudflare.com/r2/pricing/).

### R2 storage examples after the free allowance

Assume the stated total is stored throughout the month, with no other account storage using the allowance. These are storage-only calculations, before tax and operations.

| Total Standard storage | Billable GB-month | Monthly USD |
|---|---:|---:|
| 10GB | 0 | 0.00 |
| 20GB | 10 | 0.15 |
| 50GB | 40 | 0.60 |
| 100GB | 90 | 1.35 |
| 200GB | 190 | 2.85 |
| 500GB | 490 | 7.35 |
| 1,000GB | 990 | 14.85 |

Storage-only cost for these whole-GB examples is max(total GB-month - 10, 0) x USD0.015. Actual GB-month usage averages daily peak storage and is rounded to the next billing unit. For illustration, 60,000 prepared files averaging 100KB occupy approximately 6GB, excluding originals/backups.

Reads/writes are independent of stored size. Twenty million Class B operations in a month leave ten million billable, costing USD3.60; six million Class A operations leave five million billable, costing USD22.50. These are usage examples, not predicted store traffic. Image downloads can create billable reads even though outbound bandwidth is free.

Other possible costs include R2/KV/Durable Objects for assets or ISR/cache coordination, logs, WAF/bot products, domains and CI. These are excluded from the core scenarios. Workers Paid is separate from a zone's Pro/Business subscription; do not buy a zone upgrade solely on the assumption that it is required to host Workers. [Workers product pricing](https://developers.cloudflare.com/workers/platform/pricing/).

Workers Builds currently includes 6,000 paid-plan minutes/month, then USD0.005/minute. External CI has its own provider costs. Build time, supported assets and deployment limits need checking for a large generated catalogue. [Builds pricing](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/).

## Measurement before launch

Measure billable invocations per visit, CPU distribution, cache behaviour, image variants, API latency, database/query load and peak concurrency. A daily visitor total does not establish KVM capacity: search, background imports, admin jobs and inefficient queries can dominate it. Validate using representative catalogue and checkout workloads.

Keep PostgreSQL/API backups outside the single VPS failure boundary and plan recovery. Backups, monitoring, search and email costs are outside this frontend estimate. Set usage alerts and appropriate CPU limits; these controls are not a promise of a universal hard account spending cap.

No deployment, paid plan purchase or hosting-provider account access was performed.

For a combined technical budget including Cloudflare domain registration, email and backups, see [technical running cost budget](18_TECHNICAL_RUNNING_COST_BUDGET.md). Its GBP figures use an explicit budget FX assumption and preserve the distinction between monthly equivalent and prepaid VPS cash.
