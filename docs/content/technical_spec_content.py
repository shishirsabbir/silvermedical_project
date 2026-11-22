"""Editable technical design baseline. Requirements are proposed, not implemented."""
DATE = "9 November 2026"
VERSION = "1.0 / Proposed implementation baseline"

def p(t): return {"kind":"p", "text":t}
def h(t): return {"kind":"h", "text":t}
def table(headers,rows,widths=None): return {"kind":"table","headers":headers,"rows":rows,"widths":widths}
def callout(title,text,tone="teal"): return {"kind":"callout","title":title,"text":text,"tone":tone}
def diagram(name): return {"kind":"diagram","name":name}
def code(text): return {"kind":"code","text":text}
def req(id,text,acceptance,phase="P1"): return {"kind":"requirement","id":id,"text":text,"acceptance":acceptance,"phase":phase}
def section(id,title,group,intro,blocks,refs=()): return dict(id=id,title=title,group=group,intro=intro,blocks=blocks,refs=list(refs))

SECTIONS = [
section("scope","What we are building","01 / Product and architecture",
"One retailer, one owned-stock operation and a connected commerce platform for consumers and verified professional buyers.",[
p("Build a new UK-first medical-supplies business under a name and legal operator still to be confirmed. The system covers product approval, purchasing/receiving, inventory, discovery, checkout, payments, dispatch, returns, customer service and management reporting. Mixed UK/EU sourcing may include manufacturers and Praxisdienst where agreements and rights exist."),
table(["Status","Baseline"],[
["Confirmed direction","Next.js storefront; regular React admin; PostgreSQL; Hostinger KVM; Cloudflare domain and R2; upload-time image optimisation; Revolut, Apple Pay, Google Pay and PayPal."],
["Proposed technical choices","TypeScript, NestJS/Fastify, Vite, Prisma, Better Auth, pg-boss, Sharp, Docker Compose and the security/performance policies in this specification. These need an integration spike and acceptance."],
["Product permissions","Full-range ambition remains. Each product, buyer, territory, payment provider and sales channel has independent eligibility. GB and Northern Ireland are distinct; European countries activate individually."],
["Delivery baseline","Four releases using assumed kickoff 15 November 2026: 10 December 2026; 20 January, 2 March and 12 April 2027. Dates are targets with external dependencies."]],[.25,.75]),
h("How to read the specification"),
p("P1-P4 identify proposed delivery phases. Requirement IDs link features to acceptance evidence. 'Must' defines an intended implementation requirement, not an existing capability or a claim that an external approval exists. Numeric limits and service objectives are engineering proposals to validate in the pilot."),
p("The launch excludes marketplace sellers, dropshipping workflows, Stripe, native mobile apps and clinical prescribing. Prescription-medicine activation remains undecided and disabled pending a separate lawful operating route. This does not remove medicines or other categories from the longer-term ambition."),
req("SCOPE-01","Deliver a complete first-selling workflow for the agreed launch assortment.","An authorised operator can receive an item, publish it, accept a valid payment, dispatch it, refund it and trace the stock movement."),
callout("Design status","This document specifies the build. No store, database, accounts or provider integration has been deployed by preparing it. The client proposal and detailed operating plan remain supporting references.")]),

section("architecture","System architecture and trust boundaries","01 / Product and architecture",
"Keep the transactional core together initially, with explicit browser, application, database, storage and third-party boundaries.",[
diagram("architecture"),
table(["Boundary","Responsibilities and rules"],[
["Public storefront","Next.js renders catalogue pages and customer UI. It calls the API for authoritative data; customer-specific requests never enter a shared cache."],
["Staff admin","React SPA served as static assets on the admin hostname. Every operation requires a staff session and API permission checks; hiding a button is not access control."],
["API and worker","NestJS modules own decisions and transactions. A separate worker process executes durable imports, media, notification, feed and reconciliation jobs."],
["PostgreSQL / R2","PostgreSQL is private to application services. R2 has separate public-media and private-evidence buckets. Public URLs contain no personal evidence."],
["External services","Provider adapters isolate payments, email and later carrier/accounting integrations. Credentials stay server-side; callbacks are verified."]],[.26,.74]),
p("Proposed hostnames: www.<domain> for shopping, admin.<domain> for staff and media.<domain> for prepared public assets. Both browser applications use same-origin /api/v1 and /api/auth routes through the reverse proxy. Provider webhooks have dedicated public endpoints; the database is never exposed on a public port."),
req("ARCH-01","Maintain one authoritative path for commerce changes.","Changing a browser price, buyer ID, stock quantity or payment flag cannot alter a server-approved order.")],["NX01","NE01"]),

section("stack","Frameworks, libraries and repository","01 / Product and architecture",
"A TypeScript monorepo with a modular API keeps shared contracts visible while allowing the storefront, admin and worker to deploy as separate processes.",[
table(["Layer","Recommended baseline / purpose"],[
["Storefront","Next.js App Router + React; server components for catalogue reading, small client components for search/filter/cart interactions."],
["Staff application","React + Vite; TanStack Query/Table, React Hook Form and Zod; accessible reusable components and a shared design-token package."],
["API","NestJS + Fastify adapter; REST with OpenAPI, module-level services, typed validation and request IDs. Choose supported adapter-compatible middleware."],
["Data access","PostgreSQL + Prisma, subject to current adapter compatibility. Encapsulate SQL row locks and financial transactions in repositories; migrations are reviewed."],
["Identity / jobs / images","Better Auth for identity/session lifecycle; pg-boss for PostgreSQL-backed jobs; Sharp for prepared image variants. These are proposed selections."],
["Quality / delivery","Vitest for domain logic, Playwright for end-to-end flows, axe for automated accessibility, Lighthouse CI and k6 for performance. Docker Compose + Nginx for initial hosting."]],[.24,.76]),
code("apps/storefront     Next.js customer application\napps/admin          React/Vite staff application\napps/api            NestJS HTTP + business modules\napps/worker         Durable job handlers\npackages/contracts  OpenAPI schemas and generated clients\npackages/ui         Design tokens and shared UI primitives\npackages/config     Linting, TypeScript and test config\ninfra/              Containers, proxy, backup and runbooks"),
p("Use a supported Node.js LTS runtime and mutually compatible stable package releases. Pin exact versions, package-manager version and container digests at kickoff; commit the lockfile and record licences/security advisories. Do not adopt release candidates solely because they are newer."),
req("STACK-01","Prove the selected combination before committing the backlog.","The first slice demonstrates auth + MFA, Prisma/Better Auth schema integration, one stock transaction, image job and payment sandbox round-trip. Resolve incompatible adapters before broader implementation.")],["NX01","NE01","VI01","DB02","AU01","JB01","IM01","QA01","QA02"]),

section("experience","The customer experience","02 / Storefront and buying journeys",
"The storefront should feel like a dependable professional supplier: easy product identification, clear pack pricing and an uncomplicated purchase journey on desktop and mobile.",[
diagram("storefront"),
table(["Area","Required behaviour"],[
["Header/navigation","Brand, prominent identifier/name search, category navigation, account and basket. Display useful service facts only when supported by actual operations."],
["Home page","Category/specialty discovery, curated approved products and buying guides. Avoid clinical advice, invented trust badges, fake reviews or unsupported delivery claims."],
["Visual system","Proposed white/navy/teal palette, readable typography, consistent spacing, clear focus states and restrained motion. Final brand identity remains an owner decision."],
["Responsive behaviour","Test 360, 390, 768, 1024 and 1440px viewports. Mobile uses an accessible menu/filter drawer, large controls and a basket summary that does not obstruct content."]],[.27,.73]),
p("Every screen includes loading, empty, error and permission states. A product needs an approved public representation before appearing in navigation, search, recommendations or a sitemap. Restricted purchasing is explained with a clear permitted next step; private evidence is never shown in an illustration or public page."),
req("UX-01","Support a complete mobile and keyboard shopping journey.","A user can search, select the correct pack, edit quantities, see delivery/tax, pay and retrieve confirmation without a mouse or horizontal page overflow.")]),

section("routes","Routes and customer journeys","02 / Storefront and buying journeys",
"Use predictable URLs and a small set of reusable page templates. The launch market uses UK English and GBP; country expansion is configuration-backed.",[
table(["Route/template","Behaviour / access"],[
["/ and /categories/[slug]","Public home and categories with reviewed copy, filters, pagination and breadcrumbs."],
["/products/[slug]","Public approved product detail, variant/pack selection, price, availability, documents and purchase eligibility."],
["/search?q=...","On-site identifier/name search; noindex. Empty results offer useful navigation without silently substituting products."],
["/basket and /checkout","Private/no-store commerce context; consumer guest purchase supported for unrestricted goods."],
["/account/...","Authenticated profile, addresses, orders, documents and preferences. Professional verification is a separate workflow."],
["/guides/[slug], /help, policy pages","Reviewed content, contact, delivery, cancellation/returns, privacy and cookie controls. Named content review ownership."],
["admin.<domain>/...","Staff-only work queues and detail screens; authentication and noindex on every route."]],[.36,.64]),
h("Three primary journeys"),
p("Consumer: discover -> compare actual pack/specification -> basket -> guest or account checkout -> approved payment -> confirmation -> dispatch updates -> return/support if needed."),
p("Professional: create/verify email -> submit organisation/professional evidence where required -> reviewer approves scope/expiry -> purchase eligible products. An organisation label alone does not grant entitlement."),
p("Returning buyer: view previous orders -> reorder into a new basket -> review changed price, pack, availability and eligibility -> checkout at current terms. Saved lists and multi-user organisations expand in P3."),
req("UX-02","Keep historic orders and current buying decisions distinct.","An old order retains its original item/price/tax snapshot; a reorder uses current approved data and flags material changes."),
callout("European URLs","Keep stable UK URLs at launch. In P4 introduce explicit country/language routes such as /de-de/ only after a country dossier passes; canonical and hreflang mappings must reflect live, equivalent pages.")]),

section("discovery","Search, categories and product discovery","02 / Storefront and buying journeys",
"Help customers find the correct item quickly without implying that similar medical products are clinically interchangeable.",[
table(["Requirement","Implementation behaviour"],[
["Exact search","Prioritise exact SKU, GTIN and manufacturer part number. Preserve identifier strings and leading zeroes; normalise a separate search key."],
["Text relevance","Use PostgreSQL full-text search and indexed trigram matching initially; controlled synonyms and common abbreviations are maintained by staff. Query length and result counts are bounded."],
["Filters","Category-specific attributes: pack quantity, size, material, sterility and relevant specification. Show only supported attributes and permitted products; make applied filters removable."],
["Results and pagination","24 items per page by default, maximum 48 public results per request. Stable order and crawlable page links; keep filters in the URL and keyboard focus predictable."],
["Visibility","Search/facets/counts are computed from the approved public projection for the chosen market. Costs, draft SKUs, private evidence and unapproved claims cannot leak in snippets."],
["No-result / discontinued","Offer category navigation and explicit alternatives where reviewed. Do not add substitutes automatically; keep temporarily unavailable pages useful."]],[.26,.74]),
p("Autocomplete waits about 250ms after typing, cancels stale requests and shows product/category matches. It must be keyboard operable and announce results. The initial search service remains in PostgreSQL; add a dedicated search engine only after measured query/relevance needs justify its resource and maintenance cost."),
p("The search projection stores approved title, identifiers, category, public attributes, market and publication revision. Publishing or suspending a SKU emits a projection-refresh job. A synchronous public-status guard protects access while projections catch up."),
req("CAT-01","Make discovery accurate and permission-aware.","A known SKU is the first exact result; filters retain correct pack meaning; suspended/draft items disappear from results, counts and suggestions. A 20k-SKU synthetic fixture meets the read latency target."),
callout("Launch scope","Basic exact/text search, categories and key filters are P1. Advanced synonym tuning, merchandising experiments and zero-result analytics improve in P2-P3.")]),

section("product","Product page and purchase eligibility","02 / Storefront and buying journeys",
"The product page should answer what the item is, how much is supplied, what it costs and whether this buyer can order it.",[
diagram("product"),
table(["Information","Required presentation"],[
["Identity and pack","Manufacturer, SKU/MPN and available identifiers; exact variant, units per box/case and order multiple. Never confuse price per pack with price per individual item."],
["Price / availability","Consumer-facing tax-inclusive price and clear delivery estimate. Optional trade ex-VAT display is secondary and labelled. Availability comes from sellable owned stock."],
["Product evidence","Reviewed description/intended use, key specification, permitted instructions, warnings and warranty/service details. All public images/text have a recorded source/right."],
["Buyer state","Public buyer, verified professional, pending/rejected/expired evidence or unavailable destination. Explain the permitted action; do not expose private approval reasoning."],
["Interaction","Accessible image gallery, real variant controls, quantity validation and visible confirmation after add-to-basket. Related items obey identical public/market rules."]],[.27,.73]),
req("CAT-02","Make the purchase button a reflection of server rules.","A forged add-to-cart or checkout request cannot bypass a product, market, buyer, stock or provider restriction. The API returns a stable reason code and safe customer message."),
p("A temporary stock-out retains an accurate page with OutOfStock data. A suspended or unsafe product follows the takedown/recall workflow; a removed public page must not remain available through a cache or feed. No prescription purchase workflow is activated by this design.")]),

section("checkout","Basket, checkout, tax and delivery","02 / Storefront and buying journeys",
"Checkout produces a server-priced order from a current basket and an eligible address. The browser can request quantities, never dictate totals.",[
table(["Stage","Server and UI behaviour"],[
["Basket","Anonymous basket uses a scoped opaque cookie; account login merges only after current product/price/quantity checks. No payment or clinical data belongs in local storage."],
["Contact and address","Collect necessary billing/shipping/contact details, accept address correction and validate destination. Do not require a consumer account for ordinary unrestricted purchases."],
["Eligibility","Recheck exact product revision, market, buyer entitlement, evidence expiry and sellable stock. Hold or reject an ineligible mixed basket before taking payment; offer removal of blocked lines."],
["Quote","Return an immutable quote snapshot with currency, line amounts, discounts, tax, delivery and expiry. Proposed quote life: 10 minutes. Reprice at commitment if changed/expired."],
["Payment","Create an order/payment attempt with an idempotency key and a stock reservation. Load only relevant provider components; support wallet availability gracefully."],
["Confirmation","Show confirmed, processing or action-needed state from the API. A return URL is not payment proof. Send a service email after the authoritative event."]],[.23,.77]),
p("Use currency minor units for money and decimal arithmetic for rates. Store tax jurisdiction/code/rate/rounding version and line snapshots. Shipping and discounts have explicit allocation rules. An accountant approves tax-relief and cross-border rules before activation; 'medical' is not an automatic tax exemption."),
p("P1 uses a reviewed UK delivery matrix by zone, weight/size and product shipping class. Unsupported hazardous, cold-chain, oversized or special-service combinations return a quote/contact route. Never advertise a carrier service that is not actually arranged."),
req("CHK-01","Charge exactly the current accepted total once.","Price tampering, expired quotes, mixed tax rates, delivery changes, double-clicks and address changes are tested. The shown grand total equals the provider order amount and stored currency."),
callout("Account conversion","After guest purchase, offer account creation. Linking a guest order requires ownership proof; matching a typed email address alone must not expose past orders.")]),

section("customer","Accounts, organisations and after-sales","02 / Storefront and buying journeys",
"Customer self-service reduces support effort while keeping professional entitlement, organisation membership and personal account access separate.",[
table(["Capability","P1 baseline and later development"],[
["Profile / addresses","Verified email, profile and saved addresses, with explicit confirmation for sensitive changes. Do not silently change existing order snapshots."],
["Orders / documents","Own order timeline, permitted tracking links, invoices/credit notes and refund status. Downloads use an ownership check and short-lived access."],
["Professional review","Submit only necessary business/profession evidence; pending, approved, rejected, expired and revoked states, with review scope/expiry. Human approval is P1."],
["Support / returns","P1 support route with order reference and staff-managed returns. P2 order-linked cases/return intake; evidence access is role-restricted."],
["Organisations - P3","Membership and roles per organisation, approved price lists, quotes, saved lists and fast reorder. Users cannot join an organisation merely by sharing its email domain."],
["Preferences","Purpose/channel consent and withdrawals, with essential service notices maintained. No preselected marketing consent or automatic legacy-list import."]],[.26,.74]),
p("Access to an order is checked against the authenticated customer or permitted organisation membership on every request. Use opaque IDs and deny by default. Storefront identity is separate from staff identity, even where a person uses the same email address in both contexts."),
p("Reorders create new lines from current catalogue and market rules. Flag substitutions, changed pack size, discontinued items, price changes and special approval requirements. Customer pricing cannot be exposed through public product JSON or a shared cache."),
req("ACC-01","Protect customer and organisation boundaries.","User A cannot read, download, reorder, cancel or change User B's order by replacing an ID. Organisation switching never carries another organisation's cart price or permission."),
callout("Retention and deletion","Provide a documented privacy-request workflow. Separate data that can be removed from records retained for lawful accounting, disputes and product traceability; do not indiscriminately delete recall links.")]),
]

SECTIONS += [
section("auth-customer","Customer authentication and recovery","03 / Identity and access",
"Proposed identity library: Better Auth, integrated into the Fastify-backed API. The application owns commerce authorisation; the library manages credential and session lifecycle.",[
diagram("customer-auth"),
table(["Flow","Required behaviour"],[
["Registration","Email/password with required email verification and no immediate authenticated session. Return generic responses for existing/new addresses; test plugin fields do not reveal account existence."],
["Verification","Purpose-bound, one-time expiring verification link; proposed expiry 24 hours. Use a fixed trusted base URL and safe return-path allowlist; no arbitrary redirects from user input."],
["Sign-in","Generic failure message, throttling and an opaque server-side session. Normal login establishes identity only; API product/organisation entitlements are checked separately."],
["Password reset","Generic response, one-time token with proposed 30-minute lifetime; no token in logs/analytics. A completed reset revokes existing sessions and sends a security notification."],
["Change email/password","Require current credentials/recent authentication, verify the new address before changing identity, notify the old address and revoke sessions as appropriate."],
["Guest checkout","Guest basket/order access is a scoped capability, not an authenticated customer account. Claiming past orders requires a separate ownership verification flow."]],[.25,.75]),
p("Proposed password policy: at least 15 characters, allow at least 64 and cap at 128; accept password managers and paste, block known compromised/common values, and avoid arbitrary composition rules or scheduled resets. Use the library's documented scrypt implementation initially, benchmark its cost and never write a custom password hash. [AU03,AU04,OW02]"),
req("AUTH-01","Make account lifecycle secure and testable.","Verification/reset tokens are single-use and expire; unknown and existing emails have equivalent public responses; password reset removes old session access. Test mail delay and resend throttling."),
p("**Integration checkpoint.** Better Auth's official Fastify integration, session and email/password features are available. Our Nest adapter, separate realms, storage schema and mail hooks must pass the kickoff spike before this recommendation is accepted. [AU01-AU03]")],["AU01","AU02","AU03","AU04","OW02"]),

section("auth-staff","Staff sign-in, MFA and recovery","03 / Identity and access",
"The staff interface is invite-only. Customer registration must never create or promote a staff identity.",[
diagram("staff-auth"),
table(["Control","Proposed implementation contract"],[
["Identity separation","Separate customer and staff auth configurations, secrets, cookie names and auth tables/model names. Select realm from an allowlisted hostname/internal proxy route, never from a public request field."],
["Provisioning","Owner-authorised invite links, single use with a 24-hour expiry. No public staff signup. Initial owner bootstrap is a controlled one-time operational command with an audit record."],
["MFA enrollment","Require verified email, strong password, TOTP enrollment confirmation and recovery-code acknowledgement before staff API access. Two-factor status alone must not imply a completed challenge."],
["Sign-in / step-up","Require TOTP for each new staff session. No trusted-device bypass at launch. Require authentication within five minutes for role changes, secret-sensitive settings and refunds."],
["Recovery / offboarding","Recovery codes are protected and consumed once. Lost-factor recovery requires a documented identity/owner review; support cannot bypass MFA casually. Revoke all sessions on suspension or staff removal."]],[.26,.74]),
p("Better Auth provides TOTP and backup-code capabilities. Its plugin is a building block: the API must additionally enforce our invitation, mandatory-enrollment, challenge-completion and step-up policies. Configure encryption secrets and their backup/rotation procedure before accepting production enrolments. [AU05]"),
p("The gateway overwrites internal realm headers and rejects unexpected Host values. Only the private application network can reach the upstream API. Next.js server-side calls use a fixed customer realm; caller-provided forwarded headers cannot select staff authentication."),
req("AUTH-02","Protect staff operations even when the UI is bypassed.","A password-only session, unfinished enrollment, stale step-up, revoked account or customer cookie receives no staff access. Simulate losing an MFA device and completing the documented recovery process."),
p("**P1 requirement.** Staff MFA and least privilege are release requirements. Social sign-in, enterprise SSO and passkeys may be evaluated later; they are not dependencies for launch.")],["AU05","OW01","OW02"]),

section("sessions","Session, cookie and CSRF policy","03 / Identity and access",
"Use opaque, server-validated browser sessions with immediate revocation for sensitive operations. Do not place bearer tokens in browser local storage.",[
table(["Policy","Proposed baseline"],[
["Cookie scope","Separate customer/staff host-only session cookies; Secure, HttpOnly, SameSite=Lax and Path=/. Prefer __Host- names where supported by the pinned adapter; no Domain-wide sharing."],
["Customer lifetime","Seven days of inactivity and 30 days absolute from the original authentication. Re-authenticate sensitive identity actions. Enforce absolute age independently of rolling refresh."],
["Staff lifetime","15-minute idle timeout and eight-hour absolute session limit. Server guards enforce both; expiring a UI timer is insufficient. Five-minute freshness for specified step-up actions."],
["Revocation / cache","Disable auth cookie-cache shortcuts initially; read session validity and current critical permissions server-side. Logout, reset, suspension and role changes revoke/refresh access immediately."],
["CSRF / origins","Same-origin browser API; validate allowed Origin/Referer and use a session-bound CSRF token on state changes. Reject unsafe cross-origin requests. Business GET routes cannot mutate state; auth-link callbacks use purpose-bound token validation."],
["Rate limits","Proposed: five failed logins/account/15min plus IP limits; three reset/resend requests/address/hour, with progressive delay and abuse monitoring. Tune shared-clinic IP handling; avoid permanent lockout abuse."]],[.27,.73]),
p("SameSite is defence in depth, not the only CSRF control. Keep the auth library's origin protections enabled. Webhook endpoints are a distinct exception: they use provider verification and replay controls rather than a browser CSRF token. [OW03,AU04]"),
p("Pass cookies through the reverse proxy without rewriting them to a parent domain. Set no-store on auth/private responses. Never log session values, reset links or MFA secrets. Better Auth's session store contains sensitive token material; protect database/backups accordingly and do not describe those records as irreversibly hashed unless the chosen adapter proves it. [AU02,AU06]"),
p("Guest access uses a separate 32-byte cryptographically random capability, held in a secure HttpOnly host-only cookie and stored only as a hash in the business database. Scope it to one basket or order; expire and rotate it after checkout. An order reference or email address alone never grants access."),
req("AUTH-03","Enforce session boundaries on the server.","Test idle/absolute expiry, session fixation, concurrent sessions, cross-site form submission, role removal and customer-to-admin cookie reuse. Confirm no account HTML is shared through CDN or Next.js caches.")],["AU02","AU04","AU06","OW01","OW03"]),

section("permissions","Roles, permissions and ownership checks","03 / Identity and access",
"Authentication answers who the caller is. Role, resource ownership, organisation, product, destination and review status determine what they may do.",[
table(["Role","Permitted work / boundaries"],[
["Guest / consumer","Public approved catalogue; own scoped basket and guest-order capability. Authenticated consumers can access their own profile/orders only."],
["Verified professional","Consumer rights plus explicitly approved product entitlement within scope/expiry. Verification does not confer staff access, all-product access or wholesale permission."],
["Catalogue editor / reviewer","Editor prepares drafts/imports. Reviewer approves evidence, public claims and territory/channel status. Default: editor cannot self-approve regulated changes."],
["Warehouse / support","Warehouse receives, picks and dispatches eligible stock; support handles assigned cases and permitted order data. Neither changes tax rules, provider secrets or product permissions."],
["Finance / marketing","Finance reconciles and refunds within assigned authority; marketing edits approved content/campaigns and eligible audiences. Neither gains clinical evidence access by default."],
["Owner / administrator","Manages staff and configuration, with MFA/step-up and audit. System administration does not grant professional authority to approve medical supply."]],[.28,.72]),
p("Represent permissions as named capabilities such as catalogue.edit, catalogue.approve, stock.receive, order.dispatch, payment.refund and staff.manage. API guards check capabilities and service methods enforce resource ownership/context. Default deny; never trust role, customer ID, organisation ID or market from the browser without validation."),
p("For small teams, one person may hold multiple roles, but regulated review and high-impact actions still need an accountable reviewer and reason. Any temporary exception is recorded with scope, expiry and owner approval. An owner cannot override missing legal or provider permission through a software switch."),
req("ACL-01","Prevent horizontal and vertical privilege escalation.","Exercise the permission matrix through direct API calls, including cross-customer IDs, wrong organisations, revoked verification, direct document URLs and staff role manipulation."),
callout("Audit event contract","Capture actor/realm, action, resource, timestamp, request ID, reason and a safe before/after difference. Exclude passwords, tokens, full payment data and unnecessary health information.")]),

section("admin","Advanced admin workspace","04 / Admin, product data and operations",
"Prioritise the work that needs action today: evidence reviews, customer verification, receipts, held orders, stock exceptions and payment reconciliation.",[
diagram("admin"),
table(["Workspace","Expected behaviour"],[
["Work queues","Role-specific counters and filters; clear reason codes, age, owner and next action. Counts come from the API and respect permissions."],
["Data grids","Server pagination/sort/filter, saved views later, column controls, row detail and accessible bulk selection. Default 50 rows; maximum 100 per request."],
["Editing","Draft/save/preview/review/publish, field validation and evidence links. Optimistic version checks prevent one staff member overwriting another's changes."],
["Bulk operations","Preview affected rows, validate limits, queue long work and export row errors. Destructive or permission-changing operations require explicit confirmation and audit."],
["Reporting","P1 daily orders, stock exceptions and payment discrepancies. P2-P3 purchasing, margin, fulfilment, cohort and channel dashboards with documented definitions."]],[.25,.75]),
req("ADM-01","Keep staff productive without hiding failures.","A 20k-SKU fixture remains responsive with server-side pagination; failed jobs show retry/error details; concurrent edits return a conflict rather than silently losing data."),
p("Avoid loading the entire catalogue into browser memory. Use indexed lookups and bounded exports. Audit trails are read-only to ordinary staff; role-limited CSV exports use safe escaping to avoid spreadsheet formula execution.")]),

section("catalogue","Product model, evidence and approval","04 / Admin, product data and operations",
"One publication flag cannot describe a regulated catalogue. Store approval dimensions separately and calculate the effective decision for the current action.",[
table(["Record / dimension","Fields and rules"],[
["Product + variant","Family, SKU, manufacturer/MPN/GTIN, variant attributes, pack/base unit, units per pack, order multiple, dimensions/weight and revision."],
["Regulatory route","Device, IVD, PPE, biocide, medicine, veterinary or ordinary goods; intended use, classification rationale and reviewer. Multiple regimes may apply."],
["Evidence version","Source/right, label/IFU/declaration/certificate reference, scope, issuer, relevant dates, hash, reviewer and decision. Confidential terms/costs stay separate."],
["Market and buyer","GB/NI/country lane, operator roles, allowed buyer class/profession, entitlement scope/expiry and any review hold."],
["Publication and channels","Draft/review/approved/suspended/retired; independent public-content, Shopping/free-listing, Ads and provider eligibility with reasons/review dates."],
["Operations","Traceability level, expiry/shelf-life rule, storage/shipping class, warranty/service owner and recall status."]],[.27,.73]),
p("Workflow: draft -> validation -> evidence review -> approved revision -> publication. A changed intended use, pack, supplier evidence, classification or claim creates a new reviewable revision. Minor editorial changes follow a defined rule; imports cannot bypass review. Publication changes create an outbox event for search, cache, sitemap and feed refresh."),
p("Eligibility combines current product/market/buyer/provider decisions and stock status. A suspended or expired prerequisite denies the affected action and creates an operator task. Review dates are not blanket legal expiry rules; the reviewer defines which dates matter for that route."),
req("REG-01","Apply eligibility consistently across every surface.","A suspended item cannot appear in public API/search/recommendations/feed or pass checkout/dispatch. Restriction tests cover ordinary consumers, approved professionals, NI and an unapproved EU country."),
callout("Medical scope","The software records decisions and enforces gates. Exact SKU classification and legal supply arrangements remain operator/reviewer responsibilities; prescription activation stays disabled pending the separate decision.","gold")],["R01","R03","M01"]),

section("imports","Supplier data and catalogue ingestion","04 / Admin, product data and operations",
"Treat every supplier file or external record as untrusted draft input. Importing product data must never imply that it is lawful, licensed for reuse or ready to publish.",[
table(["Step","Implementation"],[
["Acquire","Prefer authorised manufacturer/distributor feeds, CSV/API exports and licensed assets. Record supplier, contract/content-right reference, retrieval time and file hash. No unrestricted competitor scraping."],
["Stage","Validate file type/size, encoding, required columns and row limits. Store originals privately, assign import batch ID and isolate parse failures."],
["Map / normalise","Preview mappings for SKU, identifiers, unit/pack, currency, tax class and attributes. Preserve original values and avoid locale/decimal/date ambiguity."],
["Validate / compare","Detect duplicates, missing evidence, unexpected pack changes, price outliers and unsafe HTML. Compare proposed revisions with current records; show field-level diffs."],
["Review / apply","Approved staff apply bounded draft updates. Publication requires the separate product workflow. Commit batches safely with row-level status and a clear partial-failure report."],
["Observe / recover","Show progress, counts and errors; retry idempotently. A rollback creates an auditable correcting revision, not silent deletion of order-linked history."]],[.25,.75]),
p("P1 supports one agreed CSV template and human review; automated supplier connectors are later, individually scoped integrations. Price/stock feeds cannot overwrite the owned-stock ledger. Supplier availability is procurement information, not inventory the retailer can immediately dispatch."),
p("Proposed initial limits: 10MB CSV and 5,000 rows per batch; larger feeds are chunked into bounded jobs. Disable formula evaluation, remote XML entities and unbounded nested payloads. Any permitted URL fetching uses hostname allowlists, time/size limits and protection against private-network requests."),
req("IMP-01","Import without losing traceability or publishing unreviewed content.","Malformed rows, duplicate batches, changed pack units, spreadsheet formulas and network failures produce safe errors. Re-running a batch creates no duplicate SKU or stock receipt."),
callout("AI assistance","AI may suggest mappings, draft original copy and flag anomalies. A named reviewer approves factual specifications, medical claims, rights and classification; AI output is not evidence.")]),

section("media","Image optimisation and R2 storage","04 / Admin, product data and operations",
"Optimise images once during admin upload and serve prepared variants. Keep public product media physically separate from private business and personal evidence.",[
diagram("media"),
table(["Item","Proposed policy"],[
["Upload","Authenticated, role-authorised upload intent with a generated object key; private quarantine destination, bounded expiry and final server verification. Do not trust file extension alone."],
["Validation","Proposed image limit 15MB and 40 megapixels; inspect magic bytes, decode safely, remove unnecessary metadata and reject executable/SVG uploads at launch. Malware-scan document types before release."],
["Variants","Sharp generates 320, 640 and 1280px widths without upscaling; WebP plus JPEG/PNG fallback as needed. Preserve relevant product markings and colour accuracy; retain permitted originals privately."],
["Public delivery","Content-addressed filenames under media.<domain>, long immutable caching and explicit dimensions/srcset. Approved assets only; removal/restriction includes cache invalidation."],
["Private files","Separate bucket with no public domain; access only after resource/role checks through short-lived signed access. Default URL lifetime five minutes; log access safely."]],[.25,.75]),
p("Use a custom R2 domain for production public caching; the r2.dev endpoint is for development, not the delivery design. Configure CORS narrowly for upload use cases and scope bucket credentials by service. R2 internet egress is free, but storage and operations still have limits and overages. [CF01,CF02]"),
req("MED-01","Keep processing isolated from customer traffic.","Large/malformed uploads cannot exhaust the API; a worker crash is retried safely; private evidence never receives a public URL; approved thumbnails retain readable product labels."),
p("**Resource control.** Start one image job at a time on KVM 4, cap worker memory and measure CPU impact. Use prepared srcset/custom image loading so Next.js does not re-transform every catalogue request.")],["IM01","CF01","CF02"]),
]

SECTIONS += [
section("deployment","Environments, deployment and release safety","09 / Hosting and operations",
"Run a production build on Hostinger KVM with separate services, private networks and repeatable deployments. Keep development tooling off the public production surface.",[
table(["Area","Specification"],[
["Environment separation","Local development and sandbox integration; private staging with synthetic data and separate secrets/buckets/provider accounts; production with restricted access. Staging is authenticated and noindex."],
["Containers / proxy","Docker Compose for Nginx, Next.js, API, worker and PostgreSQL. Serve the compiled admin statically. Publish only HTTPS/HTTP redirect ports; PostgreSQL and service ports stay private."],
["TLS / DNS","Cloudflare Registrar/DNS; validated TLS between browser, proxy and origin. Restrict trusted proxy sources/headers. Bot rules must not break approved payments, callbacks or search crawlers."],
["Build pipeline","Type/lint checks, focused domain/integration tests, production build, dependency/secret checks and artefact creation. Build in CI or a controlled build host, not during peak production traffic."],
["Deploy / migrate","Back up and validate an expand/contract migration; deploy immutable images, run readiness checks and smoke tests, then route traffic. Stop on failed health or migration validation."],
["Rollback","Keep the previous compatible images/configuration. Roll back application code when schema-compatible; data/schema rollback uses a rehearsed recovery plan, not an untested down migration."]],[.27,.73]),
p("Keep Next.js cache persistence and invalidation explicit on the single instance; multi-instance coordination is a later scaling task. Source maps, environment values and diagnostics must not expose secrets. A feature flag can disable an integration/category without bypassing its server-side checks. [NX01]"),
p("Production credentials are delivered through controlled server/CI secret stores, never committed in .env files. Use separate database roles for normal application work, jobs and migrations; ordinary runtime roles cannot alter the schema or read backup secrets."),
req("DEP-01","Make release and rollback reproducible.","Deploy to staging from a clean artefact, apply the migration, complete order/refund/restore smoke checks and demonstrate rollback to the prior compatible application. Record image digests and approver."),
callout("Release authority","This specification authorises no actual deployment. Live release later requires the owner's agreed readiness process and the existing product, payment, stock and operating gates.")],["NX01"]),

section("operations","Backups, monitoring and maintenance","09 / Hosting and operations",
"A single VPS is a shared failure point. The operating design needs independent recovery and someone responsible for responding to alerts.",[
table(["Control","Proposed target / implementation"],[
["Database recovery","RPO <=15 minutes using continuous WAL archiving plus valid base backups; daily logical export as an additional recovery option. Verify backups, archive freshness and encrypted offsite storage. [DB03]"],
["Recovery time","RTO <=4 hours from incident declaration within agreed response coverage. Rehearse restoration to a clean server; no 24/7 response SLA is assumed without staffing."],
["Retention / independence","Proposed 14 days PITR and 30 daily exports, subject to data/volume review. Separate backup credentials/account from application write access; test object/document consistency."],
["Availability / alerts","Initial service objective 99.5% monthly including planned maintenance. External uptime checks, error rate, p95 latency, CPU/RAM/disk, DB connections, queue age and payment discrepancy alerts."],
["Daily / weekly","Check held orders, failed jobs, backup freshness and payment discrepancies daily; review access, dependencies, stock/finance reconciliation and performance trends weekly."],
["Monthly / incident","Restore drill, patch review, credential/access review, capacity/cost and policy checks. Maintain incident timeline, impact, recovery actions and prevention follow-up."]],[.27,.73]),
p("Alert on an unarchived WAL gap, failing backup, low disk, sustained queue delay or repeated payment mismatch. A successful backup upload is not proof of a usable restore. Verify encryption keys, database consistency, private documents, application secrets and provider reconciliation during recovery."),
p("Use structured request/job logs with correlation IDs and redaction; avoid expensive always-on telemetry platforms at launch. Keep an independent external monitor: a monitor on the failed VPS cannot reliably report its own outage. Log retention and costs follow the privacy/service budget."),
req("OPS-01","Demonstrate recovery against the proposed objectives.","Restore a timed backup in a separate environment, replay to a chosen recovery point, check orders/stock/documents and reconcile provider transactions after the cutoff. Record achieved RPO/RTO and any gaps."),
callout("Ownership","Name an operations owner and backup responder before launch. If coverage or storage budget cannot meet these objectives, revise and record the service target before claiming it.")],["DB03"]),

section("cost-controls","Resource plan and cost controls","09 / Hosting and operations",
"The proposal's sub-US$100 target applies to infrastructure and selected tools. It is conditional on measured usage, lean service choices and a single-server launch topology.",[
table(["Service group","Initial allocation / safeguard"],[
["KVM 4","Storefront, static admin, API, worker and private database. Proposed memory planning: PostgreSQL 4GB, Next.js 2GB, API 2GB, worker 1.5GB, remaining RAM for OS/proxy/cache/headroom. Tune, do not treat allocations as benchmarks."],
["CPU / job control","Prioritise customer/API/database work; limit media/import concurrency and run heavy jobs off-peak. CI builds and load generators should not compete with production."],
["PostgreSQL / disk","Monitor WAL growth, autovacuum, query latency and disk. Use migration/connection budgets and archive cleanup only after retention/recovery checks."],
["R2 / images","Prepared variants, lifecycle rules for temporary imports/uploads and CDN caching. Measure aggregate storage and Class A/B operations; no paid on-demand transform service is assumed."],
["Email / tools","Meter email volume, contact counts and provider limits. One mailbox and a limited marketing pilot in the lean model; richer automation/connectors may need extra budget."],
["Scaling triggers","Repeated latency/resource breaches, restore window growth, job backlog or availability requirements trigger optimisation and then a costed resize/separate database/search service."]],[.27,.73]),
p("The existing illustrative model is $50.92/month initially and $69.67 at VPS renewal for services; $60.92/$79.67 including a $10 reserve before tax. Adding the model's 20% service-tax sensitivity gives $71.10/$93.60. GBP1=USD1.25 and 100GB R2 are assumptions; exact provider checkout, tax, backup and mail plans remain unconfirmed."),
p("Source of these figures: docs/models/CLIENT_PROPOSAL_MODEL.json and the dated client proposal. Do not count prepaid VPS/domain costs twice. Increased usage, redundant hosting, CI charges, additional staff seats, maintenance labour, development AI tools, payments and advertising are outside a guaranteed cap."),
req("COST-01","Review cost and capacity together.","Dashboard/export reconciles monthly service invoices with storage, requests, messages and resource metrics. Alerts at 70% and 90% of agreed budgets prompt review; they do not silently disable essential order or recovery functions."),
callout("Reliability trade-off","The lean single-VPS model does not provide high availability. A requirement for failover, 24/7 support or substantially higher traffic must be separately designed and funded.")],["T01","CF02"]),

section("roadmap","Feature phases and release boundaries","10 / Delivery and verification",
"Use the agreed four-phase structure while treating external approvals and operational readiness as parallel workstreams.",[
table(["Phase / assumed release","Proposed release package"],[
["P1 / 10 December 2026","Customer/staff identity and MFA; reviewed catalogue/import/media; responsive discovery/product/cart/checkout; professional checks; stock/traceability/reservations; approved payments/refunds; manual dispatch/tracking; financial documents, service email, policies, eligible feed, SEO foundation, backup/restore and staff training."],
["P2 / 20 January 2027","Purchase orders/receipt discrepancies; low stock/expiry and support queues; richer imports/evidence reminders; one selected carrier and one accounting workflow; operational/reconciliation reporting."],
["P3 / 2 March 2027","Saved lists/reorder; organisations/roles; professional quotes/approved pricing; reviewed lifecycle email and campaign/content workflows; funnel, margin and cohort reporting."],
["P4 / 12 April 2027","Country-aware catalogue, language/tax/shipping configuration; first-country dossier/test lane; performance/security/recovery hardening and full handover. Country goes live only after its gates pass."]],[.28,.72]),
h("The 25-day first phase"),
p("Assumed kickoff 15 November is Day 0. Days 1-3 prove the architecture/auth/payment slice and freeze the launch data/backlog. Days 4-10 build catalogue/admin/stock/discovery. Days 11-17 complete checkout/payment/fulfilment and communications. Days 18-24 validate security, accessibility, realistic load, restore and staff operation. Day 25 is a controlled selling release."),
p("Later phases each add one calendar month plus 10 days to the preceding milestone. The assumed dates are not a booked schedule or a guarantee of provider approval. The first 25 days are aggressive; validate throughput early and prioritise a bounded reviewed assortment."),
req("REL-01","Keep phase acceptance observable.","Each release has an approved backlog, representative fixtures, passed acceptance evidence, operator readiness and a deploy/rollback record. Missing legal/provider readiness cannot be marked complete by a feature flag."),
callout("Full scope and later options","Medicine activation, advanced warehousing, trade credit, loyalty/subscriptions and additional countries/connectors need separate decisions. Full-range ambition is retained; these are not automatically included in a fixed release package.")]),

section("acceptance","Verification matrix and definition of done","10 / Delivery and verification",
"Use a small set of meaningful end-to-end and invariant checks, supported by focused unit/integration tests. A polished screen alone is not release evidence.",[
table(["Test family","Required evidence"],[
["Identity / access","AUTH-01/02/03 and ACL-01: verify/reset, MFA enrollment/challenge/recovery, session expiry/revocation, CSRF, cross-user/organisation IDs and customer-to-admin boundaries."],
["Catalogue / media","CAT-01/02, REG-01, IMP-01 and MED-01: correct pack, restricted territory/buyer, evidence changes, draft imports, malicious uploads and private/public file isolation."],
["Transaction correctness","CHK-01, DATA-02, INV-01, ORD-01, PAY-01 and RET-01: last-unit races, duplicate/late events, timeouts, partial fulfilment/refund, recall and crash recovery."],
["Browser / accessibility","Playwright Chrome/Firefox/WebKit and real-device Safari/Android spot checks; responsive templates, keyboard/screen reader, errors, zoom, focus and third-party payment handoffs."],
["Quality / operations","SEO-01/02, PERF-01, SEC-01, PRIV-01, DEP-01 and OPS-01: reproducible audits, load/security checks, consent network assertions, migration, rollback and restore."],
["Business walkthrough","Owner, warehouse/support and finance complete receipt -> approval -> sale -> dispatch -> return/refund, reconcile reports and demonstrate access removal."]],[.28,.72]),
p("Use Vitest for pure eligibility/tax/state rules and integration tests against real disposable PostgreSQL for locks/constraints. Use provider sandboxes for contracts and selected authorised live smoke checks at release. Mocking every payment/database response cannot prove concurrency or provider correctness. [QA01]"),
p("No percentage-of-lines coverage target substitutes for risk coverage. Require all agreed critical paths and invalid transitions to pass, no open launch-blocking defects, reviewed dependency findings and documented recovery evidence. Re-run only the affected tests plus relevant critical-path regression after a fix."),
req("QA-01","Attach evidence to each release requirement.","The requirement register records owner, phase, test/evidence link, status and exceptions. Every P1 requirement is passed or explicitly rescheduled with the release impact recorded; legal permission is never waived by a technical exception."),
callout("Deliverable pack","Source/lockfile, OpenAPI, schema/migrations, environment template without secrets, deployment/rollback/restore runbooks, provider mappings, staff SOPs, licence inventory and acceptance reports.")],["QA01","QA02","A11Y01"]),

section("decisions","Decisions to confirm and implementation order","10 / Delivery and verification",
"The specification provides a concrete baseline. Resolve the remaining commercial and integration details before treating it as an accepted build contract.",[
table(["Decision / owner","Next evidence or action"],[
["Business owner","Legal entity/brand, launch GB/NI coverage, approved SKUs, supplier/content rights, stock/premises, tax/delivery policy, professional reviewer and support coverage."],
["Developer + owner","Accept NestJS/Fastify and the proposed library stack, auth realm separation, retention/session policies, integrations, quality targets and exact phase backlog."],
["Payment / finance owner","Actual medical catalogue approval; wallet setup; capture/refund behaviour; settlement/reconciliation files, invoice numbering and tax-rounding policy."],
["Operations / security owner","Backup destination/retention, on-call coverage, RPO/RTO feasibility, secret custody, incident process and staff permissions."],
["Marketing / privacy owner","Public-content review, historic Google notices, feed eligibility, tracking permissions, mail provider and permitted journeys; legacy-data reuse remains a separate assessment."],
["European expansion owner","First country, product/economic-operator route, local language/terms/tax, returns/service and country-release evidence."]],[.30,.70]),
h("Recommended first implementation slice"),
p("One approved unrestricted sample product flows through draft import, review, image processing, stock receipt, public product page, consumer sign-in/guest basket, quote, sandbox payment, verified event, dispatch and refund. In parallel, test staff invitation/MFA, direct API permissions and a database restore. This slice validates the high-risk dependencies together."),
p("Use roughly seven AI support roles for frontend, authorised data intake, analysis, backend guidance, database design, QA/security and release review. Humans retain architecture, integration and approval responsibility. Track actual effort and cumulative input/output tokens; the proposal's estimates are not proof of delivery capacity."),
req("READY-01","Replace assumptions with evidence early.","By the first scope review, record the tested stack, provider sandbox outcome, auth policy results, measured throughput, open dependencies and revised backlog. Maintain the decision log rather than silently changing architecture."),
callout("Document ownership","Prepared for Shishir Sabbir's delivery of the new medical e-commerce platform. Version 1.0, 9 November 2026. No development fee is included; this is the technical design and acceptance baseline.")]),
]



SECTIONS += [
section("seo-targets","SEO, accessibility and quality targets","07 / Search visibility and performance",
"A score is useful only with a defined test. These are proposed release targets, separate from search ranking, acquired traffic and Merchant Center approval.",[
diagram("scores"),
table(["Measure","Target / acceptance scope"],[
["Lighthouse SEO","100/100 on every audited indexable public template: home, category, product and guide. Fix failed applicable audits; account/checkout/admin pages are intentionally excluded from SEO scoring."],
["Lighthouse Performance","Median of five runs: >=90 mobile and >=95 desktop on the public templates. Checkout target >=85 mobile with real provider scripts; report third-party cost separately, do not hide it."],
["Accessibility / Best Practices","Aim for 100 in automated Lighthouse categories; no serious/critical axe findings on key journeys. Manual WCAG 2.2 AA checks are required; an automated score is not conformance proof."],
["Core Web Vitals - field","At the 75th percentile, separately on mobile/desktop: LCP <=2.5s, INP <=200ms and CLS <=0.1. Use real traffic over a rolling 28-day view where sufficient data exists. [SEO01]"],
["Crawl / structured data","No broken internal links on the release crawl; approved canonical pages in the sitemap; zero required-field errors for applicable product structured data. Review warnings explicitly."]],[.29,.71]),
p("Pin the Lighthouse/Chrome versions and configuration in CI. Use a production build, a fixed UK-region runner, fixed mobile/desktop profiles, representative product content and a controlled cache state. Record URLs, build SHA, device, throttling, consent state and all five results; do not select the best score. Run both consent-rejected and consent-accepted performance checks."),
p("Lighthouse's SEO category tests a limited set of technical checks; structured data also needs separate validation. Google does not publish a single overall SEO/ranking score. Good Core Web Vitals, original useful content and correct indexing support quality but do not guarantee rankings or rich results. [SEO02-SEO04]"),
req("SEO-01","Deliver reproducible quality evidence.","Attach release audit reports and manual keyboard/screen-reader findings for the template matrix. Field metrics without enough samples are marked unavailable, not assigned a fabricated passing value.")],["SEO01","SEO02","SEO03","SEO04","A11Y01"]),

section("seo-implementation","SEO implementation and indexing rules","07 / Search visibility and performance",
"Generate useful, crawlable public HTML and accurate metadata from the approved catalogue. Protect private areas with authentication rather than relying on robots directives.",[
table(["Area","Technical specification"],[
["Rendering / metadata","Server-render product/category essentials; unique useful titles/descriptions, one clear page heading, breadcrumbs, canonical URL, Open Graph data and accessible descriptive images."],
["Product data","JSON-LD Product/Offer and eligible variants, real identifiers, currency, current visible price/stock and truthful review data only. Escape JSON safely; validate with Google's rich-results tools. [SEO05]"],
["Canonical / URLs","Stable lowercase slugs with persistent IDs behind them; 301 redirects for legitimate slug changes. Paginated category pages remain distinct; do not canonical every page to page one."],
["Facets / search","Internal search and arbitrary filter combinations are noindex and absent from sitemaps. Curated category landing pages may be indexable after content review; control crawlable facet links."],
["Sitemaps / robots","Generate only approved indexable 200-status canonical URLs with honest last-modified dates. Keep noindex pages crawlable when the crawler must see that directive; robots.txt blocking is not a deletion method. [SEO06-SEO07]"],
["Unavailable / removal","Temporary stock-out: useful page and accurate availability. Permanent removal: appropriate 404/410 or a genuine relevant replacement redirect, not a blanket redirect to the homepage."],
["Europe / monitoring","P4 reciprocal hreflang for live equivalent local pages; local titles/terms/prices and country eligibility. Use Search Console and Bing Webmaster Tools to monitor index coverage and errors."]],[.28,.72]),
p("Public content follows editorial review for intended use, factual specifications and rights. Do not create bulk AI pages with unsupported clinical claims. Display actual seller/service identity and clear delivery/returns information; avoid unearned accreditations, fake review markup or hidden text."),
req("SEO-02","Keep the HTML, structured data, feeds and checkout consistent.","A catalogue update changes all approved public representations; a restriction removal purges affected discovery/cache entries. Test canonical, pagination, noindex, sitemap and product-schema cases."),
callout("Noindex is not security","Accounts, staff tools, documents and evidence require access control and no-store. A private route must not become readable simply because a crawler ignores a directive.")],["SEO05","SEO06","SEO07","S01","S03"]),

section("merchant","Merchant Center and campaign data","07 / Search visibility and performance",
"The feed is a reviewed channel projection, not an automatic export of every SKU in the database.",[
table(["Component","Implementation contract"],[
["Eligibility rules","Product+market+channel approval, provider/operating evidence where relevant, active stock/public landing page and reviewed claims. Missing evidence defaults to excluded."],
["Feed fields","Stable product/variant ID, title, description, canonical link, approved image, availability, price/currency, brand and actual identifiers. Shipping/returns/tax presentation matches the target country."],
["Publication pipeline","Build from a consistent approved revision; validate required values and link/image access; publish atomically and record version/time. Feed IDs remain stable across updates."],
["Diagnostics","Import or record disapprovals, group root causes and assign owners. Exclude affected offers promptly; resubmit only after correction. Retain the rationale and policy check date."],
["Ads / measurement","Separate paid-channel approval from free-listing eligibility. Send purchase events only under the relevant consent/policy rules, with deduplication and no sensitive health audience data."],
["Operational cadence","Review account alerts daily during launch and at least weekly thereafter. Recheck price/stock mismatches, destination changes and product-policy updates."]],[.26,.74]),
p("Under the checked UK Merchant Center policy, prescription/behind-the-counter drug listings are not allowed; OTC listing has pharmacy/Google certification conditions. Website/account review extends beyond a submitted feed. Do not assume a legally sellable product is eligible for all Google surfaces. [M01]"),
p("The owners must supply the actual previous notices and any relevant ownership/account relationships before onboarding. Truthful identity, remediation and appeal are required; a new brand/domain is not an enforcement workaround. The software stores channel decisions but cannot guarantee account acceptance. [M04]"),
req("MKT-01","Never export a product solely because it is sellable on-site.","A test catalogue with permitted, restricted, suspended and unreviewed items produces only the correct market/channel subset; a stale cache/feed cannot make an excluded SKU orderable."),
callout("P1 / later","P1: eligible feed generation, validation and operator-managed onboarding/diagnostics. P2-P3: richer diagnostics automation and campaign reporting after account/provider access is agreed.")],["M01","M03","M04","M05"]),

section("performance","Performance budgets and capacity tests","07 / Search visibility and performance",
"The earlier 10,000 daily-traffic figure is a workload assumption. Server sizing depends on requests, peak distribution, cache hits, database work and background jobs.",[
table(["Budget / test","Proposed target and method"],[
["Public transfer budget","Initial compressed first-party JS <=200KB on home/category/product; initial above-fold transfer <=1MB. Track SDKs separately and include them in page timing."],
["API latency","At the target load: p95 catalogue/search reads <=300ms; ordinary writes <=500ms excluding external-provider wait. Measure complete user-facing latency separately."],
["Error / correctness","Unexpected 5xx <0.5% during steady load; no oversell, duplicate charge or cross-user cache response. Expected rule rejections are tracked separately."],
["Synthetic fixture","20,000 SKUs, representative variants/evidence, 100,000 historic orders and 20 staff sessions. This is a test dataset, not a confirmed launch catalogue."],
["Initial load profile","25 mixed dynamic HTTP requests/second for 30min; 50/second for 5min burst; separate 2 checkout attempts/second with sandbox/mocked provider responses. Include one import/image worker."],
["Resource guardrails","No sustained swapping; investigate sustained CPU >70%, growing queue lag, connection pressure or disk >70%. Preserve headroom and compare warm/cold cache runs."]],[.29,.71]),
p("Illustrative demand model: 10,000 visitors/day x four page views x two dynamic requests = 80,000 requests/day. Over 12 busy hours this averages 1.85 requests/second; a 10x peak is about 18.5/second. Bots, prefetches, assets, staff and callbacks add work. The proposed load test is a starting scenario, not a traffic-capacity guarantee."),
p("Optimise with server rendering, cached approved public reads, explicit cache keys/invalidation, responsive prepared images, minimal client bundles, database indexes and bounded workers. Exclude personal content from shared caches. Do not weaken security, stock correctness or product gating to meet a score."),
req("PERF-01","Validate the combined KVM workload before production.","Record k6/Lighthouse traces, database query plans, CPU/RAM/disk/connection use and worker lag. If targets fail, optimise or resize and re-cost; do not claim 10k/day capacity from the VPS specification alone.")],["NX01","QA02","SEO03"]),

section("security","Application security and threat controls","08 / Security, privacy and communications",
"Prioritise the risks that could expose customers, alter regulated products or corrupt payments and stock.",[
table(["Threat","Required controls / validation"],[
["Account takeover","Verified identity lifecycle, rate limits, staff MFA, session expiry/revocation and protected recovery. Test account enumeration, stolen customer session and role escalation."],
["IDOR / data exposure","Ownership and capability checks on every object/download/export; explicit public DTOs; private storage; no secrets in client bundles or public source maps."],
["XSS / CSRF / injection","Context-safe rendering, sanitised permitted rich text, parameterised database access, server validation and CSRF/origin checks. Start CSP in reporting, enforce a tested provider-compatible policy before release."],
["Uploads / SSRF","File signature/size/pixel checks, private quarantine, document malware scanning, generated keys and allowlisted bounded remote fetches. Block private-network redirects/addresses."],
["Payment / stock abuse","Idempotency, signed verified callbacks, state guards, server totals, database locks and reconciliation. Rate-limit reservation abuse and release abandoned holds."],
["Infrastructure / supply chain","Private database, least-privilege service users, patched supported images, protected secrets, dependency/secret scanning and reviewed builds. No production credentials in AI prompts."],
["Audit / incident response","Structured redacted logs, actor/action history, alerts and an incident runbook. Preserve relevant evidence and involve the business privacy/compliance owner promptly."]],[.28,.72]),
p("Set HTTPS, tested security headers, frame restrictions, safe content types and a strict referrer policy appropriate to payment redirects. Hostname/proxy trust is allowlisted; do not trust arbitrary X-Forwarded-* values. A public health endpoint reveals only basic status; detailed diagnostics require private access."),
p("Treat supplier files, product text and AI suggestions as data rather than executable instructions. Development assistants receive scoped synthetic/redacted context. Every migration, permission change and payment transition receives human review before production."),
req("SEC-01","Release with no unresolved critical/high exploitable findings in the agreed assessment.","Run dependency/static checks and focused manual tests of auth, access, uploads, webhooks and caching. Document ownership and resolution for findings; a scanner pass alone is not a security certification.")],["OW01","OW02","OW03"]),

section("privacy","Privacy, retention and consent design","08 / Security, privacy and communications",
"Minimise the data the store needs. Ordinary medical-supply purchases should not automatically collect a diagnosis, prescription or other clinical history.",[
table(["Data group","Handling and proposed retention approach"],[
["Accounts / contact","Collect necessary identity/contact data and preferences. Retain according to the operator's documented purpose; offer correction, export and eligible deletion."],
["Orders / finance / traceability","Keep the required legal/accounting and product-safety records under a reviewed retention schedule. Separate account deletion from lawful historical retention."],
["Professional evidence","Collect only what the actual eligibility decision requires; restrict reviewer access and schedule deletion/re-review. Do not expose files to marketing or ordinary support roles."],
["Sessions / operational logs","Expire sessions automatically. Proposed routine request-log retention 30 days and security/audit retention 12 months, subject to minimisation and operator review; redact tokens and content."],
["Consent / suppression","Version purpose, channel, wording, basis, source, timestamp and withdrawal. Keep the minimum suppression proof needed to honour opt-outs; recheck at send time."],
["Analytics / third parties","Consent-aware event delivery, provider contracts and transfer assessment. Do not send names, emails, address details, prescriptions or sensitive health context to ad/analytics tools."]],[.28,.72]),
p("Identifiable health data requires an Article 6 basis plus an Article 9 condition and any applicable UK conditions. Avoid putting medical-document upload into the ordinary checkout. If a future approved medicines workflow needs sensitive evidence, scope it separately with retention, access, audit and appropriate impact assessment. [P03]"),
p("The initial tracking policy blocks non-essential advertising/behavioural analytics until valid consent; any later statistical-purpose exception requires a documented current-law assessment. Keep consent state separate from login and marketing subscription. Withdrawal stops future marketing and tracking as applicable. [P01,P04]"),
req("PRIV-01","Make consent and private-data controls observable.","Rejecting/withdrawing consent prevents the relevant network requests; a queued marketing job rechecks suppression; a privacy request can be fulfilled without deleting required recall/financial records."),
callout("Legacy data","No former Economed customer list, consent, reviews or professional verification is imported by default. Establish controller, rights, purpose and provenance before any migration.")],["P01","P03","P04"]),

section("communications","Email, CRM and product analytics","08 / Security, privacy and communications",
"Service communication is part of commerce reliability. Marketing and behaviour measurement add their own permission, eligibility and cost checks.",[
table(["Capability","Technical design / delivery phase"],[
["Service messages - P1","Verification/reset, order/payment status, dispatch, refund and safety notices. Versioned templates, durable queue, idempotent delivery and bounce/complaint handling."],
["Email infrastructure","Managed delivery provider; authenticate the sending domain with SPF/DKIM and deploy DMARC appropriately. Separate transactional and marketing reputation where supported; monitor failures."],
["Marketing - P2/P3","Reviewed welcome, replenishment and win-back workflows; preferences/suppression checked at send time, product/market eligibility enforced. Campaign editor/provider choice remains open."],
["CRM - P2","Order-linked support cases, assigned owner, safe notes, contact history and escalation. Avoid duplicating clinical information into general support notes."],
["Analytics - P1 foundation","Consent-aware view_item, add_to_cart, begin_checkout and purchase events; stable order/event IDs for deduplication and no personal/sensitive payloads. Internal order totals remain the financial truth."],
["Reporting - P3","Channel/funnel, net sales, refunds, gross margin, contribution and 30/60/90-day cohorts. Publish metric definitions and distinguish ad-attributed revenue from actual accounting."]],[.29,.71]),
p("Consent to marketing is not permission to use sensitive health information for personalised audiences. Review product identifiers/page paths before sending them to third-party analytics where they could reveal health interests. Use aggregate internal reporting when a safe external payload cannot be established. [M05,P03]"),
p("WhatsApp medical-product marketing is not a committed integration: current product/market policy restrictions must be assessed for each use case. SMS likewise needs permission, provider acceptance and a separate usage budget. The developer's personal WhatsApp contact in the proposal is unrelated to store marketing eligibility. [M06]"),
req("COM-01","Keep messages correct, lawful and recoverable.","A replayed order event does not send duplicate confirmations; an opted-out recipient is suppressed from marketing; mail failure creates an alert while order state remains intact.")],["P01","M05","M06","T12"]),
]

SECTIONS += [
section("data","Data model and relationships","05 / Database and transactional workflows",
"PostgreSQL stores the authoritative business records. Separate mutable working data from immutable evidence, order snapshots and movement/event history.",[
diagram("data"),
table(["Domain","Core entities"],[
["Identity","Library-owned customer/staff users, credentials and sessions; customer_profile, staff_permission, organisation, membership, professional_verification."],
["Catalogue","product, variant, category, attribute_value, manufacturer, supplier, evidence_revision, media_asset, product_market_rule, channel_rule."],
["Stock","stock_location, stock_lot/serial, stock_balance, stock_movement, reservation, purchase_order, receipt, quarantine and recall_case."],
["Commerce","basket/line, checkout_quote, order/line_snapshot, tax_snapshot, payment_attempt, provider_event, shipment/line, return/line, refund and financial_document."],
["Operations","outbox_event, job metadata, audit_event, consent_event, suppression, notification_delivery, support_case and integration_mapping."]],[.24,.76]),
p("Use stable opaque identifiers; public order references are separate from internal keys. Every tenant-like organisation relationship is explicit, although this remains a single retailer rather than a multi-vendor platform. Database IDs do not themselves authorise access."),
req("DATA-01","Preserve evidence for the entire transaction chain.","A paid order can be traced to its exact product/pack/tax snapshot, payment attempt, allocated lot, shipment and any return/refund or recall action."),
p("**Schema ownership.** Auth tables follow the pinned library/adapter schema. Business tables reference identities through an explicit boundary; auth upgrades and business migrations are tested together. This is a logical schema, not generated production DDL.")]),

section("integrity","Fields, constraints and indexing","05 / Database and transactional workflows",
"Correct constraints prevent classes of production failures that application validation alone cannot catch.",[
table(["Entity / concern","Required fields and invariants"],[
["Variant","Unique internal SKU; identifiers as strings; pack_size/order_multiple positive integers; unit, currency and tax configuration explicit. Product revision is versioned."],
["Money / order line","Store currency and integer minor-unit amounts, with decimal tax/rate calculations. Record net, tax, shipping/discount allocation and rounding policy. Never use binary floats for money."],
["Balance / reservation","Unique location+variant+lot balance; positive reservation quantity, expiry and state; no negative available/reserved amount. All competing stock changes use one transaction/lock convention."],
["Payment / refund","Unique provider+external transaction/event identifiers where available; total successful refunds cannot exceed captured amount less earlier refunds. Currency/amount mismatch creates a hold."],
["Versions / history","created_at/updated_at in UTC; revision or row_version for optimistic updates; immutable order/evidence snapshots and append-only movement/audit history."],
["Foreign keys / deletion","Restrict deletion of order-linked products, stock and financial records. Archive/deactivate where history is needed. Privacy erasure follows retention rules and may pseudonymise eligible fields."]],[.27,.73]),
p("Indexes: unique SKU and provider identifiers; category/market/publication lookups; GIN search vectors/trigrams; customer+created_at orders; order status+age queues; lot+expiry; reservation state+expires_at; provider_event processed_at; outbox state+next_attempt_at. Add indexes from real query plans, not every column."),
p("Proposed connection budget: API pool 10, worker pool 5 and separate short-lived migration/admin access, leaving PostgreSQL capacity for recovery. Tune against actual memory/concurrency. Use pagination, statement/lock timeouts, deterministic lock ordering and bounded transaction retries. [DB01-DB02]"),
req("DATA-02","Make invalid financial and stock state difficult to persist.","Constraint tests reject duplicate provider events, over-refunds, invalid pack amounts and conflicting stock writes. Representative EXPLAIN plans avoid full scans for the primary queues."),
callout("Migration discipline","Use reviewed, versioned migrations with expand/contract compatibility. Do not run destructive schema synchronisation at application startup. Rehearse migration and data backfill on a production-sized synthetic fixture.")],["DB01","DB02"]),

section("inventory","Owned stock, reservations and procurement","05 / Database and transactional workflows",
"Available stock reflects goods the retailer actually controls. Supplier availability, reserved stock and quarantined stock are separate quantities.",[
table(["Operation","Required state change"],[
["Receive","Match supplier receipt to item/pack and purchase reference; record usable quantity, lot/serial/expiry where applicable, location and landed-cost evidence. Unknown/damaged goods enter quarantine."],
["Reserve","Inside one short transaction, lock relevant balance rows in a deterministic order, check availability and create a reservation. Initial expiry target: 15 minutes, extended only by a controlled payment workflow."],
["Allocate / dispatch","Allocate traceable stock using the approved shelf-life rule; FEFO where relevant. Dispatch rechecks order release/payment and lot status, then posts a stock movement."],
["Expire / cancel","Atomically change active reservation to released/expired and restore availability once. Race payment success against expiry through the same locking/state rules."],
["Quarantine / recall","Remove affected lots from sale immediately; stop allocation/dispatch, identify open and delivered orders, and create a reviewer-owned incident queue."],
["Reconcile / purchase","P1 receipt/adjustment with reason and audit. P2 purchase orders, discrepancies, stock-count adjustments and replenishment suggestions using demand/lead-time inputs."]],[.25,.75]),
p("Define available = on_hand - reserved - quarantined, with all terms referring to non-overlapping quantities. A dispatched unit reduces on_hand and its reservation in the same logical operation. Returned goods enter inspection/quarantine and cannot become available merely because a refund succeeded."),
p("Use an append-only stock movement ledger and a transactionally updated balance for fast reads; reconcile them regularly. A late successful payment after reservation expiry triggers a fresh allocation attempt or an exception/refund workflow, never negative stock."),
req("INV-01","Prevent overselling and unsafe dispatch.","With one unit available, concurrent accepted reservations total at most one. Test payment/expiry races, lot quarantine during checkout, partial shipment and retrying the same receipt."),
callout("Scope constraint","Cold chain, controlled substances, installation and specialised handling require separately evidenced operating processes. Do not represent a generic stock field as a validated handling system.")],["DB01","DB02"]),

section("orders","Order state and failure handling","05 / Database and transactional workflows",
"Keep commercial order, payment, review and fulfilment states separate. A single 'completed' flag cannot describe partial shipment, review holds or refunds.",[
diagram("order-state"),
table(["State axis","Examples and guards"],[
["Commercial","draft -> placed -> accepted / cancelled / closed. Store the customer-accepted quote and policy versions; record cancellation reason and actor."],
["Payment","not_started, pending, authorised, captured, failed, partially_refunded, refunded, disputed. Provider-confirmed events drive transitions; no browser success flag."],
["Review","not_required, pending, approved, rejected, revoked. Resolve required product/buyer review before payment initiation in the P1 flow; dispatch still rechecks."],
["Fulfilment","unallocated, allocated, partially_dispatched, dispatched, returned. Shipment lines identify exact quantities/lots and cannot exceed ordered quantity."],
["Exception","amount_mismatch, payment_unknown, stock_lost, provider_rejected or delivery_blocked. Hold dispatch, assign an owner and display a safe customer status."]],[.27,.73]),
p("Commit order/reservation/outbox records atomically, then call the provider outside the database transaction. If the request times out, reconcile the same attempt before creating another charge. Status transitions use version/row locks and reject illegal regressions."),
req("ORD-01","Recover a partially completed checkout safely.","Simulate a process crash after order commit, after provider creation and after payment notification. Recovery produces one order/payment outcome and an explainable stock state."),
callout("Customer messaging","Show 'payment processing' when status is uncertain. A paid order may still need operational attention; never show 'dispatched' before staff/carrier evidence exists. Confirmation emails are idempotent events, not the source of truth.")]),

section("payments","Revolut, wallets and PayPal","05 / Database and transactional workflows",
"Use independent provider adapters behind one payment domain. Provider approval for the catalogue is a separate launch dependency from working integration code.",[
table(["Integration step","Required implementation"],[
["Create attempt","Check order eligibility/amount/currency, persist a unique attempt and provider request key, then create the provider order using server credentials. Store provider IDs and request outcome."],
["Customer interaction","Use supported Revolut checkout/wallet components and PayPal SDK flows. Verify domains and Apple Pay/Google Pay setup as required; show alternatives when a wallet is unavailable."],
["Webhook ingress","Capture required raw request bytes/headers before parsing; use the provider's documented signature/verification procedure and replay controls. Validate environment, merchant, order, amount and currency."],
["Durable processing","Persist a verified event/inbox record before acknowledging success; queue idempotent state changes. Invalid events are rejected; processing failures remain visible and retryable."],
["Duplicate / out of order","Deduplicate by stable provider event ID where available; otherwise use a documented composite/digest plus idempotent payment transitions. Re-fetch authoritative provider state when needed."],
["Reconciliation","Scheduled checks compare local pending/captured/refunded state with provider records and settlement reports. Unresolved discrepancies create finance work items."]],[.26,.74]),
p("Capture/authorisation behaviour is fixed per provider in the kickoff sandbox tests. P1 intends immediate capture only after all pre-payment checks pass; authorise-then-review is a separate operating design. A 'customer approved' PayPal event is not equivalent to successful capture. [PAY01-PAY03]"),
p("No raw card data is stored in our database, logs or browser analytics. Payment tokens/IDs are sensitive operational records. Refunds originate server-side, require finance permission and recent staff authentication, and remain pending until the provider confirms the outcome."),
req("PAY-01","Never charge or dispatch twice because of retries.","Test duplicate/delayed webhooks, forged signatures, wrong currency/amount, lost redirects, provider timeouts, repeated capture/refund calls and sandbox/live credential mix-ups."),
callout("Merchant onboarding","Revolut, wallets and PayPal remain required choices, subject to actual approval. PayPal's medical-device approval requirement and the operator's intended products must be resolved before launch. [T07]","gold")],["PAY01","PAY02","PAY03","T07"]),

section("returns","Shipping, returns, refunds and recalls","05 / Database and transactional workflows",
"Support the entire order lifecycle, including partial outcomes and safety incidents, with records that remain understandable to customers and staff.",[
table(["Workflow","Implementation contract"],[
["Dispatch","P1 manual carrier booking and tracking entry; validate allowed URL/carrier fields. Record package, shipment lines, quantities/lots, timestamp and actor; service email follows the event."],
["Partial delivery","Maintain per-line allocated/dispatched/returned quantities. Show remaining items and promised status; shipment totals cannot exceed order quantities."],
["Cancellation / return","Record request date, reason, item condition and relevant policy. Staff distinguish cancellation, defects, warranty and safety cases. Product hygiene rules are applied to actual circumstances, not as a blanket block."],
["Refund","Calculate refundable captured balance, shipping/tax allocation and credit note. Lock against simultaneous over-refund; use provider idempotency and reconcile unknown outcomes."],
["Returned stock","Receive into inspection/quarantine; record lot/serial where applicable. Only an authorised disposition may release stock, destroy it or return it to the supplier."],
["Recall","Select affected product/lot/serial, suspend sale/dispatch, identify customers/shipments, assign review and controlled notifications, then record contact/action completion."]],[.25,.75]),
p("Financial documents contain the legal seller details and immutable tax/order values. Allocate sequential legal document numbers transactionally according to the accountant-approved policy. Re-downloads use the existing document, not a newly numbered invoice."),
p("P2 adds the selected carrier/accounting integrations after provider mapping is agreed. External sync keeps local mapping IDs, job status and reconciliation; duplicate callbacks cannot create duplicate shipments or credits."),
req("RET-01","Reconcile physical goods and money independently.","A partial return/refund produces the correct credit and available balance, while inspected stock remains quarantined until released. A lot recall lists all affected dispatched orders and blocks pending ones."),
callout("Customer rights","Customer information and return/refund rules need operator-approved UK terms and destination review. Software enforces the approved workflow but does not decide whether a statutory remedy applies. [C01-C02]")],["C01","C02"]),

section("api","API conventions and endpoints","06 / Interfaces and integrations",
"Use a versioned REST contract with generated clients, explicit validation and consistent error codes. Auth-library routes remain at /api/auth; business endpoints use /api/v1.",[
table(["Route group / examples","Access and purpose"],[
["GET /catalog/products; /products/{id}","Public approved projection for the market; bounded filters and pagination. No supplier cost or private evidence."],
["POST /baskets; PATCH /baskets/{id}/lines","Customer or scoped guest capability; validate ownership, quantities and permitted product view."],
["POST /checkout/quotes; /orders","Server pricing/eligibility; order creation needs an idempotency key and accepted quote. No client-authoritative total."],
["POST /orders/{id}/payment-attempts","Owner/guest order capability, eligibility and attempt guards. Does not trust a posted paid=true value."],
["GET /me/orders; /me/documents/{id}","Authenticated ownership; signed download only after permission checks."],
["/admin/products; /reviews; /receipts; /shipments","Staff capability and resource checks, row-version protection, audit reason where required."],
["POST /admin/orders/{id}/refunds","Finance permission, fresh MFA-backed session, balance lock and provider idempotency."],
["POST /webhooks/revolut; /webhooks/paypal","Provider-verified ingress, raw-body handling and durable inbox; no browser-session CSRF mechanism."]],[.48,.52]),
p("Return JSON using stable IDs and ISO 8601 UTC timestamps. Money objects contain currency and integer minor units. Collections return data plus pagination; maximum limits are enforced. Use 400 for malformed input, 401 unauthenticated, 403 denied, 404 where hiding existence is appropriate, 409 conflicts, 422 rule failures and 429 throttling."),
p("Errors include code, safe message, optional fieldErrors and requestId; never stack traces or secrets. Idempotency records bind actor, route, key and request hash. Reusing a key with different input returns 409. Keep payment/business duplicate guards beyond the public key-retention window."),
req("API-01","Make integration behaviour predictable under retries.","Generated clients match OpenAPI; invalid/unknown writable fields are rejected; request replay returns the prior result, and cross-user idempotency keys cannot reveal data."),
callout("Contract review","Endpoint names here are proposed interfaces. Publish the exact OpenAPI schema after the integration spike; breaking changes require a migration/version plan.")]),

section("contracts","Example contracts and event envelopes","06 / Interfaces and integrations",
"Illustrative payloads expose the decisions needed by the UI. They are design examples, not responses from an existing application.",[
h("Checkout quote response"),
code('{\n  "quoteId": "quote_demo_01",\n  "currency": "GBP",\n  "marketId": "great-britain",\n  "subtotalNetMinor": 10000,\n  "productTaxMinor": 2000,\n  "shippingNetMinor": 500,\n  "shippingTaxMinor": 100,\n  "totalMinor": 12600,\n  "expiresAt": "2026-12-10T12:10:00Z",\n  "eligibility": {"canOrder": true, "reasons": []},\n  "revision": 4\n}'),
p("The currency/market and item snapshots are stored server-side. POST /orders submits quoteId, the accepted revision and delivery/contact references, with an Idempotency-Key header; the client cannot replace totalMinor. A revised quote requires renewed customer acceptance."),
h("Rule failure and internal event"),
code('{"code":"BUYER_VERIFICATION_REQUIRED",\n "message":"This item requires an approved professional account.",\n "requestId":"req_demo_01"}\n\n{"eventId":"evt_demo_01","type":"order.payment_captured",\n "schemaVersion":1,"aggregateId":"ord_demo_01",\n "occurredAt":"2026-12-10T12:04:10Z",\n "correlationId":"req_demo_01",\n "payload":{"paymentAttemptId":"pay_demo_01"}}'),
p("Events carry minimal identifiers; handlers fetch authorised current state. Customer addresses, medical evidence and raw provider secrets are not copied into every queue message. Schema versions allow old jobs to be processed during rolling application upgrades."),
req("API-02","Preserve invariants across contract boundaries.","For the example, 10000+2000+500+100 = 12600. Quote expiry/revision conflict and a replayed payment event produce safe, documented outcomes rather than a second transaction.")]),

section("jobs","Background jobs and integration contracts","06 / Interfaces and integrations",
"Use a durable outbox and bounded workers so a successful database transaction is not lost because an email, feed or provider call fails.",[
diagram("outbox"),
table(["Queue / integration","Retry and operational contract"],[
["Media / imports","Bound concurrency and payload size; idempotency by asset hash or import batch/row. Malformed data goes to review, not endless retry."],
["Email / documents","Idempotency by event+recipient+template version. Retry transient failures with backoff; process bounce/complaint webhooks and preserve suppression."],
["Feeds / cache","Coalesce product revision jobs; rebuild only approved projections. Verify version/current eligibility before publishing; takedowns receive priority."],
["Payments","Separate verified inbox and reconciliation jobs. Fetch provider truth after uncertainty; an exhausted retry creates a finance exception, never silent success."],
["Carrier / accounting","Versioned mapping, credential owner, timeout, idempotency strategy, sandbox fixtures, retry policy and manual fallback agreed for each connector."]],[.26,.74]),
p("pg-boss is proposed to reuse PostgreSQL rather than introduce Redis initially. Queue delivery does not make an external side effect exactly-once: handlers still need business idempotency and reconciliation. Use exponential backoff with jitter, a maximum attempt count and an operator-visible failed-job queue. [JB01]"),
p("Recommended initial service targets: transaction email queued within 60 seconds; payment reconciliation every five minutes for unresolved attempts; routine feed rebuild within 15 minutes. Takedown checks remain synchronous at the API and trigger urgent cache/feed work. These are targets to measure, not provider guarantees."),
req("JOB-01","Survive worker restarts and external outages.","Kill the worker after an external call but before acknowledgement; replay produces no duplicate refund, shipment, notification or import. Failed jobs have an owner, reason and safe replay path.")],["JB01"]),
]

ORDER = "scope architecture stack experience routes discovery product checkout customer auth-customer auth-staff sessions permissions admin catalogue imports media data integrity inventory orders payments returns api contracts jobs seo-targets seo-implementation merchant performance security privacy communications deployment operations cost-controls roadmap acceptance decisions".split()
assert len(SECTIONS) == len(ORDER)
SECTIONS.sort(key=lambda s: ORDER.index(s['id']))
