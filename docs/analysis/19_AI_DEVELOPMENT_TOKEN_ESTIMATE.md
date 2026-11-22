# AI assisted development token estimate

Latest revision 10 November 2026: USD1,555.56 AI funding, USD0 developer fee, Qwen mostly and ten planned workstreams supersede the earlier USD2,736/eight-role funding request. analysis/25 and the payment model now show a deliberately intensive, unmeasured 500m input/100m output scenario and current scoped API rates. This is materially higher than historical token ranges below; neither old ranges nor agent count validate the new consumption assumption. The USD4k-6k examples apply to selected premium API configurations; cheaper alternatives are shown. Replace assumptions with pilot evidence at Day 5. No API spending occurred.

Historical first update 10 November 2026, superseded later the same day: the original request was USD2,736 for eight planned AI roles with USD0 developer fee. Its 8 x 25 x USD13.68 calculation was a top-down allocation, not a token forecast. The current model/analysis now contain the revised USD1,555.56 request and sourced-rate scenarios described above.

Latest 9 November proposal: the user requested hours and millions of tokens across four releases, with approximately seven supporting AI roles, and explicitly excluded development fees. The new scope-specific model is [CLIENT_PROPOSAL_MODEL.json](../models/CLIENT_PROPOSAL_MODEL.json): 680-880 human hours and 70-150m cumulative input+output tokens; working examples 760 hours and 110m tokens (95m input/15m output). Phase ranges are 160-200h/25-65m; 180-230h/15-30m; 180-230h/15-30m; 160-220h/15-25m. These remain unmeasured analyst estimates; they do not validate a seven-agent speedup, subscription entitlement or actual capacity. The original estimates below remain historical context. Calibrate after the first accepted slice.

Update 8 November 2026: the user clarified their commissioned-developer role, non-dropshipping business model, Revolut/wallets/PayPal requirements and Hostinger frontend. Prescription/clinical order approval and legacy Google policy issues need further scoping. The unmeasured token ranges below remain historical planning illustrations and should be recalibrated after that discussion, not treated as a commitment for every newly clarified workflow.

Baseline: 7 November 2026. This is an engineering planning estimate for a person working alongside coding models. It is not measured project usage, a provider benchmark, a fixed-price quote or a promise of completion. No application code exists here yet, and no model/provider or backend commerce stack is selected.

## What to budget

For an initial production UK storefront, admin and API, use a provisional total allowance around 50 million tokens, with a planning range of 25–65 million including rework contingency. A basic MVP using established commerce components could be 5–12 million. A much broader implementation approaching the project's multi-market, professional procurement and regulated-category workflows could be 60–150 million or more over successive releases.

These are alternative planning envelopes, not additive projects or a decision to narrow the confirmed full-catalogue ambition. Reusing a tested commerce backend versus implementing pricing, orders, payments and inventory from scratch materially changes the work. Hundreds of thousands of products do not require equivalent handwritten code per product; catalogue ingestion/validation is its own workload.

## Scope behind the initial UK estimate

Assume a human provides timely decisions, reviews results and helps validate suppliers/requirements. Assume an established database/web framework, ordinary payment/shipping integration, a bounded initial release and no repeated platform rewrite. Cover admin roles, products/variants, basic organisation/customer records, stock, orders, price/tax/shipping rules, ordinary refund workflows, storefront search/categories/product detail, accounts, cart, checkout, R2 image upload/variants, bulk import, deployment and targeted verification.

Full ERP/WMS replacement, bespoke pharmacy/prescribing infrastructure, advanced equipment servicing, comprehensive credit procurement, many supplier connectors and country-by-country European workflows are not all assumed complete in that first estimate. They remain in the wider confirmed ambition and need their own work packages. Coding does not itself supply licences, clinical evidence, contracts or business approvals.

## Illustrative work allocation

Counts are millions of total input plus output tokens, including context rereads, tool results, reasoning where reported, implementation, debugging and review. Avoid counting the same cross-cutting work in multiple rows.

| Workstream | Low | High |
|---|---:|---:|
| Architecture, schema, contracts and initial setup | 1 | 3 |
| API and core commerce logic | 4 | 9 |
| Admin application | 3 | 7 |
| Next.js storefront | 3 | 7 |
| R2/media, bulk import and initial B2B/category rules | 3 | 8 |
| Cross-system testing, security fixes, deployment and operational checks | 6 | 16 |
| Base build total | 20 | 50 |

A 25% contingency gives 25–62.5 million, rounded to a 25–65 million planning range. The 50 million working allowance sits within that range; it is proposed only, not a user-approved spending limit.

## An explicit activity model

An alternative sensitivity model is 400 implementation/review/debugging cycles x 100,000 aggregate tokens per cycle = 40 million, plus 25% reserve = 50 million. A cycle can contain multiple model calls and tool interactions. Neither cycle count nor average size has been observed; this exposes the assumptions rather than validating the estimate.

Doubling the cycle count or average context processed doubles this illustrative usage. A final repository with modest code volume can still require much larger cumulative model usage because files, instructions, histories and error logs are processed repeatedly.

## Count token categories correctly

For OpenAI usage, cached input is part of input tokens and reasoning is part of output tokens; neither should be added a second time. Inputs include instructions, files, tool results and history. Output counts can exceed visible code/text. Other providers/tools need their own accounting definitions checked. [Official usage documentation](https://developers.openai.com/api/docs/guides/agents-api/observability), [Output token counts](https://developers.openai.com/api/docs/guides/token-counting).

For illustration only, a 50 million total might comprise 40 million input and 10 million output. This 80/20 split is an assumption, not a normal ratio guaranteed for coding. Reasoning effort, agent/tool behaviour and context strategy can change it substantially.

Caching changes billing treatment, not the fact that input is counted. Eligibility, hit rates and cache-write/read tariffs depend on the model and configuration; a conversation does not guarantee a cache hit. [Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching).

## Token volume is not a price

For API budgeting, split aggregate usage into mutually exclusive uncached-input, cache-read, cache-write where applicable, and output categories. Multiply each by the chosen model's rate, then add any tool or execution charges. Do not multiply all total tokens by an advertised input rate. Subscription/credit arrangements need their own current terms and do not follow automatically from API token estimates.

No currency estimate is asserted without a chosen model mix and actual billing route. Development token usage is separate from the GBP40/month proposed technical-running-cost target; visitors do not consume development-model tokens after launch unless AI features are added to the store.

## Improve the estimate before committing

1. Agree a bounded release backlog and backend reuse decision.
2. Implement representative slices: authentication/roles; product CRUD plus R2 upload; product search/detail; and an order/payment path in a sandbox. This document proposes a pilot, not authorisation to run transactions or deploy.
3. Record actual input, cached-input, output/reasoning and retries by task/model where the tool exposes them. Sum all calls; do not infer usage from visible messages.
4. Compare actual work/acceptance effort with remaining modules, including integration complexity and risk.
5. Replace this estimate with a weighted forecast and a reserve supported by observed rework.

Keep changes small, reuse stable conventions/components, provide relevant file context and clear acceptance criteria, and run focused checks to resolve actual failures. Use model capability according to task difficulty; avoid claiming a universal percentage saving from routing or caching. UI iterations, changing business rules, difficult integrations and prolonged debugging are major uncertainties.

Project-specific token ranges and allocations above are analyst estimates. The official sources support token accounting only and do not validate how many tokens this ecommerce store will require.
