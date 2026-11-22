# Silver Medical project

The `silvermedical_project` workspace is for Silver Medical, a new UK-first, own-stock medical retailer, with later European expansion. The user confirmed Silver Medical and supplied silvermedical.co.uk on 18 November 2026. The legal operator remains undecided.

The [30-logo presentation](deliverables/html/SILVER_MEDICAL_LOGO_PRESENTATION.html) is a self-contained HTML review credited to shishirsabbir.

The selected homepage design is **The Silver Edit**. In the client preview, choose **Design system** in the storefront header to explore the palette, typefaces, artwork and live components. Follow the [Cloudflare Workers preview guide](apps/storefront/README.md#cloudflare-workers-client-preview) to run or publish the complete preview. The [offline homepage preview](deliverables/html/SILVER_MEDICAL_HOMEPAGE_MOCKUPS.html) is also available for visual review.

## Start development

From the workspace root, install the dependencies and start Next.js:

```powershell
npm install
npm run dev
```

Open the [storefront](http://localhost:3000), [guided shopping demo](http://localhost:3000/demo) or [design system](http://localhost:3000/design-system). Use the port printed by Next.js. The [storefront guide](apps/storefront/README.md) covers test cards, accounts, tracking and release dependencies.

1. Read [project instructions](AGENTS.md), [project memory](memory/PROJECT_MEMORY.md), [decisions](memory/DECISIONS.md) and [open questions](memory/OPEN_QUESTIONS.md).
2. Follow the [development handoff](docs/development/README.md) for scope, unresolved technology choices and the first implementation steps.
3. Use the [technical specification](docs/plans/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.md), [25-day plan](docs/plans/UK_MEDICAL_ECOMMERCE_25_DAY_DEVELOPMENT_PLAN.md) and [feature register](docs/registers/DAY_25_FEATURE_REGISTER.json) as the proposed implementation baseline.

## Repository layout

```text
dev/designs/homepage-concepts/  The Silver Edit homepage preview
apps/                  Next.js storefront and planned admin, API and worker
packages/              Shared React UI and planned contracts and database code
infra/                 Future deployment and local-service configuration
docs/
  development/         Development handoff and file-move manifest
  plans/               Readable project, technical and delivery plans
  analysis/            Business, regulatory and architecture analysis
  research/            Dated evidence and historical-site observations
  proposals/           Earlier discussion proposal
  content/             Editable Python document content
  registers/           Requirements, features, sources and page maps
  models/              Illustrative financial inputs and outputs
  templates/           Reusable business and product-review forms
  archive/             Superseded planning inputs and original empty note
memory/                Context, decisions, assumptions and open questions
scripts/               Document builders, model calculator and validation
assets/                Supporting document assets
deliverables/          Current PDFs/HTML and clearly separated archive
.local/                Ignored previews, bundled tools and migration backup
```

The frontend uses Next.js, React, TypeScript and npm workspaces. The confirmed platform direction also includes a React admin, PostgreSQL, Hostinger hosting, Cloudflare R2, Revolut/wallets and PayPal. API framework, ORM and authentication libraries still need selection. The full product-range ambition remains; each product and destination needs its own release eligibility.

## Useful commands

Run from the repository root:

```powershell
python scripts/check_workspace.py
python -m pip install -r scripts/requirements-docs.txt
python scripts/docs/build_technical_spec.py
python scripts/docs/build_25_day_development_plan.py
python scripts/docs/build_project_plan.py
python scripts/docs/build_client_proposal.py
python scripts/docs/build_ai_token_payment_proposal.py
python scripts/models/calculate_economics.py
```

The document builders use Windows fonts and overwrite their corresponding generated files. See [script notes](scripts/README.md) before editing or rebuilding.

Browse the [complete planning library](docs/README.md) or [deliverable index](deliverables/README.md). Existing commercial estimates and legal research retain their original dates and caveats; moving them does not refresh their evidence.
