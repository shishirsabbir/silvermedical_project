"""Build the designed one-page project brief from repository-local inputs."""
from pathlib import Path
from decimal import Decimal, ROUND_CEILING
import html
import json
import re

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "docs/archive/launch-brief.json").read_text(encoding="utf-8"))
BUDGET = json.loads((ROOT / "docs/models/launch_25_day_budget.json").read_text(encoding="utf-8"))
OUT = ROOT / "deliverables/archive"
(OUT / "pdf").mkdir(parents=True, exist_ok=True)
(OUT / "html").mkdir(parents=True, exist_ok=True)


def calculate_budget():
    b = {k: Decimal(str(v)) for k, v in BUDGET.items() if isinstance(v, (int, float))}
    storage = max(Decimal(0), b["r2_standard_gb_month_assumption"] - 10).to_integral_value(rounding=ROUND_CEILING) * Decimal("0.015")
    op_a = (max(Decimal(0), b["r2_class_a_requests_assumption"] - 1_000_000) / 1_000_000).to_integral_value(rounding=ROUND_CEILING) * Decimal("4.5")
    op_b = (max(Decimal(0), b["r2_class_b_requests_assumption"] - 10_000_000) / 1_000_000).to_integral_value(rounding=ROUND_CEILING) * Decimal("0.36")
    r2 = (storage + op_a + op_b) * b["usd_to_gbp_assumption"]
    other = r2 + sum(b[k] for k in ["offsite_backup_monthly_allowance", "transactional_email_monthly_allowance", "marketing_service_monthly_allowance", "one_mailbox_monthly_allowance", "monitoring_monthly_allowance"])
    base = b["vps_monthly_promotional"] + b["domain_annual_allowance"] / 12 + other
    renewal = base - b["vps_monthly_promotional"] + b["vps_monthly_renewal"]
    cash = b["vps_monthly_promotional"] * b["vps_prepaid_months"] + b["domain_annual_allowance"] + other
    labour = b["developer_hours_assumption"] * b["hourly_rate_assumption"]
    labour_reserve = labour * (1 + b["development_contingency_fraction"])
    amounts = {"r2_gbp": r2, "monthly_base": base, "monthly_renewal_base": renewal, "annual_initial_base": base * 12, "initial_technology_cash": cash, "labour_before_reserve": labour, "labour_with_reserve": labour_reserve, "launch_software_setup": labour_reserve + b["ai_tools_allowance"] + cash}
    return {k: float(v.quantize(Decimal("0.01"))) for k, v in amounts.items()}


def rich_html(value):
    return html.escape(value).replace("&lt;b&gt;", "<strong>").replace("&lt;/b&gt;", "</strong>")


def create_html():
    sections = []
    for side in ["left", "right"]:
        column = []
        for sec in DATA[side]:
            paragraphs = "".join(f"<p>{rich_html(t)}</p>" for t in sec["items"])
            column.append(f'<section id="section-{sec["number"]}" class="section {sec["tone"]}"><h2><span>{sec["number"]}</span>{html.escape(sec["title"])}</h2>{paragraphs}</section>')
        sections.append('<div class="column">' + "".join(column) + "</div>")
    metrics = "".join(f'<div class="metric"><strong>{html.escape(m["value"])}</strong><span>{html.escape(m["label"])}</span></div>' for m in DATA["metrics"])
    sources = "".join(f'<a href="{html.escape(s["url"], quote=True)}" target="_blank" rel="noopener">[{s["id"]}] {html.escape(s["label"])}</a>' for s in DATA["sources"])
    doc = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>UK Medical Ecommerce | Day 25 Launch Brief</title>
<style>
:root{--navy:#122840;--teal:#087d79;--ink:#25364a;--muted:#617386;--line:#dce5ec;--amber:#9c6414}*{box-sizing:border-box}body{margin:0;background:#eaf0f5;font-family:"Segoe UI",Arial,sans-serif;color:var(--ink);line-height:1.48}.toolbar{max-width:1040px;margin:24px auto 18px;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:0 12px}.identity{font-size:13px;font-weight:700;color:#42566c}.identity small{display:block;font-size:11px;font-weight:400;color:#63778d}.actions{display:flex;gap:8px;align-items:center}button,.button{font:600 12px "Segoe UI",Arial,sans-serif;border:1px solid #cad6e0;border-radius:7px;padding:10px 14px;cursor:pointer;background:white;color:var(--navy);text-decoration:none}.button.primary{background:var(--navy);color:white;border-color:var(--navy)}button:hover,.button:hover{box-shadow:0 3px 10px #12284020}button:focus-visible,a:focus-visible{outline:3px solid #2daea4;outline-offset:3px}.paper{max-width:1040px;margin:0 auto 36px;background:white;box-shadow:0 20px 70px #1d385c17;border-radius:4px;overflow:hidden}.hero{background:var(--navy);color:white;padding:30px 38px 52px;position:relative}.hero:after{content:"";position:absolute;right:-30px;top:-80px;width:310px;height:310px;border:1px solid #ffffff13;border-radius:50%;pointer-events:none}.eyebrow{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#9cb5ce;display:flex;justify-content:space-between;position:relative;z-index:1}.hero h1{font-size:35px;line-height:1.1;letter-spacing:-1.1px;margin:20px 0 5px}.subtitle{font-size:13px;color:#b6c9db;margin:0 0 17px}.hero h2{font-size:17px;font-weight:600;margin:0 0 7px;color:#91e2d6}.intro{font-size:12px;max-width:810px;margin:0;color:#d7e3ee}.metrics{display:grid;grid-template-columns:repeat(3,1fr);margin:-27px 38px 25px;position:relative;background:white;border:1px solid var(--line);border-radius:8px;box-shadow:0 4px 12px #12284009}.metric{padding:14px 20px;border-right:1px solid var(--line)}.metric:last-child{border:0}.metric strong{display:block;color:var(--navy);font-size:23px;line-height:1.2}.metric span{font-size:10px;color:var(--muted)}.content{display:grid;grid-template-columns:1fr 1fr;gap:30px;padding:0 38px 14px}.section{margin:0 0 21px;break-inside:avoid}.section h2{display:flex;align-items:center;gap:8px;font-size:14px;line-height:1.3;color:var(--navy);margin:0 0 9px}.section h2 span{font-size:9px;font-weight:700;color:#4e6c89;background:#edf3f9;min-width:25px;height:25px;display:grid;place-items:center;border-radius:6px}.section.teal h2 span{background:#e6f4f1;color:var(--teal)}.section.amber h2 span{background:#fcf1dd;color:var(--amber)}.section p{font-size:11px;line-height:1.58;margin:0 0 7px;color:#3f5062}.section p strong{color:#22374c}.section.amber{border:1px solid #eddabb;background:#fffcf6;padding:13px;border-radius:7px}.footer{margin:0 38px;padding:15px 0 22px;border-top:1px solid var(--line)}.footer p{font-size:9px;line-height:1.5;color:var(--muted);margin:0 0 9px}.sources{display:flex;flex-wrap:wrap;gap:5px 14px}.sources a,.companion{font-size:9px;color:#426780;text-decoration:none}.sources a:hover,.companion:hover{text-decoration:underline}.foot-meta{display:flex;justify-content:space-between;margin-top:10px;color:#7d8c9b;font-size:8px}.below{max-width:1040px;margin:-18px auto 30px;padding:0 12px;font-size:11px;color:#65758a}.below a{color:#426780}.print-note{font-size:10px;color:#6c7e90}
@media(max-width:650px){.toolbar{margin:14px auto;align-items:flex-start}.actions{flex-wrap:wrap;justify-content:flex-end}.print-note{display:none}.paper{margin:0 10px 30px}.hero{padding:22px 22px 45px}.hero h1{font-size:29px}.eyebrow{font-size:8px;letter-spacing:1px}.metrics{margin:-24px 20px 22px}.metric{padding:12px 10px}.metric strong{font-size:19px}.metric span{font-size:9px}.content{display:block;padding:0 22px 8px}.section p{font-size:12px}.section h2{font-size:15px}.footer{margin:0 22px}.foot-meta{gap:12px}.below{margin-top:-15px}}
@page{size:A4;margin:10mm}@media print{body{background:white}.toolbar,.below{display:none}.paper{width:100%;max-width:none;margin:0;box-shadow:none;border-radius:0}.hero{padding:14px 18px 29px;print-color-adjust:exact;-webkit-print-color-adjust:exact}.hero h1{font-size:24px;margin:10px 0 4px}.subtitle{font-size:9px;margin-bottom:9px}.hero h2{font-size:12px}.intro{font-size:8.1px}.eyebrow{font-size:7px}.metrics{margin:-17px 18px 15px;print-color-adjust:exact;-webkit-print-color-adjust:exact}.metric{padding:8px 12px}.metric strong{font-size:17px}.metric span{font-size:7px}.content{display:grid;gap:20px;padding:0 18px 4px}.section{margin-bottom:12px}.section h2{font-size:10px;margin-bottom:5px}.section h2 span{min-width:19px;height:19px;font-size:6.5px}.section p{font-size:8px;line-height:1.42;margin-bottom:5px}.section.amber{padding:8px;print-color-adjust:exact;-webkit-print-color-adjust:exact}.footer{margin:0 18px;padding:9px 0}.footer p{font-size:6.5px}.sources a{font-size:6.5px}.foot-meta{font-size:6px;margin-top:6px}}
</style></head><body>
<nav class="toolbar" aria-label="Document actions"><div class="identity">PROJECT DOCUMENTATION<small>UK launch · One-page brief</small></div><div class="actions"><span class="print-note">Designed PDF available below</span><button type="button" onclick="window.print()">Print page</button><a class="button primary" href="../pdf/UK_MEDICAL_ECOMMERCE_DAY_25_BRIEF.pdf">Open one-page PDF</a></div></nav>
<main class="paper"><header class="hero"><div class="eyebrow"><span>Medical commerce / UK launch</span><span>__DATE__</span></div><h1>__TITLE__</h1><p class="subtitle">__SUBTITLE__</p><h2>__PROMISE__</h2><p class="intro">__INTRO__</p></header><div class="metrics" aria-label="Planning assumptions">__METRICS__</div><div class="content">__SECTIONS__</div><footer class="footer"><p>__FOOTER__</p><div class="sources">__SOURCES__</div><div class="foot-meta"><span>__VERSION__ · Cost inputs are illustrative; approval and quotations remain open.</span><span>Sources checked 7-8 November 2026</span></div></footer></main>
<p class="below">Supporting requirements, complete source mapping and budget assumptions: <a href="../../../docs/analysis/23_DAY_25_LAUNCH_SCOPE_AND_BUDGET.md">launch scope and budget notes</a>. <a href="../../../docs/models/launch_25_day_budget.json">Editable budget inputs</a>.</p>
</body></html>'''
    replacements = {"DATE": DATA["date"], "TITLE": DATA["title"], "SUBTITLE": DATA["subtitle"], "PROMISE": DATA["promise"], "INTRO": DATA["intro"], "FOOTER": DATA["footer"], "VERSION": DATA["version"]}
    for key, val in replacements.items():
        doc = doc.replace(f"__{key}__", html.escape(val))
    doc = doc.replace("__METRICS__", metrics).replace("__SECTIONS__", "".join(sections)).replace("__SOURCES__", sources)
    target = OUT / "html/UK_MEDICAL_ECOMMERCE_DAY_25_BRIEF.html"
    target.write_text(doc, encoding="utf-8")
    return target


def create_pdf():
    font_dir = Path("C:/Windows/Fonts")
    if (font_dir / "segoeui.ttf").exists():
        pdfmetrics.registerFont(TTFont("Brief", str(font_dir / "segoeui.ttf")))
        pdfmetrics.registerFont(TTFont("Brief-Bold", str(font_dir / "segoeuib.ttf")))
        pdfmetrics.registerFontFamily("Brief", normal="Brief", bold="Brief-Bold", italic="Brief", boldItalic="Brief-Bold")
        normal, bold = "Brief", "Brief-Bold"
    else:
        normal, bold = "Helvetica", "Helvetica-Bold"
    target = OUT / "pdf/UK_MEDICAL_ECOMMERCE_DAY_25_BRIEF.pdf"
    c = canvas.Canvas(str(target), pagesize=A4, pageCompression=1)
    c.setTitle("UK Medical Ecommerce - Day 25 Launch Brief")
    c.setAuthor("Project planning")
    c.setSubject("One-page scope, compliance, implementation and illustrative launch budget")
    width, height = A4
    navy, ink, muted = HexColor("#122840"), HexColor("#30475d"), HexColor("#65788b")
    margin, gutter = 29, 19
    col_w = (width - margin * 2 - gutter) / 2
    top, floor = 624, 61

    c.setFillColor(navy)
    c.rect(0, 655, width, height - 655, stroke=0, fill=1)
    c.setStrokeColor(Color(1, 1, 1, alpha=0.09))
    c.circle(width + 12, height - 48, 135, stroke=1, fill=0)
    c.setFillColor(HexColor("#a7bed3"))
    c.setFont(bold, 7.5)
    c.drawString(margin, 817, "MEDICAL COMMERCE / UK LAUNCH")
    c.setFont(normal, 7.5)
    c.drawRightString(width - margin, 817, DATA["date"])
    c.setFont(bold, 25)
    c.setFillColor(HexColor("#ffffff"))
    c.drawString(margin, 783, DATA["title"])
    c.setFillColor(HexColor("#b8ccdf"))
    c.setFont(normal, 9.5)
    c.drawString(margin, 765, DATA["subtitle"])
    c.setFillColor(HexColor("#9ae3d6"))
    c.setFont(bold, 12)
    c.drawString(margin, 742, DATA["promise"])
    intro_style = ParagraphStyle("intro", fontName=normal, fontSize=8.8, leading=12, textColor=HexColor("#d9e5ef"))
    intro = Paragraph(html.escape(DATA["intro"]), intro_style)
    _, ih = intro.wrap(width - margin * 2, 70)
    intro.drawOn(c, margin, 729 - ih)

    metric_y, metric_h = 642, 46
    c.setFillColor(HexColor("#ffffff"))
    c.setStrokeColor(HexColor("#dce5ec"))
    c.roundRect(margin, metric_y, width - 2 * margin, metric_h, 6, stroke=1, fill=1)
    mw = (width - margin * 2) / 3
    for i, item in enumerate(DATA["metrics"]):
        x = margin + i * mw
        if i:
            c.line(x, metric_y + 9, x, metric_y + metric_h - 9)
        c.setFillColor(navy)
        c.setFont(bold, 16)
        c.drawString(x + 13, metric_y + 24, item["value"])
        c.setFillColor(muted)
        c.setFont(normal, 7)
        c.drawString(x + 13, metric_y + 11, item["label"])

    def section_height(sec, font_size):
        pad = 8 if sec["tone"] == "amber" else 0
        style = ParagraphStyle("body", fontName=normal, fontSize=font_size, leading=font_size * 1.24, textColor=ink)
        heights = [Paragraph(t, style).wrap(col_w - pad * 2, 1000)[1] for t in sec["items"]]
        return 21 + sum(heights) + max(0, len(heights) - 1) * 4 + pad * 2 + 8, style, pad, heights

    font_size = 9.25
    while font_size >= 8.6:
        totals = [sum(section_height(sec, font_size)[0] for sec in DATA[side]) for side in ["left", "right"]]
        if max(totals) <= top - floor:
            break
        font_size -= 0.1
    if max(totals) > top - floor:
        raise RuntimeError(f"One-page content exceeds available space: {totals}")
    section_positions = []
    for side, x in [("left", margin), ("right", margin + col_w + gutter)]:
        y = top
        for sec in DATA[side]:
            total_h, style, pad, heights = section_height(sec, font_size)
            if sec["tone"] == "amber":
                c.setFillColor(HexColor("#fffcf5"))
                c.setStrokeColor(HexColor("#ecd9b7"))
                c.roundRect(x, y - total_h + 12, col_w, total_h - 10, 5, stroke=1, fill=1)
            sx, sy = x + pad, y - pad
            badge_color = {"blue": "#eaf1f8", "teal": "#e3f3ee", "amber": "#f8eacd"}[sec["tone"]]
            c.setFillColor(HexColor(badge_color))
            c.roundRect(sx, sy - 16, 20, 19, 4, stroke=0, fill=1)
            c.setFillColor(HexColor("#42627d") if sec["tone"] != "amber" else HexColor("#986817"))
            c.setFont(bold, 7)
            c.drawCentredString(sx + 10, sy - 9, sec["number"])
            c.setFillColor(navy)
            c.setFont(bold, 10.1)
            c.drawString(sx + 26, sy - 10, sec["title"])
            py = sy - 23
            for text, ph in zip(sec["items"], heights):
                para = Paragraph(text, style)
                para.wrap(col_w - pad * 2, 1000)
                para.drawOn(c, sx, py - ph)
                py -= ph + 4
            section_positions.append({"section": sec["number"], "side": side, "bottom": round(y - total_h + 12, 2)})
            y -= total_h

    c.setStrokeColor(HexColor("#dce5ec"))
    c.line(margin, 55, width - margin, 55)
    foot = Paragraph(html.escape(DATA["footer"]), ParagraphStyle("footer", fontName=normal, fontSize=6.4, leading=8.1, textColor=muted))
    _, fh = foot.wrap(width - margin * 2, 30)
    foot.drawOn(c, margin, 50 - fh)
    sx = margin
    c.setFont(normal, 6.3)
    c.setFillColor(HexColor("#426780"))
    for source in DATA["sources"]:
        label = f'[{source["id"]}] {source["label"]}'
        tw = pdfmetrics.stringWidth(label, normal, 6.3)
        c.drawString(sx, 23, label)
        c.linkURL(source["url"], (sx, 20, sx + tw, 30), relative=0, thickness=0)
        sx += tw + 11
    c.setFont(normal, 5.8)
    c.setFillColor(muted)
    c.drawString(margin, 11, "Source scopes and assumptions: project analysis/23. Checked 7-8 November 2026. Planning example; not a final quote or product clearance.")
    c.drawRightString(width - margin, 11, "1 / 1")
    c.showPage()
    c.save()
    return target, {"body_font_size": round(font_size, 2), "column_heights": [round(x, 2) for x in totals], "sections": section_positions}


if __name__ == "__main__":
    budget = calculate_budget()
    (ROOT / "docs/models/DAY_25_BUDGET_OUTPUT.json").write_text(json.dumps(budget, indent=2) + "\n", encoding="utf-8")
    html_path = create_html()
    pdf_path, layout = create_pdf()
    print(json.dumps({"html": str(html_path), "pdf": str(pdf_path), "budget": budget, "layout": layout}, indent=2))
