# Project memory

Last updated: 22 November 2026. The 8 November business brief remains in memory/BRIEF_2026-11-08.md; the latest requirements are recorded below.

## Silver Edit frontend design system

The client preview links the storefront to the live design system through its header. The Cloudflare Workers setup for reviewing both on one origin is documented in the [storefront handoff](../apps/storefront/README.md#cloudflare-workers-client-preview).

The customer frontend now covers the plan's F01–F10 journeys with ten sample SKUs. Open `/demo` to place a browser-local test order or try account and delivery states. Live payment processing, identity, inventory, notifications and owner-approved listings require the integration phase. See the [frontend handoff](../apps/storefront/README.md).

The asset gallery at `/design-system/assets` contains the storefront's responsive editorial banners, custom icons for the eight departments, logo variants, app icons and social sharing card. The project retains photo masters and crop settings so the artwork can be exported again.

The Next.js homepage in `apps/storefront` and its interactive `/design-system` gallery use the shared React components and tokens in `packages/ui`. The homepage uses the original Silver Medical logo and illustrative catalogue fixtures. See the [storefront guide](../apps/storefront/README.md) and [UI package guide](../packages/ui/README.md).

## Selected homepage design and workspace cleanup ? 22 November 2026

The user selected **The Silver Edit (B)**. The selected design, editable sources, and current client ZIP are linked from the project README. The comparison rounds, provisional Medora prototype and first logo study sources are preserved under `.local/archive/2026-11-22-design-cleanup/`. The selected design uses the client reference logo assets in `apps/storefront/public/brand/`.

## Workspace rename - 19 November 2026

The user renamed the workspace to `D:/Code/projects/silvermedical_project`.

## Silver Medical logo revision - 18 November 2026

The user found the first round generic and requested three types with ten designs each. The current standalone presentation contains 30 new vector concepts, ten each of wordmarks, instrument symbols and supply emblems. The family choices are design proposals. The previous ten PNG concepts remain historical assets. No final logo has been selected.

## Silver Medical branding - 18 November 2026

- User corrected the name to **Silver Medical**, superseding the same-session Economed wording and provisional Medora mockup identity. Supplied website: silvermedical.co.uk. Registration, control of the domain and legal operator are not established.
- Requested ten modern, high-quality generated logos followed by one beautiful, shareable HTML presentation carrying **shishirsabbir** branding.
- Delivered `deliverables/html/SILVER_MEDICAL_LOGO_PRESENTATION.html`, with ten embedded PNG concepts, enlarged keyboard-navigable views, greyscale comparison, shortlist, local notes and text review download. Built-in image generation used; source PNGs and exact prompts preserved in the local design archive under `assets/branding/silver-medical/`.
- Browser checks passed at desktop and mobile widths, including image loading, modal navigation, shortlist persistence, notes download and overflow. Local print render produced. Concepts remain proposals; no final logo selection or store publication occurred. See analysis/26.

## Development workspace organization - 16 November 2026

Latest task, later on 16 November: the user explicitly asked to start the 25-day plan by developing a complete frontend mockup in `dev/designs/web/`. The prototype was originally built there, using provisional Medora branding, 20 illustrative products, nine categories and original SVG artwork. It includes discovery/product/basket/guest checkout/demo confirmation, saved items, account/order/reorder/address/preferences, professional application, help/contact/guides and draft policies. Plain HTML/CSS/ES modules keep this design isolated and dependency-free; production Next.js remains the confirmed direction. No real payment/account/provider integration or publication occurred. All amounts/specifications/stock are fixtures. Syntax and 16 source-level interaction/calculation tests pass; actual browser visual/keyboard QA remains open because both browser and native automation were unavailable. See the Medora source in the local design archive. This later request supersedes the prior organization-only task boundary for local frontend mockup development.

- User requested organization of all project files before development. At the time, the workspace was D:/Code/projects/economed_project.
- Planning material is under docs/{analysis,research,proposals,models,templates,plans,content,registers}; current PDFs/HTML are under deliverables/. Builders live under scripts/docs/ and scripts/models/. Superseded one-sheet inputs, builder and HTML are separated as archive.
- Root README.md and docs/development/README.md provide navigation and the development handoff. apps/{storefront,admin,api,worker}, packages/{contracts,ui,database} and infra contain boundary notes only; no application code or new library selection is implied.
- All 814 original files are preserved. File destinations are recorded in docs/development/FILE_MOVES.json. Local previews/tools are under ignored .local/; original project files are backed up under .local/organization/originals/. No Git repository existed at inspection; ignore/editor conventions were added without initializing Git.
- This request authorizes local organization in preparation for development. No store publication, stock purchase, external communication or deployment occurred. API/ORM/auth/workspace tooling decisions and product/provider readiness remain open.

## AI development cost explanation - 10 November 2026

- Latest revision 5: user requests non-round OpenAI/Claude totals (examples were random-looking figures). Use a transparent illustrative sensitivity case instead of changing provider rates or inventing measured bills: 5,000 cycles x 105k input/21.4k output = 525m input/107m output (632m). Same quantities for every model. Results: OpenAI chat-latest USD5,835; Claude Opus 5.5 USD4,240; Sol/Sonnet USD2,120. Qwen USD1,396.007 rounds to USD1,396.01 plus USD159.55 allowance = unchanged USD1,555.56. Direct RMB base10,152; total FX equivalent remains RMB10,379.99. These assumptions were selected for illustrative presentation and are not a newly measured forecast. Earlier scenario amounts below are historical. Cost-only/no-payment/no-old-calculation constraints persist.

- Latest instruction, revision 4: this is an informational cost explanation, with no funding ask or payment request. Lead with "The estimated AI cost for the initial 25-day development phase is USD1,555.56." Remove funding/request headings, client payment/unused-fund return/carry-forward/overspend-agreement terms and approval language from the client PDF/Markdown/metadata. USD0 developer fee, arithmetic, usage assumptions, source dates and design remain. Earlier funding-oriented entries below are historical and superseded on presentation/payment terms.

- Latest presentation correction: user says not to mention the old calculation. Revision 3 removes the previous request, reduction amount/percentage and earlier token-estimate comparison from the client PDF/Markdown; it states the current USD1,555.56 request directly. Historical decisions remain internal. Current model/calculated output no longer carry the old-price reduction fields.

- User reports the client is dissatisfied and reduces the request to USD1,555.56, retaining USD0 developer fee. They request a new design, at least ten planned AI agents, Qwen mostly, RMB and separate OpenAI/Claude comparisons. They explicitly clarified USD4,000-6,000 means whole-project scenarios. Earlier USD2,736/eight-role funding presentation is superseded.
- Delivery message: most agreed core platform foundation and important basic features are targeted within 25 days; later extend those systems. No quantified share of all four phases, universal ten-agent minimum, available concurrency or guaranteed completion is established.
- Six-page redesigned PDF at the existing stable path; generated Markdown, model and builder retain their paths. New docs/registers/AI_TOKEN_PAYMENT_SOURCES.json records seven official URLs/check dates/scopes; docs/models/AI_TOKEN_PAYMENT_CALCULATED.json records arithmetic. See docs/analysis/25.
- New intensive unmeasured scenario: 10 x 25 x 20 cycles/day x aggregate 100k input/20k output = 500m input/100m output. This is materially higher than historical token estimates; calibrate at Day 5. Current source-backed standard rates give Qwen Frankfurt/global -0902 USD1,320.10, OpenAI chat-latest USD5,500, Claude Opus 5.5 USD4,000; Sol/Sonnet alternatives USD2,000. No universal provider minimum or equivalent-quality benchmark is claimed.
- USD235.46 usage reserve is derived from the cap, not a provider bill or measured rework forecast. Main routing is Qwen; selective premium review can use reserve. Total USD1,555.56 is approximately RMB10,379.99 at ECB 9 Nov cross rate 7.4689/1.1193. Direct Aliyun RMB12/36 tariffs are a separate billing route, producing RMB9,600 base; do not mix with USD model.
- Pricing cost uplifts are labelled context/speed/tokenizer effects. No blanket recent tariff-rise claim is made; Anthropic cancelled the previously announced September Sonnet 5 increase. Official sources checked 10 Nov. No client acceptance, provider purchase, payment, external message or application implementation occurred. Proposed reporting/reconciliation controls remain unaccepted.

## Original AI funding request - superseded later on 10 November 2026

- User requests a USD2,736 client-facing AI-token funding proposal for eight planned agents over the 25-day initial release and explicitly charges no developer fee (USD0). No client acceptance, payment, external sending or guarantee of actual provider cost is established.
- Two-page PDF: deliverables/pdf/UK_MEDICAL_ECOMMERCE_AI_TOKEN_PAYMENT_PROPOSAL.pdf; editable Markdown/client message under docs/; inputs docs/models/AI_TOKEN_PAYMENT_MODEL.json; builder scripts/docs/build_ai_token_payment_proposal.py; docs/analysis/25_AI_TOKEN_PAYMENT_PROPOSAL.md.
- Calculation: 8 x 25 x USD13.68 = USD2,736; USD342 per role/project and USD109.44 for all roles/day. This is a top-down allocation, not a token-volume forecast, provider tariff or incurred bill. Provider/model/billing route/actual tokens remain unknown. Eight roles apply to this new funding document; older 6-7-role references are historical illustrations.
- Proposed controls: fund before work or direct provider payment where supported, document token charges, reviews Days 5/15/25, return unused funds unless client agrees carry-forward, separately agree overspend. These terms and equal allocations are proposals. Hosting/operations/later phases are separate; tax/FX/transfer/non-token charges are uncalculated.
- Both PDF pages rendered and visually checked. No agents were spawned for document preparation; no external communication or payment occurred.

## Latest 25-day development plan - 9 November 2026

- User requested an executable first-release plan. Day 1 should be a collaborative AI-assisted branding/website/functional-design session with the owners, including logo, banners, images and packaging concepts. They choose their direction and priorities with Shishir facilitating.
- User reports 250 products still in the warehouse and wants the first release to sell those products and permit further catalogue expansion. This is reported stock context, not verified quantities, distinct SKU count or lawful-sale status. The new plan assumes 250 SKU/product records pending the actual stock list; all enter review and only approved eligible stock is published.
- Current deliverable: deliverables/pdf/UK_MEDICAL_ECOMMERCE_25_DAY_DEVELOPMENT_PLAN.pdf (17 pages). It includes one-page overview, workshop/asset pack, 20 feature groups, daily build/client/evidence cards, five 50-record batches and launch/expansion checks. Editable content/Markdown and JSON feature/day/source/page registers are under docs/; generator is scripts/docs/build_25_day_development_plan.py.
- Proposed workshop is 5.5 hours plus breaks; select a direction on Day 1 and refine/approve by Day 3. Asset counts and revision rounds are suggested scope, not user-approved quantities. Shipping-packaging concepts do not authorise regulated product repackaging or private labelling. AI does not invent product appearance, specifications or approval evidence.
- Calendar preserves the earlier Day 0 convention: illustrative preparation/kickoff 15 November 2026, development Day 1/workshop 16 November, Day 25 launch target 10 December. Dates/working arrangements remain illustrative; no calendar was booked.
- Assumed capacity: 200-240 developer hours including verification/corrections and AI supervision, plus a separate roughly 42-83 basic catalogue preparation/review person-hours at assumed 10-20 minutes per record. Specialist review, missing evidence and photography are additional. These are unmeasured proposals; Days 5 and 15 revalidate scope/capacity.
- Expansion is explicit: adding a normal product within an approved handling route uses draft intake, evidence/rights review, image preparation, stock receipt and publication. A separate staging test on Day 18 proves this; no fixed 250-item application cap is planned. No application or actual brand artwork was created/published by this documentation task.

## Latest technical specification - 9 November 2026

- User requested comprehensive, professionally designed technical documentation: what is built, customer experience, frameworks/features, auth and measurable SEO targets. The new output is deliverables/pdf/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.pdf, with editable Markdown/Python and JSON requirement/source/page registers under docs/.
- The 47-page specification has 39 sections/acceptance requirements, 11 diagrams or illustrative interface concepts and 49 dated references. It complements, rather than replaces, the 20-page client proposal and 27-page operating/project plan.
- New recommendations: Better Auth with isolated customer/staff configurations and data tables, opaque server-side sessions, verified customer email, invite-only staff with mandatory TOTP, same-origin browser API routes and server-enforced role/resource/product/market permissions. Integration compatibility and policies require a kickoff spike; no user selection of these libraries is implied.
- Proposed quality baseline: Lighthouse SEO 100 for audited indexable public templates; five-run median performance >=90 mobile / >=95 desktop, checkout >=85 mobile with actual provider scripts; manual WCAG 2.2 AA plus automated checks; field p75 LCP <=2.5s, INP <=200ms, CLS <=0.1 when enough traffic data exists. These are engineering targets, not ranking or compliance guarantees.
- PostgreSQL stock locks/reservations, immutable order/tax snapshots, verified webhook inbox, transactional outbox/pg-boss worker, pre-generated Sharp/R2 media and backup/restore acceptance are specified as proposed implementation contracts. Capacity, RPO/RTO, session lifetimes and budgets remain unmeasured proposals. No application implementation, account creation, purchase, deployment or external message occurred.

## Latest proposal brief - 9 November 2026

- Cover wording updated at the user's request to "UNITED KINGDOM FIRST / EUROPE NEXT" and "Medical E-commerce". Use the correctly spelled Kingdom; the first-page title uses two lines.
- The user accepted the detailed project document and requested a separate, attractive client proposal with plentiful icons/banners, summarised coverage, four delivery phases, six-month growth analysis and the supplied portrait.
- Include Shishir Sabbir, shishirsabbir.github.io, shishir.sabbir@gmail.com and +8801883061280 (WhatsApp/Telegram). The portrait is stored locally at assets/proposal/shishir-sabbir-portrait.png for the authorised document; no publication or sending occurred.
- Use 15 November 2026 as an assumed start, not a booked date. Phase 1 is 25 elapsed calendar days after kickoff; phases 2-4 each add one calendar month plus 10 days. Target releases: 10 December 2026, 20 January 2027, 2 March 2027 and 12 April 2027. The Day 0 convention is explicit in the proposal.
- The user explicitly excluded development fees from this document. Include human hours and cumulative AI tokens instead, with roughly 6-7 supporting agent roles. This describes a planned development workflow, not a request to spawn agents for documentation.
- Current client-facing output: deliverables/pdf/UK_MEDICAL_ECOMMERCE_CLIENT_PROPOSAL.pdf (20 pages), built from docs/content/client_proposal_content.py and scripts/docs/build_client_proposal.py. The original 27-page plan remains the detailed supporting reference.
- Analyst estimates for the four proposed packages: 680-880 human hours, 760 working example; 70-150 million cumulative AI tokens, 110 million working example (95m input + 15m output). These are unmeasured and require calibration. No fee, model price or token entitlement is quoted.
- New lean recurring platform model: USD50.92 initial / USD69.67 renewal service subtotal; USD60.92 / USD79.67 with USD10 reserve before tax. A 20% tax sensitivity on services plus reserve gives USD71.10 / USD93.60. This uses GBP1=USD1.25 assumed FX, 100GB R2, within-free-tier requests, one mailbox and limited marketing. Initial technology cash USD361.05 before tax/reserve. It excludes maintenance labour, AI development tools, merchant costs, retail operations and ads. This is a narrower service allowance than the earlier expanded marketing budget, not equivalent service for less money.
- Six-month trading review assumes launch on 10 December and is 10 June 2027. Sales scenarios are illustrative; no six-month revenue/profit guarantee or validated demand estimate exists.

## Confirmed by the user

- Build a medical ecommerce business under a new name.
- Operate in the UK initially and expand across Europe later.
- Use https://www.praxisdienst.com/ as an operating-model benchmark.
- Analyse all selling parameters for medical supplies in the UK.
- Store project memory and analysis in this repository (original location D:/Code/projects/economed; current location D:/Code/projects/silvermedical_project).
- Use a mixed model including UK and EU sourcing.
- Cover all products. Do not assume a consumables-only or narrow-specialty business.
- The user is commissioned to build the complete platform for the owners; the user is the developer, not established as the business operator.
- This is a new brand and a non-dropshipping medical-supply business. The owners may source from Praxisdienst and directly from medical-product manufacturers; resale agreements remain unverified.
- The owners explicitly selected the single-retailer model over a multi-vendor marketplace: procure products, hold their own stock and sell to customers themselves. Supplier self-publishing, third-party seller checkout and marketplace payouts are not requirements. The precise premises and stock operations remain to be defined.
- Hosting direction updated 8 November: Next.js storefront, admin, API and PostgreSQL on Hostinger. This supersedes Cloudflare frontend hosting. KVM 4 was the earlier plan; capacity with all applications hosted together needs validation. No deployment or hosting purchase is established.
- Payments: Revolut, Apple Pay, Google Pay and PayPal. Stripe is explicitly excluded. Merchant approval and exact integration/fees remain unresolved.
- Optimise product images during upload through the admin panel. Budget for prepared image delivery rather than Cloudflare on-demand transformations; exact processor and variants are undecided.
- Use Cloudflare R2 for image/object storage. Standard storage is the cost-model assumption; no bucket has been created by this work.
- Buy the domain through Cloudflare Registrar; silvermedical.co.uk was supplied on 18 November 2026, while purchase/control and actual price remain unverified.
- Launch purchasing supports both consumers and verified professional/business customers, confirmed 8 November. Product-specific entitlement remains separate from business verification and consumer contract status.
- Prescription-only medicines are undecided. Present the requirements and operating-model decision separately; neither authorisation nor permanent exclusion is established.
- The user wants a regular React admin application, Next.js storefront and PostgreSQL database. API framework remains open; Vite, TypeScript, NestJS/Fastify and Prisma are recommendations rather than accepted choices.
- Immediate deliverable: a proposal for the owners covering UK selling rules, Google Merchant Center/campaigns, tax and the technical build, followed by discussion. No client sending or application implementation is authorised by this request.
- The user requested a gap review and specifically identified email and WhatsApp marketing as insufficiently discussed. Research and proposal coverage now include customer messaging/retention and related CRM/admin/cost scope; no marketing provider, channel activation or campaign spend is selected.
- The user has promised the owners a first selling phase within 25 days of the agreed start, followed by remaining features. Record this as the target for a complete initial purchase/fulfilment journey, not a guaranteed finish of every future feature or external approval.
- Document format clarified: full, detailed, self-explanatory multi-page documentation now. Only the 25-day launch plan should occupy one brief page. The previous entire-project one-page interpretation was the assistant's mistake, not a user decision to narrow the documentation.
- The detailed supporting output is deliverables/pdf/UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.pdf (27 pages), matching HTML/Markdown, and a one-page launch-only extract. The separate latest client proposal is recorded above. The Day 25 roadmap is page 19; docs/content/project_plan_content.py and scripts/docs/build_project_plan.py are the current source/generator. The earlier whole-project one-sheet is historical and superseded.

## Meaning of the scope

The analysis includes human medical, dental and veterinary supply categories, consumables, equipment, furniture, diagnostics, PPE, infection control and medicine-related routes. The exact SKU universe remains to be defined. Full-range ambition does not establish legal permission for each category or decide which items launch together.

Both consumer and verified professional/business purchasing are confirmed. The first acquisition segment and detailed restricted-product entitlement rules remain open.

## Context from the earlier Economed investigation

Economed.co.uk was researched before this planning request. It identifies Economedical Ltd, company 15367622, as operator. On 8 November the user explained that the owners are planning the new venture and the user is their developer. The user reports roughly 7,000 old SKUs, prescription-related products, scraped Praxisdienst content, Google Merchant Center notices or a ban and closure by the owner. These enforcement/closure causes are user-reported, not independently verified. The new venture's legal entity and any relationship to Economedical Ltd remain unresolved. Do not transfer old contact details, VAT numbers, authorisations, reviews or rights to the new brand. See docs/research/ECONOMED_BASELINE.md and the latest brief.

## Proposed approach, not accepted decisions

- Build a full taxonomy and data model from the outset; activate categories when their prerequisites pass.
- Design purchasing, goods receipt, owned inventory and retailer fulfilment for the confirmed business model; earlier supplier-direct recommendations are not adopted. Exact warehouse, shipment flow and operational systems need clarification.
- Avoid adopting manufacturer, UK Responsible Person, private-label or medicines-wholesaler obligations by accident.
- Evaluate an EU fulfilment route before scaling EU orders from a GB warehouse.
- Make dependable supply, clear pack quantities, documentation, expiry information and repeat ordering core differentiators.
- Use NestJS with its Fastify adapter for a modular API, React/Vite for the admin and a separate worker; compare plain Fastify before acceptance. See docs/analysis/20_API_FRAMEWORK_AND_ADMIN_ARCHITECTURE.md.
- Keep prescription-medicine activation disabled pending the separate business decision and substantiated supply arrangements. This is a recommended release gate, not a user decision to remove medicines from the eventual range.
- Prioritise service email, preferences/suppression and reviewed email automations; assess WhatsApp feasibility before committing it and treat SMS/loyalty/referrals as scope options. See docs/analysis/21_CUSTOMER_MESSAGING_AND_RETENTION.md and docs/analysis/22_PROPOSAL_GAP_REVIEW.md. Do not assume legacy customer data or messaging permission transfers to the new business.
- Use the bounded Day 25 backlog and acceptance gates in docs/analysis/23. Earlier 8 November expanded-service cost example: 200 developer hours at GBP30/hour plus 20% reserve, GBP150 unquoted AI/tools and GBP317.84 initial technology cash totals GBP7,667.84. Proposed technology envelope GBP85/month initially and GBP105 at VPS renewal. These are analyst inputs, not a user-approved quotation or complete retail operating budget.

## Unconfirmed facts

Silver Medical is the confirmed brand name as of 18 November 2026. Legal entity, ownership, registrations, professional staff, premises, 3PL, budget, supplier contracts, launch date, commerce/backend platform, inventory availability and launch countries remain unconfirmed. The frontend framework and intended hosting split are recorded above; deployment tooling is not selected. Local design work exists; no production store has been published through this work.

## Evidence baseline

Research date: 7 November 2026, using the user's Asia/Shanghai date context. Laws and competitor policies can change. Detailed references are in docs/research/SOURCES.md. Financial examples use illustrative assumptions and must not be presented as market benchmarks.

## Current project state

A research and planning library and a client discussion proposal have been created. The workspace was organized for upcoming development on 16 November 2026; application folders contain boundary notes only. Next decisions concern the legal operator, detailed buyer entitlement, medicines activities, initial category activation order, funding and fulfilment. Full commercial validation requires supplier quotes, a matched product basket and customer interviews. The latest client-facing proposal is deliverables/pdf/UK_MEDICAL_ECOMMERCE_CLIENT_PROPOSAL.pdf, issued 9 November; the earlier discussion draft remains in docs/proposals/UK_MEDICAL_ECOMMERCE_PROPOSAL_2026-11-08.md. Neither establishes licence, payment-provider or Google approval.

The Cloudflare frontend scenarios in docs/analysis/17_HOSTING_ARCHITECTURE_AND_COSTS.md are historical after the 8 November move to Hostinger frontend hosting. R2 and the Cloudflare domain remain selected; upload-time image optimisation remains planned. Frontend/API/database capacity together, delivery/cache configuration and actual traffic remain unmeasured.

docs/analysis/18_TECHNICAL_RUNNING_COST_BUDGET.md preserves the earlier running-cost estimate. It needs revision for Hostinger frontend hosting and Revolut/PayPal; Stripe rates are not an active cost assumption. No revised payment quote, final capacity validation or accepted budget exists.

The prior GBP40/55 planning targets were conditional on the earlier architecture and are historical. The latest illustrative budget in docs/analysis/23 uses 100GB R2 and expanded messaging/service allowances with Hostinger frontend. Storage, hourly rate, developer effort, service choices and spend remain assumptions; no final quote is agreed.

The user intends to develop alongside AI models. docs/analysis/19_AI_DEVELOPMENT_TOKEN_ESTIMATE.md proposes approximately 50 million cumulative input+output tokens for a bounded initial production UK build, with a 25–65 million planning range; broader full-scope work could be 60–150 million or more. These are unmeasured analyst estimates, not an approved token/spend limit. Model/provider, commerce reuse and release backlog remain open; pilot usage should replace assumptions.

Current stage: The Silver Edit is selected as the visual direction. Production integration and launch work remain open. Existing requirements/regulatory research remains the baseline. The user clarified that the owners selected their own-stock retailer over a multi-vendor marketplace. That earlier business-model clarification did not itself authorize implementation; the 16 November mockup request above now authorizes the recorded local design work. Prescription, product approval, Google feeds and payment acceptance must be modelled as distinct requirements if implemented.
