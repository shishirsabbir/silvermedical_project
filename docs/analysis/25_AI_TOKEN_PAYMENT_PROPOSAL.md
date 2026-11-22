# AI development cost explanation - 10 November 2026

Current revision 5: user wants non-round comparison totals. Keep published rates and change only explicitly illustrative usage inputs: 5,000 x 105,000 input / 21,400 output = 525m input / 107m output (632m total). This scenario is selected for presentation/sensitivity, not newly measured project use or evidence of necessary spend. Apply it equally to every model: chat-latest USD5,835; Opus 5.5 USD4,240; Sol/Sonnet USD2,120; Qwen USD1,396.007 -> USD1,396.01. Qwen output USD529.757 -> USD529.76 and input USD866.25. Allowance USD159.55 preserves total USD1,555.56; direct RMB base is RMB10,152. USD/RMB conversion and total remain unchanged. At 25% more usage, raw Qwen cost is USD1,745.00875 -> USD1,745.01. No provider rates or source dates changed. Client text labels comparisons as illustrative, not incurred bills. All affected PDF pages were rendered/visually checked; arithmetic and text checks pass. Earlier scenarios in the chronological history below are superseded; cost-only and no-old-calculation instructions remain.

Current instruction, revision 4: explain the estimated USD1,555.56 AI cost without asking for funding or payment. The current PDF/Markdown, headings, footer and metadata use cost-estimate language. Remove client funding/acceptance/reconciliation/return/carry-forward/overspend-agreement terms. Retain arithmetic, USD0 developer fee, usage assumptions, provider comparisons and scoped sources. The model now uses `estimated_total_usd`, informational status and cost-tracking fields; former payment controls are removed. Earlier funding-oriented paragraphs below preserve internal history only and do not describe current client terms.

Presentation correction, revision 3: the user requests no old calculation in the client document. The PDF/Markdown now state USD1,555.56 directly and omit prior price, reduction amount/percentage and historical token-range comparisons. The current input model and calculated output omit old-price reduction fields. This analysis retains internal history for continuity. Current source-backed rates, workload caveat, funding calculation and delivery scope remain in the proposal.

## User direction and history

The user reports client dissatisfaction and reduces the requested AI budget from USD2,736 to USD1,555.56, keeping the developer fee at USD0. They request a changed design, at least ten planned AI agents, Qwen for most API use, RMB pricing and separate OpenAI/Claude cost calculations. They clarified that "4-6 USD" meant USD4,000-6,000 for the project. The earlier eight-role, USD13.68/agent-day allocation is superseded. No client acceptance, payment, sending or provider purchase is established.

The intended delivery shape is to complete most agreed core platform development and important launch features in 25 days, then extend those systems. Do not turn that into an unsupported percentage of all four phases or a guarantee that every future feature/approval is completed. The existing twenty launch feature groups and release gates remain the scope baseline. At least ten agents is the developer's intended capacity requirement, not a measured universal minimum or proof of available concurrency. No agents were spawned to author this document.

## Published rates versus model inputs

All source URLs, check date 2026-11-10 and product/billing/geographic scopes are in `docs/registers/AI_TOKEN_PAYMENT_SOURCES.json` and the PDF's linked references. Official sources establish rates only, not development consumption.

Assumed workload: 10 agents x 25 days x 20 implement/review cycles/day = 5,000 cycles. Each cycle assumes aggregate 100,000 billed input and 20,000 billed output tokens across potentially multiple API calls. Total 500m input + 100m output = 600m cumulative tokens. This is a deliberately intensive unmeasured scenario, materially higher than previous 25-65m launch estimates. It is not validated by agent count or reverse-engineered evidence of necessity; replace it with pilot records at Day 5. No observed API usage exists for the application build here.

Standard uncached synchronous text API comparison, excluding tax/tools, without assumed cache/batch/credit discounts:

| Model and tariff | Input USD/m | Output USD/m | 500m input + 100m output |
|---|---:|---:|---:|
| OpenAI chat-latest, direct standard short context | 5 | 30 | USD5,500 |
| Claude Opus 5.5, direct standard base tokens | 4 | 20 | USD4,000 |
| Qwen 3.8 Max -0902, Frankfurt/global <=1m input/request | 1.65 | 4.951 | USD1,320.10 |
| OpenAI GPT-6.1 Sol, direct standard short context | 2 | 10 | USD2,000 |
| Claude Sonnet 5.5, direct standard base tokens | 2 | 10 | USD2,000 |

The USD4k-6k claim is conditional on the selected premium scenarios, not a universal provider floor. Cheaper configurations exist. Equal-token arithmetic is not an equal-quality/effort benchmark: tokenizers, reasoning, cache hits and retries can differ. ChatGPT subscription charges are not API tariffs. The proposed Qwen model/account/region must be checked for eligibility, quotas, availability and fitness; no API call was executed.

## Reduced funding calculation

500 x USD1.65 = USD825 input; 100 x USD4.951 = USD495.10 output. Qwen base USD1,320.10 + uncommitted usage reserve USD235.46 + developer fee USD0 = USD1,555.56. Reserve is derived from the requested cap (17.84% of base), not independently measured expected rework. It can fund extra tokens, rate/tier differences or selective premium review; no separate fixed premium-token allocation is included in base. At 25% more base usage Qwen alone would be USD1,650.13; monitor/reforecast before reaching the cap.

ECB's latest populated reference date observed on 10 November was 9 November: EUR1=CNY7.4689 and EUR1=USD1.1193. CNY/USD=7.4689/1.1193=6.6728312338; USD1,555.56 is approximately RMB10,379.99, using the unrounded cross rate. This is not a settlement quotation. Sources S6/S7 record both official URLs and dates. Separately, Aliyun's RMB-billed Frankfurt/global or Beijing tariff is RMB12/36 per million input/output; the same volume costs RMB9,600 before reserve. This is a distinct account/billing tariff, not interchangeable with the USD list converted at ECB FX.

## Price-increase accuracy

No verified across-the-board dated Qwen/OpenAI/Claude tariff increase is asserted. Show real cost exposure instead: Qwen Coder Flash Singapore context tier 0.3/1.5 to 0.5/2.5 (+66.7%); OpenAI GPT-6.1 Sol standard 2/10 to Fast 4/20 (+100%); Claude newer-tokenizer volume may rise approximately 30% for the same text. These are distinct effects. Anthropic's Sonnet 5 release article explicitly cancels the formerly announced September price increase in an August 10 update. Do not repeat the cancelled increase as enacted. See S1-S5.

## Deliverables, controls and verification

The redesigned six-page PDF uses cream/forest/coral styling, scope/extension table, ten-role plan, workload calculation, five-model rate table, comparative bars, Qwen funding calculation, RMB conversion and linked references. Files: `deliverables/pdf/UK_MEDICAL_ECOMMERCE_AI_TOKEN_PAYMENT_PROPOSAL.pdf`; generated editable Markdown under docs/; inputs `docs/models/AI_TOKEN_PAYMENT_MODEL.json`; calculated outputs `docs/models/AI_TOKEN_PAYMENT_CALCULATED.json`; sources under docs/; builder `scripts/docs/build_ai_token_payment_proposal.py`.

Provider usage reporting, Day 5/15/25 reviews, unused-fund return/carry-forward and separate agreement for overspend remain proposed client terms. Hosting/stock/domains/paid image generation/other tools/maintenance/later phases are separate. Tax/FX/transfer fees are uncalculated; no automatic increase is authorised. The document is a funding proposal, not an incurred invoice or receipt.

All six pages rendered and visually inspected; arithmetic, expected key amounts, page count and horizontal text bounds checked. No external communication, payment or publication occurred.
