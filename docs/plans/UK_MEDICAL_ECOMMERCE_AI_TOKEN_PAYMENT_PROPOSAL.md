# Medical E-commerce | AI development cost

10 November 2026 | Revision 5 | Cost explanation with usage assumptions

## Build the core. Then extend it.

Medical E-commerce | United Kingdom first / Europe next

USD 1,555.56
Approximately RMB 10,379.99 | Developer fee: USD 0
Estimated AI cost for the initial 25-day build

25 days | Core release target
10+ agents | Planned minimum
USD 0 | Development fee

### AI development cost

The estimated AI cost for the initial 25-day development phase is USD 1,555.56. This includes modeled API usage and an allowance for additional usage or selective review. My development work carries no professional fee.

### Qwen for most development

Modeled Qwen API usage: USD 1,396.01
Additional usage / selective review reserve: USD 159.55
Total estimated AI cost: USD 1,555.56

### Most core development belongs in the first 25 days

The plan is to build the main commerce foundation and the most important basic features together: shopping, product management, stock, payments, orders and daily administration. Later phases will mainly expand and extend this foundation, rather than start it again.

This is the intended shape of the agreed core release, not a measured percentage of the entire future programme. The target still depends on data, timely decisions, integrations and acceptance. Model rates are published facts; token volumes and the reserve are planning assumptions. Actual API costs will depend on measured usage.

## A substantial foundation within 25 days.

Twenty planned launch feature groups connect the buyer journey to everyday operations.

| Core system | Built during the first 25 days | Later extension |
|---|---|---|
| Brand and buying | Brand direction; responsive pages; categories/search; product pages; customer accounts. [F01-F04] | Broader merchandising, richer discovery and additional customer journeys. |
| Eligibility and checkout | Professional purchase checks; basket/checkout; Revolut/wallets and PayPal; information and service email. [F05-F09] | More approved payment/market routes and reviewed customer-service automation. |
| Staff and catalogue | SEO/consent foundation; staff MFA/roles; product CRUD/CSV; images and documents. [F10-F13] | More products, improved imports, content workflows and reporting. |
| Trading operations | Stock/traceability; orders/dispatch; returns/refunds; financial records/exports. [F14-F17] | Deeper purchasing, carrier/accounting connectors and operational automation. |
| Controlled release | Product/channel approval; hosting and restore; training and launch evidence. [F18-F20] | Capacity tuning, additional eligible categories and country-by-country expansion. |

### Build once; extend the systems

The first phase targets a complete basic receive -> publish -> buy -> ship -> refund workflow. Later work should add depth, scale and new capabilities on top of tested core modules.

### Practical sequence

Days 1-5: design decisions, architecture and a first transaction slice.
Days 6-15: connected commerce modules, admin and catalogue intake.
Days 16-25: integration, audits, corrections, business acceptance, restore rehearsal and release.

Scope follows the existing 20-feature register and 25-day plan. Initial intake targets the reported 250 warehouse products; exact SKUs, lawful sale and evidence remain to be verified. Future full-catalogue ambition continues. Merchant/product approvals and owner-controlled readiness remain release dependencies; AI agents cannot supply them.

## At least ten agents for the planned workflow.

Developer-led coordination, integration and review remain part of the work.

For the 25-day target, I plan a minimum of ten AI agents across these workstreams. This is a developer capacity assumption; provider quotas and simultaneous-session access still need verification.

1. Architecture and coordination
2. Brand and UX design
3. Next.js storefront
4. API and commerce rules
5. PostgreSQL and inventory
6. React admin workspace
7. Catalogue and media imports
8. Payments and order integrations
9. Testing and security review
10. Deployment, recovery and handover

### An explicit workload model

| Assumed activity | Calculation | Total |
|---|---|---|
| Agent-days | 10 agents x 25 days | 250 |
| Implementation/review cycles | 250 x 20 cycles per agent-day | 5,000 |
| Cumulative input tokens | 5,000 x 105,000 input tokens | 525 million |
| Cumulative output tokens | 5,000 x 21,400 output tokens | 107 million |
| Combined planning volume | 525m input + 107m output | 632 million |

A cycle can contain several calls to read files, implement, review and debug. Input is cumulative context; output includes billable reasoning where applicable. These are assumptions, not unique code counts or single-prompt sizes.

### Illustrative scenario; validate it early

These token quantities are illustrative planning inputs, not measured project consumption. Ten agents alone do not justify 632m tokens. Apply the same quantities to every model and reforecast using actual throughput and spend on Day 5.

## What the same token volume would cost.

Illustrative scenario: 525m input + 107m output | standard uncached text API assumptions

### The API billing formula

Cost = (input tokens / 1,000,000 x input rate)
+ (output tokens / 1,000,000 x output rate)

| Selected model | Input / 1m | Output / 1m | Project scenario |
|---|---|---|---|
| ChatGPT API: chat-latest [S2] | USD 5.00 | USD 30.00 | USD 5,835.00 |
| Claude Opus 5.5 [S3] | USD 4.00 | USD 20.00 | USD 4,240.00 |
| Qwen 3.8 Max [S1] | USD 1.65 | USD 4.951 | USD 1,396.01 |
| OpenAI GPT-6.1 Sol [S2] | USD 2.00 | USD 10.00 | USD 2,120.00 |
| Claude Sonnet 5.5 [S3] | USD 2.00 | USD 10.00 | USD 2,120.00 |

### OpenAI / ChatGPT calculation

525 x USD 5 + 107 x USD 30 = USD 5,835.00.
This illustrative scenario uses the chat-latest API rate; it is not a ChatGPT subscription price or an incurred bill. [S2]

### Claude calculation

525 x USD 4 + 107 x USD 20 = USD 4,240.00.
This illustrative scenario uses Claude Opus 5.5 standard base-token rates, not a measured project bill. [S3]

Illustrative scenarios, not measured bills or provider minimum prices. Cheaper alternatives are shown. Equal tokens do not establish equal quality; tokenizers and retries differ. No cache/batch/credit savings, tax or tool fees are assumed. OpenAI: standard short context. Qwen: Frankfurt/global <=1m input/request. [S1-S3]

## USD 1,555.56, explained.

Qwen is the main development API; the usage allowance covers extra tokens or selective review.

| Cost component | Calculation | USD |
|---|---|---|
| Qwen input | 525m x USD 1.65 / million | 866.25 |
| Qwen output | 107m x USD 4.951 / million | 529.76 |
| Modeled Qwen usage | Input + output | 1,396.01 |
| Additional usage reserve | Total estimate less Qwen base | 159.55 |
| Developer professional fee | No charge | 0.00 |
| Total estimated AI cost | 1,396.01 + 159.55 | 1,555.56 |

The reserve is 11.43% of the modeled Qwen base, included in the total cost estimate. It is an allowance, rather than an incurred provider charge or measured contingency. It covers potential additional tokens, tier/rate changes or selective OpenAI/Claude review. The base includes no separate premium-review token allocation.

### Indicative RMB equivalent: RMB 10,379.99

ECB reference date: 9 November 2026.
CNY per USD = 7.4689 / 1.1193 = 6.67283.
USD 1,555.56 x 6.67283 = approximately RMB 10,379.99. Calculation uses the unrounded cross rate. [S6-S7]

### Direct RMB API pricing is a separate route

Aliyun lists Qwen 3.8 Max at RMB 12 input / RMB 36 output per million for its Frankfurt/global or Beijing RMB billing route. The same assumed volume would be 525 x 12 + 107 x 36 = RMB 10,152 before any reserve. Account eligibility and settlement must be checked. This tariff is not mixed into the USD 1,396.01 baseline. [S4]

### How actual usage affects the estimate

Compare actual usage and provider charges with this model on Days 5, 15 and 25. If base usage rises 25%, the Qwen estimate becomes USD 1,745.01, exceeding the total estimate shown here. Update the forecast as measured token volumes, model choices and billing rates become available.

RMB is indicative, not a settlement quote. Hosting, stock, domains, paid image generation, other tools, maintenance and later phases are separate. Tax/FX/transfer fees are uncalculated.

## Current rates. Honest cost exposure.

Sources checked 10 November 2026. Published tariffs establish prices, not the project workload.

### Where bills can increase

Qwen: Singapore Coder Flash rises from USD 0.30/1.50 per million input/output at 66.7% tier uplift. This is a context-based cost increase, not a recent across-the-board tariff rise. [S1]

OpenAI / ChatGPT: GPT-6.1 Sol standard rates are USD 2/10 per million input/output; Fast rates are USD 4/20, a 100% speed-tier uplift. Model, context and region also affect billing. This is not a claim that the standard tariff recently doubled. [S2]

Claude: Anthropic says newer tokenizers may produce about 30% more tokens for the same text, affecting bills. It also cancelled the planned September 2026 Sonnet 5 price increase; the announced USD 3/15 tariff did not take effect. A blanket claim that all Claude prices rose would be inaccurate. [S3, S5]

### Dated, scoped references

[S1] [Alibaba Cloud Model Studio pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing) | Checked 2026-11-10 | Qwen 3.8 Max -0902, Frankfurt/global, <=1m input/request: USD1.65 input/4.951 output per million. Singapore/international is USD2/6. Coder Flash Singapore steps from 0.3/1.5 at <=32K to 0.5/2.5 at 32K-128K. | Limit: Does not establish project usage, model fitness, availability or account access.

[S2] [OpenAI API pricing](https://developers.openai.com/api/docs/pricing) | Checked 2026-11-10 | Direct standard short-context USD per million: chat-latest 5/30; GPT-6.1 Sol standard 2/10 and Fast 4/20 (+100%). Long-context, region and tool charges differ. | Limit: API billing is separate from ChatGPT subscriptions. Recheck mutable aliases.

[S3] [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing) | Checked 2026-11-10 | Direct standard USD per million base tokens: Opus 5.5 4/20; Sonnet 5.5 2/10. Newer tokenizer may produce about 30% more tokens for the same text; cache writes/reads differ. | Limit: Same token counts do not establish equal work or quality; partner/regional routes differ.

[S4] [Aliyun Model Studio RMB pricing](https://help.aliyun.com/zh/model-studio/model-pricing) | Checked 2026-11-10 | Qwen 3.8 Max -0902, Frankfurt/global or Beijing direct RMB tariff: CNY12/36 per million input/output. | Limit: Separate account/billing route; not interchangeable with USD tariff or spot-FX conversion.

[S5] [Anthropic: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) | Checked 2026-11-10 | Release 30 June 2026; August 10 edit makes USD2/10 permanent and cancels proposed September USD3/15 increase. | Limit: Specific cancelled increase, not a conclusion about all historical AI prices.

[S6] [ECB reference: CNY per EUR](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-cny.en.html) | Checked 2026-11-10 | Latest populated date observed: 9 November 2026, EUR1=CNY7.4689. | Limit: Reference, not settlement; November 10 unpopulated when checked.

[S7] [ECB reference: USD per EUR](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html) | Checked 2026-11-10 | 9 November 2026 EUR1=USD1.1193. Cross rate CNY/USD=7.4689/1.1193. | Limit: Payment rate and fees may differ.

Provider accounts, rates, limits, model availability and tax treatment need verification before API use. This is a cost explanation based on published rates and assumed usage; actual charges will depend on consumption. Prepared by Shishir Sabbir | shishirsabbir.github.io | shishir.sabbir@gmail.com
