"""Generate the full project plan, HTML handbook, and a one-page launch-only extract."""
from pathlib import Path
from io import BytesIO
import html
import importlib.util
import json
import re

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("project_plan_content", ROOT / "docs/content/project_plan_content.py")
CONTENT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CONTENT)
SOURCES = {row[0]: row for row in CONTENT.SOURCES}
PDF_DIR, HTML_DIR = ROOT / "deliverables/pdf", ROOT / "deliverables/html"
PDF_DIR.mkdir(parents=True, exist_ok=True)
HTML_DIR.mkdir(parents=True, exist_ok=True)
NAVY, INK, TEAL, MUTED = map(HexColor, ["#142d45", "#2d4155", "#087f79", "#65788b"])
WIDTH, HEIGHT = A4
LEFT, RIGHT = 42, WIDTH - 42
COL_W = RIGHT - LEFT
FONT, BOLD = "Plan", "Plan-Bold"
for name, filename in [(FONT, "segoeui.ttf"), (BOLD, "segoeuib.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(Path("C:/Windows/Fonts") / filename)))
pdfmetrics.registerFontFamily(FONT, normal=FONT, bold=BOLD, italic=FONT, boldItalic=BOLD)


def rich(text):
    text = html.escape(str(text))
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)


def para(text, size=10.1, leading=None, color=INK, bold=False):
    return Paragraph(rich(text), ParagraphStyle("p", fontName=BOLD if bold else FONT, fontSize=size, leading=leading or size * 1.4, textColor=color))


def make_flowables(block, compact=False):
    kind = block["kind"]
    size = 9.7 if compact else 10.1
    if kind == "p": return [(para(block["text"], size), 10)]
    if kind == "h": return [(para(block["text"], 12, color=NAVY, bold=True), 8)]
    if kind == "list":
        return [(para("• " + text, size), 7) for text in block["items"]] + [(None, 4)]
    if kind == "callout":
        amber = block.get("tone") == "amber"
        body = [para(block["title"], 10.1, color=HexColor("#8c5f18") if amber else TEAL, bold=True), para(block["text"], size)]
        box = Table([[body]], colWidths=[COL_W], hAlign="LEFT")
        box.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), HexColor("#fff8ec") if amber else HexColor("#edf7f4")), ("BOX", (0,0), (-1,-1), .6, HexColor("#edd9b8") if amber else HexColor("#c8e5db")), ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12), ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 11)]))
        return [(box, 12)]
    if kind == "table":
        ratios = block.get("widths") or [1 / len(block["headers"])] * len(block["headers"])
        font_size = 8.65 if compact else 9.15
        cells = [[para(t, font_size, color=HexColor("#ffffff"), bold=True) for t in block["headers"]]]
        cells += [[para(t, font_size, leading=font_size * 1.32) for t in row] for row in block["rows"]]
        t = Table(cells, colWidths=[COL_W * r for r in ratios], hAlign="LEFT", repeatRows=1)
        t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), NAVY), ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#f0f5f8"), HexColor("#ffffff")]), ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 9), ("RIGHTPADDING", (0,0), (-1,-1), 9), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7), ("LINEBELOW", (0,0), (-1,0), .3, NAVY), ("LINEBELOW", (0,1), (-1,-1), .3, HexColor("#dce5eb"))]))
        return [(t, 13)]
    raise ValueError(kind)


def build_pdf(target, known_map=None, total=None):
    c = canvas.Canvas(target, pagesize=A4, pageCompression=1)
    c.setTitle("UK Medical Ecommerce - Complete Project Plan")
    c.setAuthor("Project planning")
    c.setSubject("Business, UK requirements, scope, implementation, costs and one-page Day 25 roadmap")
    page_map, chapter_pages = {}, {}

    def footer(refs=()):
        y = 39
        c.setStrokeColor(HexColor("#d8e3eb")); c.line(LEFT, y+15, RIGHT, y+15)
        c.setFillColor(MUTED); c.setFont(FONT, 7)
        c.drawString(LEFT, 25, "UK MEDICAL ECOMMERCE  /  PROJECT PLAN  /  8 NOVEMBER 2026")
        c.drawRightString(RIGHT, 25, f"{c.getPageNumber():02d}" + (f" / {total:02d}" if total else ""))
        if refs:
            x = LEFT
            c.setFont(FONT, 6.8)
            c.drawString(x, 43, "Sources: "); x += 31
            for sid in refs:
                label = sid + "  "
                w = pdfmetrics.stringWidth(label, FONT, 6.8)
                c.setFillColor(TEAL); c.drawString(x, 43, label)
                c.linkURL(SOURCES[sid][2], (x, 40, x+w, 51), relative=0, thickness=0)
                x += w
            c.setFillColor(MUTED)
            c.drawString(x+4, 43, "Dates and scope in source appendix")

    def heading(ch, continued=False):
        c.setFillColor(NAVY); c.rect(0, HEIGHT-10, WIDTH, 10, stroke=0, fill=1)
        c.setFillColor(TEAL); c.setFont(BOLD, 8)
        c.drawString(LEFT, HEIGHT-38, ch["group"].upper())
        c.setFillColor(MUTED); c.setFont(FONT, 7.5)
        c.drawRightString(RIGHT, HEIGHT-38, "PROJECT DOCUMENTATION")
        title = para(ch["title"] + (" - continued" if continued else ""), 23, 28, NAVY, True)
        _, th = title.wrap(COL_W, 1000); title.drawOn(c, LEFT, HEIGHT-65-th)
        y = HEIGHT-65-th-13
        if not continued:
            intro = para(ch["intro"], 11.1, 15.5, MUTED)
            _, ih = intro.wrap(COL_W, 1000); intro.drawOn(c, LEFT, y-ih); y -= ih+18
        return y

    # Cover: an executive overview with sufficient room to read comfortably.
    c.setFillColor(NAVY); c.rect(0, 433, WIDTH, HEIGHT-433, stroke=0, fill=1)
    c.setFillColor(HexColor("#a2c0d5")); c.setFont(BOLD, 8)
    c.drawString(LEFT, 799, "PROJECT DOCUMENTATION  /  UK LAUNCH")
    c.setFillColor(HexColor("#ffffff")); c.setFont(BOLD, 42)
    c.drawString(LEFT, 724, "UK medical")
    c.drawString(LEFT, 672, "ecommerce")
    c.setFillColor(HexColor("#a4e5d9")); c.setFont(FONT, 16)
    c.drawString(LEFT, 626, "Business scope, implementation")
    c.drawString(LEFT, 603, "and operating plan")
    cover = para("A complete project plan for a new retailer buying and holding its own medical stock, serving consumers and verified professionals. Next.js, React admin, PostgreSQL, Hostinger KVM and Cloudflare R2 form the current direction.", 11, 16, HexColor("#d5e4ef"))
    _, ch = cover.wrap(COL_W-20, 120); cover.drawOn(c, LEFT, 562-ch)
    c.setFillColor(HexColor("#a2c0d5")); c.setFont(FONT, 8.5)
    c.drawString(LEFT, 455, CONTENT.DATE + "  /  New brand and legal operator to be confirmed")
    cards = [("25-day target", "First complete selling phase"), ("Full-range ambition", "Activation after product review"), ("UK first", "Europe through country releases")]
    card_w = (COL_W-18) / 3
    for i, (title, label) in enumerate(cards):
        x=LEFT+i*(card_w+9)
        c.setFillColor(HexColor("#edf5f7")); c.roundRect(x, 352, card_w, 61, 6, stroke=0, fill=1)
        c.setFillColor(NAVY); c.setFont(BOLD, 11); c.drawString(x+10, 388, title)
        c.setFillColor(MUTED); c.setFont(FONT, 7.8); c.drawString(x+10, 371, label)
    y=319
    for title, text in [("What this document explains", "The business model, build scope and exclusions; UK product and ecommerce requirements; supplier/catalogue controls; customer/admin features; payments, marketing and communications; architecture, implementation, budgets, acceptance and ownership."), ("How to use the launch milestone", "Only the Day 25 roadmap is a one-page summary. The detailed chapters explain the wider project. Initial release is conditional on lawful products, ready stock, accepted payments and operational readiness; the remaining features follow in stages."), ("Decision and budget status", "Confirmed user requirements are distinguished from proposed technology and illustrative cost inputs. The API framework, medicine activities, legal operator, providers and final budget require decisions. Software delivery does not create product permissions.")]:
        title_p=para(title,11,color=NAVY,bold=True); _,ph=title_p.wrap(COL_W,1000); title_p.drawOn(c,LEFT,y-ph); y-=ph+6
        body=para(text,10.3); _,ph=body.wrap(COL_W,1000); body.drawOn(c,LEFT,y-ph); y-=ph+18
    footer(); c.showPage()

    # Contents with navigable PDF destinations.
    toc={"title":"Contents and document status","group":"How to use this plan","intro":"Read the business and release scope first. The dedicated Day 25 page condenses the timetable only; the remaining chapters provide the explanations."}
    y=heading(toc)
    group=None
    for ch in CONTENT.CHAPTERS:
        if ch["group"]!=group:
            group=ch["group"]; y-=4
            c.setFillColor(TEAL); c.setFont(BOLD,8.1); c.drawString(LEFT,y,group.upper()); y-=17
        c.setFillColor(INK); c.setFont(FONT,9.1); c.drawString(LEFT+8,y,ch["title"])
        if known_map:
            c.drawRightString(RIGHT,y,str(known_map[ch["id"]]))
            c.linkRect("",ch["id"],(LEFT,y-3,RIGHT,y+12),relative=0,thickness=0)
        y-=17
    y-=8
    c.setFillColor(TEAL); c.setFont(BOLD,8.1); c.drawString(LEFT,y,"SOURCE APPENDIX"); y-=17
    c.setFillColor(INK); c.setFont(FONT,9.1); c.drawString(LEFT+8,y,"Primary references, checked dates and geographical/product scope")
    if known_map: c.drawRightString(RIGHT,y,str(known_map["sources-1"]))
    footer(); c.showPage()

    def render_chapter(ch, blocks=None):
        start=c.getPageNumber(); page_map[ch["id"]]=start
        c.bookmarkPage(ch["id"]); c.addOutlineEntry(ch["title"],ch["id"],level=0,closed=False)
        y=heading(ch)
        for block in blocks or ch["blocks"]:
            for flow,gap in make_flowables(block, compact=ch["id"]=="day-25"):
                if flow is None: y-=gap; continue
                _,fh=flow.wrap(COL_W,1000)
                if y-fh < 69:
                    footer(ch.get("refs",[])); c.showPage(); y=heading(ch,True)
                if y-fh < 69: raise RuntimeError(f"Unsplittable block in {ch['id']} ({fh})")
                flow.drawOn(c,LEFT,y-fh); y-=fh+gap
        end=c.getPageNumber(); chapter_pages[ch["id"]]=(start,end)
        if ch["id"]=="day-25" and end!=start: raise RuntimeError("Day 25 roadmap must occupy exactly one page")
        footer(ch.get("refs",[])); c.showPage()

    for ch in CONTENT.CHAPTERS: render_chapter(ch)

    for i in range(0,len(CONTENT.SOURCES),14):
        subset=CONTENT.SOURCES[i:i+14]
        ch={"id":f"sources-{i//14+1}","title":f"Primary sources {i//14+1}","group":"Evidence and applicability","intro":"Each linked title opens the source URL. Checked dates describe this research; product/activity/territory conditions still require the actual operator's review.","refs":[]}
        page_map[ch["id"]]=c.getPageNumber()
        c.bookmarkPage(ch["id"]); c.addOutlineEntry(ch["title"],ch["id"],level=0,closed=False)
        y=heading(ch)
        for sid,title,url,date,scope in subset:
            line=Paragraph(f'<b>{sid}</b>  <link href="{html.escape(url,quote=True)}" color="#087f79">{html.escape(title)}</link>  <font color="#65788b">| Checked {date}</font>',ParagraphStyle("source",fontName=FONT,fontSize=9,leading=12.5))
            details=para(scope,8.6,11.5,MUTED)
            _,lh=line.wrap(COL_W,1000); _,dh=details.wrap(COL_W-30,1000)
            if y-lh-dh-14<69: raise RuntimeError("Source appendix page overflow")
            line.drawOn(c,LEFT,y-lh); y-=lh+3
            details.drawOn(c,LEFT+30,y-dh); y-=dh+12
        footer(); c.showPage()
    pages=c.getPageNumber()-1
    c.save()
    return page_map,chapter_pages,pages


def to_html_block(block):
    k=block["kind"]
    if k=="p": return f'<p>{rich(block["text"])}</p>'
    if k=="h": return f'<h3>{rich(block["text"])}</h3>'
    if k=="list": return '<ul>'+''.join(f'<li>{rich(t)}</li>' for t in block["items"])+"</ul>"
    if k=="callout": return f'<aside class="callout {block.get("tone","teal")}"><strong>{rich(block["title"])}</strong><p>{rich(block["text"])}</p></aside>'
    if k=="table":
        head=''.join(f'<th scope="col">{rich(t)}</th>' for t in block["headers"])
        rows=''.join('<tr>'+''.join(f'<td>{rich(t)}</td>' for t in row)+'</tr>' for row in block["rows"])
        return '<div class="table-wrap"><table><thead><tr>'+head+'</tr></thead><tbody>'+rows+'</tbody></table></div>'
    raise ValueError(k)


def create_html(page_map):
    nav=[]; sections=[]; group=None
    for ch in CONTENT.CHAPTERS:
        if ch["group"]!=group:
            group=ch["group"]; nav.append(f'<span class="nav-group">{html.escape(group)}</span>')
        nav.append(f'<a href="#{ch["id"]}">{html.escape(ch["title"])}</a>')
        refs=' '.join(f'<a href="{SOURCES[sid][2]}" target="_blank" rel="noopener">{sid}</a>' for sid in ch.get("refs",[]))
        extra='<a class="small-button" href="../pdf/UK_MEDICAL_ECOMMERCE_25_DAY_ROADMAP.pdf">Open this one-page roadmap</a>' if ch["id"]=="day-25" else ''
        sections.append(f'<section class="chapter" id="{ch["id"]}"><div class="section-top"><span>{html.escape(ch["group"])}</span><span>PDF page {page_map[ch["id"]]}</span></div><h2>{html.escape(ch["title"])}</h2><p class="intro">{html.escape(ch["intro"])}</p>{extra}{"".join(to_html_block(b) for b in ch["blocks"])}'+(f'<div class="chapter-sources">Sources: {refs}. Checked dates and scope below.</div>' if refs else '')+'</section>')
    sources=''.join(f'<article class="source-card"><div><b>{sid}</b><a href="{html.escape(url,quote=True)}" target="_blank" rel="noopener">{html.escape(title)}</a></div><p>{html.escape(scope)}</p><small>Checked {date} · {html.escape(url)}</small></article>' for sid,title,url,date,scope in CONTENT.SOURCES)
    doc='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>UK Medical Ecommerce | Complete Project Plan</title><style>
:root{--navy:#142d45;--teal:#087f79;--ink:#2d4155;--muted:#65788b;--line:#dce6ed}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:25px}body{margin:0;font:15px/1.68 "Segoe UI",Arial,sans-serif;color:var(--ink);background:#eef3f7}a{color:var(--teal)}.rail{position:fixed;inset:0 auto 0 0;width:276px;background:var(--navy);color:white;padding:28px 20px;overflow:auto;z-index:20}.brand{font-size:19px;font-weight:700;line-height:1.3;margin:0 8px 4px}.rail small{display:block;margin:0 8px 22px;color:#a7bfd3;font-size:11px}.rail nav a{display:block;color:#d3e0eb;text-decoration:none;font-size:12px;padding:7px 10px;border-radius:5px;line-height:1.4}.rail nav a:hover,.rail nav a.active{background:#ffffff11;color:white}.nav-group{display:block;margin:22px 10px 7px;color:#7fbebd;font-size:9px;letter-spacing:1.1px;text-transform:uppercase;font-weight:700}.workspace{margin-left:276px;padding:30px 36px 50px;max-width:1500px}.toolbar{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:22px;font-size:11px;color:var(--muted)}.button,.small-button{display:inline-block;background:var(--navy);color:white;text-decoration:none;padding:10px 15px;border-radius:6px;font-size:12px;font-weight:600}.small-button{background:#eaf5f1;color:var(--teal);margin:0 0 18px}.cover{background:var(--navy);border-radius:11px;padding:44px;color:#e0ebf3;overflow:hidden;position:relative}.cover:after{content:"";width:350px;height:350px;position:absolute;right:-110px;top:-160px;border:1px solid #ffffff13;border-radius:50%;pointer-events:none}.kicker{color:#93c7c8;font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase}.cover h1{font-size:42px;letter-spacing:-1.2px;line-height:1.15;margin:15px 0;color:white;max-width:650px}.cover>p{max-width:760px;font-size:15px;line-height:1.7;color:#c9dae7}.metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:27px}.metrics div{padding:15px 18px;background:#ffffff0c;border:1px solid #ffffff15;border-radius:6px}.metrics strong{display:block;font-size:19px;color:#a7e4d6}.metrics span{font-size:10px;color:#bed0e0}.reading-note{margin:20px 0 30px;padding:18px 22px;border-left:3px solid var(--teal);background:#e3f0ec;color:#355954;font-size:13px}.chapter{margin:0 0 26px;padding:32px 36px 30px;background:white;border:1px solid var(--line);border-radius:9px;scroll-margin-top:20px}.section-top{display:flex;justify-content:space-between;gap:12px;color:var(--teal);font-size:10px;text-transform:uppercase;letter-spacing:1px;font-weight:700}.section-top span:last-child{color:#8291a1;font-weight:400;letter-spacing:0}.chapter h2{font-size:27px;line-height:1.25;color:var(--navy);letter-spacing:-.6px;margin:12px 0}.chapter .intro{font-size:16px;color:#697f92;line-height:1.65;margin-bottom:24px}.chapter p{margin:0 0 16px}.chapter h3{font-size:17px;color:var(--navy);margin:25px 0 10px}.chapter li{padding:3px 0}.table-wrap{overflow-x:auto;margin:20px 0 24px}table{border-collapse:collapse;width:100%;font-size:13px;line-height:1.55}th{text-align:left;background:var(--navy);color:white;font-size:12px;padding:12px 14px}td{padding:12px 14px;border-bottom:1px solid var(--line);vertical-align:top}tr:nth-child(even) td{background:#f4f8fa}td:first-child{font-weight:600;color:var(--navy);min-width:120px}.callout{background:#edf7f4;border:1px solid #c9e5dc;padding:17px 20px;border-radius:6px;margin:21px 0}.callout strong{color:var(--teal)}.callout p{font-size:13px;line-height:1.7;margin:7px 0 0}.callout.amber{background:#fff8ec;border-color:#edd9b8}.callout.amber strong{color:#8c5f18}.chapter-sources{font-size:10px;color:#7c8e9e;margin-top:24px;padding-top:14px;border-top:1px solid var(--line)}.chapter-sources a{margin-right:7px}.source-card{padding:15px 0;border-bottom:1px solid var(--line)}.source-card div{display:flex;gap:14px;align-items:baseline}.source-card b{font-size:11px;min-width:32px;color:var(--navy)}.source-card p{font-size:12px;margin:7px 0;color:var(--muted)}.source-card small{font-size:10px;overflow-wrap:anywhere;color:#7c8e9e}.menu{display:none;border:1px solid var(--line);background:white;padding:8px 12px;border-radius:6px;color:var(--navy);font:600 12px "Segoe UI",Arial}.scrim{display:none}.footer-note{font-size:11px;color:var(--muted);padding:6px 4px}a:focus-visible,button:focus-visible{outline:3px solid #39b9a7;outline-offset:3px}
@media(min-width:1500px){.workspace{max-width:1420px;margin-left:auto;margin-right:auto;padding-left:310px}}@media(max-width:1000px){.rail{width:235px;padding:22px 13px}.workspace{margin-left:235px;padding:23px}.chapter{padding:26px}.cover{padding:30px}.cover h1{font-size:34px}.metrics{gap:8px}.metrics div{padding:12px}.metrics strong{font-size:16px}}@media(max-width:740px){.rail{width:276px;transform:translateX(-100%);transition:transform .18s}.rail.open{transform:translateX(0)}.workspace{margin:0;padding:16px}.menu{display:block}.toolbar{flex-wrap:wrap}.toolbar>span{display:none}.cover{padding:28px 24px}.cover h1{font-size:33px}.cover>p{font-size:14px}.metrics{grid-template-columns:1fr}.metrics div{display:flex;justify-content:space-between;align-items:center}.metrics strong{font-size:16px}.chapter{padding:23px 21px}.chapter h2{font-size:24px}.chapter .intro{font-size:15px}.chapter p{font-size:14px}.section-top{font-size:8px}th,td{padding:10px;min-width:110px}table{min-width:450px}.scrim.open{display:block;position:fixed;inset:0;background:#142d4566;z-index:19}}
</style></head><body><aside class="rail" id="rail"><div class="brand">Medical ecommerce<br>Project plan</div><small>UK first · Full project documentation</small><nav aria-label="Document contents">__NAV__<span class="nav-group">Evidence</span><a href="#sources">Sources and scope</a></nav></aside><div class="scrim" id="scrim"></div><main class="workspace"><div class="toolbar"><button class="menu" id="menu" aria-controls="rail" aria-expanded="false">Contents</button><span>PROJECT DOCUMENTATION · 8 NOVEMBER 2026</span><a class="button" href="../pdf/UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.pdf">Open full PDF</a></div><header class="cover"><div class="kicker">Business scope / UK selling rules / Implementation</div><h1>A complete plan for<br>UK medical ecommerce</h1><p>A new own-stock retailer for consumers and verified professionals. This document explains what we will build, how it will operate, the requirements to sell, the implementation and the costs.</p><div class="metrics"><div><strong>25-day target</strong><span>First selling phase</span></div><div><strong>Full-range ambition</strong><span>Activation after review</span></div><div><strong>UK first</strong><span>Europe through country releases</span></div></div></header><div class="reading-note"><strong>The complete document is detailed.</strong> Only the Day 25 roadmap is condensed to a single page. Cost figures are clearly labelled planning inputs; product permissions, providers, legal operator and final quote require the actual business decisions.</div>__SECTIONS__<section class="chapter" id="sources"><div class="section-top"><span>Evidence and applicability</span></div><h2>Sources, dates and scope</h2><p class="intro">Primary sources support requirements within the stated market/product/activity. Links open the exact source. Access limitations are recorded alongside the references.</p>__SOURCES__</section><p class="footer-note">Local planning documentation. No store, merchant account, licence or campaign was deployed through this work. Editable source: docs/content/project_plan_content.py.</p></main><script>
const rail=document.getElementById('rail'),menu=document.getElementById('menu'),scrim=document.getElementById('scrim');function setMenu(open){rail.classList.toggle('open',open);scrim.classList.toggle('open',open);menu.setAttribute('aria-expanded',String(open))}menu.addEventListener('click',()=>setMenu(!rail.classList.contains('open')));scrim.addEventListener('click',()=>setMenu(false));document.addEventListener('keydown',e=>{if(e.key==='Escape'){setMenu(false);menu.focus()}});document.querySelectorAll('.rail a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));const observer=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){document.querySelectorAll('.rail a').forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+e.target.id))}}},{rootMargin:'-10% 0px -70% 0px'});document.querySelectorAll('.chapter').forEach(e=>observer.observe(e));
</script></body></html>'''
    doc=doc.replace('__NAV__',''.join(nav)).replace('__SECTIONS__',''.join(sections)).replace('__SOURCES__',sources)
    path=HTML_DIR/'UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.html'; path.write_text(doc,encoding='utf-8')
    return path


def create_markdown(page_map):
    lines=['# UK medical ecommerce project plan','',CONTENT.SUBTITLE,'',f'Dated {CONTENT.DATE}. Full project documentation; only the Day 25 roadmap is condensed to one PDF page.','']
    for ch in CONTENT.CHAPTERS:
        lines += ['## '+ch['title'],'',ch['intro'],'']
        for b in ch['blocks']:
            if b['kind']=='p': lines += [b['text'],'']
            elif b['kind']=='h': lines += ['### '+b['text'],'']
            elif b['kind']=='list': lines += ['- '+t for t in b['items']]+['']
            elif b['kind']=='callout': lines += ['**'+b['title']+'**', '',b['text'],'']
            elif b['kind']=='table':
                lines += ['| '+' | '.join(b['headers'])+' |','| '+' | '.join(['---']*len(b['headers']))+' |']
                lines += ['| '+' | '.join(row)+' |' for row in b['rows']]+['']
        if ch['refs']: lines += ['Sources: '+', '.join('['+sid+']('+SOURCES[sid][2]+')' for sid in ch['refs'])+'.','']
    lines += ['## Primary source register','']
    for sid,title,url,date,scope in CONTENT.SOURCES: lines += [f'- **{sid}** [{title}]({url}). Checked {date}. Scope: {scope}.']
    path=ROOT/'docs/plans/UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.md';path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return path


if __name__=='__main__':
    mapping,ranges,pages=build_pdf(BytesIO())
    pdf_path=PDF_DIR/'UK_MEDICAL_ECOMMERCE_PROJECT_PLAN.pdf'
    final_map,final_ranges,final_pages=build_pdf(str(pdf_path),mapping,pages)
    assert pages==final_pages and mapping==final_map
    day_start,day_end=final_ranges['day-25']; assert day_start==day_end
    doc=pymupdf.open(pdf_path); extract=pymupdf.open();extract.insert_pdf(doc,from_page=day_start-1,to_page=day_start-1)
    page=extract[0]
    page.draw_rect(pymupdf.Rect(WIDTH-100,HEIGHT-35,WIDTH,HEIGHT-8),color=None,fill=(1,1,1),overlay=True)
    page.insert_text((WIDTH-65,HEIGHT-25),'1 / 1',fontsize=7,color=(.39,.47,.54))
    roadmap=PDF_DIR/'UK_MEDICAL_ECOMMERCE_25_DAY_ROADMAP.pdf';extract.save(roadmap)
    html_path=create_html(final_map);md_path=create_markdown(final_map)
    report={'full_pdf':pdf_path.relative_to(ROOT).as_posix(),'pages':final_pages,'day_25_page':day_start,'roadmap_pdf':roadmap.relative_to(ROOT).as_posix(),'html':html_path.relative_to(ROOT).as_posix(),'markdown':md_path.relative_to(ROOT).as_posix(),'chapter_pages':final_ranges}
    (ROOT/'docs/registers/PROJECT_PLAN_PAGE_MAP.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
