# Customer messaging and retention

Updated 8 November 2026. UK launch planning for both consumers and verified professional/business customers. The user asked to address omitted email, WhatsApp and related marketing scope. Providers, budgets and campaign activation are not selected. The recommendations below supplement the existing acquisition analysis and proposal.

## Recommended launch scope

Build dependable customer communications and repeat purchasing into the platform. Use a managed email service for delivery and campaign automation, with customer permissions and product eligibility controlled by our API. Select the service after checking catalogue acceptance, integration, data handling and costs. Retain an exportable record of customer permissions in our own database.

| Channel or capability | Proposed purpose | Scope decision |
|---|---|---|
| Transactional email | Account security, order confirmation, dispatch, delivery exceptions, refunds and safety notices | Core launch requirement proposed; keep promotional content out of service templates |
| Email marketing | Welcome campaigns, relevant product news, eligible basket recovery, replenishment and reactivation | Proposed launch channel, limited to eligible recipients and approved products |
| WhatsApp | Evaluate specific support or messaging use cases | Conditional investigation only; see the policy finding below before promising campaigns or integration |
| SMS | Time-sensitive updates and carefully scoped marketing | Optional; validate customer demand, permissions, provider acceptance and unit economics |
| Website account tools | Saved lists, repeat order, stock alerts, quotes and preference management | Core retention features proposed; distinguish requested alerts from ongoing campaigns |
| Support inbox | Email, web enquiries and phone case history linked to orders | Define staff ownership, hours, escalation and a realistic response target |
| Loyalty and referrals | Retention incentives for eligible goods | Optional commercial design; require margin, abuse and marketing review before scope commitment |

The old proposal mentioned email/replenishment and privacy but did not specify the journeys, permissions, delivery setup, admin controls or recurring service budget. WhatsApp and SMS were not defined as deliverables.

## UK messaging rules

Email, SMS and private social messages can fall within PECR electronic-mail marketing. Purely administrative messages are distinct from marketing; adding promotion changes the assessment. A requested stock alert must be assessed by its actual request and content, rather than labelled automatically as transactional. [ICO key concepts](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/key-concepts-for-direct-marketing-using-electronic-mail/), UK electronic mail, checked 8 November 2026 via indexed official guidance; direct access returned 403.

For unsolicited marketing to individual subscribers, use valid consent or a properly evidenced products/services soft opt-in. The latter requires details obtained directly during a sale or negotiation, marketing of the sender's own similar offerings, an opt-out at collection and an opt-out in each message. It is not permission to market every catalogue category. Consent must cover the sender and method; provide an easy withdrawal route and retain suppression records. A public contact address is not consent, and bought-in lists cannot use this soft opt-in. [ICO electronic-mail rules](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-direct-marketing-using-electronic-mail/how-do-we-comply-with-the-pecr-electronic-mail-marketing-rules/), UK PECR, checked 8 November 2026 via indexed official passages; direct access returned 403.

Corporate subscribers can receive electronic-mail marketing without PECR consent, subject to identification and opt-out requirements and applicable data-protection duties. Sole traders and some partnerships are individual subscribers. A professional account, clinical job title or named work address does not settle subscriber status; UK GDPR still applies to personal data. [ICO B2B marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/), UK business recipients, checked 8 November 2026 via indexed official passages; direct access returned 403.

Recommended implementation: offer clear channel-specific choices, record the applicable basis rather than a single marketing checkbox, and honour objections across all relevant systems. Assess each automation before enabling it. Treat basket reminders, offers and replenishment suggestions as marketing in the initial design unless a documented assessment establishes another route. Starting a basket alone should not automatically subscribe someone.

Product advertising restrictions also apply to messages: do not promote prescription-only medicines to the public, and review professional promotion separately. Business verification alone does not establish an authorised professional audience. [MHRA medicines advertising](https://www.gov.uk/guidance/advertise-your-medicines), UK human medicines, checked 8 November 2026; see the proposal's medicines decision section.

Do not import the former Economed customer list as marketable by default. Establish the old and new controller identities, lawful transfer/use, original notices, sender/channel permission, collection history and suppression records. Quarantine unresolved records from campaign selection. A new brand name or the same beneficial owner does not, on its own, answer these questions.

## WhatsApp policy finding

WhatsApp's policy restricts buying, selling, promoting or facilitating medical/healthcare products and drugs, regardless of local licences. Its limited OTC messaging exception does not list the UK. Opt-in is required; Platform outreach uses approved templates, with a 24-hour reply window. These rules do not establish permission for this retailer's support workflow. [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/), App/Platform and UK applicability, checked 8 November 2026; policy dated 23 September 2026.

Keep WhatsApp outside committed launch functionality until the exact products, message content, destinations and business use are assessed. Assess service messages separately; do not assume an order update is exempt. A provider's technical onboarding or template approval should not be treated as permission to run a prohibited product campaign. Use email/web support for the initial operating design. Do not disguise product names or redirect customers through messages to circumvent restrictions.

## Proposed customer journeys

| Trigger | Intended customer experience | Controls and stop conditions |
|---|---|---|
| Account or professional verification | Confirm application, request necessary evidence, communicate the decision | Service-only copy; private evidence flow; no automatic newsletter subscription |
| Marketing signup | Confirm preferences and provide a short, useful welcome | Record permission; double opt-in is recommended for address verification, not asserted as a universal UK legal requirement |
| Abandoned basket | A limited reminder for permitted goods | Eligible marketing recipient; approved product content; stop after purchase, withdrawal, stock loss or review failure; no prescription or sensitive-health basket detail in messages |
| Completed purchase | Confirmation, dispatch and refund information | Reliable service delivery; minimal necessary details; no promotional banners in service templates |
| Expected replenishment | Help a business reorder routine supplies | Customer-selected schedule or reviewed marketing flow; confirm stock/current price; no automatic charge; avoid inferring personal health conditions |
| Requested stock alert | Notify that the specific requested item is available | Save request scope and expiry; recheck product permissions; do not extend the request to unrelated promotions |
| Equipment service due | Notify about an agreed service or warranty process | Distinguish contracted service information from selling a new plan; verify provider and equipment record |
| Inactive marketing subscriber | A limited reactivation campaign | Permission still valid, relevant products, frequency limit and inactivity sunset; do not chase opted-out recipients |
| Review request | Collect authentic product/service feedback | Approve message purpose and permitted contact route; avoid rewarding only favourable reviews |
| Recall or safety issue | Reach affected buyers promptly | Separate safety workflow and accountable owner; marketing opt-out must not erase order/traceability records needed for a lawful safety response |

Timing and frequency remain model inputs. Start with conservative limits and test them against complaints, opt-outs, incremental orders and support capacity. Do not hard-code assumed clinical usage intervals or send treatment advice.

## Admin and API requirements

The admin should show a customer's organisation, account status, relevant order history, communication preferences and support cases to authorised staff. For campaigns, support audience previews, approved templates, product exclusions, scheduling, review history, send limits and a pause action.

Proposed messaging records:

- Recipient and organisation references; channel/contact reference; subscriber classification and verification basis where relevant.
- Sender/controller identity, purpose, consent or other reviewed basis, collection surface, timestamp, notice/version and evidence reference.
- Withdrawal/objection and delivery-suppression events, with scope and timestamp; provider sync status.
- Campaign/template revision, approved content/product set, audience rule, reviewer and country scope.
- Send attempt, idempotency key, provider ID, status, error, cost category and retry history.

Do not store actual customer details or permission evidence in these general research files. Keep sensitive documents and health information outside routine marketing exports, subject lines, tracking URLs, pixels and audience uploads. Prefer broad professional purchasing interests over inferred medical conditions. The existing privacy analysis still applies.

Recommended event flow: a committed order/account event enters a durable queue; the worker checks purpose, recipient preference, product/channel eligibility and frequency limit immediately before sending; the provider delivers; verified delivery/complaint/withdrawal events update our records. Permission changes must cancel or block queued marketing. Duplicate webhooks or job retries must not cause duplicate messages.

Separate delivery failure from marketing withdrawal: a hard bounce can block email delivery, while an unsubscribe normally blocks the stated marketing scope. Maintain another appropriate way to deliver necessary service information when an address fails. A marketing unsubscribe must not disable password resets or order confirmations.

Use a managed platform's campaign editor/automation tools initially, integrated with our API. Build the medical-product approval, customer entitlement and preference controls locally. A full custom drag-and-drop campaign builder would be a separate, substantial scope item.

## Deliverability and provider selection

Configure authenticated branded sending domains with SPF, DKIM and DMARC, TLS, bounce/complaint handling and straightforward unsubscribe. Gmail has additional requirements for bulk senders, including one-click unsubscribe for relevant messages. Its rules concern delivery to personal Gmail accounts, not a complete statement of UK law. [Google sender guidelines](https://support.google.com/mail/answer/81126?hl=en), checked 8 November 2026.

Use separate transactional and promotional streams, credentials and monitoring; consider branded subdomains with correct alignment. Ramp sending to a verified audience and monitor domain reputation. Avoid operating a bulk-mail server on the store VPS as the initial design.

Evaluate providers on acceptance of the actual catalogue, transactional reliability, campaign automation, API/webhooks, suppression export, data-processing terms, transfer safeguards, support, billing units and exit options. One vendor may provide multiple functions, but staff mailboxes, transactional delivery and marketing automation are separate requirements.

## Costs and measurement

Add distinct budget lines for staff mailboxes, transactional email, marketing contacts/sends/automation, SMS, any eligible WhatsApp service, support-inbox seats, template work and ongoing campaign management. Visits per day do not determine subscriber count or messaging spend.

Illustrative volume formulas, not forecasts:

- Monthly marketing emails = eligible audience reached per campaign summed across campaigns + permitted automation sends.
- Monthly service emails = order/account/service events multiplied by their respective notification counts, with failures/retries accounted for according to provider billing.
- Messaging cost = selected plan + billable traffic by country/category + provider additions + inbox seats and applicable tax.

WhatsApp Platform pricing is message-based and depends on market/category; use the applicable current rate card and provider terms if an eligible use case is established. Do not price it using an old conversation allowance. No precise tariff or free-window entitlement is assumed here. [Official WhatsApp pricing](https://whatsappbusiness.com/products/platform-pricing/), checked 8 November 2026; service availability and billed categories must be confirmed at selection.

Measure delivery failures, complaints, unsubscribes, eligible-audience growth, repeat orders, time to second order and contribution after discounts/messaging costs. Compare automations against a holdout group where practical. Do not use email opens as the main success criterion; review tracking pixels separately from permission to send marketing.

## Acceptance and remaining decisions

Before enabling a channel, demonstrate that withdrawal blocks scheduled marketing, provider failures are visible, duplicate events do not duplicate sends, failed product approval excludes content, and service messages remain available for opted-out customers through an appropriate route. Test imported lists with missing evidence and changed product permissions.

Owners need to identify who will manage campaigns/support, whether any legacy customer data will be considered, expected eligible contact volumes, channels and budget, and approval responsibilities. Provider selection and WhatsApp feasibility remain open. Proposed sequencing: service email and preferences first; email campaigns and useful reorder tools next; optional channels after policy, demand and cost validation.
