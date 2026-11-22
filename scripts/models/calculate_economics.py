"""Reproduce hypothetical basket economics using only Python's standard library.

No live prices, supplier quotes, tax advice or forecasts are represented.
Run from any directory; paths are resolved relative to this script.
"""

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def calculate(scenario):
    product = scenario["product_revenue_ex_vat"]
    shipping = scenario["shipping_revenue_ex_vat"]
    rates = (
        "gross_margin_rate", "vat_rate", "payment_rate_on_gross",
        "returns_warranty_reserve_rate", "credit_loss_rate",
    )
    for key in rates:
        if not 0 <= scenario[key] <= 1:
            raise ValueError(f"Invalid fractional rate: {key}")
    for key, value in scenario.items():
        if isinstance(value, (int, float)) and (not math.isfinite(value) or value < 0):
            raise ValueError(f"Invalid nonnegative finite input: {key}")
    if product <= 0:
        raise ValueError("Product revenue must be positive")

    net_sales = product + shipping
    gross_charged = net_sales * (1 + scenario["vat_rate"])
    cogs = product * (1 - scenario["gross_margin_rate"])
    payment = gross_charged * scenario["payment_rate_on_gross"] + scenario["payment_fixed"]
    reserve = product * scenario["returns_warranty_reserve_rate"]
    credit_loss = product * scenario["credit_loss_rate"]
    fixed_variable = sum(scenario[k] for k in ("pick_pack", "packaging", "outbound_freight", "support"))
    cm1 = net_sales - cogs - payment - reserve - credit_loss - fixed_variable
    cm2 = cm1 - scenario["cac"]
    slope = (
        scenario["gross_margin_rate"]
        - scenario["payment_rate_on_gross"] * (1 + scenario["vat_rate"])
        - scenario["returns_warranty_reserve_rate"]
        - scenario["credit_loss_rate"]
    )
    numerator = (
        fixed_variable + scenario["payment_fixed"] + scenario["cac"]
        - shipping * (1 - scenario["payment_rate_on_gross"] * (1 + scenario["vat_rate"]))
    )
    return {
        "net_sales": net_sales,
        "gross_charged": gross_charged,
        "landed_cogs": cogs,
        "gross_profit": product - cogs,
        "payment_fees": payment,
        "returns_warranty_reserve": reserve,
        "credit_loss": credit_loss,
        "cm1": cm1,
        "cac": scenario["cac"],
        "cm2": cm2,
        "break_even_cac": cm1 if cm1 > 0 else None,
        "net_sales_roas_break_even": net_sales / cm1 if cm1 > 0 else None,
        "gross_sales_roas_break_even": gross_charged / cm1 if cm1 > 0 else None,
        "product_revenue_for_cm2_break_even": max(0, numerator / slope) if slope > 0 else None,
        "monthly_fixed_cost": scenario["monthly_fixed_cost"],
        "orders_to_cover_fixed_cost": math.ceil(scenario["monthly_fixed_cost"] / cm2) if cm2 > 0 else None,
    }


def money(value):
    return "Not viable at these assumptions" if value is None else f"GBP {value:,.2f}"


def render(data):
    lines = [
        "# Illustrative unit economics output", "",
        "Baseline model: 7 November 2026. Generated from unit_economics_inputs.json.", "",
        data["basis"], "",
        "All figures are assumed. Product revenue is after discounts and excluding VAT. Payment fees are charged on gross product plus shipping receipts. Landed COGS excludes recoverable VAT. No market benchmark or forecast is implied.", "",
    ]
    results = []
    for scenario in data["scenarios"]:
        result = calculate(scenario)
        results.append((scenario, result))
        lines += [f"## {scenario['name']}", "", "| Metric | Result |", "|---|---:|"]
        for label, key in [
            ("Net sales", "net_sales"), ("Gross customer payment", "gross_charged"),
            ("Landed product cost", "landed_cogs"), ("Product gross profit", "gross_profit"),
            ("Payment fees", "payment_fees"), ("Returns/warranty reserve", "returns_warranty_reserve"),
            ("Expected credit loss", "credit_loss"), ("CM1 before acquisition", "cm1"),
            ("CAC allowance", "cac"), ("CM2 after acquisition", "cm2"),
            ("Maximum acquisition spend at zero CM2", "break_even_cac"),
            ("Product revenue for zero CM2 at unchanged mix", "product_revenue_for_cm2_break_even"),
            ("Monthly fixed cost assumption", "monthly_fixed_cost"),
        ]:
            lines.append(f"| {label} | {money(result[key])} |")
        for label, key in [
            ("Break-even ROAS on net-sales basis", "net_sales_roas_break_even"),
            ("Break-even ROAS on gross-sales basis", "gross_sales_roas_break_even"),
        ]:
            value = result[key]
            formatted = "No positive acquisition allowance" if value is None else f"{value:.2f}x"
            lines.append(f"| {label} | {formatted} |")
        orders = result["orders_to_cover_fixed_cost"]
        lines += [f"| Orders/month to cover stated fixed cost | {orders if orders is not None else 'No finite break-even at this contribution'} |", ""]

    lines += [
        "## Interpretation", "",
        "Small baskets can lose money before advertising. A positive gross margin does not establish positive contribution. The maximum acquisition spend shown leaves zero contribution for fixed costs or profit; practical CAC targets must be lower.", "",
        "The order-volume calculation assumes every order carries the stated acquisition allowance and the same basket/cost profile. It is not a sales forecast or a prediction of accounting profit. Repeat-order and category mix require a separate weighted model.", "",
        "The basket threshold holds margin, tax, returns rates and per-order freight/handling constant. Real bulk, equipment, hazardous and split orders can have nonlinear costs; this is not a recommended free-shipping threshold.", "",
        "Costs are hypothetical and separate pick/pack from packaging. Replace with actual contracts and avoid double counting if a provider bundles those fees. Model mixed VAT/relief, currency, installation, licences, stock finance, taxes and omitted business costs separately.", "",
        "## Base basket sensitivity", "",
        "All other base assumptions remain unchanged.", "",
        "| Change | CM1 | CM2 |", "|---|---:|---:|",
    ]
    base = data["scenarios"][1]
    variants = [
        ("Base", {}),
        ("Margin lower by 5 percentage points", {"gross_margin_rate": base["gross_margin_rate"] - 0.05}),
        ("Freight higher by GBP 2", {"outbound_freight": base["outbound_freight"] + 2}),
        ("CAC higher by GBP 5", {"cac": base["cac"] + 5}),
        ("Charge GBP 4.95 delivery including VAT", {"shipping_revenue_ex_vat": 4.95 / (1 + base["vat_rate"])}),
    ]
    for label, changes in variants:
        value = calculate({**base, **changes})
        lines.append(f"| {label} | {money(value['cm1'])} | {money(value['cm2'])} |")
    return "\n".join(lines) + "\n"


def main():
    inputs = ROOT / "docs/models" / "unit_economics_inputs.json"
    data = json.loads(inputs.read_text(encoding="utf-8"))
    output = ROOT / "docs/models" / "UNIT_ECONOMICS_OUTPUT.md"
    output.write_text(render(data), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
