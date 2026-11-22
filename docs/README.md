# Medical ecommerce UK launch and European expansion

Research baseline: 7 November 2026. Library reorganized 16 November 2026; paths are relative to the repository root. See [development handoff](development/README.md) for the current workspace layout.

## Latest deliverable

The latest commercial addendum is the six-page [AI development cost explanation](../deliverables/pdf/UK_MEDICAL_ECOMMERCE_AI_TOKEN_PAYMENT_PROPOSAL.pdf), revision 5, 10 November 2026: **USD1,555.56 (approximately RMB10,379.99)** for a Qwen-led 25-day core build with at least ten planned AI workstreams and a USD0 developer fee. Modeled Qwen usage USD1,396.01 + additional usage allowance USD159.55 gives the total estimate. This is informational cost documentation, with no funding ask or payment request. The illustrative, unmeasured 525m-input/107m-output scenario separately costs USD5,835 for OpenAI chat-latest or USD4,240 for Claude Opus 5.5 at checked rates; cheaper alternatives are also shown. See [editable text](plans/UK_MEDICAL_ECOMMERCE_AI_TOKEN_PAYMENT_PROPOSAL.md), [inputs](models/AI_TOKEN_PAYMENT_MODEL.json), [calculated outputs](models/AI_TOKEN_PAYMENT_CALCULATED.json), [dated/scoped sources](registers/AI_TOKEN_PAYMENT_SOURCES.json) and [analysis](analysis/25_AI_TOKEN_PAYMENT_PROPOSAL.md). Rebuild with `python scripts/docs/build_ai_token_payment_proposal.py`. Actual usage and account availability remain unverified.

The latest deliverable is the [25-day development and launch plan](../deliverables/pdf/UK_MEDICAL_ECOMMERCE_25_DAY_DEVELOPMENT_PLAN.pdf): 17 pages covering a collaborative AI-assisted branding/design workshop on Day 1, a bounded asset pack, 20 launch feature groups, all 25 daily task cards, a 250-product intake and release checks. Page 2 is the one-page overview; the rest explains execution. The user reports 250 warehouse products; distinct SKU count, quantities and eligibility still need verification. The illustrative Day 0 remains 15 November, with development Days 1-25 on 16 November-10 December 2026. See the [editable text](plans/UK_MEDICAL_ECOMMERCE_25_DAY_DEVELOPMENT_PLAN.md), [feature register](registers/DAY_25_FEATURE_REGISTER.json), [daily task register](registers/DAY_25_DAILY_PLAN.json) and [scope notes](analysis/24_25_DAY_DEVELOPMENT_PLAN.md). Rebuild with `python scripts/docs/build_25_day_development_plan.py`; editable content is in `docs/content/development_25_day_content.py`. No actual brand artwork or store has been built by preparing this plan.

The [detailed technical specification PDF](../deliverables/pdf/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.pdf), issued 9 November 2026, has 47 pages, 39 sections and acceptance requirements, 11 architecture/workflow/interface illustrations, and 49 dated references. It defines the proposed storefront, admin, API, data model, authentication, payments/stock workflows, SEO/performance, hosting, recovery and delivery baseline. The [editable text](plans/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.md), [content source](content/technical_spec_content.py), [requirement register](registers/TECHNICAL_SPEC_REQUIREMENTS.json), [source register](registers/TECHNICAL_SPEC_SOURCES.json) and [page map](registers/TECHNICAL_SPEC_PAGE_MAP.json) accompany it. Rebuild with `python scripts/docs/build_technical_spec.py`, then render and visually verify. This is a proposed design, not an implemented or approved stack.

The [illustrated project proposal](../deliverables/pdf/UK_MEDICAL_ECOMMERCE_CLIENT_PROPOSAL.pdf), also issued 9 November 2026, remains the business-facing proposal. It has 20 pages, Shishir Sabbir's supplied portrait/contact details, four release phases, a conditional sub-USD100 platform budget and human-hour/AI-token estimates. No development fee appears, as requested. The assumed 15 November 2026 kickoff produces releases on 10 December 2026, 20 January 2027, 2 March 2027 and 12 April 2027; these are targets, not a booked schedule.

Rebuild with `python scripts/docs/build_client_proposal.py`. The [editable content](content/client_proposal_content.py), [calculation model](models/CLIENT_PROPOSAL_MODEL.json), [dated/scoped sources](registers/CLIENT_PROPOSAL_SOURCES.json) and [page map](registers/CLIENT_PROPOSAL_PAGE_MAP.json) accompany it. Only the launch roadmap is a one-page treatment, on page 13 of this proposal. The full document below remains the detailed supporting plan.

The [full project plan PDF](../deliverables/pdf/UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.pdf) has a [navigable HTML handbook](../deliverables/html/UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.html) and [Markdown text](plans/UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.md). It has 27 pages; its Day 25 launch roadmap is on page 19 and is also available as a [standalone launch roadmap](../deliverables/pdf/UK_MEDICAL_ECOMMERCE_25_DAY_ROADMAP.pdf).

The earlier whole-project one-page summary was based on an assistant misinterpretation and is superseded. The user wants detailed, self-explanatory documentation, with only the 25-day plan brief. The [launch scope and budget notes](analysis/23_DAY_25_LAUNCH_SCOPE_AND_BUDGET.md) retain acceptance gates, sources, exclusions and unapproved cost assumptions. This is documentation, not a deployed application or an agreed development quote.

Latest brief: [8 November developer/client clarification](../memory/BRIEF_2026-11-08.md). The user is the commissioned developer. This is a new non-dropshipping supplier, with Revolut/wallets and PayPal, no Stripe, and Next.js now hosted on Hostinger. Earlier Cloudflare frontend costs are historical. The workspace is prepared for development; application implementation has not started.

Business model confirmed: one retailer procures and holds its own stock and sells directly to customers. The owners declined the multi-vendor marketplace option. Supplier self-publication and marketplace payouts are outside the requested model.

Launch buyers confirmed: consumers and verified professional/business customers. Prescription-only medicines remain undecided; requirements and the operating decision are presented separately. The admin direction is regular React, with PostgreSQL behind an API.

Latest discussion deliverables: [UK medical ecommerce proposal draft](proposals/UK_MEDICAL_ECOMMERCE_PROPOSAL_2026-11-08.md) and [API framework and admin architecture recommendation](analysis/20_API_FRAMEWORK_AND_ADMIN_ARCHITECTURE.md). NestJS with Fastify is recommended, not selected by the user. The proposal includes dated legal/channel references and release dependencies; it is not a completed product-specific legal clearance or development quotation.

Marketing scope expanded on 8 November: [customer messaging and retention](analysis/21_CUSTOMER_MESSAGING_AND_RETENTION.md) and [proposal gap review](analysis/22_PROPOSAL_GAP_REVIEW.md) cover email, WhatsApp/SMS feasibility, lifecycle automation, CRM, consent, delivery and budget dependencies. Messaging providers and campaign activation remain open.

The planned business is a new medical ecommerce brand, initially selling in the UK and later across Europe. Praxisdienst is the operating and customer-experience benchmark. The user confirmed mixed UK and EU sourcing and a full product-range ambition. The brand, legal operating entity, budget and launch date remain undecided.

This repository is a planning library, not a declaration that products or activities are authorised. Verified requirements, competitor observations, recommendations and illustrative financial assumptions are identified separately. No suppliers, regulators or customers have been contacted.

## Start here

1. [Project memory](../memory/PROJECT_MEMORY.md) records confirmed context and boundaries.
2. [Decision log](../memory/DECISIONS.md) distinguishes user decisions from proposals.
3. [Executive analysis](analysis/01_EXECUTIVE_ANALYSIS.md) explains the proposed operating model.
4. [Selling parameter register](analysis/02_SELLING_PARAMETER_REGISTER.md) is the master coverage checklist.
5. [Research sources](research/SOURCES.md) records evidence and its limits.
6. [Launch plan and gates](analysis/15_LAUNCH_PLAN_AND_GATES.md) translates the analysis into work.

## Analysis library

| File | Covers |
|---|---|
| [03 Customer and market analysis](analysis/03_CUSTOMERS_AND_MARKET.md) | Buyer segments, purchasing behaviour, market-sizing method and validation |
| [04 Praxisdienst and competition](analysis/04_PRAXISDIENST_AND_COMPETITORS.md) | Observed benchmark features, UK service comparisons and differentiation |
| [05 Catalogue and category gates](analysis/05_CATALOGUE_AND_CATEGORY_GATES.md) | Broad taxonomy, product selection and category-specific prerequisites |
| [06 UK regulatory framework](analysis/06_UK_REGULATORY_FRAMEWORK.md) | GB/NI, devices, IVDs, PPE, chemicals, medicines and specialist products |
| [07 Suppliers and mixed sourcing](analysis/07_SUPPLIERS_AND_MIXED_SOURCING.md) | Supplier approval, UK/EU routes, imports, contracts and landed costs |
| [08 VAT pricing and economics](analysis/08_VAT_PRICING_AND_ECONOMICS.md) | VAT, contribution, acquisition economics, working capital and scenarios |
| [09 Fulfilment quality and support](analysis/09_FULFILMENT_QUALITY_AND_SUPPORT.md) | Stock, traceability, expiry, deliveries, recalls and service |
| [10 Consumer and commercial terms](analysis/10_CONSUMER_AND_COMMERCIAL_TERMS.md) | B2B/B2C, cancellation, defects, pricing and credit |
| [11 Store and product data requirements](analysis/11_STORE_AND_PRODUCT_DATA.md) | Product information, search, accounts, checkout and system requirements |
| [12 Marketing retention and measurement](analysis/12_MARKETING_RETENTION_AND_MEASUREMENT.md) | Channels, claims, privacy, repeat purchasing and KPIs |
| [13 Public sector and NHS sales](analysis/13_PUBLIC_SECTOR_AND_NHS.md) | Procurement routes, tenders, sustainability and evidence |
| [14 European expansion](analysis/14_EUROPEAN_EXPANSION.md) | Country gates, EU roles, VAT/customs, localisation and logistics |
| [15 Launch plan and gates](analysis/15_LAUNCH_PLAN_AND_GATES.md) | Workstreams, responsibilities, risk controls and release criteria |
| [16 Brand and governance](analysis/16_BRAND_AND_GOVERNANCE.md) | Naming, legal identity, insurance, teams and ownership of decisions |
| [17 Hosting architecture and costs](analysis/17_HOSTING_ARCHITECTURE_AND_COSTS.md) | Historical Cloudflare frontend scenarios; latest Hostinger direction noted |
| [18 Technical running cost budget](analysis/18_TECHNICAL_RUNNING_COST_BUDGET.md) | Prior cost envelope; revision required for latest hosting/payment requirements |
| [19 AI development token estimate](analysis/19_AI_DEVELOPMENT_TOKEN_ESTIMATE.md) | Initial UK build versus broader scope, module allowances, token accounting and calibration |
| [20 API framework and admin architecture](analysis/20_API_FRAMEWORK_AND_ADMIN_ARCHITECTURE.md) | NestJS/Fastify comparison, advanced React admin, transactional stock/payments and Hostinger deployment |
| [21 Customer messaging and retention](analysis/21_CUSTOMER_MESSAGING_AND_RETENTION.md) | Email, WhatsApp/SMS feasibility, lifecycle journeys, consent, delivery, CRM and cost drivers |
| [22 Proposal gap review](analysis/22_PROPOSAL_GAP_REVIEW.md) | Missing versus partial scope, launch priorities, optional features and quote/handover dependencies |
| [23 Day 25 launch scope and budget](analysis/23_DAY_25_LAUNCH_SCOPE_AND_BUDGET.md) | First selling release, 25-day plan, illustrative development/technology budget and one-page source map |
| [24 Collaborative 25-day development plan](analysis/24_25_DAY_DEVELOPMENT_PLAN.md) | Workshop, reported 250-product intake, daily implementation tasks and release checks |
| [25 AI cost explanation](analysis/25_AI_TOKEN_PAYMENT_PROPOSAL.md) | Current cost-only presentation, illustrative model and historical revision context |

## Reusable working tools

- [Supplier qualification form](templates/SUPPLIER_QUALIFICATION.md)
- [SKU approval and product-data form](templates/SKU_APPROVAL.md)
- [Competitor basket specification](templates/COMPETITOR_BASKET.md)
- [Customer interview guide](templates/CUSTOMER_INTERVIEW.md)
- [Country launch dossier](templates/COUNTRY_LAUNCH_DOSSIER.md)
- [Illustrative model inputs](models/unit_economics_inputs.json) and [calculator](../scripts/models/calculate_economics.py)
- [Day 25 budget inputs](models/launch_25_day_budget.json), [calculated outputs](models/DAY_25_BUDGET_OUTPUT.json) and [brief generator](../scripts/archive/build_launch_brief.py)

Rebuild the current full PDF, HTML, Markdown and standalone Day 25 extract with `python scripts/docs/build_project_plan.py`. Editable content is in [docs/content/project_plan_content.py](content/project_plan_content.py); [page mapping](registers/PROJECT_PLAN_PAGE_MAP.json) records section locations. Render and visually review PDFs after content changes.

The previous `scripts/archive/build_launch_brief.py` and `docs/archive/launch-brief.json` belong to the historical whole-project one-sheet and should not be used as the current document generator.

Run the financial illustration with Python 3:

    python scripts/models/calculate_economics.py

The generated [scenario report](models/UNIT_ECONOMICS_OUTPUT.md) uses assumed inputs, not supplier quotes or a revenue forecast.

## Updating this library

Read [AGENTS.md](../AGENTS.md), then the memory files. Recheck laws and competitor terms before implementation. Add evidence links and dates when changing factual claims. Record accepted choices in the decision log; leave unapproved recommendations labelled as proposals. Do not replace the full-catalogue objective with a narrower permanent scope.

Open commercial and operational questions are tracked in [OPEN_QUESTIONS.md](../memory/OPEN_QUESTIONS.md). Quantitative market sizing, matched-SKU competitive pricing and supplier economics need further evidence; those gaps are explicit rather than filled with invented numbers.
