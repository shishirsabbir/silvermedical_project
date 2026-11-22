# API Framework and Admin Architecture

Discussion recommendation dated 8 November 2026. The user confirmed Next.js, a regular React admin, PostgreSQL and Hostinger hosting. The API framework remains undecided. No application implementation has started.

9 November expansion: the [detailed technical specification](../plans/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.md) now provides the proposed end-to-end design, identity/session policies, API examples, domain model, transactional workflows, measurable SEO/performance targets and 39 acceptance requirements. The [designed PDF](../../deliverables/pdf/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.pdf) is the technical review edition. Better Auth, pg-boss, Sharp and the numerical policies are new recommendations requiring a pilot; they do not convert the framework proposals here into accepted selections. Dated technical evidence is in [TECHNICAL_SPEC_SOURCES.json](../registers/TECHNICAL_SPEC_SOURCES.json).

## Recommended API

Use NestJS with the Fastify adapter for a modular monolith. The deciding factor is the size of the business workflow: product evidence and approval, professional entitlement, procurement, owned stock, orders, payments, returns and audit records need consistent boundaries and access checks. Nest's application structure is a useful starting point for that work. This is an architectural recommendation, not a measured speed claim.

| Option | Benefit for this project | Cost or limitation | Assessment |
|---|---|---|---|
| NestJS with Fastify | A shared module/service structure for many business domains, with Fastify as the HTTP provider | More framework concepts and boilerplate; integrations must suit the selected adapter | Preferred for a substantial admin/API maintained over time |
| Fastify directly | A lean API with explicit plugins and less framework structure | The developer must establish and consistently maintain service boundaries, permissions, transaction conventions and review workflows | Good alternative if the developer prefers and will maintain these conventions |

Official capability sources: [Nest HTTP adapters](https://docs.nestjs.com/techniques/performance), [Nest modules](https://docs.nestjs.com/modules), [Fastify documentation](https://fastify.dev/docs/latest/). Checked 8 November 2026; Node.js API framework scope. The comparative judgement above is project-specific analysis. Fastify is Nest's HTTP provider when its adapter is selected; the two are not competing processes that both need deployment. Express-specific middleware may need Fastify alternatives.

Do not choose an API by synthetic requests-per-second headlines. Measure realistic queries, authorisation, stock contention, payment notifications and rendering on the selected server. Neither option establishes legal compliance automatically.

## Application boundaries

Use one repository with logical applications for storefront, admin, API and worker, plus shared API schemas and reusable UI/domain types as appropriate. Share validated contracts without exposing server secrets or database access to browser bundles. Exact tooling and package versions should be selected at implementation time.

- Next.js handles the public shopping experience and server rendering where useful.
- React with Vite handles the staff interface. TypeScript is recommended across the applications; it was not explicitly selected by the user.
- The API owns all authoritative prices, tax decisions, product/customer eligibility, stock mutations, orders and payment transitions.
- PostgreSQL stores transactional records with constraints and migration history. Prisma is a proposed data-access layer; evaluate its current API and migration workflow before adoption.
- A worker handles long imports, upload optimisation, exports, notifications and feed builds. Use a durable job mechanism with retry and idempotency; select a PostgreSQL-backed queue or add Redis only after reviewing job volume and operational cost.

[Vite React/build support](https://vite.dev/guide/) and [Prisma transaction documentation](https://www.prisma.io/docs/orm/fundamentals/transactions), checked 8 November 2026; development tooling and database-access capabilities. These do not establish production resource requirements.

## Proposed domain modules

| Module | Owns |
|---|---|
| Identity and organisations | Staff roles, account security, organisations, account verification and purchasing authority |
| Catalogue and evidence | Products/variants/pack units, manufacturers, documents, classifications, reviewed claims and permissions |
| Purchasing | Suppliers, purchase orders, expected receipts, costs and discrepancies |
| Inventory | Stock movements, lots/serials/expiry, reservations, quarantine and reconciliation |
| Pricing and tax | Effective prices, approved contract terms, tax treatments and relief evidence references |
| Orders and fulfilment | Quotes, checkout, order states, holds, dispatch, returns and customer documents |
| Payments | Revolut/PayPal adapters, verified events, payment/refund states and reconciliation |
| Channels and content | Publication, permitted feeds, destination scope, content revisions and campaign review tasks |
| Audit and operations | Actor/reason/time records, approvals, jobs, notifications and operational exports |
| Customer messaging | Purpose/channel preferences, suppression, reviewed templates, provider events, delivery history and campaign eligibility; see analysis/21 |

These are code boundaries in one application initially. Microservices would introduce distributed transactions and deployment work before the need is demonstrated.

Messaging detail is in [analysis/21](21_CUSTOMER_MESSAGING_AND_RETENTION.md). Keep product and permission checks authoritative in our API while using a managed delivery/automation provider. Recheck eligibility at send time, cancel withdrawn marketing, process provider events idempotently and preserve necessary service communications. A custom campaign editor is not assumed within the base admin scope.

## Product permissions need several dimensions

Avoid a single `prescription_required` flag as the release policy. Proposed independent dimensions include:

| Dimension | Example states or evidence |
|---|---|
| Product route | Device, IVD, PPE, biocide, medicine, ordinary good; multiple routes where applicable |
| Jurisdiction | GB, NI, then individual destinations |
| Seller activity | Distributor/importer/other applicable role and documented permissions |
| Buyer entitlement | Public, verified professional, named profession or other approved restriction |
| Supply review | Required evidence, authorised reviewer and order hold/release decision |
| Publication | Draft, reviewed public page, restricted content, suspended |
| Channel | Separate Shopping, free-listing and Ads decisions with reasons and policy review dates |
| Payment | Provider/category approval and supported transaction route |

This is a proposed software model, not a determination that any product may be supplied. The legal requirements and channel findings are in [the proposal](../proposals/UK_MEDICAL_ECOMMERCE_PROPOSAL_2026-11-08.md). Keep medicine routes disabled pending the owners' separate decision and substantiated arrangements; this is a recommendation, not a confirmed exclusion.

Enforce the effective rules at checkout and dispatch as needed, not only when rendering a button. Search results, related products, exports, feeds and public APIs also need the applicable publication rules. Revalidate a held order when underlying entitlement or product status changes.

## Stock and payment correctness

Proposed acceptance scenarios should cover concurrent orders for the last unit, lot quarantine during checkout, duplicate and delayed payment notifications, expired reservations, failed payment after reservation, partial refund, partial dispatch and return inspection. These are material transaction risks, not cosmetic UI tests.

Record payment-provider events and process them idempotently. A browser redirect cannot be the sole proof of payment. Design provider-specific verification and retries using current documentation during implementation. Keep the database transaction short; do not hold locks across external payment calls. Use durable pending states and reconciliation for interrupted operations.

Preserve stock movements as an auditable ledger and derive or reconcile balances. Use explicit available, reserved and quarantined quantities rather than a single editable stock number. Decide reservation/capture/dispatch sequencing after the providers and any restricted supply process are agreed.

## Admin performance and usability

Start with role-based work queues: products awaiting evidence, customer verification, receipts, quarantined stock, held orders, failed jobs and reconciliation discrepancies. Staff should see why an item is blocked and the permitted next action.

Use server-side filtering, sorting and pagination; indexed lookup by SKU, identifier, lot and order; virtualise large tables where justified; keep bulk actions bounded and preview changes. Queue large imports and exports with progress and error reports. Provide draft/preview/review/publish steps, clear validation, keyboard access and useful audit differences.

Agree measurable performance targets in the pilot for representative catalogue size, staff concurrency and query shapes. The old store's reported 7,000 SKUs are context, not a confirmed new-catalogue size or load-test dataset.

## Hostinger and R2 deployment

Place a reverse proxy before Next.js and the API, serve the built admin as static assets, and keep PostgreSQL on a private interface. Separate service users/resources and production/staging credentials. Cache only responses that are safe to share; personal prices, accounts, baskets and restricted responses must not enter a public cache.

Persist Next.js cache where required and review coordination before adding instances. [Next.js self-hosting guidance](https://nextjs.org/docs/app/guides/self-hosting), checked 8 November 2026; reverse proxy and cache guidance. The intended KVM 4 needs combined workload testing rather than a visitor-count capacity guarantee.

Optimise product images once during upload, then store prepared variants in R2. A public product image path and a private document path must have separate access policies. Do not place prescription or other sensitive evidence in the publicly accessible catalogue bucket/path. Set upload limits and worker concurrency to protect storefront/database capacity.

Before production, demonstrate restoration to a separate environment, safe schema migration/rollback strategy, provider-event replay, service recovery and order reconciliation. Agree recovery-time/data-loss objectives with the owners. A single VPS is a shared point of failure even if its services are isolated.

## Decision to discuss

Accept NestJS with Fastify if the developer is comfortable with its conventions and the pilot verifies the required integrations. Choose plain Fastify if lower framework overhead is more valuable and the developer will own the missing application conventions. Decide existing commerce-engine reuse versus a custom domain layer before committing delivery cost; the present recommendation is a framework direction, not a completed build-versus-buy evaluation.
