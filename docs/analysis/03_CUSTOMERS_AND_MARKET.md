# Customers and market analysis

Baseline: 7 November 2026. No customer segment is confirmed as the first priority; the user wants all products covered.

## Buyer segments and purchase drivers

| Segment | Likely basket and buying pattern to validate | Buying participants | Main selling questions |
|---|---|---|---|
| GP practices and private clinics | Repeat consumables plus diagnostic replacement | Practice manager, nurse, clinician | Reliable replenishment, familiar brands, pack size, PO/invoices |
| Care homes and domiciliary providers | Hygiene, PPE, dressings, continence and handling | Owner, regional procurement, care manager | Multi-site ordering, bulk freight, continuity and credit |
| Dental practices and laboratories | Dental consumables, sterilisation and instruments | Principal, practice manager, dental nurse | Compatibility, specialist suppliers, servicing |
| Veterinary practices | Instruments, consumables, diagnostics and medicine routes | Vet, owner, procurement lead | Species/intended use, service support and medicine permissions |
| Hospitals and public bodies | Contracted categories and project equipment | Procurement, clinical evaluators, finance | Tender access, specification evidence and delivery SLAs |
| Allied health/podiatry/physiotherapy | Specialty consumables and furniture | Practitioner or owner | Discoverability, technical suitability and delivered price |
| Aesthetic and minor-procedure clinics | Instruments, PPE, diagnostics, licensed products | Clinician, owner, procurement | Professional eligibility, claims and authorised supply |
| Laboratories and education | Lab consumables, equipment, training aids | Lab manager, technician, purchasing | Research versus clinical intended use and documentation |
| Workplace/first-aid buyers | Kits, refills, emergency and hygiene supplies | Facilities, health and safety, schools | Expiry replenishment, product appropriateness and delivery |
| Consumers and carers | Home diagnostics, dressings, mobility and care items | Individual/carer | Gross price, understandable suitability, accessibility and returns |

These are hypotheses about buying behaviour, not measured demand. Medicines or professional-only items need separate controls even when adjacent ordinary products are sold publicly.

## Market sizing without false precision

Use an account-based model, not total NHS spending as the addressable ecommerce market. The CQC publishes locations in England across hospitals, care homes, GPs, dentists and other regulated services. Its directory has known update delays and does not cover the whole UK. [CQC data](https://www.cqc.org.uk/about-us/transparency/using-cqc-data).

Construct a deduplicated organisation/location table. Separate head-office procurement from branches and separate NHS/independent activity. Add country-specific sources for Scotland, Wales and NI rather than extrapolating England mechanically. Use NHS practice datasets to cross-check GP coverage, keeping the dataset period and publication date. [NHS general practice series](https://digital.nhs.uk/data-and-information/publications/statistical/general-and-personal-medical-services).

Calculate:

    Segment serviceable spend = eligible buying accounts x validated annual spend in approved categories
    Obtainable annual revenue = activated accounts x orders per account x net product AOV

Deduct contracted/locked spend, unavailable brands, excluded destinations and categories not ready to sell. Count branches and parent organisations consistently. Staff or patient counts are demand indicators, not numbers of buyers.

No verified UK-wide revenue TAM or current organisation count is asserted in this baseline. Obtain spend estimates from buyer invoices/quotes with permission, supplier evidence and interviews.

## Validation programme

Proposed first cycle: interview buyers across at least five segments, then recruit a small paid pilot once products and fulfilment are approved. Treat sample sizes and conversion targets as research design choices, not statistically representative estimates.

Ask for the last three replenishment baskets, decision criteria, ordering frequency, tolerable lead times, minimum shelf life, existing supplier issues, payment requirements, approval process and switching barriers. Test whether gross price, unit price or delivered basket matters most. Do not collect patient information.

Use the [interview template](../templates/CUSTOMER_INTERVIEW.md). Evidence that changes strategy should enter memory/DECISIONS.md; verbatim identifiable interview material belongs in restricted storage rather than general project memory.
