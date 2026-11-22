# Technical running cost budget

Latest planning example: [analysis/23](23_DAY_25_LAUNCH_SCOPE_AND_BUDGET.md) and [budget inputs](../models/launch_25_day_budget.json) now model the Hostinger frontend and expanded messaging scope. Base technology is approximately GBP69.74/month initially and GBP84.74 at the stated VPS renewal, with proposed reserve envelopes GBP85/105. This supersedes the old numerical planning targets below; actual service selection, usage and tax remain unconfirmed. No frontend Workers charge is included in that new example.

Status update, 8 November 2026: this is the historical budget for the previous Cloudflare frontend model. Next.js is now planned on Hostinger, with admin/API/PostgreSQL there too. Revolut and PayPal are selected, with Apple Pay/Google Pay required; Stripe is excluded. The fee example below must not be used as an active payment assumption. No new final total is established until server sizing and actual payment terms are reviewed.

Additional scope identified 8 November: distinguish staff mailboxes, transactional delivery, marketing contacts/sends/automations, support-inbox seats, optional SMS/eligible WhatsApp traffic and ongoing campaign work. The earlier email allowance is not a quote for this expanded scope. See [customer messaging costs and inputs](21_CUSTOMER_MESSAGING_AND_RETENTION.md). No provider, subscriber volume, messaging tariff or revised total is selected.

Checked: 7 November 2026. Scope: recurring technology for the user's planned ecommerce setup at an assumed 10,000 visitors/day. This is not the total cost of building or operating a medical-supply business.

## Confirmed plans and unselected services

The user plans Next.js on Cloudflare, admin/API/PostgreSQL on Hostinger KVM 4, upload-time image optimisation, R2 image/object storage, and domain registration through Cloudflare. The domain name/TLD, backend commerce platform, email provider and monitoring tools are not selected. No services have been purchased or deployed through this work.

Use USD1 = GBP0.80 as an explicit budget conversion assumption, not a current FX quote. Prices below exclude applicable taxes and payment-provider currency fees. Actual invoices depend on checkout, usage and currency conversion.

## Component budget

| Component | Monthly GBP equivalent | Evidence or assumption |
|---|---:|---|
| Hostinger KVM 4 | 9.99 promotional; 24.99 renewal | Verified public offer, 24-month term paid upfront |
| Cloudflare Workers frontend | 4–8 | Prior USD5–10 runtime scenarios converted at assumed FX; not a usage guarantee |
| One ordinary non-premium domain at Cloudflare | 1–2 | GBP12–24/year budget allowance; exact name/TLD price is not quoted |
| Prepared product-image storage/delivery | 0–3 | Usage allowance for selected R2 route, assuming modest storage/operations; not a cap |
| Independent offsite backups | 1–5 | Incremental storage/operations allowance, not a managed-backup quote |
| Transactional email | 0–16 | Free-tier eligibility or illustrative USD20/month service tier; usage dependent |
| One staff mailbox | 1–6 | Provider/seat allowance, not a verified selected plan |
| Basic monitoring and error tracking | 0–5 | Free/self-hosted or small paid allowance; labour excluded |
| DNS and ordinary SSL/CDN functions | 0 additional | Use included/free service features; no paid zone upgrade assumed |
| Admin/API/database software licence | 0 assumed | Conditional on a suitable open-source/custom stack with no paid commercial add-ons |

Arithmetic: GBP16.99–54.99/month during the initial VPS term, including the annual domain apportioned monthly. The corresponding range after the stated VPS renewal is GBP31.99–69.99/month. Rounded recurring ranges: GBP17–55 initially and GBP32–70 at renewal.

Proposed practical planning envelope with a small buffer: GBP30–60/month initially and GBP45–75/month at renewal. These are proposed allowances, not accepted spending authority or a guaranteed maximum. Extra search, cache persistence, plugins, logs or higher usage can add costs.

## Verified pricing and qualifications

Hostinger currently advertises KVM 4 at GBP9.99/month equivalent, GBP239.76 paid for 24 months, renewing at GBP24.99/month for the same term. Public plan details include weekly backups, but the independent offsite allowance above is a separate proposed copy. Its domain offer does not replace the user's choice to register at Cloudflare. [Hostinger VPS](https://www.hostinger.com/uk/vps-hosting).

The frontend scenarios are calculated in [hosting analysis](17_HOSTING_ARCHITECTURE_AND_COSTS.md). They assume a particular request/CPU profile rather than inferring cost from visitors alone. [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

Cloudflare Registrar publishes at-cost registration/renewal and included DNS/security features. Actual domain cost depends on name, extension, eligibility and checkout. GBP12–24/year is a provisional allowance for one ordinary domain, not a quoted .com or .co.uk tariff or a name availability claim. [Cloudflare Registrar](https://www.cloudflare.com/domains/).

R2 Standard offers included storage/operations and free internet egress, with costs beyond allowances. Sum images, originals, backups and all other account usage before applying free allocations; do not claim the same free storage independently for each cost row. If stored on the VPS instead, files share its disk/bandwidth and need backup capacity. [R2 pricing](https://developers.cloudflare.com/r2/pricing/).

Resend is an example, not a selected provider: its published free transactional tier has 3,000 emails/month with a 100/day limit; Pro lists USD20/month for 50,000 emails, with overage. At 10,000 visits/day, email volume depends on orders, login/reset traffic and notification count, not visits alone. Marketing email is a separate workload. [Resend pricing](https://resend.com/pricing).

## Cash required versus monthly equivalent

The VPS is not a GBP9.99 monthly payment under the advertised offer. Budget GBP239.76 upfront, plus the domain's annual checkout price and first-month paid services.

Under the component assumptions, recurring expense is about GBP203.88–659.88 per year during the initial term. First-year cash is approximately GBP323.76–779.76 because the VPS payment covers two years upfront: GBP239.76 + GBP12–24 domain + 12 x GBP6–43 other monthly services. Tax, variations in actual domain/FX and additional services are excluded. Do not count the prepaid VPS again as monthly cash during that covered term.

## Variable payment fees

Payment processing is separate from hosting. Stripe currently publishes 1.5% + GBP0.20 for standard UK cards; premium/non-UK cards, conversion and other services have different fees. Stripe is not selected or approved for this catalogue. [Stripe UK pricing](https://stripe.com/gb/pricing).

Illustratively, 100 standard-UK-card payments charging customers GBP100 each produce GBP170 in processing fees: 1.5% x GBP10,000 + GBP0.20 x 100. Calculate on gross amounts charged, not automatically on ex-VAT product revenue. Fees depend on actual card mix, refunds, disputes and provider terms.

## Costs not established by this hosting estimate

Development/design, integrations, product-data ingestion, maintenance labour, commercial software, security work, paid search infrastructure, warehouse/3PL integrations, accounting systems, licences/compliance, insurance, stock, staff, freight and marketing remain separate. A full bespoke store with the planned product and regulated-category breadth cannot be priced as development from hosting invoices alone.

The next estimate needs a defined build scope, chosen software stack and provider quotes. This file establishes only an initial technical-running-cost envelope.

## Consolidated estimate with 100GB R2

The user asked for the consolidated cost after selecting R2. Use 100GB as an illustrative storage volume, not a confirmed storage requirement. At the existing USD1 = GBP0.80 planning assumption, USD1.35 storage is GBP1.08/month. KVM 4 GBP9.99 + Workers GBP4–8 + R2 storage GBP1.08 + domain GBP1–2 monthly equivalent gives GBP16.07–21.07/month for core hosting/domain. R2 request overages are excluded.

A simple proposed planning target is GBP40/month initially, within the previously stated GBP30–60 envelope, to allow for basic email, independent backups and a usage contingency. At the advertised VPS renewal, add GBP15/month: core becomes GBP31.07–36.07 and the proposed planning target GBP55/month. These targets are allowances rather than fixed supplier bills or an accepted spending decision. Applicable taxes, variable payment fees, development/maintenance labour and business operations remain excluded. The VPS still requires the stated 24-month upfront payment.
