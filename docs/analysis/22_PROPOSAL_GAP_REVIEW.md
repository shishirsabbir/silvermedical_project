# Proposal gap review

Review date: 8 November 2026. This compares the client proposal with the existing research library and the user's request about email/WhatsApp marketing. Status describes documentation coverage, not implemented functionality or an accepted commercial scope.

The largest omission was a practical customer lifecycle and messaging plan. Several other subjects were mentioned in research but still need concrete deliverables, integrations, owners and acceptance criteria before the developer can quote a complete store.

## Coverage and next work

| Area | Previous coverage | What needs to be specified | Suggested priority |
|---|---|---|---|
| Email marketing | Brief mention in analysis/12 and general privacy section | Campaigns, permitted audiences, automation triggers, suppression, sender setup, provider and ongoing owner | Launch planning |
| WhatsApp and SMS | Not defined as proposal deliverables | Channel feasibility, actual permitted use, consent, provider, costs and support process; see analysis/21 | Feasibility first; no guaranteed WhatsApp launch |
| Transactional communications | Notifications mentioned | Template inventory, service/marketing separation, delivery failures, retries, sender authentication and support fallback | Before launch |
| Customer permissions and legacy data | General privacy principles | Channel/purpose evidence, old/new controller review, suppression import, deletion/retention and provider synchronisation | Before data import or marketing |
| CRM and support | CRM boundary and support principles in analyses/09 and /11 | Single case history, ownership, hours, response targets, returns/complaint routing and escalation | Before launch |
| Retention and promotions | Saved baskets/reordering mentioned | Reorder lists, account-specific offers, stock alerts, discount stacking, minimum margin and misuse prevention | Core repeat-order tools first |
| Loyalty and referrals | Not a defined deliverable | Points/credits, funding, redemption/refund rules, professional appropriateness and referral-contact permissions | Optional, separately priced |
| B2B purchasing | Covered at requirements level | Quotes, company purchasers/approvers, PO handling, account prices, credit decisions and multi-site ordering | Decide launch subset |
| On-site search and content | Principles in analysis/11 | Search by identifier/synonym, facets, compatible products, pack clarity, CMS ownership, redirects and approved SEO content | Before launch |
| Reviews and reputation | Authenticity principles in analysis/12 | Collection route, moderation, incentive disclosure, complaint escalation and ownership of imported reviews | Decide launch scope |
| Accounting and carriers | System boundaries named | Select actual integrations, authoritative records, reconciliation, labels/tracking, tax invoices and failed-sync handling | Before quote and launch |
| Equipment after-sales | Described in analysis/09 | Warranty cases, installation, maintenance/calibration, parts, provider responsibilities and customer messages | Before relevant equipment activation |
| Analytics | KPI list exists | Event specification, consent handling, net revenue/refunds, campaign attribution, owner and reporting cadence | Before campaigns |
| Accessibility and usability | WCAG 2.2 AA proposed in analysis/11 | Agreed test matrix for mobile, keyboard, screen readers, forms, search, checkout and admin | Before launch |
| Security and continuity | Principles in architecture/proposal | Recovery objectives, restore drill, access reviews, secret ownership, incident process and scheduled maintenance | Before launch |
| Handover and commercial scope | Dependencies mentioned | Source/account ownership, documentation, staff training, support hours, warranty period, change control, third-party fees and exit/export process | Before contract |
| Budgets and responsibility | Hosting/payment estimates and open questions | Separate build, ongoing maintenance, campaigns, messaging, operational staffing and licence/professional costs | Before commitment |

Stock, lots, expiry, recalls, product approval, tax, payments and regulated-product routes were already covered. Their remaining gaps are actual supplier/SKU evidence and operational choices, rather than absence from the plan. The user has not yet accepted the recommended API framework, channel vendors or launch priority list.

## Proposed minimum launch additions

1. A complete service-email list, authenticated sender, delivery monitoring and an owner for failed communications.
2. A preference centre and auditable permission/suppression records integrated with the chosen marketing service.
3. A small set of reviewed email automations, ordinary reorder lists and requested stock notifications where suitable.
4. A staffed support workflow linked to orders, with a returns/safety escalation path.
5. An integration schedule naming the accounting, carrier and communications systems and who operates each one.
6. An acceptance and handover schedule covering accessibility, recovery, reconciliation, permissions and staff training.

WhatsApp remains a separate feasibility item under [the messaging analysis](21_CUSTOMER_MESSAGING_AND_RETENTION.md). Advanced loyalty, referral incentives, automatic subscriptions, a custom campaign builder and complex CRM automation should be priced as explicit options. This proposed sequencing does not remove any product category from the user's full-range ambition.

## How to make the proposal quotable

For each proposed module, record the business owner, launch or later priority, provider/integration, data inputs, permissions, deliverable, acceptance scenario, one-off development cost and recurring cost driver. A feature title such as "email marketing" is too broad to price: two reviewed welcome emails and a complete custom campaign editor are very different commitments.

Next owner decisions should cover campaign/support staffing, available customer data and rights, desired launch automations, marketing budget, accounting/carrier choices, optional loyalty/credit features and maintenance responsibility. Requirements for medicines, legal operator and NI scope remain the existing higher-priority release dependencies.

## Evidence and boundaries

This is a documentation coverage assessment against [the proposal](../proposals/UK_MEDICAL_ECOMMERCE_PROPOSAL_2026-11-08.md), [marketing analysis](12_MARKETING_RETENTION_AND_MEASUREMENT.md), [store requirements](11_STORE_AND_PRODUCT_DATA.md), [operations](09_FULFILMENT_QUALITY_AND_SUPPORT.md), [launch gates](15_LAUNCH_PLAN_AND_GATES.md) and [open questions](../../memory/OPEN_QUESTIONS.md), reviewed 8 November 2026. Current channel/legal references and their scope/access limits are in analysis/21 and docs/research/SOURCES.md. No channels were connected, no customer lists were imported and no messages were sent.
