# VAT pricing and economics

Baseline: 7 November 2026. Commercial models below are recommendations and illustrations; supplier costs, acquisition performance and actual margin are unknown.

## Tax treatment

Do not assume that medical goods, NHS sales, charities or disabled customers are automatically VAT-free. Assign an evidence-backed tax code by product, transaction and eligible use/customer. Separate zero-rated, reduced-rated, standard-rated and exempt treatment.

HMRC's disabled-person relief is conditional on the goods and eligible supply, including personal/domestic use where required. A diagnosis or checkout tickbox alone is not universal eligibility. Keep a proportionate evidence trail. [VAT Notice 701/7](https://www.gov.uk/guidance/reliefs-from-vat-for-disabled-and-older-people-notice-7017).

Charity-funded medical equipment relief requires qualifying goods, eligible bodies/use and funding conditions. Some consumables/general items do not qualify under that equipment relief. NHS identity alone is insufficient. [VAT Notice 701/6](https://www.gov.uk/guidance/charity-funded-equipment-for-medical-and-veterinary-uses-notice-7016).

The published UK-established-business VAT threshold is more than GBP90,000 taxable turnover, with backward-looking and expected-next-30-day tests. Non-established taxable persons have different rules. The legal operator must be confirmed before applying the threshold. [HMRC registration](https://www.gov.uk/register-for-vat).

Have the accountant review tax mapping, bundles, freight, relief declarations, mixed baskets and invoice/credit-note handling. Many healthcare buyers cannot fully recover input VAT; validate gross-price sensitivity rather than assuming net price is all that matters.

## Price architecture

Show clear pack quantity and unit price. In a mixed/public consumer store, make gross totals and mandatory charges clear; a net-price toggle does not excuse misleading consumer pricing. Variable shipping should be disclosed with the information required to calculate it and included when known. [CMA price transparency](https://www.gov.uk/government/publications/price-transparency-cma209/providing-clear-and-accurate-information-about-prices-summary).

Proposed price layers: public price, documented quantity breaks, approved organisation contract price and quotation-led equipment. Recheck contribution after coupons, loyalty discounts and negotiated freight. Never promise blanket price matching before identical-product and delivery conditions are defined.

## Contribution model

    Net sales = product revenue after discounts, excluding VAT + shipping revenue excluding VAT
    Gross profit = net product revenue - landed product cost
    CM1 = net sales - landed cost - payment fees - pick/pack - outbound freight - expected returns/warranty loss - support - expected credit loss
    CM2 = CM1 - attributable acquisition cost

Payment fees often apply to the gross charged amount, including VAT and shipping. The illustration models that explicitly. A model that charges a fee only on ex-VAT revenue understates cost. Do not count freight twice if already included in a quoted fulfilment rate.

    Gross margin % = gross profit / net product revenue
    Markup % = gross profit / landed product cost

Margin and markup are different. Revenue-based ROAS is not profit. Break-even paid ROAS must use the same revenue/VAT basis as the ad report.

## Illustration and sensitivity

Run [the calculator](../../scripts/models/calculate_economics.py) with [assumed inputs](../models/unit_economics_inputs.json). The [generated output](../models/UNIT_ECONOMICS_OUTPUT.md) includes weak, base and stronger baskets, CM1/CM2, break-even acquisition cost, contribution-based ROAS and a simple mixed-basket break-even threshold.

These are intentionally hypothetical, not quoted processor fees, industry margins or a business forecast. A large capital-equipment order can have worse contribution than a smaller replenishment basket once installation, warranty and split freight are included.

For a proposed free-delivery threshold, compare incremental basket gross profit with lost shipping revenue, extra picking/packing and any jump to a larger parcel. Test bulk paper, liquids, low-margin branded items and mixed supplier shipments separately. Do not use a single blended percentage to guarantee profitability for every basket.

## Retention and acquisition

    Contribution LTV = sum of expected retained-order CM1 over a defined horizon - retention/service costs
    Maximum CAC = contribution LTV - required contribution buffer

State the horizon and observed reorder/retention assumptions. Do not extrapolate a first-order customer to perpetual repeat revenue. Track first-order CAC, 90/180/365-day cohort contribution and payback. Treat benchmarks as hypotheses until paid pilot data exist.

## Cash and funding

    Operating working capital = inventory at cost + customer receivables - supplier payables
    Cash conversion cycle = inventory days + receivable days - payable days

Add VAT/duty timing, PSP reserves, deposits, refundable balances, returns stock, minimum buys and fixed operating costs to a cash forecast. Illustratively, GBP100,000 monthly net product sales, 70% landed COGS, 60 inventory days, 30 receivable days and 30 payable days imply about GBP170,000 operating working capital using 30-day months: GBP140,000 inventory + GBP100,000 receivables - GBP70,000 payables. This is an assumption-led example, excluding VAT and other cash items.

Prepare a 13-week cash forecast before granting credit or buying significant stock. Model supplier deposits, slow stock, expiry, FX movement, customer default, a recall and adverse delivery costs. Keep cash viability separate from accounting profit.
