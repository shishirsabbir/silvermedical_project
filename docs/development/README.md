# Development handoff

**The Silver Edit** is the selected direction for the Next.js storefront. Start the app from the repository root with `npm install` and `npm run dev`. The homepage at `/` and component gallery at `/design-system` use the same UI components and design tokens. See the [storefront handoff](../../apps/storefront/README.md), [component reference](../../packages/ui/README.md) and [offline visual reference](../../dev/designs/homepage-concepts/README.md).

## Implementation references

| Reference | Use |
|---|---|
| [Technical specification](../plans/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.md) | Proposed architecture, workflows, security and acceptance requirements |
| [Technical requirements](../registers/TECHNICAL_SPEC_REQUIREMENTS.json) | Requirement identifiers and verification expectations |
| [25-day development plan](../plans/UK_MEDICAL_ECOMMERCE_25_DAY_DEVELOPMENT_PLAN.md) | Collaborative design, product intake, delivery tasks and release gates |
| [Feature register](../registers/DAY_25_FEATURE_REGISTER.json) / [daily plan](../registers/DAY_25_DAILY_PLAN.json) | Planned scope and task tracking; entries are not completed work |
| [API and admin analysis](../analysis/20_API_FRAMEWORK_AND_ADMIN_ARCHITECTURE.md) | Proposed application boundaries and API alternatives |
| [Decisions](../../memory/DECISIONS.md) / [open questions](../../memory/OPEN_QUESTIONS.md) | Confirmed directions versus choices requiring evidence or a decision |

The reported 250 warehouse products require reconciliation into actual SKUs, quantities and sale evidence. The previously illustrated calendar remains an assumption; this file does not establish an agreed kickoff or launch date.

## Code locations

| Location | Intended responsibility | Status |
|---|---|---|
| `apps/storefront/` | Next.js customer shopping experience | Responsive catalogue, accounts, basket, checkout, delivery tracking, returns, message previews and interactive design gallery. See the [storefront guide](../../apps/storefront/README.md). |
| `apps/admin/` | React staff interface | React confirmed; tooling open; no code |
| `apps/api/` | Authoritative commerce rules, eligibility, stock, orders and payment state | API framework open; no code |
| `apps/worker/` | Imports, prepared media, notifications and background work | Proposed boundary; no code |
| `packages/contracts/` | Shared request/response schemas and safe types | Proposed boundary; no code |
| `packages/ui/` | Shared presentation components and tokens | React components for controls, navigation, overlays, feedback and shopping |
| `packages/database/` | Server-only schema, migrations and database access | PostgreSQL confirmed; ORM open; no code |
| `infra/` | Deployment, reverse proxy, local services and recovery configuration | Hosting direction confirmed; configuration open |

Paths above are relative to the repository root. The storefront and UI package use npm workspaces and TypeScript. Installed frontend versions are recorded in the root lockfile. Remaining service tooling decisions belong to the corresponding implementation phase.

## First implementation sequence

1. Walk through the frontend with the sample catalogue and record owner feedback. The [shopping regression](../../scripts/qa/check_shopping_journey.py) exercises the purchase through refund on mobile and desktop.
2. For the subsequent integration phase, resolve API, data-access and authentication choices and prepare the associated services and test configuration.
3. Prove one representative product-to-payment flow using test data and provider sandbox facilities. Check server-side eligibility, stock contention, webhook authenticity and idempotency.
4. Measure effort, provider usage and combined hosting needs against the proposed delivery baseline before expanding the backlog.

GB, Northern Ireland and later European destinations require separate treatment. Product routes, publication eligibility, buyer entitlement, payment acceptance and feed eligibility remain independent controls. The full-catalogue objective is preserved.

## Organization and recovery

The previous top-level analysis, research, proposals, models and templates now live under `docs/`. Readable plans, Python document content and JSON registers have separate folders. Builders moved from `tools/` into `scripts/docs/` and `scripts/models/`. Current outputs moved from `output/` to `deliverables/`; the superseded whole-project one-sheet and its builder/input are marked as archive.

Original file destinations and migration hashes are in [FILE_MOVES.json](FILE_MOVES.json). Original project files are backed up under `.local/organization/originals/`; the one-time migration script is retained beside them. PDF previews and bundled Poppler tools are preserved under `.local/pdfs/` and `.local/tools/`. Nothing was deleted. The original empty `Note.md` is retained under `docs/archive/notes/`.

See [validation results](VALIDATION.md) for preservation checks and document rebuild verification.

The workspace had no Git repository when inspected. `.gitignore` is prepared for future version control; initialization, remotes and commits remain unconfigured. Keep `.local/` available until you are satisfied with the migration. Do not copy that backup into source control.
