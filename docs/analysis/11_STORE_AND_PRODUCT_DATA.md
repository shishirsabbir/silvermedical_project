# Store and product data requirements

Updated: 8 November 2026. The user plans Next.js, admin, API and PostgreSQL on Hostinger; the earlier Cloudflare frontend plan is superseded. R2 and the Cloudflare domain remain selected. Revolut, Apple Pay, Google Pay and PayPal are required; Stripe is excluded. Commerce/backend framework and deployment topology remain unselected. No store is built by this research task. See the [latest discussion brief](../../memory/BRIEF_2026-11-08.md).

## Core design principle

8 November business-model clarification: build for one retailer procuring and holding its own inventory. Supplier accounts are procurement data, not independent sellers. Include purchasing, receipt, stock/lot control and dispatch requirements; a vendor marketplace portal, commissions and split seller payouts are not requested.

Model products, regulatory evidence, destinations, buyer permissions, price lists and fulfilment sources separately. One global published flag is insufficient for a full-range UK/EU medical catalogue.

## Product information record

| Domain | Fields |
|---|---|
| Identity | Internal SKU, manufacturer, MPN, GTIN/EAN, family, variant, applicable UDI identifiers |
| Sellable unit | Unit/box/case, units per pack, base unit, order multiple, dimensions and weight |
| Intended purpose | Manufacturer's intended use, intended users, professional/self-test status, relevant warnings |
| Classification | Device/IVD/PPE/biocide/medicine/ordinary goods, class where applicable, rationale and reviewer |
| Evidence | Declaration/certificate IDs, manufacturer label/IFU, version, dates, scope and source |
| Supply role | Manufacturer, supplier, importer, UKRP/EU representative where applicable and role by lane |
| Destination | GB, NI and each approved country/channel; reason and review date |
| Commercial | Currency, landed cost, tax code, price list, discounts, freight class, minimum margin |
| Fulfilment | Own stock, supplier-direct, quote only, availability timestamp, lead time and cutoff |
| Traceability | Lot/serial requirement, expiry, storage limits, recall link and minimum delivered shelf life |
| Service | Warranty owner, installation, training, calibration, spares and return conditions |
| Content rights | Image/data permission, translation owner and claims approval |

Not every field is legally mandatory for every product. Required-field rules should follow the product regime and business activity. Store confidential supplier cost separately from public product content. Use the [SKU approval form](../templates/SKU_APPROVAL.md).

## Discovery and purchasing

Support category and specialty navigation, exact identifier search, synonyms, common abbreviations, spelling tolerance and filters for pack, size, sterility, connector, compatibility and intended use. A search match must not imply that two products are clinically interchangeable.

Product pages should show clear identifiers, pack quantity, gross/net prices as appropriate, availability source, destination-specific delivery, shelf-life promise where relevant, essential warnings, permitted buyer type, downloadable instructions and service/warranty information. Restriction rules should apply to feeds and ads as well as checkout.

At reorder, flag changed price, pack, availability, product revision, expiry promise, restriction or discontinued status. Never silently substitute a revised/alternative device in a saved basket. Saved lists and organisation purchasing patterns are useful benchmark features. [Praxisdienst](https://www.praxisdienst.com/).

## Accounts and checkout

Support organisation and consumer account types, professional verification where required, multiple ship-to sites, purchase permissions, PO references, approved price lists, quotes, invoices/credit notes, eligible tax-relief review and trade credit. Do not require account creation for ordinary consumer purchasing without a commercial reason.

Validate address, country, postcode, product eligibility, stock reservation, tax, delivery class and complete total before payment. Split incompatible shipments and disclose separate costs/timing. Mixed restricted/ordinary baskets need a deliberate review/acceptance model to avoid charging for an order that cannot be supplied.

## System boundaries

| System | Responsibility |
|---|---|
| Commerce | Presentation, basket, buyer access and order capture |
| PIM/document store | Approved product data, evidence and publication rules |
| ERP/accounting | Purchasing, supplier costs, tax, invoices, credits and receivables |
| WMS/3PL | Stock, lots, expiry, quarantine, allocation and shipments |
| Order management | Split sourcing, acceptance, promises and exception handling |
| CRM/helpdesk | Organisation context, support, complaints and recall contacts |
| Analytics | Consent-aware behavioural and commercial measurement |

A platform comparison should test actual workflows, APIs, auditability, scale and total cost. Avoid choosing solely from storefront appearance or theme availability.

## Security and accessibility

Use MFA and least privilege for staff, approved payment-provider components, signed/validated integrations, backups, audit logs and incident procedures. Minimise health information in orders and support. Define retention and processor contracts.

Proposed accessibility acceptance target: WCAG 2.2 AA with keyboard, screen-reader, form/error, contrast and checkout checks. This is a design target, not a claim of universal legal certification. Assess destination legal obligations separately, including EU consumer ecommerce accessibility requirements. [European Accessibility Act](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/european-accessibility-act-eaa_en).

## Essential acceptance scenarios

Test exact pack ordering, product/country blocks, professional validation, mixed VAT/relief, bulky/hazardous shipping, supplier feed failure, split shipment, cancellation/refund, reorder changes, lot-to-order recall and invoice reconciliation. Include failures and recovery, not only successful payment.
