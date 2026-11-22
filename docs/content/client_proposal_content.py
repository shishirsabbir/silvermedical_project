"""Client proposal content. User assumptions and analyst estimates are explicitly labelled."""
from datetime import date, timedelta
from calendar import monthrange

ISSUED = "9 November 2026"
START = date(2026, 11, 15)
def month_plus(d, n=1):
    m = d.month - 1 + n
    y = d.year + m // 12
    return date(y, m % 12 + 1, min(d.day, monthrange(y, m % 12 + 1)[1]))
RELEASES = [START + timedelta(days=25)]
for _ in range(3): RELEASES.append(month_plus(RELEASES[-1]) + timedelta(days=10))
SIX_MONTH = month_plus(RELEASES[0], 6)
def fmt(d): return f"{d.day} {d.strftime('%B %Y')}"

def p(t): return {"kind":"p", "text":t}
def h(t): return {"kind":"h", "text":t}
def banner(t, b, tone="teal"): return {"kind":"banner", "title":t, "text":b, "tone":tone}
def cards(*entries): return {"kind":"cards", "entries":entries}
def table(headers, rows, widths=None): return {"kind":"table", "headers":headers, "rows":rows, "widths":widths}
def steps(*entries): return {"kind":"steps", "entries":entries}
def stats(*entries): return {"kind":"stats", "entries":entries}

PAGES = [
dict(id="vision", icon="spark", label="01 / THE OPPORTUNITY", title="A trusted supplier.\nA complete digital business.",
intro="A new medical-supplies brand serving UK consumers and professional buyers, with owned stock, a capable operations team and a platform built for European expansion.", blocks=[
cards(
 ("shop", "One retailer, one accountable service", "The business buys from approved UK/EU suppliers, holds its own stock and manages each customer order. Praxisdienst is the benchmark for breadth and convenience."),
 ("globe", "UK first. Europe by destination.", "Build the full-range catalogue structure now. Activate products and countries when evidence, supply arrangements, payment acceptance and operations are ready."),
 ("screen", "Three connected applications", "A fast Next.js storefront, a versatile React admin and a central API backed by PostgreSQL. Cloudflare handles the domain and R2 object storage."),
 ("rocket", "A first selling release in 25 days", "Deliver the complete discovery-to-refund journey for a reviewed launch assortment, then improve operations, repeat purchasing and expansion over three further phases.")
),
banner("The customer promise", "Correct products and pack sizes, clear prices, dependable availability, useful documentation and responsive after-sales support."),
table(["Inside this proposal", "Where to look"], [
 ["Selling model and UK/European requirements", "Pages 3-6"],
 ["Search visibility, Merchant Center and marketing", "Pages 7-8"],
 ["Technology, business operations and running costs", "Pages 9-11"],
 ["Four releases, launch features and AI-assisted effort", "Pages 12-15"],
 ["Six-month measurement and project responsibilities", "Pages 16-17"]], [.73,.27]),
p("This proposal summarises the detailed project plan. The new brand, legal operator, exact catalogue and supplier agreements remain to be confirmed. Product-specific clearance and external approvals are release dependencies.")], refs=[]),

dict(id="selling", icon="box", label="02 / THE SELLING MODEL", title="From approved supply\nto repeat purchasing.",
intro="Support both consumers and verified professional/business customers, with product-specific eligibility enforced throughout the purchase journey.", blocks=[
steps(
 ("shield", "01  Qualify", "Approve suppliers, resale/content rights, product evidence and destination. Record the business's actual distributor or importer responsibilities."),
 ("box", "02  Receive", "Purchase and receive owned stock; record quantities, landed costs, applicable lots/serials/expiry, storage conditions and quarantine."),
 ("search", "03  Present", "Publish original, reviewed descriptions, clear pack quantities, supported claims, accurate availability and complete prices."),
 ("card", "04  Sell", "Validate buyer and destination, calculate tax/delivery server-side, reserve stock and confirm an approved payment."),
 ("truck", "05  Fulfil and retain", "Pick, check, dispatch and track; manage returns, refunds, complaints and recalls. Make future ordering straightforward.")
),
cards(
 ("users", "For consumers", "Mobile-first discovery, accessible product pages, straightforward checkout, order updates, transparent returns and support."),
 ("clipboard", "For professional buyers", "Business verification at launch; later saved lists, repeat ordering, quotations, organisation roles and approved pricing arrangements.")
),
banner("Separate permissions for every SKU", "Legal sale, buyer entitlement, destination, public content, payment acceptance and advertising/feed eligibility are distinct decisions. A professional account or prescription upload does not authorise every purchase."),
p("The platform will not include a multi-vendor marketplace or dropshipping workflows. Full catalogue ambition remains; phased activation controls the release sequence, not the eventual product range.")], refs=[]),

dict(id="uk-rules", icon="shield", label="03 / UK PRODUCT REQUIREMENTS", title="Approve the product route\nbefore publishing the product.",
intro="A category name such as 'medical supplies' is not a legal classification. Review intended purpose, labels, evidence, seller activity and destination for each SKU.", blocks=[
table(["Product route", "What the business must establish"], [
 ["Medical devices", "GB: applicable UK MDR 2002 conformity route, valid marking/evidence, MHRA registration arrangements, relevant UK Responsible Person and importer/distributor duties. CE transitional eligibility is conditional. [R01-R02]"],
 ["IVDs and diagnostic tests", "Use the specific IVD route and intended-user restrictions; assess self-test versus professional use. GB and Northern Ireland requirements differ. [R01,R03]"],
 ["PPE", "Confirm intended protective use, conformity, declaration, labels/instructions and supply-chain duties under the applicable GB/NI route. Some products have more than one regulatory role. [R04]"],
 ["Biocides / disinfectants", "Check product/active-substance status, applicable authorisation or transitional route, claims and labelling. GB BPR and NI EU BPR differ. [R05]"],
 ["Human medicines", "Separate general-sale, pharmacy and prescription-only supply. Establish product authorisation, authorised supplier/premises/professional oversight and any wholesale/import licences for the activity. [R06,R07,R11]"],
 ["Veterinary / ordinary goods", "Veterinary medicines have their own categories and professional supply rules. Ordinary goods retain applicable product-safety, electrical and other duties. [R09,R12]"]], [.26,.74]),
banner("Prescription-only medicines: separate decision", "This activity is still undecided. Keep activation gated until an authorised operating route is evidenced. A prescription checkbox is insufficient; public advertising of prescription-only medicines is prohibited. [R08]", "gold"),
p("Northern Ireland is a separate market decision: EU MDR/IVDR apply to devices there, with role-specific requirements. Do not enable NI automatically because GB checkout is ready. Registration is not an MHRA endorsement. [R02-R03]"),
p("For every active SKU, retain evidence and responsible contacts, track applicable lots/expiry, control storage and quarantine, and operate complaint/recall procedures. These controls need real staff and processes as well as software.")], refs=["R01","R02","R03","R04","R05","R06","R07","R08","R09","R11","R12"]),

dict(id="europe", icon="globe", label="04 / EUROPEAN EXPANSION", title="Open countries with evidence.\nThen scale the operating lane.",
intro="Europe is a sequence of country launches. EU Member States, EEA countries outside the EU, Switzerland and other destinations do not share every rule.", blocks=[
cards(
 ("shield", "Product and operator readiness", "For EU devices/IVDs, verify the MDR/IVDR route, permitted transition, relevant economic operators, language/IFU requirements and role-specific registrations. UK permission alone is insufficient. [E01]"),
 ("receipt", "Tax and border readiness", "Map B2B/B2C, stock location, customs importer, VAT registrations and applicable OSS/IOSS. IOSS is conditional and limited to eligible imported B2C consignments up to EUR150. [E02]"),
 ("truck", "Service and returns readiness", "Price the actual landed delivery/returns route, warranty support and local-language service. Start from GB stock only when that lane is commercially and legally workable."),
 ("users", "Local customer requirements", "Review local consumer terms, marketing/privacy and accessibility, plus packaging, WEEE and battery obligations where applicable. Assess EAA applicability and exemptions. [E03-E05]")
),
banner("Do not assume low-value imports are duty-free", "The EU introduced a temporary EUR3 customs-duty mechanism for affected low-value imports from 1 July 2026. Have a customs adviser confirm scope, calculation and origin treatment for the actual lane. [E06]", "gold"),
h("The proposed country-release dossier"),
p("Approved products and supplier territories; named economic operators; tax/customs route; translated evidence and customer terms; pricing and payment acceptance; dispatch/returns tests; support owner; environmental obligations; and positive landed contribution."),
p("Phase 4 delivers expansion capability and a first-country readiness review. A live European country opens only when its dossier passes. Medicines, biocides and veterinary products require their separate local routes; device marking does not authorise them."),
p("An eventual EU warehouse can hold the retailer's own stock. This preserves the chosen business model; a supplier-to-customer dropshipping model is not included.")], refs=["E01","E02","E03","E04","E05","E06"]),

dict(id="trust", icon="lock", label="05 / CUSTOMER TRUST & PAYMENTS", title="Make every transaction clear,\nsecure and accountable.",
intro="Selling rules, privacy controls and merchant approvals must be part of the operating model from the first release.", blocks=[
table(["Area", "Launch requirement and implementation"], [
 ["Consumer information", "Identify the seller and contact route; show full consumer prices, tax and unavoidable charges; explain delivery, cancellation and complaints. Confirm orders in a durable form. [C01,C03]"],
 ["Returns and defects", "Online consumers generally have 14 days to notify cancellation, with a further return period. Apply exceptions accurately; health/hygiene exceptions are not a blanket ban on medical returns. Faulty-goods rights remain. [C02]"],
 ["VAT", "Standard UK VAT is 20%, but exact product/customer reliefs need evidence. For a UK-established business, monitor the GBP90,000 rolling-12-month or next-30-days-alone registration tests. Different establishment rules can apply. [C04-C06]"],
 ["Privacy", "Minimise data, record lawful purposes/retention, contract with processors and assess transfers. Identifiable health data requires Article 6 and Article 9 conditions; use private, restricted storage. [P03]"],
 ["Cookies and marketing", "Gate advertising tracking behind valid consent. Assess any analytics exception against current rules. Keep purpose/channel permission and suppression records; essential service notices stay separate. [P01,P04]"]], [.25,.75]),
cards(
 ("card", "Revolut + Apple Pay + Google Pay", "Implement approved merchant checkout and wallet support, verified webhooks, payment reconciliation and refunds. An integration is not proof of catalogue acceptance. [T08]"),
 ("shield", "PayPal", "Obtain category approval for the intended catalogue. PayPal's policy requires prior approval for medical devices and prescription items. Provider acceptance is separate from lawful sale. [T07]")
),
banner("Payment reliability", "Use provider-hosted payment components where possible; verify server events and process retries idempotently. Do not store raw card data. Agree applicable PCI responsibilities with the payment providers."),
p("Stripe is excluded. Payment processing, currency conversion, disputes/reserves and any business-account subscription are additional to the platform hosting budget.")], refs=["C01","C02","C03","C04","C05","C06","P01","P03","P04","T07","T08"]),

dict(id="search", icon="search", label="06 / SEARCH & MERCHANT CENTER", title="Earn visibility through\naccurate products and trust.",
intro="Organic search, Merchant Center listings and paid campaigns are separate routes. Each needs its own data quality, policy checks and measurement.", blocks=[
cards(
 ("search", "Organic Google and Bing", "Publish useful original pages with correct specifications, pack sizes, availability and supported claims. Use crawlable links, canonical URLs, XML sitemaps and clear category structure. [S01-S03]"),
 ("code", "Technical search foundation", "Server-render key pages, optimise prepared images, review mobile speed and accessibility, and keep Product/Offer data consistent. Connect Search Console and Bing Webmaster Tools; use IndexNow where appropriate. [S02-S03]"),
 ("shield", "Merchant Center approval", "Verify the business/domain, display policies/contact details and submit only eligible products. Keep price, stock, identifiers, shipping and returns aligned between feed and checkout. [M03-M04]"),
 ("chart", "Controlled campaigns", "Start small with approved, in-stock, profitable products. Separate brand/product-intent tests, review search terms and measure contribution after ad cost. Ads healthcare rules apply independently. [M02]")
),
banner("Medical products need channel-level controls", "UK prescription and behind-the-counter drug listings are not permitted in Merchant Center. UK OTC listings require the applicable pharmacy and Google certification. Review the whole site/account, not only the feed. [M01]", "gold"),
p("Inspect the actual historic Merchant Center notices and any related accounts before onboarding. Use accurate ownership and business information, resolve violations and follow the review/appeal process. A new brand is not a way around enforcement. [M01,M04]"),
p("Avoid copied competitor content, invented reviews, unsubstantiated medical claims, cloaking and mass low-value AI pages. Never build advertising audiences from sensitive health conditions. Eligibility, indexing, rankings and rich results cannot be guaranteed. [S01,M05]"),
p("Weekly routine: review disapprovals, structured-data issues, index coverage, broken pages and price/stock mismatches; correct causes and record decisions before resubmission.")], refs=["S01","S02","S03","M01","M02","M03","M04","M05"]),

dict(id="growth-plan", icon="mail", label="07 / MARKETING & SIX-MONTH EXECUTION", title="Acquire carefully.\nMake reordering easy.",
intro="The six-month objective is a reliable, measurable retail operation with improving repeat contribution. Sales and profitability depend on actual demand, margins, stock and execution.", blocks=[
table(["Trading period", "Priority and experiment"], [
 ["Month 1", "Validate fulfilment and demand. Interview initial buyers, fix checkout friction and compare a matched basket of approved products. Launch limited eligible campaigns only after approval."],
 ["Month 2", "Improve product pages and search intent coverage. Test genuine clinic starter bundles, clear pack pricing and a staffed professional quote service."],
 ["Month 3", "Introduce saved lists/reorders, permission-based replenishment reminders and useful buying guides reviewed for product claims."],
 ["Month 4", "Scale only categories with proven contribution and dependable supply. Negotiate supplier terms and improve stock availability before expanding ads."],
 ["Month 5", "Refine cohort retention and organisation purchasing. Test manufacturer partnerships and strengthen after-sales/warranty support."],
 ["Month 6", "Review acquisition payback, repeat contribution, stock ageing and cash. Expand winners; pause weak channels and assess the first European lane."]], [.21,.79]),
cards(
 ("mail", "Email and CRM", "Launch service emails, consent/preferences and suppression. Add reviewed welcome, replenishment and win-back journeys later. Individuals need valid consent or a qualifying soft opt-in; corporate rules differ. [P01-P02]"),
 ("phone", "WhatsApp and SMS", "Do not promise WhatsApp medical-product campaigns: its current policy restricts these products, and the limited OTC exception does not include the UK. Assess exact use cases separately; SMS needs permission and budget. [M06]")
),
p("A valid products/services soft opt-in needs direct collection during a sale/negotiation, the sender's own similar offerings and opt-outs at collection and in each message. Do not treat an abandoned basket or an old customer list as automatic marketing permission. [P01]"),
banner("A dated review, not a revenue promise", f"Assuming first sales on {fmt(RELEASES[0])}, the six-month trading review is {fmt(SIX_MONTH)}. Review performance weekly and reallocate effort monthly. Campaign spend and operation are separate business budgets.")], refs=["P01","P02","M06"]),

dict(id="stack", icon="code", label="08 / THE TECHNOLOGY STACK", title="One dependable core.\nClear room to grow.",
intro="Keep launch operations simple: one modular backend, one transactional database and a dedicated worker, with clear boundaries between customers, staff and integrations.", blocks=[
{"kind":"architecture"},
table(["Layer", "Proposed implementation"], [
 ["Storefront - confirmed", "Next.js + React on Hostinger. Responsive shopping, server-rendered public pages, account and checkout experiences."],
 ["Admin - confirmed direction", "Regular React. Recommend Vite + TypeScript, reusable accessible components, server-side filters/pagination and role-based work queues."],
 ["API - recommendation", "NestJS with Fastify adapter, REST/OpenAPI contracts and modular business services. Plain Fastify remains an alternative. [T10]"],
 ["Database / jobs", "PostgreSQL with constraints, transactions and migrations; ORM choice to confirm. Durable background jobs for imports, media, feed generation and notifications."],
 ["Media / integrations", "Upload-time image optimisation, prepared variants in R2; separate private evidence storage. Revolut, wallets, PayPal and a managed email provider."]], [.29,.71]),
p("Use a reverse proxy, HTTPS, private PostgreSQL, staff MFA, secret management, rate limits, validated uploads and audited actions. Cache only safe public content; never share cached customer baskets, personal prices or restricted records. [T09]"),
banner("Design for correctness before scale", "The API is authoritative for prices, eligibility, stock and order/payment states. Prove concurrent last-unit orders, duplicate events, quarantine, partial refunds and recovery before release.")], refs=["T09","T10"]),

dict(id="operations", icon="clipboard", label="09 / RUNNING THE BUSINESS", title="An admin that organises work,\nnot just data.",
intro="Give staff clear queues, useful filters, safe bulk actions and the reason behind every hold. Keep commercial, stock and customer records connected.", blocks=[
cards(
 ("box", "Catalogue and purchasing", "Draft imports, supplier records, product evidence, approval states and media. Later add purchase orders, replenishment suggestions and landed-cost reporting."),
 ("truck", "Stock and fulfilment", "Receipts, reservations, applicable lot/serial/expiry tracking, quarantine, picking, dispatch and returns. Use one authoritative inventory ledger."),
 ("users", "Customers and support", "Consumer/business accounts, professional review queue, orders, cases and preferences. Add organisation roles, quotes and repeat lists in later phases."),
 ("chart", "Finance and management", "Tax-configured invoices/credit notes, refunds and reconciliation exports at launch. Later reporting connects margin, stock ageing, channel cost and retention.")
),
table(["Cadence", "Accountable routine"], [
 ["Daily / operations", "Review held orders, failed payments, stock exceptions, dispatch commitments, support and supplier delays. Watch backup/job alerts."],
 ["Weekly / commercial", "Reconcile payments and inventory, inspect feed/search issues, analyse contribution and campaign results, and review low stock/expiry."],
 ["Monthly / management", "Review cash runway, aged stock, supplier performance, access rights, patches, restore evidence and product/channel policy changes."]], [.26,.74]),
banner("A real operating team is required", "Owners appoint purchasing, product/compliance review, fulfilment, finance, support and marketing owners. The developer builds and maintains the agreed system; business permissions and daily retail work remain with the operator."),
p("At launch, carrier booking, tracking entry and accounting exports can be manual but must be staffed and tested. Automated courier/finance connectors are later deliverables after the exact providers and contracts are chosen.")], refs=[]),

dict(id="budget", icon="receipt", label="10 / HOSTING & RUNNING COSTS", title="A lean platform budget\nunder US$100 per month.",
intro="A conditional target for infrastructure and selected tools, with the frontend, admin, API, worker and PostgreSQL on Hostinger KVM 4. Maintenance labour is separate.", blocks=[
{"kind":"budget"},
p("Model assumptions: GBP1 = USD1.25 (planning FX, not a live rate); 100GB-month R2 Standard; request counts within free allocations; one mailbox; limited marketing pilot. Backup, mailbox and marketing amounts are unquoted spending allowances. [T01-T04]"),
banner("Allow for tax and headroom", "Adding an illustrative 20% tax sensitivity to the service subtotal, then a $10 reserve, gives $71.10 initially and $93.60 at VPS renewal. Actual tax treatment varies. This is a target, not a guaranteed cap."),
p("KVM 4 is advertised at GBP239.76 paid upfront for 24 months (GBP9.99/month equivalent), renewing at GBP24.99/month equivalent. Initial model cash is $361.05 before tax/reserve: $299.70 VPS + $25 annual domain allowance + $36.35 first-month services. Do not count the VPS twice. [T01,T03]"),
p("R2 storage examples after the shared 10GB free allowance: 100GB = $1.35; 500GB = $7.35; 1,000GB = $14.85/month. Standard includes 1m Class A and 10m Class B operations; overages are $4.50/m and $0.36/m with billing-unit rounding. Egress is free. Prepared images avoid a separate transformation service. [T02]"),
p("Keep costs controlled with public asset caching, upload limits, bounded jobs, measured email volumes and spend alerts. KVM capacity for 10,000 daily visitors is unproven; test peaks and upgrade if required. More countries, usage or paid automation may exceed the target."),
p("Excluded: developer maintenance/support, AI development tools, merchant/account fees, paid campaigns, stock, warehouse, staff, shipping, licences/advice, insurance and new integrations. Monthly/annual equivalents are not the same as invoice timing.")], refs=["T01","T02","T03","T04"]),

dict(id="roadmap", icon="calendar", label="11 / FOUR-PHASE DELIVERY", title="Four releases.\nOne continuous improvement plan.",
intro=f"Illustrative kickoff: {fmt(START)}. Phase 1 releases 25 elapsed calendar days later; each following release adds one calendar month and 10 days to the previous milestone.", blocks=[
{"kind":"roadmap"},
table(["Release", "Outcome and exit evidence"], [
 ["1 / Launch commerce", "Approved customers can find, buy and receive approved stock. Staff can fulfil, refund, reconcile and recover the service."],
 ["2 / Operational control", "Purchasing and support queues, stock/replenishment reporting and one selected courier/accounting workflow reduce repetitive work."],
 ["3 / Repeat growth", "Organisation buying tools, saved lists, reviewed lifecycle automation and contribution reporting support repeat purchasing."],
 ["4 / Expansion readiness", "Country-aware catalogue/tax/content configuration, first-country dossier, performance hardening and a complete handover."]], [.29,.71]),
banner("The calendar is explicit", "Kickoff is Day 0; the launch milestone is 25 full days later. Phases 2-4 use calendar months, not a fixed 40-day duration. These are target release dates, with no automatic weekend or holiday adjustment."),
p("The first release falls in December; confirm holiday staffing and supplier/provider availability early. Owners provide product data, lawful stock, merchant access and daily decisions alongside development. Replan if dependencies or measured capacity do not support the dates."),
p("Use weekly demonstrations, a versioned backlog, acceptance criteria and owner sign-off. Review scope and capacity before adding integrations or regulated activities.")], refs=[]),

dict(id="day25", icon="rocket", label="12 / THE DAY-25 SELLING RELEASE", title="Ready to take the first order.\nReady to fulfil it properly.",
intro=f"Target release: {fmt(RELEASES[0])}. A complete launch purchase journey for a bounded, approved assortment; full catalogue and country activation continue in later releases.", blocks=[
table(["Window", "Build and demonstrate"], [
 ["15-18 Nov", "Kickoff, backlog/data freeze, sample SKU evidence, architecture slice, operator/tax/shipping rules and provider access. Owners begin/complete external approvals in parallel."],
 ["19-25 Nov", "Database/API; React admin roles/MFA; product/variant/pack records, review status and draft CSV import; upload optimisation/R2; stock receipt, reservations, relevant traceability and quarantine."],
 ["26 Nov-2 Dec", "Next.js categories/search/product pages, basket and checkout; consumer/business accounts and professional checks; Revolut/wallets and PayPal integration subject to approval."],
 ["3-9 Dec", "Verified payment events/refunds, orders, tax/delivery, invoices/credit notes, manual dispatch/tracking, service email, policies/preferences, eligible feeds, search metadata and production checks."],
 ["10 Dec", "Controlled selling release, monitored live order/refund checks, staffed fulfilment/support and a prioritised defect/feedback queue."]], [.22,.78]),
cards(
 ("check", "Launch acceptance", "Test mobile/keyboard checkout, restricted-product access, last-unit contention, duplicate/failed payment events, dispatch/refund, backup restoration and realistic load."),
 ("clipboard", "What is deliberately manual", "Professional review, courier booking and accounting export. No bespoke ERP/WMS, trade credit, native app or multi-country rollout is promised in this first release.")
),
banner("Business readiness is part of the release", "Go live only with approved stock/content, lawful supply arrangements, accepted payment providers and a trained operating team. A late dependency changes the lawful launch assortment or the date; software completion cannot replace it.", "gold"),
p("The 25-day plan is aggressive. Validate the first end-to-end slice during kickoff and adjust scope against measured delivery capacity. No prescription-medicine activation is assumed.")], refs=[]),

dict(id="later", icon="layers", label="13 / WHAT FOLLOWS THE LAUNCH", title="Remove friction.\nBuild repeat demand. Expand.",
intro="The following are proposed release packages. Exact integration providers and measurable acceptance targets are agreed before each phase begins.", blocks=[
steps(
 ("clipboard", f"PHASE 2  /  {fmt(RELEASES[1])}", "Purchase orders and receipt discrepancies; low-stock/expiry dashboards; reorder suggestions; safer bulk catalogue workflows; supplier/evidence review reminders; order-linked support cases; one agreed courier connector and one accounting export/connector. Demonstrate stock and payment reconciliation end to end."),
 ("users", f"PHASE 3  /  {fmt(RELEASES[2])}", "Saved buying lists, fast reorder and professional quotations; organisation users/permissions; approved customer pricing; reviewed email journeys and suppression checks; content/campaign workflows; funnel, margin and cohort dashboards. Demonstrate a repeat order and auditable campaign eligibility."),
 ("globe", f"PHASE 4  /  {fmt(RELEASES[3])}", "Country-specific catalogue, price/tax/shipping and language configuration; first European market dossier and test order/return lane; performance/security hardening; recovery rehearsal; training and handover. Activate a country only when the separate business/legal gates pass.")
),
cards(
 ("lock", "Outside these baseline packages", "Marketplace, dropshipping, Stripe, native mobile apps, custom ERP replacement, clinical prescribing and automatic UK-wide/Europe-wide permission. Trade credit and loyalty/subscription schemes need separate scope."),
 ("shield", "Conditional future capabilities", "Medicines, special-storage logistics, advanced warehouse automation, additional connectors and additional countries remain possible, subject to the operator's decisions, evidence and resourcing.")
),
banner("Full-range ambition stays intact", "Delivery phasing prioritises a dependable first selling journey. It does not permanently remove a product category, and it does not imply that every future category is authorised or included in a fixed release package.")], refs=[]),

dict(id="effort", icon="spark", label="14 / HUMAN HOURS & AI CAPACITY", title="Seven supporting AI roles.\nOne accountable delivery lead.",
intro="Plan AI as assistance for a human-led build. The estimates below are analyst planning ranges, not measured throughput, a token entitlement or a guarantee of the release dates.", blocks=[
table(["Phase", "Human hours", "AI tokens (millions)", "Working model"], [
 ["1 / First selling release", "160-200", "25-65", "180 h / 40m"],
 ["2 / Operational control", "180-230", "15-30", "200 h / 25m"],
 ["3 / Repeat growth", "180-230", "15-30", "200 h / 25m"],
 ["4 / Expansion readiness", "160-220", "15-25", "180 h / 20m"],
 ["TOTAL", "680-880", "70-150", "760 h / 110m"]], [.32,.18,.27,.23]),
{"kind":"roles"},
p("Tokens mean cumulative input plus output across all calls, agents and retries, including repeated context. Cached input is a subset of input; do not add it twice. The 110m working model assumes 95m input + 15m output. It is not a single context window or 110m newly written words."),
p("Human hours cover design, implementation, supervision, integration, review, testing, deployment and handover. They exclude the retailer's operational staffing, supplier content production at unknown scale, legal/licensing work and campaign management. Phase 1 averages 6.4-8 hours across all 25 calendar days; it requires an agreed work pattern."),
p("Role 2 uses authorised supplier feeds/files or permitted collection only. Do not copy competitor content without rights, bypass access controls or place patient/customer secrets in prompts. AI-generated medical claims and regulatory classifications require accountable review."),
banner("Calibrate before extrapolating", "Measure hours, input/output/cache tokens and rework on the first product-to-payment slice. Re-estimate after Days 3 and 10. Seven roles need not run simultaneously; shared context, duplicated effort and review can increase token use. No development fee is included.")], refs=[]),

dict(id="analytics", icon="chart", label="15 / A MEASURABLE PATH TO SUCCESS", title="Measure profitable demand.\nProtect service and cash.",
intro="Use the first six months to establish demand, fulfilment quality and repeat contribution. The numbers below are illustrations for planning, not market benchmarks or a sales forecast.", blocks=[
table(["Monthly scenario", "Cautious", "Working", "Stronger"], [
 ["Sessions (assumed)", "5,000", "15,000", "30,000"],
 ["Order conversion", "1.0%", "1.5%", "2.0%"],
 ["Orders", "50", "225", "600"],
 ["Net product sales at GBP80/order", "GBP4,000", "GBP18,000", "GBP48,000"],
 ["Contribution before ads/fixed costs", "GBP850", "GBP3,825", "GBP10,200"]], [.49,.17,.17,.17]),
p("Calculation: GBP80 net sales x 30% gross margin = GBP24, less GBP7 variable fulfilment/payment/returns cost = GBP17/order before ads and fixed costs. All inputs are assumptions, using one consistent ex-VAT basis. Supplier and carrier quotes must replace them."),
banner("The spending rule", "On this example, GBP17 acquisition cost is only a first-order contribution break-even ceiling; target below it to fund overhead and profit. Equivalent first-order revenue/ad-spend break-even is about 4.71x. Validate repeat margin before accepting a longer payback."),
table(["Measure", "Proposed action / internal target"], [
 ["Demand and conversion", "Track sessions, product-to-basket and checkout completion by device/channel; investigate friction before buying more traffic."],
 ["Service quality", "Propose >=98% stock-record accuracy and >=95% dispatch within the promised window; review failures weekly. These are chosen goals, not industry benchmarks."],
 ["Retention and contribution", "Compare 30/60/90-day customer cohorts, repeat orders and net contribution after refunds/ads; do not scale on revenue alone."],
 ["Cash and stock", "Monitor cash runway, stock cover, aged/expiring stock and supplier commitments before increasing purchasing or credit."]], [.30,.70]),
p("The earlier 10,000-daily-traffic figure is a capacity-planning scenario, not acquired demand. This proposal contains no keyword-volume study, validated market-size estimate or signed supplier-margin evidence. Choose an owner-approved monthly ad test budget and scale only after the data supports it.")], refs=[]),

dict(id="partner", icon="users", label="16 / DELIVERY PARTNERSHIP", title="Built with care.\nHanded over with clarity.",
intro="Prepared by Shishir Sabbir for a new UK medical-supplies venture. The business identity and final launch assortment will be confirmed during kickoff.", blocks=[
{"kind":"profile"},
cards(
 ("code", "Developer responsibilities", "Agreed application build, integration, tests, deployment documentation, source handover and staff training. Human review remains accountable across the AI-assisted workflow."),
 ("clipboard", "Business responsibilities", "Legal operator, supplier/content rights, product review, licences where required, stock/premises, tax decisions, provider approvals, customer policies and daily operations.")
),
h("A clear way of working"),
p("Weekly demonstrations, a prioritised backlog, one business decision owner and release acceptance records. Handover includes source/configuration guidance, schema/migrations, account ownership, backup/restore and order/refund/stock procedures. Keep secrets outside general documentation."),
p("Agree maintenance ownership, support hours, incident response, defect handling and change control before launch. The sub-$100 platform model excludes maintenance labour; this proposal does not establish a paid support plan or a response-time SLA."),
banner("Kickoff decisions", "Confirm brand/operator, launch geography and SKUs, evidence reviewers, merchant readiness, warehouse workflow, API choice, integration providers, delivery capacity and acceptance criteria. The assumed kickoff is 15 November 2026; it is not a booked start."),
p("No development fee is stated. Deliverables and dates depend on the agreed backlog and readiness evidence; the detailed project plan remains the supporting reference.")], refs=[]),
]
