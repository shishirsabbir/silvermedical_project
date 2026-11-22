# Illustrative unit economics output

Baseline model: 7 November 2026. Generated from unit_economics_inputs.json.

Illustrative assumptions only; GBP; hypothetical basket after discounts; all sales assumed standard-rated at 20 percent for this example. Replace with quote-based costs and actual mixed-basket taxes.

All figures are assumed. Product revenue is after discounts and excluding VAT. Payment fees are charged on gross product plus shipping receipts. Landed COGS excludes recoverable VAT. No market benchmark or forecast is implied.

## Weak small basket

| Metric | Result |
|---|---:|
| Net sales | GBP 45.00 |
| Gross customer payment | GBP 54.00 |
| Landed product cost | GBP 35.10 |
| Product gross profit | GBP 9.90 |
| Payment fees | GBP 1.15 |
| Returns/warranty reserve | GBP 0.81 |
| Expected credit loss | GBP 0.14 |
| CM1 before acquisition | GBP -1.44 |
| CAC allowance | GBP 9.00 |
| CM2 after acquisition | GBP -10.44 |
| Maximum acquisition spend at zero CM2 | Not viable at these assumptions |
| Product revenue for zero CM2 at unchanged mix | GBP 103.65 |
| Monthly fixed cost assumption | GBP 15,000.00 |
| Break-even ROAS on net-sales basis | No positive acquisition allowance |
| Break-even ROAS on gross-sales basis | No positive acquisition allowance |
| Orders/month to cover stated fixed cost | No finite break-even at this contribution |

## Base repeatable basket

| Metric | Result |
|---|---:|
| Net sales | GBP 100.00 |
| Gross customer payment | GBP 120.00 |
| Landed product cost | GBP 70.00 |
| Product gross profit | GBP 30.00 |
| Payment fees | GBP 2.30 |
| Returns/warranty reserve | GBP 1.20 |
| Expected credit loss | GBP 0.30 |
| CM1 before acquisition | GBP 16.35 |
| CAC allowance | GBP 15.00 |
| CM2 after acquisition | GBP 1.35 |
| Maximum acquisition spend at zero CM2 | GBP 16.35 |
| Product revenue for zero CM2 at unchanged mix | GBP 94.89 |
| Monthly fixed cost assumption | GBP 20,000.00 |
| Break-even ROAS on net-sales basis | 6.12x |
| Break-even ROAS on gross-sales basis | 7.34x |
| Orders/month to cover stated fixed cost | 14815 |

## Stronger larger basket

| Metric | Result |
|---|---:|
| Net sales | GBP 180.00 |
| Gross customer payment | GBP 216.00 |
| Landed product cost | GBP 118.80 |
| Product gross profit | GBP 61.20 |
| Payment fees | GBP 3.98 |
| Returns/warranty reserve | GBP 1.80 |
| Expected credit loss | GBP 0.72 |
| CM1 before acquisition | GBP 42.50 |
| CAC allowance | GBP 20.00 |
| CM2 after acquisition | GBP 22.50 |
| Maximum acquisition spend at zero CM2 | GBP 42.50 |
| Product revenue for zero CM2 at unchanged mix | GBP 106.23 |
| Monthly fixed cost assumption | GBP 25,000.00 |
| Break-even ROAS on net-sales basis | 4.24x |
| Break-even ROAS on gross-sales basis | 5.08x |
| Orders/month to cover stated fixed cost | 1112 |

## Interpretation

Small baskets can lose money before advertising. A positive gross margin does not establish positive contribution. The maximum acquisition spend shown leaves zero contribution for fixed costs or profit; practical CAC targets must be lower.

The order-volume calculation assumes every order carries the stated acquisition allowance and the same basket/cost profile. It is not a sales forecast or a prediction of accounting profit. Repeat-order and category mix require a separate weighted model.

The basket threshold holds margin, tax, returns rates and per-order freight/handling constant. Real bulk, equipment, hazardous and split orders can have nonlinear costs; this is not a recommended free-shipping threshold.

Costs are hypothetical and separate pick/pack from packaging. Replace with actual contracts and avoid double counting if a provider bundles those fees. Model mixed VAT/relief, currency, installation, licences, stock finance, taxes and omitted business costs separately.

## Base basket sensitivity

All other base assumptions remain unchanged.

| Change | CM1 | CM2 |
|---|---:|---:|
| Base | GBP 16.35 | GBP 1.35 |
| Margin lower by 5 percentage points | GBP 11.35 | GBP -3.65 |
| Freight higher by GBP 2 | GBP 14.35 | GBP -0.65 |
| CAC higher by GBP 5 | GBP 16.35 | GBP -3.65 |
| Charge GBP 4.95 delivery including VAT | GBP 20.39 | GBP 5.39 |
