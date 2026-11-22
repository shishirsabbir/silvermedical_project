"""Editable client delivery plan. Planning only; no application is implemented."""
from datetime import date, timedelta

DATE = '9 November 2026'
TITLE = '25-day development & launch plan'
KICKOFF = date(2026,11,15)  # Existing illustrative Day 0 convention.

def p(text): return dict(kind='p',text=text)
def h(text): return dict(kind='h',text=text)
def table(headers,rows,widths=None): return dict(kind='table',headers=headers,rows=rows,widths=widths)
def note(title,text): return dict(kind='callout',title=title,text=text)
def s(id,title,group,intro,blocks,refs=()): return dict(id=id,title=title,group=group,intro=intro,blocks=blocks,refs=list(refs))

FEATURES = [
('F01','Brand and responsive website','Selected brand applied to home, navigation, category, product, basket and checkout; desktop/mobile and essential error/loading states.','1-8','Owner approves the chosen design and can shop on a phone.'),
('F02','Catalogue and discovery','Categories, keyword/SKU search, essential filters, pagination and clear in-stock/out-of-stock display.','6-8','A buyer finds a known item by SKU and category.'),
('F03','Accurate product pages','Images, manufacturer reference, variant/pack size, approved description, applicable documents, price/tax and delivery information.','4-8','Page matches the physical item and approved product record.'),
('F04','Guest and customer accounts','Guest buying, verified-email registration, sign-in/reset, saved addresses and own order history.','3-12','Customers can buy and view only their own orders.'),
('F05','Professional purchase controls','Application and human verification, reviewer notes, approved entitlement and server-side restricted-item checks.','3-8','A pending or ineligible buyer cannot pay for a restricted item.'),
('F06','Basket and checkout','Quantity changes, authoritative prices/stock, tax/delivery totals, address validation, final review and clear payment confirmation.','9-11','Altered browser prices and unavailable quantities are rejected.'),
('F07','Revolut and wallets','Revolut checkout with Apple Pay/Google Pay where approved and supported; verified payment events and failure/retry handling.','5-10','Supported device/browser completes a verified test payment; failures do not dispatch.'),
('F08','PayPal','PayPal checkout, verified capture/refund events and order reconciliation.','11-14','Duplicate or late events cannot cause duplicate dispatch/refund.'),
('F09','Customer information and email','Seller/contact pages, delivery/returns/privacy/terms, order confirmation, dispatch and refund messages.','13-17','Customer receives correct totals, terms and useful order updates.'),
('F10','Search and consent foundation','Metadata/canonicals, sitemap, product data, mobile accessibility, consent/preferences and approved-product feed export.','16-20','Audits pass; rejected tracking stays off; ineligible items stay out of feeds.'),
('F11','Secure staff workspace','Invite-only staff, MFA, role checks, audit history and a focused order/review/stock dashboard.','3-5','Customer credentials cannot enter admin or change staff permissions.'),
('F12','Product management and imports','Create/edit/archive products, categories, prices, variants and evidence; CSV draft import with errors/duplicates and preview.','4-15','250 planned records can be reviewed; an additional product needs no code change.'),
('F13','Images and documents','Upload-time validation/optimisation, prepared responsive images in R2 and separately protected private evidence.','4-7','Approved media loads quickly; private evidence has no public URL.'),
('F14','Stock and traceability','Receipt/opening counts, adjustments, reservations, applicable lot/serial/expiry, quarantine and a movement audit trail.','4-14','Last-unit contention cannot oversell; held/expired stock cannot be bought.'),
('F15','Orders and dispatch','Paid/held/failed queues, pick/pack record, manual carrier booking/tracking entry and partial fulfilment where needed.','12-14','Staff can trace order lines to the stock dispatched.'),
('F16','Returns and refunds','Return request logging, authorised full/partial refunds, returned-stock quarantine and recall/hold records.','11-14','Refund amount never exceeds captured funds less previous refunds.'),
('F17','Financial records and exports','Order/invoice/credit-note records, tax snapshots, basic sales/stock exports and payment reconciliation exceptions.','13-17','Finance can reconcile an order, refund and provider settlement reference.'),
('F18','Product/channel approval','Draft/review/approved/held states; distinct territory, buyer, payment and feed eligibility.','4-18','A suspended item cannot remain purchasable through an old URL or basket.'),
('F19','Hosting and recovery','Hostinger apps/API/PostgreSQL; Cloudflare domain/R2; TLS, private database, secrets, logs, alerts, backups and tested restore.','2-23','A clean environment can restore an order and stock history from backup.'),
('F20','Training and launch controls','Owner walkthrough, staff SOPs, defect log, deployment/rollback procedure and release evidence.','19-25','Business team completes receive -> publish -> buy -> ship -> refund.'),
]

# Each day has an engineering deliverable, an owner action and concrete evidence.
DAYS = [
(1,'Co-design the brand and buying journey','Run the AI-assisted workshop: compare three creative directions, choose a website layout and prioritise launch functionality. Record the design decisions and asset brief.','Owners join the workshop, explain their buyers and choose one direction; nominate one decision-maker.','Chosen concept, draft home/product screens and agreed must-have feature list.'),
(2,'Refine the design and establish the project','Turn the chosen direction into reusable UI tokens/components. Set up repository, staging, schema outline, CI and secrets approach; start provider integration checks.','Provide legal/operator details, domain shortlist, merchant access through safe channels, shipping and tax inputs. Begin provider onboarding if needed.','Clickable design direction, staging shell and a dated dependency register.'),
(3,'Secure identities and approve the brand pack','Implement customer verification/reset, invite-only staff and MFA. Validate the proposed auth/database adapters. Finalise initial logo, banners and shipping-packaging concepts.','Approve the brand/UI baseline; supply ten representative products with quantities, evidence and permitted images.','Customer/staff separation works; ten product dossiers and approved design files exist.'),
(4,'Build the first catalogue and stock records','Implement product/variant forms, draft import, evidence controls, image processing and opening stock/receipt records using the ten pilot items.','Warehouse checks the ten physical items, pack sizes, lots/expiry where relevant and usable stock.','Pilot products move from draft to reviewed staging pages with accurate stock.'),
(5,'Prove a complete first transaction','Connect one approved sample item to basket, server quote, a sandbox payment and verified event, dispatch/refund logic and backup proof. Review actual delivery throughput.','Join the demonstration; close product, provider and policy questions or record blockers with an owner/date.','First end-to-end slice passes; scope and schedule are revalidated before wider build.'),
(6,'Build the shopping shell','Implement responsive home, category navigation, header/search, account/basket links and approved banner placement. Connect reusable listing cards to real catalogue data.','Confirm navigation language, category names, support contacts and truthful service promises.','Desktop/mobile storefront works with real pilot data.'),
(7,'Deliver search and catalogue browsing','Implement search, essential filters, pagination and availability. Complete image delivery/cache behaviour; import batch 1, including the ten pilot records.','Prepare and review the first 50 records; correct image/content or stock mismatches.','50 records processed; a buyer can find approved products by name and SKU.'),
(8,'Complete product pages and professional checks','Deliver variants/pack sizes, product documents and eligibility messages. Add professional application/review and enforce the same rules in the API.','Name the professional reviewer and approve product/buyer rules; inspect mobile product pages.','Wrong buyer/territory is blocked; approved buyer follows a clear purchase route.'),
(9,'Complete basket, quotes and delivery totals','Build editable basket, guest checkout, address capture, server-calculated tax/delivery totals and stock reservations. Import batch 2.','Approve shipping zones/rates, tax treatment and next 50 product records.','100 records processed; quoted total matches a hand-checked order.'),
(10,'Complete Revolut and supported wallets','Integrate the approved Revolut flow, wallet domain/device setup, success/cancel/retry screens and event verification. Review provider approval readiness.','Resolve merchant verification/category requests and confirm provider acceptance evidence.','Payment status comes from verified provider state; no browser-only paid flag.'),
(11,'Add PayPal and payment reliability','Integrate PayPal, durable webhook handling and reconciliation; test retries, duplicate/late capture and refund primitives. Import batch 3.','Review the next 50 records and confirm refund/settlement responsibility.','150 records processed; duplicate events create no extra fulfilment or refund.'),
(12,'Give warehouse staff an order workflow','Build admin order queues, holds, pick/pack records, manual shipping/tracking entry and stock allocation controls.','Run a warehouse walkthrough; provide the actual carrier booking and return-address process.','A test paid order can be picked, dispatched and traced to its stock record.'),
(13,'Deliver documents and service email','Add confirmations, dispatch/refund email, invoice/credit-note records and safe mail retry/suppression handling. Import batch 4.','Approve email text, seller details, invoice/tax format and next 50 records.','200 records processed; documents and mail match the order and refund totals.'),
(14,'Finish the after-sales loop','Complete partial shipment/refund cases, return logging, quarantined returns and lot-based hold/recall records. Test stock/payment state transitions.','Finance and support operate example returns and agree escalation ownership.','Receive -> sale -> dispatch -> return/refund works without losing stock or money history.'),
(15,'Complete the initial catalogue intake','Import batch 5; add reports/exports and resolve data validation errors. Review remaining scope against working capacity.','Submit the final 50 records and finish missing evidence/rights/pricing decisions.','250 reported records have an explicit status; unresolved records remain held.'),
(16,'Apply policies and search foundations','Implement approved seller/policy pages, metadata, canonical URLs, sitemap and product structured data; finish financial/support exports.','Approve final public content, consumer information and actual fulfilment promises.','Public pages describe the business accurately; indexing includes only approved pages.'),
(17,'Finish consent, feeds and measurement','Wire consent/preferences, service-versus-marketing separation, basic funnel events and an eligibility-filtered Merchant feed. Prepare account setup/review checklist.','Review channel permissions and old Google notices; approve the eligible feed list and tracking choices.','No forbidden feed items or non-essential tracking before required consent.'),
(18,'Audit all 250 records and the next-product flow','Check counts, pack units, images, prices, stock and rule gates. Fix import errors; add one extra test product in staging to prove catalogue expansion.','Reviewer signs each sellable record or records a hold reason; warehouse resolves count differences.','250 = approved + held + excluded/duplicate; no unreviewed launch record.'),
(19,'Test the complete customer and staff journeys','Run meaningful browser/integration tests: guest/customer/professional, staff MFA, ID access, checkout, failed payment, last-unit race, dispatch and refunds.','Owners test representative consumer and professional orders; staff record usability issues.','Critical paths have evidence; defects are ranked by launch impact.'),
(20,'Verify performance, security and recovery','Audit mobile/desktop SEO/performance/accessibility, consent network behaviour, realistic load, dependencies and backup restoration.','Confirm operational response contacts and review evidence against the agreed release targets.','Measured audit/load/restore reports; no unresolved critical security or transaction failure.'),
(21,'Run business acceptance and training','Demonstrate everyday admin, product intake, stock adjustment, eligibility decisions, reconciliation, returns and incident recovery.','Warehouse, support, finance and product reviewer each complete their task unaided.','Signed UAT checklist and staff SOPs; handover gaps are assigned.'),
(22,'Fix release blockers and regress','Use the protected correction window for UAT/security/transaction/data defects. Repeat affected tests and critical purchase/refund regression.','Respond to remaining decisions promptly; approve corrected content and operational procedures.','Critical/high-impact launch blockers are closed with evidence.'),
(23,'Rehearse the production release','Rehearse migration, TLS/routing, mail/provider credentials, real backup restoration and rollback. Verify authorised live payment/refund smoke tests when accounts are ready.','Confirm payment accounts, catalogue acceptance, fulfilment readiness and owner-controlled service accounts.','Production checklist and rollback/restore proof; no sandbox credentials in production.'),
(24,'Freeze launch data and decide go/no-go','Reconcile final stock changes, finalise approved catalogue/feed, repeat key checks and assemble the release record. Freeze non-essential changes.','Owner signs the sellable assortment and operating readiness; warehouse supplies final counts.','Named release approval, supported payment methods, shipping rules and monitoring coverage.'),
(25,'Launch and supervise the first orders','Carry out the approved release, verify public routes, payment/stock/email flows and monitor errors, orders and jobs. Keep rollback and support ready.','Operate the first orders, confirm packing/dispatch and reconcile payments; record feedback.','Controlled first-selling release for the approved stocked assortment; next-product intake is usable.'),
]

SECTIONS = [
s('overview','From warehouse stock to online sales','01 / The launch commitment',
'A collaborative 25-day build focused on a complete first-selling operation, beginning with the reported 250 products already in the warehouse.',[
table(['Period','Outcome'],[
['Day 1','Choose the brand, website direction and launch priorities together using AI-assisted concepts.'],
['Days 2-5','Refine the design, secure the platform and prove one complete transaction.'],
['Days 6-15','Complete the shopping/admin workflows and process five batches of 50 product records.'],
['Days 16-20','Review the whole catalogue, apply search/consent rules and test the complete system.'],
['Days 21-25','Train the team, correct defects, rehearse recovery and launch the approved assortment.']],[.23,.77]),
h('What success means on Day 25'),
p('A customer can find an eligible in-stock item, understand the pack/price/delivery terms, pay through an approved method and receive confirmation. Staff can pick, dispatch, support, refund and reconcile the order. The same admin can receive, review and publish additional products after launch.'),
note('250 is the intake target','The user reports 250 products in the warehouse. This plan assumes roughly 250 distinct product/SKU records, not 250 units. The actual list, variants, quantities and lawful sale status are not yet verified. All 250 enter review; only eligible, approved stock becomes purchasable.'),
p('Calendar convention: retain the earlier illustrative 15 November 2026 preparation/kickoff as Day 0. Day 1 of development, including the branding workshop, is 16 November; Day 25 is 10 December. These are calendar days and planning dates, not booked working arrangements. A different confirmed kickoff requires the dates to be recalculated.'),
p('Reading guide: workshop and assets; launch features and boundaries; product intake and teamwork; the daily plan; release and expansion; official references. This page is the brief launch overview; the following pages explain how to deliver it.')]),
s('workshop','Day 1: design the business together','02 / Collaborative branding workshop',
'Shishir facilitates a working session in which the owners shape their own brand, website and functionality by comparing options and recording shared decisions.',[
table(['Session','Team activity and output'],[
['Discover / 45 min','Clarify buyers, product range, values, competitors, tone, warehouse realities and what must work at launch. Create a one-page brand brief.'],
['Explore / 75 min','Use AI image/design tools to produce three visual directions: logo concepts, colour/type palette, home-page mood and a shipping-box mockup. Compare them side by side.'],
['Choose / 45 min','Score clarity, trust, accessibility, distinctiveness and practical use. Owners choose one direction and record requested changes in the shared decision board.'],
['Shape the website / 75 min','Co-design desktop/mobile home, category and product layouts, then walk through basket/checkout and a simple admin order screen.'],
['Choose functionality / 60 min','Review the F01-F20 launch list. Mark launch-essential, useful-next and later ideas. Trade optional scope against the available days; preserve safe selling and payment controls.'],
['Confirm / 30 min','Capture the chosen concept, draft assets, screen map, owners, feedback deadlines and unresolved name/legal/provider questions.']],[.25,.75]),
p('Suggested workshop duration: 5.5 hours plus breaks. The Day 1 output is a selected creative direction and prototype, with refined assets/design approval targeted by Day 3. It is not a promise to finish every graphic or production screen in one session.'),
note('Participation and decision-making','Use a shared board with Concept A/B/C, comments, side-by-side previews and a dated decision log. One nominated owner consolidates feedback. Proposed limit: one selection round and two focused refinement rounds by Day 3; new ideas remain visible in the next-phase backlog.'),
p('A name/domain shortlist is provisional until checks are complete. The UK trade-mark search is an initial check, not proof of full clearance or EU protection. Review font, icon, image and AI-tool usage rights before the selected assets are used publicly. [B01]')],['B01']),
s('assets','The launch branding and asset pack','02 / Design deliverables',
'A bounded creative package gives the owners meaningful choices while protecting time for the commerce workflows.',[
table(['Asset','Proposed launch package / completion'],[
['Logo and brand guide','Three initial directions; one chosen logo system with primary/compact/monochrome versions, favicon, palette, type choices and a short usage sheet. Refine Days 2-3.'],
['Website screens','Desktop/mobile home, category, product and checkout prototypes plus a practical admin order view. Final core layouts by Day 3; reusable components continue through Day 8.'],
['Banners and tiles','Three approved campaign/category banner designs with desktop/mobile exports, four category tiles, two reusable social templates and one service-email header. Final wording must be factual.'],
['Shipping packaging','One outer shipping-box concept, one thank-you/care insert and one branded label-area concept. Use the printer/carrier requirements before production export; do not alter required shipping barcodes.'],
['Product images','A consistent crop/background/size treatment for the 250 catalogue records using licensed supplier assets or accurate photographs. Missing images are a data task; do not invent medical product details.'],
['Editable handover','Keep editable logo/vector masters, design files, web exports, asset names, dimensions and licence/provenance notes. Printer-ready files require actual dielines, materials, bleed and proof approval.']],[.26,.74]),
h('How AI contributes'),
p('Use image-generation tools for creative exploration and non-product brand graphics; design/prototyping tools for screen alternatives; writing assistants for draft copy; coding assistants for implementation. The owners choose the direction, Shishir integrates the system, and a responsible reviewer checks factual claims. Tools and subscriptions are to be selected; no capability or licence entitlement is assumed.'),
note('Packaging boundary','The launch branding scope covers shipping presentation. It does not include relabelling medical products, changing sterile packaging, replacing manufacturer labels/instructions or introducing a private-label medical product. Preserve safety information and assess any such change through its separate product/operator route. GB and Northern Ireland requirements differ. [R01]'),
p('Physical printing, buying boxes and packaging production lead times are operational workstreams. Plain compliant shipping materials can support launch while approved branded materials are produced; the website build does not depend on a printing order.')],['R01']),
s('customer-features','Features customers can use at launch','03 / First-release feature list',
'Ten customer-facing feature groups form the first purchase journey. Each has a concrete acceptance outcome.',[
table(['ID / feature','What we will build','Ready when'],[[a+' / '+b,c,e] for a,b,c,d,e in FEATURES[:10]],[.21,.48,.31]),
note('Payments and channels','Payment methods require merchant approval for the actual business and catalogue; wallet display also depends on device/browser support. Merchant Center acceptance is a separate external review. These dependencies are tracked from the start, not promised as automatic software outcomes.')]),
s('admin-features','Features the business can operate','03 / Admin and operations',
'Ten connected admin and operating capabilities make the website a working retailer, with a repeatable path for products beyond the first 250.',[
table(['ID / feature','What we will build','Ready when'],[[a+' / '+b,c,e] for a,b,c,d,e in FEATURES[10:]],[.21,.48,.31]),
p('The proposed implementation remains Next.js, React/Vite admin and PostgreSQL on Hostinger, with Cloudflare domain/R2 and a NestJS/Fastify API. Auth/job/data libraries remain recommendations subject to the early compatibility slice. The detailed technical specification contains the engineering contracts.')]),
s('boundaries','What fits inside the first 25 days','03 / Delivery boundaries',
'The launch package prioritises a usable, reliable selling operation. Manual steps are explicit and assigned to staff.',[
table(['Launch approach','Boundary'],[
['Included as a working workflow','Customer/staff identities, approved catalogue, owned stock, checkout, payments, dispatch, service email, financial records, refunds, eligibility controls, hosting and recovery.'],
['Manual but supported','Human professional/product review; carrier booking outside the store with tracking entered in admin; export-based accounting; supplier purchasing outside the system with receipts entered into stock.'],
['Later development','Automated carrier/accounting connectors, full purchase-order management, organisation hierarchies, trade quotes/pricing/credit, subscriptions, loyalty, elaborate CRM and marketing automations.'],
['Separate activation decisions','Prescription-medicine supply, sensitive clinical workflows, new countries and special storage/service categories require their own operating evidence and reviewed scope.'],
['Outside this business model','Multi-vendor seller portals, marketplace payouts, dropshipping and Stripe. A native mobile app and clinical prescribing service are not first-release features.']],[.28,.72]),
h('How to handle extra ideas'),
p('Owners can choose navigation, visual style, messaging and the priority of optional enhancements. After the Day 3 baseline, changes are logged with effort and impact. A new optional feature replaces comparable optional work or moves to the next phase; it is not silently added to the same deadline.'),
note('First-release rules','Do not cut stock correctness, payment verification, necessary buyer/product controls, staff MFA, customer disclosures or recovery to meet a date. If these are incomplete, the release moves or uses a specifically approved smaller lawful assortment; held products remain unavailable.'),
p('The full-range ambition remains unchanged. The initial UK operating lane must be confirmed: GB and Northern Ireland are separately configured, and European checkout is not enabled until the relevant country work is complete. A product approval, a payment approval and a Google listing approval are different decisions. [R01,M01]')],['R01','M01']),
s('catalogue','The 250-product warehouse workstream','04 / Catalogue and stock readiness',
'Product preparation runs alongside development, with a named business reviewer and warehouse contact. It cannot be completed by code or AI alone.',[
table(['Checkpoint','Intake target / action'],[
['By Day 3','Ten representative pilot records: include ordinary, variant/pack and restricted/expiry examples where present. They are part of the 250, not additional products.'],
['Days 7 / 9 / 11 / 13 / 15','Five batches of 50; cumulative processed totals 50 / 100 / 150 / 200 / 250. These are intake/review targets, not claims of approval.'],
['By Day 18','Every record has a disposition: approved, held, or excluded/duplicate, with reason and owner. Resolve variant-versus-SKU counting before reporting completion.'],
['Day 24 / daily after launch','Reconcile opening physical counts and subsequent movements; verify sellable stock, locations and applicable lots/expiry. Use the admin as the stock authority.']],[.28,.72]),
h('Minimum product record'),
p('SKU and manufacturer reference; category/intended use and regulatory route; variant/pack/unit; approved title/description; supplier and content/image rights; relevant labels/evidence; cost/selling price and reviewed tax treatment; physical quantity/location; lot/serial/expiry where applicable; dimensions/weight/delivery constraints; buyer/territory/provider/channel eligibility; review owner/date and status.'),
p('Flow: inventory list -> draft import -> validation -> image preparation -> human product/content review -> stock reconciliation -> approved publication and eligible feed. Unresolved rights, evidence, expiry or buyer requirements create a hold. Never infer legal status from a scraped category name.'),
note('Capacity assumption','At an illustrative 10-20 minutes for basic record preparation/review, 250 records need about 42-83 person-hours before photography, missing evidence or specialist assessment. This is a planning range, not measured productivity. Assign a separate client data/warehouse workstream and test throughput on the ten pilot items.'),
p('Target all 250 records for review, with a dashboard showing approved + held + excluded/duplicate = 250. If the real count differs, update the baseline explicitly. A lower lawful live count is reported honestly and requires an owner decision; it is not called full-catalogue completion.')]),
s('team','A shared delivery team, every day','04 / Collaboration and ownership',
'AI supports the work; the developer and business owners remain responsible for decisions, accuracy and acceptance.',[
table(['Role','Responsibility'],[
['Shishir / technical lead','Facilitate the design sessions; own architecture, integration, reviewed code, daily demos, testing and release preparation.'],
['One client decision-maker','Consolidate design/feature feedback; approve commercial choices and launch readiness; resolve decisions within an agreed response window.'],
['Product/data reviewer','Supply lawful source data and rights, review descriptions/eligibility and clear or hold each launch product. A qualified adviser is used where the route requires one.'],
['Warehouse / support / finance','Verify stock, storage and shipping; operate returns; provide prices/tax/financial details and perform acceptance exercises.'],
['AI support roles','Creative exploration, interface drafts, authorised data cleanup, backend/database assistance, test drafting and review. Use actual product facts; keep secrets and personal evidence out of general prompts.']],[.28,.72]),
h('Working rhythm and shared board'),
p('Daily: a short blocker check, an async preview/build update, and a written decision/action log. Joint demos on Days 1, 5, 10, 15, 21 and 24. Use columns for ideas, agreed launch scope, in progress, client review, tested and complete. Every item has an owner, acceptance proof and deadline.'),
p('Proposed feedback target: one business day, with an agreed weekend/holiday arrangement. Silence does not approve a brand, product or release. If an essential decision is late, move independent work forward and show its schedule impact.'),
note('Capacity and contingency','Treat 200-240 focused developer hours as an unmeasured planning envelope, including AI supervision, integration and review: roughly 160-190 hours for design/build plus 40-50 for verification, corrections and launch. The separate catalogue effort is not included. Confirm staffing/working days; this is an aggressive target, not a guaranteed throughput claim.'),
p('Days 5 and 15 are re-planning gates. Validate real progress and provider readiness. If the work does not fit, defer optional enhancements, add accountable capacity or revise the date; several AI tools do not remove the human integration and approval workload.')]),
]

for idx in range(5):
    subset=DAYS[idx*5:(idx+1)*5]
    start,end=subset[0][0],subset[-1][0]
    themes=['Design, foundations and proof','Build the shopping journey','Complete the business workflow','Review the catalogue and verify quality','Accept, rehearse and launch']
    SECTIONS.append(s(f'days-{start}-{end}',f'Days {start}-{end}: {themes[idx]}','05 / Daily development plan',
       'Dates below retain the illustrative Day 0 convention. Each day shows the build, the business contribution and the evidence needed to call it complete.',
       [dict(kind='day',day=n,date=(KICKOFF+timedelta(days=n)).strftime('%d %b %Y'),title=title,build=build,client=client,evidence=evidence) for n,title,build,client,evidence in subset]))

SECTIONS += [
s('readiness','The Day 24 release decision','06 / Acceptance and launch readiness',
'The owner and technical lead review evidence together. Passing a screen demo is not enough to start taking orders.',[
table(['Gate / owner','Evidence required before launch'],[
['Products / reviewer + warehouse','All 250 records accounted for; every live item has approved evidence/content, correct pack/price/tax, owned available stock and supported destination/buyer rules. Held items are not purchasable.'],
['Payments / finance + developer','Approved merchant accounts/catalogue; supported wallets verified; capture, failure, duplicate event, reconciliation and refund tests passed. No card details stored by our application.'],
['Customer / owner + developer','Guest, account and professional journeys tested on mobile/desktop; disclosures, delivery costs, terms and confirmation are correct. [C01]'],
['Safety and resilience / developer','Staff MFA/roles and cross-user access tests pass; no open critical/high-impact security or transaction blockers; tested backup/restore, rollback and monitoring.'],
['Search and accessibility / developer','Lighthouse SEO 100 on audited public templates; performance median targets 90 mobile/95 desktop (checkout 85 mobile with provider scripts); manual WCAG 2.2 AA checks. Targets, not ranking guarantees.'],
['Operations / warehouse + support','Staff demonstrate pick/pack/dispatch, return/refund and stock hold; real delivery/returns workflow, service mailbox, incident contact and opening-day coverage are ready.'],
['Channel / marketing owner','Eligible feed validated and historic notices reviewed honestly; account/product review status recorded. Google approval and search traffic are not prerequisites that can be promised by a coding date. [M01]']],[.28,.72]),
p('Field Core Web Vitals targets remain p75 LCP <=2.5s, INP <=200ms and CLS <=0.1 when sufficient real-user data exists. At a new launch, unavailable field data is recorded as unavailable; synthetic scores are not substituted for actual user measurements. [Q01]'),
note('If a gate fails','List the blocker, affected products/methods, owner and next decision date. Core lawful-selling, payment, stock or security failures block selling. A different supported payment mix or smaller eligible assortment needs an explicit owner scope decision. Merchant/campaign review may continue separately while the lawful store operates.')],['C01','M01','Q01','Q02']),
s('growth','Day 25 and the next products','06 / Controlled launch and continuation',
'The first 250 products establish the workflow. The platform must support the next product without a development request or a fixed catalogue cap.',[
table(['Time / action','What the team does'],[
['Before opening','Confirm release authority, final stock/rules, provider readiness, backup point, production secrets, mail delivery and monitoring. Freeze unrelated changes.'],
['Controlled opening','Verify public pages/TLS and an authorised live payment/refund smoke check. Confirm stock, confirmation email, order queue and actual packing/dispatch behaviour.'],
['During the first orders','Watch failed payments, webhook backlog, stock conflicts, delivery questions and support. Reconcile captured payments with orders and shipped quantities.'],
['End-of-day review','Record sales/refunds/stock changes, errors and support issues. Assign corrections and the next operating shift. No mass campaign runs without separate campaign approval/readiness.']],[.26,.74]),
h('How another product reaches the website'),
p('Create/import a draft -> attach supplier/evidence/rights -> add accurate images and pack/price/tax data -> confirm buyer/market/payment/channel rules -> receive and verify owned stock -> human approval -> publish -> include in eligible feeds -> monitor. A new product outside the existing approved handling route may require further operational work; adding a row is not regulatory clearance.'),
note('Demonstrate expansion before launch','On Day 18, use a clearly marked additional staging test item, separate from the 250 stock records. A trained operator adds it through the admin, reviews it, receives stock and publishes it to staging. Remove test data from production imports. No code deployment should be required for an ordinary product in an already supported route.'),
p('Proposed first 72 hours: named developer/operations review windows for payment, mail, stock and support issues; actual coverage hours and support terms must be agreed. This is not an assumed 24/7 maintenance contract.'),
p('Later releases retain the earlier illustrative dates: Phase 2 on 20 January 2027 for operating depth; Phase 3 on 2 March for B2B/repeat purchasing and reviewed marketing; Phase 4 on 12 April for country-readiness and further hardening. Features and destination activation remain subject to each phase review.'),
p('Handover pack: editable brand/design assets with rights notes; repository and deployment instructions; product intake and staff SOPs; role/account ownership; source/configuration inventory without secrets; acceptance evidence, recovery procedure and prioritised backlog. No development fee is quoted in this plan.')]),
]

SOURCES=[
dict(id='B01',title='UK Intellectual Property Office: trade-mark search',url='https://www.gov.uk/search-for-trademark',checked='9 November 2026',scope='UK preliminary name/logo search; not comprehensive clearance or EU protection.'),
dict(id='R01',title='MHRA: regulating medical devices in the UK',url='https://www.gov.uk/guidance/regulating-medical-devices-in-the-uk',checked='9 November 2026',scope='Medical devices/IVDs; distinct GB/NI routes, operator and labelling responsibilities. Other product routes remain separately reviewed.'),
dict(id='C01',title='GOV.UK: online selling',url='https://www.gov.uk/online-and-distance-selling-for-businesses/online-selling',checked='9 November 2026',scope='UK ecommerce order information, prices, payment obligations, terms and confirmation.'),
dict(id='M01',title='Google Merchant Center: healthcare and medicines',url='https://support.google.com/merchants/answer/6150151?hl=en',checked='9 November 2026',scope='Merchant product/country restrictions; store eligibility does not imply Google listing approval.'),
dict(id='Q01',title='Core Web Vitals',url='https://web.dev/articles/vitals',checked='9 November 2026',scope='Field p75 LCP, INP and CLS definitions/thresholds; inherited from the technical specification research.'),
dict(id='Q02',title='Lighthouse scoring documentation',url='https://github.com/GoogleChrome/lighthouse/blob/main/docs/scoring.md',checked='9 November 2026',scope='Automated audit score interpretation; 100 SEO is a proposed project target, not a Google ranking score.'),
]

assert len(DAYS)==25 and [d[0] for d in DAYS]==list(range(1,26))
assert len(FEATURES)==20 and len(SECTIONS)==15
