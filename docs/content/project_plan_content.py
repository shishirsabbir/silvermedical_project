"""Editable content for the full project document; dates and scope travel with sources."""

TITLE = "UK medical ecommerce"
SUBTITLE = "Business scope, implementation and operating plan"
DATE = "8 November 2026"


def p(text): return {"kind": "p", "text": text}
def h(text): return {"kind": "h", "text": text}
def items(*text): return {"kind": "list", "items": list(text)}
def table(headers, rows, widths=None): return {"kind": "table", "headers": headers, "rows": rows, "widths": widths}
def callout(title, text, tone="teal"): return {"kind": "callout", "title": title, "text": text, "tone": tone}


SOURCES = [
    ("R01", "MHRA medical devices in GB", "https://www.gov.uk/guidance/regulating-medical-devices-in-the-uk", "8 Nov 2026", "GB devices/IVDs; conformity and conditional CE transitions"),
    ("R02", "MHRA device registration", "https://www.gov.uk/guidance/register-medical-devices-to-place-on-the-market", "8 Nov 2026", "Registration/economic-operator arrangements; registration is not approval"),
    ("R03", "MHRA Northern Ireland devices", "https://www.gov.uk/guidance/medical-devices-eu-regulations-for-mdr-and-ivdr", "8 Nov 2026", "NI EU MDR/IVDR; role-specific requirements"),
    ("R04", "OPSS PPE guidance", "https://www.gov.uk/government/publications/personal-protective-equipment-enforcement-regulations-2018", "8 Nov 2026", "Separate GB/NI PPE guidance; intended purpose and operator duties"),
    ("R05", "HSE biocides", "https://www.hse.gov.uk/biocides/about/introduction.htm", "8 Nov 2026", "GB BPR and NI EU BPR; product boundaries"),
    ("R06", "MHRA medicines licensing", "https://www.gov.uk/guidance/apply-for-manufacturer-or-wholesaler-of-medicines-licences", "8 Nov 2026", "Human medicines activities; indexed official passages, intermittent direct timeouts"),
    ("R07", "MHRA human medicine imports", "https://www.gov.uk/guidance/import-a-human-medicine", "8 Nov 2026", "Activity/origin-dependent import permissions"),
    ("R08", "MHRA medicines advertising", "https://www.gov.uk/guidance/advertise-your-medicines", "8 Nov 2026", "Public versus professional promotion of human medicines"),
    ("R09", "VMD online sales", "https://www.gov.uk/guidance/sell-veterinary-medicines-on-the-internet", "8 Nov 2026", "Veterinary medicine categories, premises, professionals and NI qualifications"),
    ("R10", "MHRA post-market surveillance", "https://www.gov.uk/government/publications/medical-devices-post-market-surveillance-requirements/introduction-and-scope", "7 Nov 2026", "GB manufacturer duties; cooperation and complaint process implications"),
    ("C01", "GOV.UK online selling", "https://www.gov.uk/online-and-distance-selling-for-businesses/online-selling", "8 Nov 2026", "UK online checkout/disclosure/confirmation rules"),
    ("C02", "GOV.UK returns and refunds", "https://www.gov.uk/accepting-returns-and-giving-refunds", "8 Nov 2026", "UK consumer cancellation and faulty-goods guidance"),
    ("C03", "CMA price transparency", "https://www.gov.uk/government/publications/price-transparency-cma209/providing-clear-and-accurate-information-about-prices-summary", "8 Nov 2026", "Consumer total prices and unavoidable charges under current rules"),
    ("C04", "HMRC VAT registration", "https://www.gov.uk/register-for-vat", "8 Nov 2026", "UK establishment/turnover tests; entity-specific assessment needed"),
    ("C05", "HMRC VAT rates", "https://www.gov.uk/vat-rates", "8 Nov 2026", "UK standard and other VAT rates; not SKU classification"),
    ("C06", "HMRC disability relief", "https://www.gov.uk/guidance/reliefs-from-vat-for-disabled-and-older-people-notice-7017", "8 Nov 2026", "Qualifying goods/customer/use/evidence; indexed official text after timeout"),
    ("C07", "HMRC charity equipment relief", "https://www.gov.uk/guidance/charity-funded-equipment-for-medical-and-veterinary-uses-notice-7016", "8 Nov 2026", "Qualifying funding/recipient/goods; indexed official guidance"),
    ("C08", "UKIPO image copyright", "https://www.gov.uk/government/publications/copyright-notice-digital-images-photographs-and-the-internet/copyright-notice-digital-images-photographs-and-the-internet", "8 Nov 2026", "Commercial image reuse and rights"),
    ("M01", "Google Merchant healthcare", "https://support.google.com/merchants/answer/6150151?hl=en", "8 Nov 2026", "UK listings; pharmacy certification and restricted goods"),
    ("M02", "Google Ads healthcare", "https://support.google.com/adspolicy/answer/176031?hl=en", "8 Nov 2026", "UK online-pharmacy passage; separate advertising rules"),
    ("M03", "Google product data", "https://support.google.com/merchants/answer/7052112?hl=en", "8 Nov 2026", "Feed identifiers and landing-page consistency"),
    ("M04", "Google misrepresentation", "https://support.google.com/merchants/answer/6150127?hl=en", "8 Nov 2026", "Identity, offer and account representations"),
    ("M05", "Google health audiences", "https://support.google.com/adspolicy/answer/16701855", "8 Nov 2026", "Sensitive-interest targeting"),
    ("M06", "WhatsApp Business policy", "https://whatsappbusiness.com/policy/", "8 Nov 2026", "Medical/healthcare restrictions, opt-in, templates and country exceptions"),
    ("P01", "ICO electronic-mail rules", "https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/how-do-we-comply-with-the-pecr-electronic-mail-marketing-rules/", "8 Nov 2026", "Indexed official consent/soft-opt-in passages; direct page 403"),
    ("P02", "ICO B2B marketing", "https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/", "8 Nov 2026", "Indexed official subscriber distinctions; direct page 403"),
    ("P03", "ICO special-category data", "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-rules-on-special-category-data/", "8 Nov 2026", "Indexed Article 6/9 conditions; direct page 403"),
    ("P04", "ICO storage/access guidance", "https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-the-use-of-storage-and-access-technologies/", "7 Nov 2026", "Tracking and exceptions; 8 Nov direct refresh blocked"),
    ("T01", "Hostinger UK KVM offer", "https://www.hostinger.com/uk/vps-hosting", "8 Nov 2026", "Published specifications, upfront term and renewal; checkout unverified"),
    ("T02", "Cloudflare R2 pricing", "https://developers.cloudflare.com/r2/pricing/", "8 Nov 2026", "Standard storage/operations, shared free allowances and rounding"),
    ("T03", "Cloudflare Registrar", "https://www.cloudflare.com/domains/", "8 Nov 2026", "At-cost registration model; exact name/TLD not quoted"),
    ("T04", "Resend pricing example", "https://resend.com/pricing", "8 Nov 2026", "Unselected transactional-email example; no catalogue approval established"),
    ("T05", "Revolut UK merchant fees", "https://help.revolut.com/help/merchant-accounts/fees/how-much-does-it-cost-to-accept-card-payments/business/", "8 Nov 2026", "Specified online card-type rates; actual mix/terms unknown"),
    ("T06", "PayPal UK fees", "https://www.paypal.com/uk/business/paypal-business-fees", "8 Nov 2026", "Specified domestic commercial example; other methods differ"),
    ("T07", "PayPal UK acceptable use", "https://www.paypal.com/uk/legalhub/paypal/acceptableuse-full", "8 Nov 2026", "Approval requirements for medical devices/prescription items"),
    ("T08", "Revolut wallet integration", "https://developer.revolut.com/docs/guides/merchant/accept-payments/online-payments/apple-pay-google-pay/introduction", "8 Nov 2026", "Active Merchant-account Apple Pay/Google Pay support"),
    ("T09", "Next.js self-hosting", "https://nextjs.org/docs/app/guides/self-hosting", "8 Nov 2026", "Reverse proxy, cache persistence and instance coordination"),
    ("T10", "Nest HTTP adapters", "https://docs.nestjs.com/techniques/performance", "8 Nov 2026", "Fastify adapter and compatibility"),
    ("T11", "Vite guide", "https://vite.dev/guide/", "8 Nov 2026", "React templates and production build"),
    ("T12", "Gmail sender guidelines", "https://support.google.com/mail/answer/81126?hl=en", "8 Nov 2026", "Personal Gmail authentication and bulk-sender requirements"),
    ("E01", "EU economic operators", "https://health.ec.europa.eu/medical-devices-topics-interest/economic-operators_en", "7 Nov 2026", "EU MDR/IVDR supply-chain roles; country dossiers still required"),
]

CHAPTERS = [
{
"id":"business", "group":"Business and scope", "title":"The business we are building",
"intro":"Build a substantial UK medical supplies retailer with its own stock, under a new brand. The website, admin and API support a real procurement and fulfilment operation.",
"blocks":[
p("The owners selected a single-retailer model: the business purchases goods, receives and holds stock, sells directly and remains responsible for the customer order. Mixed UK/EU sourcing may include Praxisdienst and original manufacturers. No supplier or content agreement is established by this plan."),
table(["Area","Project direction"],[
["Customers","Consumers and verified professional/business buyers; product entitlement is checked separately."],
["Range","Full-range ambition across supplies, equipment, diagnostics, PPE, infection control and relevant medicine/veterinary routes. Actual SKUs are unknown."],
["Market","UK first. Great Britain and Northern Ireland need separate eligibility decisions; Europe follows country by country."],
["Benchmark","Praxisdienst is the operating/customer-experience benchmark. Its catalogue is not a UK permission or a content licence."],
["Operating identity","New brand and legal operator still to be confirmed. The workspace name does not establish either."]],[0.23,0.77]),
h("How an ordinary sale should work"),
p("Qualify a supplier, approve the exact product and destination, receive usable stock, publish accurate information, accept an eligible order, reserve stock, confirm payment, dispatch and support the customer. Refunds, returns and recalls remain part of the same record."),
callout("Definition of success","A buyer can find the correct item and pack, see the complete price, order with an approved method and receive the promised goods. Staff can explain every hold, stock movement and refund.")
],"refs":[]},
{
"id":"phase-one", "group":"Business and scope", "title":"What Phase 1 will include",
"intro":"The first release must support a complete selling journey for a bounded, reviewed assortment. It serves both buyer groups and includes the operational controls required for the activated products.",
"blocks":[
table(["Module","Launch deliverable"],[
["Storefront","Responsive Next.js categories/search, product/variant pages, pack quantities, availability, basket, checkout, guest/account journeys and order history."],
["Admin/catalogue","Products, manufacturers, suppliers, draft imports, evidence references, approval status, staff roles, original/licensed content and R2 image uploads."],
["Owned inventory","Receipts, stock adjustments, reservations, quarantine and applicable lot/serial/expiry records. One authoritative stock balance."],
["Orders/payments","Server-calculated VAT/delivery, professional order checks, Revolut/wallets and PayPal subject to approval, verified payment events, dispatch and refunds."],
["Customer service","Order emails, invoices/credit notes, basic communication preferences, support ownership and documented returns/complaints."],
["Operations","Production configuration, monitoring, independent backups, restoration procedure, access review and staff training."]],[0.22,0.78]),
h("Deliberate initial simplifications"),
p("Manual carrier booking and tracking entry, accounting exports and human professional verification are acceptable if documented, staffed and tested. They must be described honestly and must not bypass product, tax or payment controls."),
callout("Complete means usable end to end","An attractive storefront with unfinished refunds, stock or dispatch handling does not meet the initial selling requirement. The acceptance scenarios later in this document define completion.")
],"refs":[]},
{
"id":"later", "group":"Business and scope", "title":"Later features and build exclusions",
"intro":"A staged release controls delivery order. It does not remove product categories from the full-range objective or create permission to sell unreviewed goods.",
"blocks":[
table(["Status","Features and boundaries"],[
["Later procurement","Company purchasing roles, multi-level approvals, quotes at scale, trade-credit limits and collections, contract prices and multi-site controls."],
["Later integrations","Accounting/ERP/WMS connectors, automated carrier labels, deeper supplier feeds and equipment servicing/calibration workflows."],
["Later growth","Richer CRM and automation, loyalty/referral schemes, merchandising experiments and European localisation/country activation."],
["Separate decisions","Prescription-medicine workflows, SMS/WhatsApp use cases, recurring subscriptions, financing and any clinical service."],
["Outside this model","Multi-vendor sellers, supplier self-publication, split marketplace payouts and dropshipping."],
["Outside initial software","Native mobile apps, a clinical prescribing service, a custom email delivery platform or campaign editor, and complete ERP/WMS replacement."],
["Explicit exclusion","Stripe. The required payment direction is Revolut with supported wallets and PayPal."]],[0.24,0.76]),
h("Content and migration boundaries"),
p("Do not copy competitor descriptions/images, trust badges, reviews, VAT numbers or licence statements without appropriate rights and accuracy. Old catalogue/customer data needs its own provenance, permission and suppression review. The former store's reported 7,000 SKUs are not a confirmed new catalogue."),
callout("Pricing boundary","Later integrations and regulated activities need separate work packages, acceptance criteria and budgets. The first-phase cost example does not fund every future capability.","amber")
],"refs":["C08"]},
{
"id":"product-rules", "group":"UK selling requirements", "title":"Medical product rules in the UK",
"intro":"There is no single universal medical-supplies licence. Determine the product's intended purpose, claims, buyer, destination and the retailer's actual supply-chain role.",
"blocks":[
table(["Route","Review required before activation"],[
["Devices and IVDs","GB: applicable UK Medical Devices Regulations 2002 conformity/registration route. Retain relevant declarations, labels, instructions and required certificates/operator evidence. [R01-R02]"],
["Northern Ireland","Review EU MDR/IVDR device arrangements, applicable marking and role-specific registration separately. A GB decision is not an NI decision. [R03]"],
["PPE","Assess wearer-protection purpose, conformity and operator duties. Dual-purpose items can need both PPE and device routes. [R04]"],
["Biocides","Establish product boundary, permitted claims and applicable authorisation/transitional route. GB BPR and NI EU BPR differ. [R05]"],
["Human medicines","Separate GSL, pharmacy/POM, patient supply, wholesale and import activities; see the dedicated decision page. [R06-R08]"],
["Veterinary medicines","VMD distribution category, authorised product, professional/premises and internet-sale requirements; NI qualifications matter. [R09]"],
["Other/specialist goods","Assess ordinary product safety, electrical/chemical/transport rules, sharps, gases, radiation, servicing and environmental duties as applicable."]],[0.25,0.75]),
p("Current GB CE recognition has conditional transitions: eligible legacy MDD/AIMDD products to certificate expiry or 30 June 2028, eligible IVDD products to certificate expiry or 30 June 2030, and MDR/IVDR products to 30 June 2030. Exceptions and transition conditions apply. Proposed indefinite recognition is not enacted permission. [R01]"),
callout("What the software should enforce","Store classification, evidence revision, seller role, buyer and destination permissions, review dates and stop-sale status. Registration is not MHRA endorsement; the platform must not display it as approval. [R02]")
],"refs":["R01","R02","R03","R04","R05","R06","R09"]},
{
"id":"medicines", "group":"UK selling requirements", "title":"Medicines and restricted purchasing",
"intro":"Prescription-only medicines remain an open business decision. A prescription upload field or a professional account does not establish an authorised supply operation.",
"blocks":[
table(["Activity","Decision and evidence needed"],[
["Patient supply","Appropriate pharmacy/professional model, premises where required, lawful prescribing/dispensing and accountable oversight. Establish GB/NI scope."],
["Supply to clinics","Wholesale activity assessment, relevant WDA(H) or applicable exception, premises/personnel, good distribution practice and customer entitlement."],
["Importing medicines","Origin/activity-specific authorisations and responsibilities. An EU supplier invoice does not settle the medicine import route."],
["Controlled drugs/clinical service","Separate specialist assessment of additional permissions and professional/healthcare-service responsibilities."]],[0.28,0.72]),
p("The legal and operational assessment must cover the exact activities rather than treating every sale to a medical customer alike. Relevant exceptions require confirmation; a licensed partner's permissions do not automatically cover this retailer. [R06-R07]"),
h("Buyer verification and order release"),
p("Separate business verification, a person's purchasing authority, profession-specific entitlement and any medicine supply review. A professional-use device is not automatically a prescription medicine. Store the reason, reviewer, evidence and expiry of each approval; recheck the effective rules at checkout and dispatch where necessary."),
p("If a future prescription workflow is accepted, use private documents, named authorised reviewers, access logs and a retention policy. Do not send clinical documents through public R2 asset URLs or routine marketing exports."),
callout("Publication and advertising gate","Recommended: keep prescription-medicine activation disabled until the owners substantiate the operating route. Public POM advertising is prohibited; professional promotion has separate audience/content requirements. [R08]","amber")
],"refs":["R06","R07","R08"]},
{
"id":"consumer-tax", "group":"UK selling requirements", "title":"Consumer rights, pricing and VAT",
"intro":"Consumer and professional purchasing share infrastructure, but contract status, product entitlement and tax treatment must be assessed independently.",
"blocks":[
h("What customers must understand"),
p("Show the actual seller, contact/address details, accurate product information, complete prices and payment/delivery terms. Explain cancellation and returns before purchase, allow error correction and provide a durable confirmation. Consumer prices must account for VAT and unavoidable charges; handle variable delivery charges transparently. [C01,C03]"),
p("For goods within ordinary distance-cancellation rules, consumers generally have 14 days after receipt to notify cancellation and another 14 days to return. Apply refund timing and standard-delivery rules. A qualifying sealed hygiene exception applies after unsealing; it is not a blanket medical-products exclusion. Faulty-goods rights remain separate. [C02]"),
h("How tax is implemented"),
p("The UK standard VAT rate is 20%. The ordinary UK-established registration tests include taxable turnover above £90,000 over the previous 12 months or expected above £90,000 in the next 30 days alone. Non-established operators can face different rules. [C04-C05]"),
p("Use product/transaction tax categories. Disability relief and charity-funded equipment relief have separate qualifying-goods, recipient/use/funding and evidence conditions. An NHS address, professional account or declaration does not make every item zero-rated. Obtain accountant approval for the actual rules, mixed baskets, delivery and imports. [C06-C07]"),
callout("Policies to prepare","Consumer terms, commercial terms, delivery, cancellation/returns, warranty/service, complaints, privacy/tracking and restricted-product policies. Review against CCR 2013, CRA 2015, Electronic Commerce Regulations 2002 and current DMCC 2024 requirements; preserve version/acceptance records.")
],"refs":["C01","C02","C03","C04","C05","C06","C07"]},
{
"id":"catalogue", "group":"Product and customer experience", "title":"Supplier approval and catalogue control",
"intro":"Supplier data is an intake source. It becomes saleable content only after commercial, product and rights review.",
"blocks":[
table(["Record","Information to capture"],[
["Supplier","Legal identity, relevant authorisations, supply-chain legitimacy, dispatch country, territory/resale rights, returns, warranty and recall contact."],
["Commercial lane","Purchase currency, case quantities, lead time, minimum shelf life, stock ownership, importer role, origin/customs and landed cost."],
["Product","Manufacturer/model, SKU/GTIN/MPN where assigned, variants, pack units, intended use and user, dimensions and compatibility."],
["Evidence","Applicable declarations/certificates, authorisations, labels/IFU, regulatory route, required operator evidence, expiry and reviewer."],
["Permissions","Destination, eligible buyer, public content, payment-provider/category and individual marketing-channel decisions."],
["Handling","Storage, dangerous-goods/carrier needs, lot/serial/expiry tracking, quarantine and minimum usable shelf life."]],[0.23,0.77]),
h("Publishing workflow"),
p("Import to draft, validate identifiers/pack data, resolve evidence errors, review claims/content rights, then approve the appropriate sale and channel states. Do not invent GTINs or publish copied disease claims. Track source revisions and re-review material changes."),
h("Media workflow"),
p("Validate uploads, optimise images in a bounded background job, store prepared variants in Cloudflare R2 and publish versioned public asset URLs. Keep originals/retention explicit. Private evidence and any future prescription records need separate access policies."),
callout("Fast launch without unsafe bulk publication","Start with a reviewed, in-stock assortment and reusable import templates. The wider taxonomy can exist as drafts while remaining categories become ready.")
],"refs":["R01","R02","C08","M03"]},
{
"id":"storefront", "group":"Product and customer experience", "title":"Storefront features and UI design",
"intro":"The shopping interface should make correct product selection and dependable purchasing easy for both occasional consumers and repeat professional buyers.",
"blocks":[
table(["Journey","Experience and implementation"],[
["Find","Category/specialty navigation, identifier search, technical facets and clear empty results. Begin with indexed PostgreSQL search; add a separate search service only if measured needs justify it."],
["Compare","Visible unit/box/case quantities, manufacturer/model, intended purpose, compatibility, stock, shelf-life information where relevant and downloadable approved documents."],
["Buy","Persistent basket, clear restrictions, address/delivery validation, complete total, approved wallet/payment methods and useful error recovery."],
["Return","Account order history, tracking, invoices, refund status and clear support/return routes. Ordinary consumer checkout should not need an unexplained compulsory account."],
["Reorder","Saved lists and repeat-order tools with current stock/price and eligibility rechecks; do not silently substitute medical products."]],[0.2,0.8]),
h("Visual and interaction standards"),
p("Use a restrained clinical palette, readable typography, clear pack/price hierarchy and authentic product imagery. Design mobile first, with large usable controls, keyboard navigation, visible focus, accessible forms and useful validation messages. WCAG 2.2 AA is the proposed acceptance target, not a claimed legal certification."),
h("Performance and content"),
p("Use appropriate Next.js rendering/cache strategy for public product pages, responsive prepared R2 images and bounded client JavaScript. Personal account, basket and restricted-price responses must not enter a public cache. Keep SEO titles, canonical URLs, sitemap and redirects aligned with approved pages."),
callout("Proposed screen set","Home/category/search, product detail, basket, checkout, order result, consumer account, professional application, support and policy pages. Review representative desktop/mobile journeys before expanding page templates.")
],"refs":["T09"]},
{
"id":"admin", "group":"Product and customer experience", "title":"Advanced admin and owned inventory",
"intro":"The admin is the operating workspace for the retailer. Its first priority is helping staff act correctly and see why an item or order is blocked.",
"blocks":[
table(["Workspace","Capabilities"],[
["Work queues","Products awaiting evidence, verification applications, incoming receipts, quarantined lots, held orders, failed jobs and reconciliation issues."],
["Catalogue","Draft imports with previews/errors, variants and pack units, document revisions, permissions, price/tax codes and upload optimisation."],
["Purchasing/stock","Supplier orders or basic purchase records, goods receipt, discrepancies, stock movement ledger, reservations, expiry/lot/serial data and quarantine."],
["Orders/service","Order timeline, payment status, verification holds, picking/dispatch, refunds, returns, complaint ownership and communications."],
["Governance","Least-privilege roles, MFA, named reviewers, actor/reason/time audit records, bounded exports and restricted-document access."]],[0.25,0.75]),
h("React implementation"),
p("Use regular React with a proposed Vite/TypeScript setup. The browser calls the API and never connects directly to PostgreSQL. Shared API contracts, server-side pagination/filtering, indexed lookups and background imports keep large screens responsive."),
h("Inventory rules"),
p("Separate available, reserved and quarantined stock. Reserve and release through transactions; avoid a single freely edited stock number. Returns are inspected before becoming saleable. For a recall, link the affected receipt/lot/serial to stock and customer orders, with a named safety escalation owner. Manufacturer PMS duties and reseller cooperation must not be confused. [R10]"),
callout("Later expansion","Add richer purchase-order approvals, multi-location allocation, cycle counts, automated supplier feeds and deeper warehouse systems after the core stock/order record is reliable.")
],"refs":["R10","T11"]},
{
"id":"orders", "group":"Product and customer experience", "title":"Orders, fulfilment and after-sales",
"intro":"An order must remain understandable from basket through payment, dispatch, returns and reconciliation.",
"blocks":[
table(["Step","Control and responsible action"],[
["Checkout","API recalculates price/tax/delivery, validates product/buyer/destination and reserves the appropriate stock. Snapshot the accepted terms and totals."],
["Payment","Create a pending payment/order record. Verify provider events and update state idempotently; a browser success redirect is not sufficient proof."],
["Release","Resolve professional/supply holds and confirm stock/payment. Recheck affected orders if eligibility or stock status changes."],
["Dispatch","Pick the correct pack/lot, record shipment/tracking and communicate the actual delivery promise. Define partial dispatch and restricted mixed-basket handling."],
["Return/refund","Record reason, statutory/commercial route, inspection/quarantine, refund/credit note and payment reconciliation."],
["Safety/service","Escalate complaints and adverse-event concerns; trace affected orders. Equipment installation, repair and calibration need a named provider/owner."]],[0.23,0.77]),
h("Fulfilment arrangements to establish"),
p("Owners must provide premises or an appropriate stock operation, trained staff, storage/temperature requirements, suitable carriers, packaging and returns handling. Bulky, hazardous or temperature-sensitive goods need their actual routes and pricing rather than a universal parcel promise."),
h("Customer support"),
p("Link email/web/phone cases to orders, assign ownership and set staffed response hours. Distinguish factual product information from clinical advice and route safety or suitability questions to the appropriate professional/operator."),
callout("Acceptance example","Staff can explain a held order, locate its stock, resolve the hold, dispatch it, issue a partial refund and reconcile the final amount without editing database records manually.")
],"refs":["C02"]},
{
"id":"payments", "group":"Payments and growth", "title":"Payment methods, approvals and fees",
"intro":"Required methods are Revolut, Apple Pay, Google Pay and PayPal. Technical support and approval for the medical catalogue are separate questions.",
"blocks":[
p("Revolut documents supported wallet integrations for an active Merchant account. Implement the approved checkout/domain configuration and customer-device fallbacks. PayPal's UK acceptable-use policy requires approval for medical devices as well as prescription items; obtain the relevant provider decisions before going live. [T07-T08]"),
table(["Published online example","Fee on a £100 payment"],[
["Revolut UK Visa/Mastercard consumer: 1% + £0.20","£1.20"],
["Revolut UK/EEA Visa/Mastercard commercial: 2.5% + £0.20","£2.70"],
["PayPal UK domestic All Other Commercial Transactions: 2.9% + £0.30 received in GBP","£3.20"]],[0.75,0.25]),
p("These are specified published examples, not a blended forecast or negotiated offer. Card type, method, cross-border, FX, refunds, disputes and actual agreements can change the cost. Professional purchasing makes commercial-card mix especially relevant. Payment fees sit outside the fixed technology budget. [T05-T06]"),
h("Implementation and verification"),
items("Use provider components and keep secrets server-side; validate totals and permitted payment routes in the API.","Persist provider IDs/events, verify signatures using current integration documentation, deduplicate notifications and reconcile delayed or missing events.","Agree reservation, authorisation/capture, restricted-order approval and refund sequencing; do not hold database locks across provider calls."),
callout("Launch dependency","Owners need approved merchant accounts and accepted catalogue terms. No integration choice can guarantee an approval date. Do not substitute a misleading product category to obtain acceptance.","amber")
],"refs":["T05","T06","T07","T08"]},
{
"id":"google", "group":"Payments and growth", "title":"Google Merchant Center and campaigns",
"intro":"Lawful website supply, Merchant Center listings and Google Ads are separate eligibility decisions. Build controlled channel rules into the catalogue.",
"blocks":[
p("UK prescription/behind-the-counter drug listings are excluded from Merchant Center. Its UK OTC route requires a GPhC-registered online pharmacy certified by Google. Other healthcare goods need individual review, and Google can assess the website/accounts as well as submitted products. [M01]"),
p("Google Ads has separate UK online-pharmacy conditions and certification; prescription drugs cannot be promoted in the relevant UK pharmacy ads/landing pages. Apply UK medicines advertising law as well. [M02,R08]"),
h("Onboarding sequence"),
items("Obtain the former store's actual notices, affected products/entities and appeal status. The reported ban/closure causes are unverified; a new name does not resolve underlying enforcement.","Use truthful operator/domain/contact information and clear delivery, payment and returns terms. Review the whole launch site before submitting a feed.","Verify/claim the domain, configure required business/shipping/returns settings, and submit only reviewed, available, purchasable items with genuine identifiers and consistent prices/stock.","Resolve diagnostic causes, follow the applicable review process and monitor product/policy changes. Approval cannot be guaranteed. [M03-M04]"),
h("Campaign approach"),
p("Start with original category/product SEO and tightly scoped Search/Shopping for eligible stocked goods with known contribution. Review claims, search terms, landing pages, exclusions and spend. Evaluate Performance Max after feed controls work, including URL expansion and automated assets."),
callout("Measurement and targeting","Reconcile conversions to paid orders/refunds and contribution after advertising. Do not build audiences from prescriptions or inferred health conditions; review sensitive-interest targeting rules before activating remarketing/customer lists. [M05]")
],"refs":["M01","M02","M03","M04","M05","R08"]},
{
"id":"messaging", "group":"Payments and growth", "title":"Email, WhatsApp, SMS and CRM",
"intro":"Plan the customer lifecycle alongside acquisition: essential service notices, useful reordering and relevant marketing with recorded permissions.",
"blocks":[
table(["Capability","Implementation and scope"],[
["Service email","Account/verification, order, dispatch, exceptions, refund and safety templates; delivery failures/retries, with promotional content kept separate."],
["Marketing email","Reviewed welcome, eligible basket reminders, stock alerts, replenishment and reactivation; timing/frequency remain decisions."],
["Permissions","Record sender, channel, purpose, applicable basis, evidence/version, timestamp and withdrawal/suppression. Recheck before each queued send."],
["CRM/support","Order-linked case history, ownership and escalation. Use a managed platform's editor/inbox first; a custom campaign builder is separate scope."],
["Optional channels","SMS after demand/permission/provider/cost review. WhatsApp remains a feasibility decision rather than a promised campaign channel."]],[0.25,0.75]),
p("For unsolicited electronic-mail marketing to individuals, use valid consent or an evidenced products/services soft opt-in: direct collection during sale/negotiation, the sender's own similar offerings, and opt-outs at collection and each message. Corporate subscriber rules differ; sole traders/some partnerships are individual subscribers. Personal-data duties still apply. [P01-P02]"),
p("WhatsApp restricts promotion/sale/facilitation of medical/healthcare products and drugs. Its limited OTC exception does not list the UK. Its opt-in/template rules do not grant this retailer permission. Assess exact products and service/marketing workflows separately. [M06]"),
callout("Practical safeguards","Do not treat an abandoned basket as automatic subscription, or import old customers as marketable without provenance/controller/permission review. Suppress withdrawn marketing while preserving appropriate service communication. Authenticate branded email and monitor bounces/complaints. [T12]")
],"refs":["P01","P02","M06","T12"]},
{
"id":"privacy", "group":"Technology and implementation", "title":"Privacy, security and trust",
"intro":"Medical ecommerce should minimise sensitive information and maintain clear access, retention and processing responsibilities.",
"blocks":[
h("Data and tracking"),
p("Document UK GDPR/DPA 2018 purposes, lawful bases, retention, processor contracts and international transfer arrangements. Identifiable health information requires both an Article 6 basis and an Article 9 condition, with associated UK conditions where required. Do not collect prescriptions or condition details for ordinary supply orders by default. [P03]"),
p("Block advertising tracking until valid consent. Review any applicable statistical-purpose exception against current ICO conditions; permission to receive marketing is not blanket permission for tracking pixels or advertising audiences. [P04]"),
table(["Control","Proposed implementation"],[
["Staff access","MFA, least-privilege roles, secure sessions, access reviews and rapid offboarding. Separate review and operational responsibilities where needed."],
["Documents","Private storage and short-lived authorised access for sensitive records; audit access and exports. No public image URLs for clinical evidence."],
["Infrastructure","Private PostgreSQL, restricted network access, secret management, patching, validated uploads and rate/payload limits."],
["Application","API validation/authorisation, CSRF/session protection as appropriate, server totals, idempotency, safe logs and dependency review."],
["Recovery","Independent backups, documented retention, restore drills, recovery objectives and incident escalation."],
["Rights and retention","Request handling, deletion/retention review and necessary suppression/transactional records; do not indiscriminately erase recall traceability."]],[0.23,0.77]),
callout("Legacy information","The new brand does not automatically inherit the former business's customer permissions, reviews, registrations or content rights. Establish the actual legal/controller relationship before reuse.")
],"refs":["P03","P04"]},
{
"id":"architecture", "group":"Technology and implementation", "title":"Architecture and hosting design",
"intro":"Host the application services on Hostinger KVM and use Cloudflare for the domain and R2 objects. This supersedes the earlier Cloudflare frontend plan.",
"blocks":[
table(["Layer","Technology and responsibility"],[
["Public storefront","Next.js on Hostinger; product discovery, rendering, basket and account UI."],
["Admin","Regular React; Vite/TypeScript recommended, not selected by the user. Browser calls the API."],
["API","NestJS with Fastify recommended; plain Fastify is an alternative. One authoritative business service, initially a modular monolith."],
["Data","PostgreSQL, transactions/constraints and migrations. Prisma is a proposed access layer; ORM choice remains open."],
["Worker","Durable imports, image optimisation, notifications, exports and feed jobs with limits/retries. Choose a queue after workload review."],
["Cloudflare","Registrar/DNS and R2 prepared media. Keep private records separate from public assets."],
["Integrations","Approved payment providers, managed email and later accounting/carrier systems; verified events and reconciliation."]],[0.25,0.75]),
h("Deployment topology"),
p("Internet -> reverse proxy -> Next.js / static React admin / API. The API and worker use private PostgreSQL and permitted R2/provider connections. Use distinct service users, secrets and environments. Keep builds and resource-heavy jobs from starving the production database."),
p("Nest supports a Fastify adapter; integration packages must suit the adapter. Next.js self-hosting guidance covers a reverse proxy, cache persistence and multi-instance coordination. Framework choice alone does not establish throughput. [T09-T11]"),
callout("KVM 4 capacity is a hypothesis","The published starting plan has 4 vCPU, 16GB RAM, 200GB NVMe and 16TB bandwidth. Measure combined rendering/API/database/worker peaks. One VPS remains a shared outage point even with isolated services. [T01]")
],"refs":["T01","T09","T10","T11"]},
{
"id":"implementation", "group":"Technology and implementation", "title":"How the features will be implemented",
"intro":"Use clear domain modules and shared API contracts so UI changes do not bypass stock, approval, pricing or payment rules.",
"blocks":[
table(["Domain","Records and key behaviour"],[
["Identity","Users, organisations, memberships, professional approvals and roles. Apply product entitlement independently of account labels."],
["Catalogue","Products, variants, pack units, evidence revisions, approval decisions, territory/channel permissions and media assets."],
["Inventory","Receipts, lot/serial/expiry records, stock movements, reservations and quarantine. Use transactions for competing stock changes."],
["Commerce","Price/tax/delivery rules, baskets, quotes where accepted, orders and immutable order-line snapshots."],
["Payments","Provider accounts/IDs, events, attempts and refunds; idempotent transitions and reconciliation jobs."],
["Operations","Shipments, returns, cases, notifications, permission events, audit history and durable jobs."]],[0.23,0.77]),
h("Build a representative vertical slice first"),
p("Demonstrate one reviewed product through admin upload, stock receipt, storefront, eligible checkout, provider sandbox event, dispatch and refund. Record actual effort and failures before extrapolating to the whole backlog. This tests architecture and integration decisions together."),
h("Where implementation effort should go"),
p("Reuse established authentication/payment/UI components where appropriate. Keep medical approval, owned-stock traceability and effective buyer/destination rules explicit in our domain. Background jobs must be bounded, observable and safe to retry; material supplier/evidence changes should trigger review."),
callout("AI-assisted development","AI tools can draft modules, migrations, interfaces and tests and help review changes. Human review, integration, accountable product decisions and operational checks remain required. Multiple agents do not establish a 25-day guarantee.")
],"refs":[]},
{
"id":"day-25", "group":"Delivery and budget", "title":"The 25-day launch plan",
"intro":"One-page roadmap for the first complete selling phase. Day 1 is the agreed start date; 25 calendar days and about 200 focused developer hours are planning assumptions to confirm.",
"blocks":[
table(["When","Build and prepare","Evidence of completion"],[
["Days 1-3","Freeze launch assortment/backlog, choose API/reuse approach; establish operator/supplier/tax/delivery information, domain/KVM and merchant applications.","Named owners, sample SKU dossiers, scope decisions and dependency tracker."],
["Days 4-10","Database/API, React admin, product review/imports, stock/media and responsive Next.js discovery pages.","Approved product received into stock and visible only in its permitted routes."],
["Days 11-17","Checkout, approved payment flows/events, reservations, tax/delivery, professional holds, dispatch/refunds and service emails/preferences.","A complete sandbox order-to-dispatch/refund journey with clear failures/holds."],
["Days 18-24","Freeze launch data/policies; test mobile/accessibility, concurrent stock, failed/duplicate payments, roles, fulfilment, peak load and restore; train staff.","Acceptance checklist passes; staff can operate and recover the service."],
["Day 25","Controlled release of approved products/destinations with staffed support, monitored orders and limited eligible campaigns.","Release owner signs off legal/product, provider, stock and operational readiness."]],[0.17,0.48,0.35]),
h("Work that must run alongside development"),
p("Owners secure lawful products/content rights, ready stock, premises/fulfilment, tax decisions and merchant approval. Product/professional reviewers respond daily. Keep the initial scope bounded; use tested components and documented manual carrier/accounting workflows where suitable."),
callout("Release gate","Go live only after the order/payment/dispatch/refund path, access checks and restoration work, and actual product/provider/stock arrangements are ready. If a dependency fails, revise the lawful assortment or release date; do not bypass the gate.","amber"),
p("After launch, stabilise orders and support, then activate advanced procurement, automation, integrations and additional categories/countries. Full-range ambition remains. AI assists implementation/review; external approvals and complete future scope cannot be promised within this one milestone.")
],"refs":[]},
{
"id":"technology-cost", "group":"Delivery and budget", "title":"Technology costs and payment timing",
"intro":"The latest example assumes Hostinger frontend/backend, prepared R2 images and separate messaging/service allowances. It is a planning model, not an agreed bill.",
"blocks":[
table(["Component","Monthly GBP","Basis"],[
["KVM 4 initial term","9.99","Published 24-month offer; £239.76 paid upfront."],
["Cloudflare domain","1.67","£20/year allowance; name/TLD checkout unknown."],
["R2 Standard, 100GB-month","1.08","$1.35 storage at assumed USD1 = GBP0.80; requests within allowances."],
["Independent backups","5.00","Unquoted storage/service allowance."],
["Transactional email","16.00","$20 tier example at assumed FX; provider unselected."],
["Marketing service","25.00","Unquoted; contacts/sends/automation unknown."],
["One staff mailbox","6.00","Unquoted one-seat allowance."],
["Monitoring","5.00","Unquoted tools allowance; labour excluded."],
["Base / reserve envelope","69.74 / 85.00","Monthly equivalents during initial term."],
["At VPS renewal","84.74 / 105.00","VPS becomes £24.99/month equivalent."]],[0.42,0.17,0.41]),
p("Initial technology cash = £239.76 VPS + £20 annual domain allowance + £58.08 other first-month services = £317.84 before applicable taxes. Do not add the VPS again as a monthly payment after counting its prepayment. Exact initial annual base is £836.84; reserve envelopes are not caps. [T01,T03-T04]"),
p("R2 Standard includes 10GB-month, 1m Class A and 10m Class B operations/month. Overage is $0.015/GB-month, $4.50/m Class A and $0.36/m Class B; internet egress is free. Apply shared account allowances and billing-unit rounding. Infrequent Access differs. [T02]"),
callout("What is additional","Payment/account fees, taxes, maintenance labour, campaign work/spend, optional SMS/WhatsApp/helpdesk, higher usage, extra staging/search services and later integrations. Combine overlapping provider plans before quoting.","amber")
],"refs":["T01","T02","T03","T04"]},
{
"id":"project-budget", "group":"Delivery and budget", "title":"Development and business budgets",
"intro":"Separate software delivery from recurring technology and the capital needed to run a stocked medical retailer.",
"blocks":[
table(["Illustrative Phase 1 item","GBP"],[
["200 developer hours x £30 (assumed rate/capacity)","6,000.00"],
["20% labour contingency","1,200.00"],
["AI/tools allowance, unquoted","150.00"],
["Initial technology cash from previous page","317.84"],
["Software/setup example total","7,667.84"]],[0.76,0.24]),
p("This is not a market-rate finding or fixed-price quotation. Replace the hourly rate, effort and AI allowance with the developer's accepted terms and pilot evidence. About 200 focused hours across 25 calendar days is an aggressive capacity assumption, not measured throughput. Price later work separately as accepted effort x rate plus agreed reserve and third-party costs."),
h("Retail funding that still needs quotations"),
items("Opening inventory, minimum orders, freight, customs/duty/import VAT timing and supplier payment terms.","Premises/storage, picking/packing/carriers, returns, equipment service, stock loss and expiry.","Legal/regulatory/pharmacy/tax advice, applicable registrations, professional staff and insurance.","Payment fees/reserves, support and operations staff, maintenance labour, marketing management and campaign spend."),
h("How to control spending"),
p("Track landed cost and contribution after fulfilment, payment, returns and advertising. Use planned cash-flow scenarios and a reserve before buying stock or extending customer credit. An illustrative £85 technology envelope is not the monthly cost of operating the retailer."),
callout("Budget decision required","Owners must approve the actual developer quote, stock/working-capital limit, operating budget and marketing test budget. No final all-in business total can be established from hosting prices alone.","amber")
],"refs":[]},
{
"id":"acceptance", "group":"Delivery and budget", "title":"Testing, operations and handover",
"intro":"Release evidence should demonstrate that the retailer can transact, handle failure and recover, rather than just showing finished screens.",
"blocks":[
table(["Acceptance area","Representative checks"],[
["Product eligibility","Unreviewed item, wrong destination, pending professional account, changed evidence and mixed restricted basket are handled correctly."],
["Stock","Two buyers compete for the last unit; reservation expires; lot is quarantined; returned stock cannot reappear without inspection."],
["Payments","Failed/duplicate/delayed events, abandoned redirects, partial refunds and reconciliation do not cause duplicate orders or dispatch."],
["Customer experience","Mobile/keyboard checkout, clear totals, order emails, accessible forms, returns and support escalation work."],
["Privacy/security","Staff roles, MFA, private document access, exports, consent withdrawal and safe logs are checked."],
["Continuity","Restore a backup to a separate environment, recover services, verify order consistency and document rollback/reconciliation."],
["Performance","Test realistic search/rendering/query and worker peaks; 10,000 daily traffic is not itself a capacity guarantee."]],[0.25,0.75]),
h("Handover deliverables"),
p("Provide source and account ownership records, deployment/configuration guide, schema/migrations, provider and secret handover, backup/restore instructions, order/refund/receipt SOPs and staff training. Agree support hours, defect warranty, maintenance scope, incident ownership, change control and exit/export arrangements."),
callout("Named operational ownership","The owners run procurement, stock, fulfilment, support and product permissions. The developer implements agreed controls and verification. Professional/legal/tax reviewers confirm their relevant routes; software does not confer a licence.")
],"refs":[]},
{
"id":"growth-europe", "group":"Growth and governance", "title":"Growth ideas and European expansion",
"intro":"Prioritise useful service and repeat procurement, and test commercial hypotheses before expanding spend or inventory.",
"blocks":[
table(["Idea","Why test it / first experiment"],[
["Reviewed starter range","Launch available, documented items with clear pack prices. Compare a matched basket and track margin after freight/payment."],
["Clinic starter bundles","Create genuinely compatible supplies for a named use case; validate contents, evidence and economics before promoting."],
["Fast quote response","Give professional customers a staffed quote/reorder route and measure conversion and response time."],
["Reorder convenience","Saved lists, stock continuity and appropriate reminders reduce purchasing effort without relying on broad discounts."],
["Supplier partnerships","Seek legitimate manufacturer/distributor referral and educational content arrangements; permission is not assumed."],
["Transparent trust","Original specifications, realistic dispatch promises, authentic reviews and accountable problem resolution."],
["Measured campaigns","Use small eligible pilots, cohort repeat contribution and holdouts where practical; do not promise fast success."]],[0.29,0.71]),
h("Europe is a series of releases"),
p("Select destinations using demand, supplier rights, language/support, contribution and fulfilment evidence. For each country review product/economic-operator roles, tax/customs, labels/instructions, local terms/returns, packaging/environmental duties, marketing/privacy and accessibility. UK permissions do not transfer automatically. [E01]"),
p("Compare GB stock exports with an eventual own-stock EU fulfilment route. Currency and translation alone do not make a country ready. NI remains a separate initial UK decision; EU/EEA/Switzerland and other destinations need their actual routes."),
callout("Activation rule","A category or country is activated only after its dossier and operating lane pass review. The full-range ambition is preserved while cash and compliance remain manageable.")
],"refs":["E01"]},
{
"id":"decisions", "group":"Growth and governance", "title":"Ownership, decisions and release authority",
"intro":"The main unresolved items need accountable owners and evidence so development does not depend on assumptions that only surface at launch.",
"blocks":[
table(["Owner","Before commitment or release"],[
["Business owners","Choose brand/legal operator, start date, stock/premises, launch assortment/destinations, suppliers/content rights, insurance and working capital."],
["Product/regulatory lead","Classify actual SKUs and activities, approve evidence/restrictions and oversee complaints/recall routes."],
["Pharmacy/medicines specialist","If medicines are selected, substantiate patient/wholesale/import routes, permissions and professional processes."],
["Tax/legal advisers","Confirm transaction tax, imports/reliefs, company disclosures and final consumer/business/privacy policies."],
["Developer","Agree API/reuse strategy, design/backlog, integrations, acceptance targets, delivery/maintenance quote and technical handover."],
["Operations/marketing","Staff fulfilment/support, select permitted messaging/campaigns, run consent/suppression and monitor contribution."],
["Release owner","Review acceptance evidence and product/provider/stock readiness, then approve or defer the controlled release."]],[0.28,0.72]),
h("Decisions to resolve early"),
items("Does initial UK delivery include Northern Ireland, and which exact SKUs may sell to each buyer group?","Which medicine activities, if any, will be operated and by whom? Prescription-only medicines remain undecided.","Which merchant accounts are approved, and what did the old Google notices actually require?","Which launch integrations are manual versus automated, and who performs each task?","What are the accepted development/operating budgets and actual staffing capacity?"),
callout("Status of this plan","Confirmed requirements, proposed implementation choices and illustrative cost inputs are distinguished throughout. Product permissions and external approvals require the actual operator's evidence. This is the complete planning document; only its Day 25 roadmap is condensed to one page.")
],"refs":[]}
]
