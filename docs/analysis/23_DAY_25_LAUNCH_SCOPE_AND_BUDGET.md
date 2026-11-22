# Day 25 launch scope and budget

Latest execution update, 9 November: the [new detailed 25-day development plan](../plans/UK_MEDICAL_ECOMMERCE_25_DAY_DEVELOPMENT_PLAN.md) adds the user's Day 1 collaborative branding/design workshop and reported 250 warehouse products. It is the current daily task/feature baseline; [analysis/24](24_25_DAY_DEVELOPMENT_PLAN.md) records new assumptions. A one-page overview is retained within the 17-page dedicated plan. Actual SKU count, quantities and eligibility remain unverified. The new schedule explicitly preserves Day 0 on 15 November and development Days 1-25 on 16 November-10 December; the older generic "Day 1 is project start" statement below is historical. Fees below remain historical and are not quoted in the new plan.

Latest proposal update, 9 November: the user selected an assumed 15 November 2026 kickoff for illustration and four phases. The new client proposal uses 25 elapsed days (kickoff Day 0), yielding 10 December 2026, then 20 January, 2 March and 12 April 2027 by adding one calendar month plus 10 days each time. This is not a booked schedule. The user explicitly requested no development fees in the client proposal; historical fee examples below must not be copied into it. See [the client proposal](../../deliverables/pdf/UK_MEDICAL_ECOMMERCE_CLIENT_PROPOSAL.pdf) and [its lean USD model](../models/CLIENT_PROPOSAL_MODEL.json). The earlier GBP budget included larger service/marketing allowances and is not equivalent to the new limited pilot model.

Updated 8 November 2026. The user has promised a first selling phase within 25 days. The document-format request was initially misread: the user clarified that the full project documentation must be detailed and multi-page, with only the 25-day launch plan condensed to one page. The current full plan is deliverables/pdf/UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.pdf; its launch roadmap is page 19 and has a separate one-page extract. This documentation task does not authorise building or publishing the store.

## What the first phase means

Target a complete, tested customer-to-fulfilment journey for a bounded, reviewed launch assortment. Both consumers and verified professional/business customers remain in scope. The first phase needs sufficient product, inventory, tax, payment, order, communications, privacy and support functionality to transact and resolve problems. It is not a promise to implement the full future medical catalogue, every ERP integration or all European markets in 25 days.

Day 1 is the agreed project start, not automatically 8 November. The plan uses 25 calendar days as a planning assumption; confirm the actual working pattern. Approximately 200 focused developer hours is an explicit capacity assumption, equivalent to eight hours across each of 25 days. It is not measured throughput or a recommended expectation of uninterrupted work. Owner/product-review capacity must run alongside development. If the available hours are lower, reduce the first-release backlog or revise the date.

AI-assisted development can help with implementation, exploration and review, but several agents are not equivalent to several staffed engineers. Integration, human review, product decisions, payment-provider review and operational preparation remain on the critical path. This request mentions using multiple AI tools/agents as the user's intended approach; it is not an instruction to spawn agents for the documentation work.

## Proposed launch backlog and boundaries

| Work package | Phase 1 deliverable | Acceptance |
|---|---|---|
| Identity and security | Consumer/business accounts, staff roles, admin MFA, secure sessions and necessary professional checks | A pending professional account cannot bypass a restricted-product check; ordinary consumers have the intended checkout route |
| Catalogue and media | Products/variants/pack units, draft imports, evidence references, territory/channel status, upload-time optimisation and R2 variants | Unapproved products are absent from public discovery, checkout and feeds |
| Stock and procurement | Supplier records, receipt/stock adjustments, reservations, applicable lots/serials/expiry and quarantine | Concurrent checkout cannot oversell the last unit; quarantined stock is not offered |
| Storefront | Responsive Next.js categories/search, product pages, availability, clear prices, basket, checkout and account orders | Mobile and keyboard flows can complete a real eligible order |
| Payments | Revolut/wallets and PayPal subject to actual merchant approval, verified webhooks and idempotent processing | Failed, duplicate and delayed events reconcile without duplicate orders or dispatch |
| Orders and fulfilment | VAT/delivery rules, professional holds, manual dispatch/tracking entry, order emails, invoices/credit notes and refunds | Staff can receive, fulfil, track, refund and reconcile an order |
| Compliance and communications | Seller identity, reviewed policies, price/returns rules, preferences and suppression, service email | Marketing withdrawal blocks campaigns without breaking necessary service notices |
| Operations | Production configuration, logs, alerting, offsite backups, restore procedure and staff training | Successful restore, access review and order/refund/dispatch walkthrough |

Manual carrier booking, export-based accounting and human professional review are acceptable initial workflows if they are documented, staffed and tested. They must not be represented as automated integrations. Select one authoritative inventory record and avoid untracked spreadsheet edits that break stock truth.

Defer complex trade credit, multi-level procurement approvals, loyalty/referral schemes, sophisticated marketing automation, native mobile apps, comprehensive ERP/WMS replacement and European country activation to separately scoped phases. Prescription-only medicines remain undecided, with the requirements described in the proposal; publication/supply remains gated pending substantiated permissions and an accountable operating route. A staged launch does not remove any category from the full-range ambition.

Do not develop a multi-vendor seller marketplace or dropshipping workflow for this confirmed own-stock business. Stripe is excluded by the user. No clinical prescribing service or proprietary bulk-email delivery infrastructure is included in the initial plan. Imported product descriptions/images require actual rights and review.

## Delivery plan and release rule

Days 1-3 establish scope, sample SKUs, legal operator and supplier evidence, API/reuse choices, domain/hosting, tax and delivery rules and merchant onboarding. Days 4-10 build the first catalogue/admin/stock/storefront slice. Days 11-17 complete order/payment/fulfilment and communications workflows. Days 18-24 freeze launch data, conduct functional/security/accessibility/load/restore checks and train staff. Day 25 is a controlled release only when the product, provider, stock and operational gates pass.

Review scope and dependency status daily. If an external approval is late, do not disguise a missing payment or product permission as a completed feature. Revise the launch assortment or release date where lawful and practical. A payment provider's rejection must not be circumvented through a different product label or checkout flow.

## Technology assumptions and budget

The [budget inputs](../models/launch_25_day_budget.json) are transparent planning inputs, not a quotation. The latest topology is Hostinger KVM for Next.js, React admin, API/worker and PostgreSQL; Cloudflare domain/R2. NestJS with Fastify remains a recommendation. No Cloudflare frontend runtime or image-transformation bill is included.

| Item | Monthly GBP equivalent | Evidence or assumption |
|---|---:|---|
| KVM 4 initial term | 9.99 | Published UK offer, GBP239.76 prepaid for 24 months |
| Domain | 1.67 | GBP20/year allowance; exact Cloudflare name/TLD checkout not chosen |
| R2 Standard, 100 GB-month | 1.08 | USD1.35 storage at assumed USD1 = GBP0.80; modelled operations within account free allocations |
| Independent backups | 5.00 | Unquoted allowance; assess independence, retention and recovery requirements |
| Transactional email | 16.00 | USD20 example tier at assumed FX; provider not selected |
| Marketing service | 25.00 | Unquoted allowance; list/send/automation volume unknown |
| One mailbox | 6.00 | Unquoted allowance; one seat only |
| Monitoring | 5.00 | Unquoted allowance; no labour included |
| Base total | 69.74 | Rounded monthly equivalent; exact annual base GBP836.84 |
| Base at VPS renewal | 84.74 | VPS component rises to GBP24.99/month equivalent |
| Proposed reserve envelope | 85.00 / 105.00 | Initial/renewal planning envelopes, not guaranteed caps |

Initial technology cash in this example is GBP239.76 VPS prepayment + GBP20 annual domain allowance + GBP58.08 other first-month services = GBP317.84, excluding applicable taxes. The VPS prepayment buys 24 months; do not add a second VPS charge in the same initial cash calculation. Monthly equivalents are useful for cost comparison but do not describe payment schedules.

Illustrative Phase 1 labour: 200 hours x GBP30 = GBP6,000, plus 20% contingency GBP1,200 = GBP7,200. Add an unquoted AI/tools allowance GBP150 and technology cash GBP317.84 for a launch software/setup example of GBP7,667.84. Developer rate, effort, AI provider/subscriptions and budget have not been agreed. This is not a market-rate claim or a fixed-price offer. Do not add AI API estimates to a subscription allowance unless they are distinct, actually incurred charges.

These figures exclude inventory, import VAT/duties, freight, warehouse/premises, staff, insurance, licences/specialist advice, payment fees, business-account subscriptions, maintenance labour, advertising/campaign operation, optional SMS/WhatsApp/helpdesk and later features. The total funding required to operate the retailer remains unpriced until these inputs are supplied.

The example assumes separate service allowances. If a selected provider combines transactional delivery and marketing in one plan, recalculate to avoid counting the same subscription twice. Replace the AI allowance with measured subscription/API/tool usage; no particular model mix or token entitlement is priced here.

## R2 and payment cost details

Standard R2 includes 10 GB-month storage, 1 million Class A and 10 million Class B operations per month. Published overage rates are USD0.015/GB-month, USD4.50/million Class A and USD0.36/million Class B; internet egress is free. Respect provider billing-unit rounding and shared account allowances; other R2 usage consumes the same allowance. Infrequent Access has a different charging model and is not assumed. [Cloudflare R2 pricing](https://developers.cloudflare.com/r2/pricing/), checked 8 November 2026, Standard class.

Revolut's published online rates include UK Visa/Mastercard consumer cards at 1% + GBP0.20 and UK/EEA Visa/Mastercard commercial cards at 2.5% + GBP0.20. Card mix matters for this professional retailer. PayPal's standard UK domestic "All Other Commercial Transactions" rate is 2.9% + GBP0.30 received in GBP; different methods, cross-border, FX and negotiated terms can differ. At GBP100, these three examples cost GBP1.20, GBP2.70 and GBP3.20 respectively. Approval of the actual medical catalogue is separate. These fees are variable additions, not included in the GBP85 envelope.

Sources: [Revolut UK merchant fees](https://help.revolut.com/help/merchant-accounts/fees/how-much-does-it-cost-to-accept-card-payments/business/) and [PayPal UK fees](https://www.paypal.com/uk/business/paypal-business-fees), checked 8 November 2026; UK online/domestic examples, not a provider offer to this operator.

Other current evidence: [Hostinger UK KVM offer](https://www.hostinger.com/uk/vps-hosting), [Cloudflare Registrar](https://www.cloudflare.com/domains/) and [Resend pricing example](https://resend.com/pricing), checked 8 November 2026. KVM 4 advertises 4 vCPU/16GB RAM/200GB NVMe/16TB bandwidth; combined application capacity is not measured. Resend's USD20 tier is an example with 50,000 emails/month; catalogue acceptance and actual volume remain open. Neither its selection nor a marketing provider is confirmed.

## Legal and policy source map

The [full project plan](../plans/UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.md) provides detailed planning guidance and a dated primary-source appendix; product-specific legal clearance still requires actual SKUs, activities and operator evidence. Supporting research remains in [the proposal](../proposals/UK_MEDICAL_ECOMMERCE_PROPOSAL_2026-11-08.md), [regulatory analysis](06_UK_REGULATORY_FRAMEWORK.md), [messaging analysis](21_CUSTOMER_MESSAGING_AND_RETENTION.md) and [source register](../research/SOURCES.md), checked 7-8 November 2026 with source-specific dates/access limits. Apply:

- GB devices/IVDs: UK Medical Devices Regulations 2002 as amended, applicable conformity/registration and operator roles; NI device rules separately. [MHRA device framework](https://www.gov.uk/guidance/regulating-medical-devices-in-the-uk), [registration](https://www.gov.uk/guidance/register-medical-devices-to-place-on-the-market), [NI](https://www.gov.uk/guidance/medical-devices-eu-regulations-for-mdr-and-ivdr).
- PPE and biocides: separate intended-use/role/territory routes. [OPSS PPE](https://www.gov.uk/government/publications/personal-protective-equipment-enforcement-regulations-2018), [HSE biocides](https://www.hse.gov.uk/biocides/about/introduction.htm).
- Medicines: patient supply, wholesale and import activities separately; pharmacy/POM/GSL and veterinary routes are distinct. [MHRA licensing](https://www.gov.uk/guidance/apply-for-manufacturer-or-wholesaler-of-medicines-licences), [VMD](https://www.gov.uk/guidance/sell-veterinary-medicines-on-the-internet).
- Consumers: Consumer Contracts Regulations 2013/Consumer Rights Act 2015 and current pricing/unfair-practices requirements, including DMCC Act 2024. [Returns](https://www.gov.uk/accepting-returns-and-giving-refunds), [CMA pricing](https://www.gov.uk/government/publications/price-transparency-cma209/providing-clear-and-accurate-information-about-prices-summary).
- Tax/privacy: applicable VAT treatment, UK GDPR/DPA 2018/PECR, genuine messaging permissions and secure records. [VAT registration](https://www.gov.uk/register-for-vat), [ICO electronic-mail rules](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/how-do-we-comply-with-the-pecr-electronic-mail-marketing-rules/). Indexed ICO evidence/access restrictions are recorded in analysis/21.
- Channels: [Google healthcare policy](https://support.google.com/merchants/answer/6150151?hl=en) and [WhatsApp Business policy](https://whatsappbusiness.com/policy/); channel eligibility does not follow automatically from lawful website supply. [PayPal approval policy](https://www.paypal.com/uk/legalhub/paypal/acceptableuse-full) applies separately to medical devices/prescription items.

The superseded whole-project one-sheet used short reference labels as subject gateways. The current full plan instead includes a primary-source appendix with URLs, checked dates and scopes, alongside chapter references; neither format substitutes for product-specific clearance.

## Growth recommendations

Use a reviewed in-stock starter assortment, transparent pack/unit prices, matched-product price checks, clinic starter bundles, prompt quote handling, reliable dispatch and easy reordering. Build a pilot cohort of professional buyers and seek supplier/manufacturer referrals. Test acquisition with known contribution and limited stock exposure. These are hypotheses to validate, not assurances of fast success, NHS endorsement or special supplier access.
