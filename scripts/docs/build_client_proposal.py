"""Build the illustrated, client-facing proposal without a development fee."""
from pathlib import Path
import importlib.util
import html
import json
import re
import shutil
from urllib.parse import urlsplit
from decimal import Decimal

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
def module(name, file):
    s=importlib.util.spec_from_file_location(name, ROOT/file)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
C = module("client_content", "docs/content/client_proposal_content.py")
OLD = module("plan_content", "docs/content/project_plan_content.py")
OUT = ROOT / "deliverables/pdf/UK_MEDICAL_ECOMMERCE_CLIENT_PROPOSAL.pdf"
ASSET = ROOT / "assets/proposal/shishir-sabbir-portrait.png"
ASSET.parent.mkdir(parents=True,exist_ok=True)
if not ASSET.exists(): shutil.copy2("C:/Users/shishirsabbir/Downloads/Portrait.png", ASSET)
OUT.parent.mkdir(parents=True,exist_ok=True)

NAVY, TEAL, GOLD, INK, MUTED, PALE, LINE = map(HexColor,["#102B3F","#087E83","#F2C94C","#263D4A","#5D7180","#EFF6F5","#DAE5E8"])
WHITE=HexColor("#FFFFFF")
W,H=A4; X=40; CW=W-80
FONT,BOLD="Proposal","Proposal-Bold"
for n,f in [(FONT,"segoeui.ttf"),(BOLD,"segoeuib.ttf")]:
    pdfmetrics.registerFont(TTFont(n,str(Path("C:/Windows/Fonts")/f)))
pdfmetrics.registerFontFamily(FONT,normal=FONT,bold=BOLD,italic=FONT,boldItalic=BOLD)

UPDATED = set("R01 R03 R04 R05 R06 R08 R09 C01 C02 C04 C05 M01 M02 M03 M04 M05 M06 T01 T02 T03 T04 T07 T08 T09 T10 E01 P01".split())
sources = {r[0]:list(r) for r in OLD.SOURCES}
for k in UPDATED: sources[k][3]="9 Nov 2026"
sources["R06"][4]="UK human medicines; manufacturing/wholesale permissions; direct guidance checked"
sources["P01"][4]="UK electronic mail; official indexed consent/soft-opt-in passages"
sources.update({r[0]:list(r) for r in [
 ("R11","GPhC distance pharmacy guidance","https://assets.pharmacyregulation.org/files/2025-02/gphc-guidance-registered-pharmacies-providing-pharmacy-services-distance-february-2025.pdf","9 Nov 2026","GB registered pharmacies; February 2025 guidance, professional responsibilities"),
 ("R12","OPSS general product safety","https://www.gov.uk/government/publications/general-product-safety-regulations-2005/general-product-safety-regulations-2005-great-britain","9 Nov 2026","GB general goods/uncovered risks; official indexed guidance"),
 ("E02","European Commission VAT One Stop Shop","https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en","9 Nov 2026","EU OSS/IOSS schemes; transaction and stock-location conditions"),
 ("E03","European Accessibility Act","https://eur-lex.europa.eu/eli/dir/2019/882/oj","9 Nov 2026","EU ecommerce services; national implementation and exemptions"),
 ("E04","EU packaging producer responsibility","https://environment.ec.europa.eu/topics/waste-and-recycling/packaging-waste/extended-producer-responsibility-packaging-small-businesses_en","9 Nov 2026","EU/national packaging duties; proposed suspension is not enacted exemption"),
 ("E05","European Commission product safety","https://commission.europa.eu/topics/business-and-industry/product-safety_en","9 Nov 2026","EU consumer product safety; sector-specific legislation considered separately"),
 ("E06","EU low-value import duty guidance","https://taxation-customs.ec.europa.eu/news/guidance-and-legal-text-temporary-flat-fee-low-value-imports-which-will-apply-until-1-july-2028-2026-06-08_en","9 Nov 2026","Affected low-value imports from 1 July 2026; official indexed guidance"),
 ("E07","European Commission batteries","https://environment.ec.europa.eu/topics/waste-and-recycling/batteries_en","9 Nov 2026","EU batteries; role-specific obligations, official indexed text"),
 ("E08","Swedish authority: EEE producer responsibility","https://www.naturvardsverket.se/en/guidance/extended-producer-responsibility-epr/producer-responsibility-for-electrical-and-electronic-equipment/","9 Nov 2026","Swedish WEEE implementation example; not clearance for other destinations"),
 ("S01","Google: helpful, reliable content","https://developers.google.com/search/docs/fundamentals/creating-helpful-content","9 Nov 2026","Organic Google Search; content quality principles"),
 ("S02","Google: share ecommerce product data","https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google","9 Nov 2026","Organic product discovery, structured data and Merchant Center"),
 ("S03","Bing Webmaster Guidelines","https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a","9 Nov 2026","Official indexed guidelines; direct page is a JavaScript shell")
]})
# The country-review checklist includes environmental product routes as applicable.
next(p for p in C.PAGES if p["id"]=="europe")["refs"] += ["E07","E08"]
used={r for p in C.PAGES for r in p["refs"]}
SOURCES=[sources[k] for k in sorted(used)]
for p in C.PAGES:
    for k in p["refs"]: assert k in sources,k

def clean(t):
    return str(t).replace("\u2013","-").replace("\u2014","-").replace("\u2011","-")
def rich(t):
    return re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",html.escape(clean(t))).replace("\n","<br/>")
def para(t,size=10.2,color=INK,bold=False,leading=None):
    return Paragraph(rich(t),ParagraphStyle("p",fontName=BOLD if bold else FONT,fontSize=size,leading=leading or size*1.34,textColor=color))

class Document:
    def __init__(self):
        self.c=canvas.Canvas(str(OUT),pagesize=A4,pageCompression=1)
        self.c.setTitle("Medical E-commerce - Project Proposal | Shishir Sabbir")
        self.c.setAuthor("Shishir Sabbir")
        self.c.setSubject("UK and Europe; four phases; assumed 15 November 2026 kickoff; running costs, hours and AI tokens")
        self.map={}; self.ends={}; self.icon_count=0
    def box(self,x,y,w,h,fill,stroke=None,r=8):
        c=self.c;c.setFillColor(fill);c.setStrokeColor(stroke or fill)
        c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=bool(stroke))
    def text(self,t,x,y,w,size=10.2,color=INK,bold=False,leading=None):
        a=para(t,size,color,bold,leading);_,h=a.wrap(w,2000);a.drawOn(self.c,x,H-y-h);return h
    def line(self,x,y,x2,y2,color=LINE,width=1):
        self.c.setStrokeColor(color);self.c.setLineWidth(width);self.c.line(x,H-y,x2,H-y2)
    def icon(self,name,x,y,size=23,color=TEAL):
        self.icon_count+=1;c=self.c;c.saveState();c.translate(x,H-y-size);c.scale(size/24,size/24)
        c.setStrokeColor(color);c.setFillColor(color);c.setLineWidth(1.65);c.setLineCap(1);c.setLineJoin(1)
        def path(points,close=False):
            p=c.beginPath();p.moveTo(*points[0]);[p.lineTo(*q) for q in points[1:]]
            if close:p.close()
            c.drawPath(p,stroke=1,fill=0)
        if name in ("shield","check"):
            if name=="shield":path([(12,22),(21,18),(20,9),(17,4),(12,1),(7,4),(4,9),(3,18),(12,22)])
            else:c.circle(12,12,10,stroke=1,fill=0)
            path([(7,12),(10.5,8.5),(17,15)])
        elif name=="box":
            path([(2,17),(12,22),(22,17),(22,6),(12,1),(2,6),(2,17)]);path([(2,17),(12,12),(22,17)]);path([(12,12),(12,1)]);path([(7,19.5),(17,14.5),(17,10)])
        elif name in ("screen","code"):
            c.roundRect(1,5,22,17,2,stroke=1,fill=0);path([(7,1),(17,1)]);path([(12,5),(12,1)])
            if name=="code":path([(8,17),(5,13),(8,9)]);path([(16,17),(19,13),(16,9)])
            else:path([(5,10),(9,14),(13,11),(19,18)])
        elif name=="globe":
            c.circle(12,12,10,stroke=1,fill=0);c.ellipse(7,2,17,22,stroke=1,fill=0);path([(2,12),(22,12)]);path([(4,18),(20,18)]);path([(4,6),(20,6)])
        elif name=="search":c.circle(10,14,7,stroke=1,fill=0);path([(15,9),(22,2)])
        elif name=="users":
            c.circle(9,17,4,stroke=1,fill=0);c.arc(1,0,17,12,0,180);c.arc(14,13,22,21,270,180);c.arc(15,1,24,12,0,90)
        elif name=="clipboard":
            c.roundRect(3,1,18,20,2,stroke=1,fill=0);c.roundRect(8,18,8,5,1,stroke=1,fill=0)
            for a in [7,11,15]:path([(7,a),(17,a)])
        elif name=="receipt":
            path([(4,1),(4,23),(7,21),(10,23),(13,21),(16,23),(20,21),(20,1),(17,3),(14,1),(11,3),(8,1),(4,1)])
            path([(8,16),(16,16)]);path([(8,11),(16,11)]);path([(8,7),(13,7)])
        elif name=="truck":
            c.rect(1,6,13,13,stroke=1,fill=0);path([(14,6),(23,6),(23,13),(19,17),(14,17)]);c.circle(6,4,2.5,stroke=1,fill=0);c.circle(18,4,2.5,stroke=1,fill=0)
        elif name=="card":c.roundRect(1,4,22,16,3,stroke=1,fill=0);path([(1,15),(23,15)]);path([(5,8),(10,8)])
        elif name=="lock":
            c.roundRect(3,1,18,13,2,stroke=1,fill=0);c.arc(7,9,17,24,0,180);path([(7,17),(7,14)]);path([(17,17),(17,14)]);c.circle(12,8,1,stroke=1,fill=0);path([(12,7),(12,5)])
        elif name=="mail":c.roundRect(1,4,22,16,2,stroke=1,fill=0);path([(2,19),(12,10),(22,19)])
        elif name=="phone":
            c.roundRect(6,1,12,22,2,stroke=1,fill=0);path([(10,19),(14,19)]);c.circle(12,4,0.7,stroke=1,fill=0)
        elif name=="chart":
            path([(2,22),(2,2),(23,2)]);path([(5,8),(10,13),(15,10),(22,20)]);path([(16,20),(22,20),(22,14)])
        elif name=="calendar":
            c.roundRect(2,2,20,19,2,stroke=1,fill=0);path([(2,16),(22,16)]);path([(7,23),(7,19)]);path([(17,23),(17,19)]);path([(7,10),(10,7),(17,13)])
        elif name=="layers":
            path([(1,16),(12,22),(23,16),(12,10),(1,16)]);path([(1,11),(12,5),(23,11)]);path([(1,6),(12,0),(23,6)])
        elif name=="rocket":
            path([(7,9),(10,18),(17,23),(22,23),(22,18),(17,11),(9,8),(7,9)]);c.circle(17,18,2,stroke=1,fill=0);path([(7,9),(2,9),(5,15),(10,17)]);path([(15,10),(15,5),(9,2),(9,8)]);path([(5,6),(1,2)])
        else:
            path([(12,23),(15,15),(23,12),(15,9),(12,1),(9,9),(1,12),(9,15),(12,23)])
        c.restoreState()
    def footer(self,refs=()):
        self.line(X,H-50,W-X,H-50)
        self.text("SHISHIR SABBIR  /  MEDICAL ECOMMERCE PROPOSAL",X,H-36,440,7.2,MUTED)
        self.text(f"{self.c.getPageNumber():02d}",W-63,H-36,30,8,TEAL,True)
        if refs:
            tx=X; ty=H-66
            self.text("Sources",tx,ty,35,7.2,MUTED);tx+=37
            for k in refs:
                sw=pdfmetrics.stringWidth(k,FONT,7.2)+9
                self.text(k,tx,ty,sw,7.2,TEAL)
                self.c.linkURL(sources[k][2],(tx,H-ty-11,tx+sw,H-ty+1),relative=0,thickness=0);tx+=sw
    def header(self,page):
        self.c.setFillColor(WHITE);self.c.rect(0,0,W,H,fill=1,stroke=0)
        self.box(0,0,W,10,TEAL,r=0)
        self.text(page["label"],X,38,CW-60,9,TEAL,True)
        self.box(W-X-45,31,45,45,PALE,r=12);self.icon(page["icon"],W-X-35,41,25)
        y=78; y+=self.text(page["title"],X,y,CW,27,NAVY,True,31)+13
        y+=self.text(page["intro"],X,y,CW,10.8,MUTED,leading=14.6)+18
        return y
    def table(self,b,y,size=9.2):
        ws=b.get("widths") or [1/len(b["headers"])]*len(b["headers"])
        cells=[[para(t,size,WHITE,True,size*1.25) for t in b["headers"]]]
        cells += [[para(t,size,INK,False,size*1.29) for t in row] for row in b["rows"]]
        t=Table(cells,colWidths=[CW*v for v in ws])
        t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("ROWBACKGROUNDS",(0,1),(-1,-1),[PALE,WHITE]),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),("LINEBELOW",(0,1),(-1,-1),.4,LINE)]))
        _,hh=t.wrap(CW,2000);t.drawOn(self.c,X,H-y-hh);return hh+13
    def cards(self,entries,y):
        cw=(CW-14)/2; start=y
        for i in range(0,len(entries),2):
            pair=entries[i:i+2]; heights=[]
            for ic,title,body in pair:
                a=para(title,11,NAVY,True,14);_,th=a.wrap(cw-30,1000)
                a=para(body,9.7,INK,False,13);_,bh=a.wrap(cw-30,1000)
                heights.append(54+th+bh)
            rh=max(heights)
            for j,(ic,title,body) in enumerate(pair):
                x=X+j*(cw+14);self.box(x,y,cw,rh,PALE,LINE)
                self.icon(ic,x+15,y+13,23)
                th=self.text(title,x+15,y+43,cw-30,11,NAVY,True,14)
                self.text(body,x+15,y+48+th,cw-30,9.7,INK,leading=13)
            y+=rh+13
        return y-start
    def banner(self,b,y):
        gold=b.get("tone")=="gold";bg=HexColor("#FFF6D9") if gold else NAVY
        col=INK if gold else WHITE
        th=para(b["title"],11.2,col,True).wrap(CW-65,1000)[1]
        bh=para(b["text"],9.6,col,False,13).wrap(CW-65,1000)[1]
        hh=th+bh+29
        self.box(X,y,CW,hh,bg)
        self.icon("shield" if gold else "spark",X+14,y+17,22,TEAL if gold else GOLD)
        self.text(b["title"],X+47,y+12,CW-65,11.2,col,True)
        self.text(b["text"],X+47,y+17+th,CW-65,9.6,col,leading=13)
        return hh+13
    def steps(self,entries,y):
        start=y
        for n,(ic,title,body) in enumerate(entries):
            self.box(X,y,35,35,PALE,r=10);self.icon(ic,X+7,y+7,21)
            th=self.text(title,X+49,y,CW-49,11,NAVY,True,14)
            bh=self.text(body,X+49,y+th+5,CW-49,10,INK,leading=13.4)
            hh=max(42,th+bh+13)
            if n<len(entries)-1:self.line(X+17.5,y+40,X+17.5,y+hh+3,LINE,1.5)
            y+=hh+9
        return y-start
    def architecture(self,y):
        hh=146;self.box(X,y,CW,hh,PALE,LINE)
        nodes=[("screen","Next.js","Storefront"),("clipboard","React","Staff admin"),("code","API + worker","Business rules"),("box","PostgreSQL","Private data")]
        w=(CW-44)/4
        for i,(ic,a,b) in enumerate(nodes):
            x=X+12+i*(w+6);self.box(x,y+15,w,72,WHITE,LINE);self.icon(ic,x+9,y+24,22)
            self.text(a,x+9,y+51,w-18,9.5,NAVY,True);self.text(b,x+9,y+67,w-18,8,MUTED)
        self.text("HOSTINGER KVM 4",X+14,y+99,190,8.5,TEAL,True)
        self.text("CLOUDFLARE: DOMAIN + R2 MEDIA",X+205,y+99,285,8.5,TEAL,True)
        self.text("Storefront / admin call API; API / worker use PostgreSQL and R2.",X+14,y+120,CW-28,8.3,MUTED)
        return hh+13
    def budget(self,y):
        rows=[
            ["Hostinger KVM 4","$12.49","$31.24"],
            ["Cloudflare domain ($25/year allowance)","$2.08","$2.08"],
            ["R2 Standard - 100GB-month","$1.35","$1.35"],
            ["Independent backup allowance","$5.00","$5.00"],
            ["Service email - $20 / 50k tier example","$20.00","$20.00"],
            ["One mailbox / limited marketing allowances","$5 + $5","$5 + $5"],
            ["Basic monitoring / DNS / TLS","$0.00","$0.00"],
            ["Service subtotal","$50.92","$69.67"],
            ["Subtotal + $10 reserve, before tax","$60.92","$79.67"],
        ]
        return self.table({"headers":["Monthly equivalent (USD)","Initial term","VPS renewal"],"rows":rows,"widths":[.60,.20,.20]},y,8.65)
    def roadmap(self,y):
        start=y
        for i,(d,name) in enumerate(zip(C.RELEASES,["LAUNCH COMMERCE","OPERATIONAL CONTROL","REPEAT GROWTH","EXPANSION READINESS"])):
            self.box(X,y,CW,50,PALE if i else NAVY,r=7)
            self.icon(["rocket","clipboard","users","globe"][i],X+13,y+13,24,TEAL if i else GOLD)
            self.text(f"0{i+1}  {name}",X+49,y+10,245,10.1,TEAL if i else GOLD,True)
            self.text("25 elapsed days" if i==0 else "Previous release + 1 calendar month + 10 days",X+49,y+28,285,8.0,MUTED if i else WHITE)
            self.text(C.fmt(d),X+330,y+16,CW-342,12,NAVY if i else WHITE,True)
            y+=53
        return y-start+2
    def roles(self,y):
        labels=[("screen","Frontend"),("box","Data intake"),("chart","Analyst"),("code","Backend guide"),("layers","Database"),("shield","QA / security"),("rocket","Release / review")]
        w=(CW-18)/4; start=y
        for i,(ic,label) in enumerate(labels):
            col=i%4;row=i//4;x=X+col*(w+6);yy=y+row*65
            self.box(x,yy,w,57,PALE,r=6);self.icon(ic,x+10,yy+9,20)
            self.text(label,x+10,yy+34,w-20,8.8,NAVY,True)
        return 130+5
    def profile(self,y):
        hh=166; self.box(X,y,CW,hh,NAVY)
        self.c.drawImage(str(ASSET),X+10,H-y-hh+10,width=146,height=146,mask="auto")
        x=X+176
        self.text("YOUR DEVELOPMENT PARTNER",x,y+17,CW-193,8.5,GOLD,True)
        self.text("Shishir Sabbir",x,y+39,CW-193,24,WHITE,True)
        links=[("shishirsabbir.github.io","https://shishirsabbir.github.io"),("shishir.sabbir@gmail.com","mailto:shishir.sabbir@gmail.com"),("+8801883061280","tel:+8801883061280")]
        for i,(txt,url) in enumerate(links):
            yy=y+80+i*19; self.text(txt,x,yy,CW-193,10.5,WHITE)
            self.c.linkURL(url,(x,H-yy-15,x+CW-193,H-yy),relative=0,thickness=0)
        self.text("WhatsApp / Telegram",x,y+139,CW-193,8.7,GOLD)
        return hh+12
    def cover(self):
        c=self.c;c.setFillColor(NAVY);c.rect(0,0,W,H,fill=1,stroke=0)
        # Vector artwork stays crisp in print.
        c.setStrokeColor(Color(.16,.33,.40));c.setLineWidth(.6)
        for xx in range(370,650,33):c.line(xx,H-30,xx,H-350)
        for yy in range(30,355,33):c.line(365,H-yy,595,H-yy)
        self.box(X,42,335,27,TEAL,r=13)
        self.text("UNITED KINGDOM FIRST  /  EUROPE NEXT",X+15,49,315,9,WHITE,True)
        self.icon("shield",W-93,42,40,GOLD)
        self.text("Medical\nE-commerce",X,110,CW,52,WHITE,True,57)
        self.text("Built for trust.\nReady to grow.",X,242,CW,36,GOLD,True,41)
        self.text("Project proposal for an owned-stock medical retailer:\na complete storefront, advanced admin and dependable API.",X,346,CW,12.4,WHITE,leading=18)
        vals=[("rocket","25 days","First selling release"),("layers","4 phases","A staged delivery plan"),("receipt","<$100/mo*","Lean platform target")]
        ww=(CW-20)/3
        for i,(ic,a,b) in enumerate(vals):
            xx=X+i*(ww+10);self.box(xx,416,ww,94,HexColor("#1B3E50"),r=9);self.icon(ic,xx+12,428,22,GOLD)
            self.text(a,xx+12,456,ww-24,22,WHITE,True)
            self.text(b,xx+12,486,ww-24,8.5,WHITE)
        self.box(X,544,CW,214,HexColor("#F2C94C"),r=10)
        self.text("PREPARED BY",X+20,565,260,9,TEAL,True)
        self.text("Shishir\nSabbir",X+20,589,265,31,NAVY,True,35)
        self.text("shishirsabbir.github.io",X+20,674,265,10,NAVY)
        self.text("Proposal issued 9 November 2026",X+20,701,265,9,NAVY)
        self.text("Assumed kickoff 15 November 2026",X+20,720,265,9,NAVY)
        c.drawImage(str(ASSET),W-X-207,H-751,width=200,height=198,mask="auto")
        self.text("*Infrastructure and selected tools only; assumptions, taxes and exclusions on page 11.",X,778,CW,7.7,WHITE)
        self.map["cover"]=1;c.bookmarkPage("cover");c.addOutlineEntry("Project proposal","cover",level=0);c.showPage()
    def page(self,page):
        c=self.c;self.map[page["id"]]=c.getPageNumber();c.bookmarkPage(page["id"]);c.addOutlineEntry(page["title"].replace("\n"," "),page["id"],level=0)
        y=self.header(page)
        for b in page["blocks"]:
            k=b["kind"]
            if k=="p": y+=self.text(b["text"],X,y,CW,9.7 if page["id"] in ("budget","effort") else 10.1,leading=12.8 if page["id"] in ("budget","effort") else 13.5)+10
            elif k=="h":y+=self.text(b["text"],X,y,CW,12,NAVY,True)+8
            elif k=="table":y+=self.table(b,y,8.9 if page["id"] in ("uk-rules","trust","budget","day25","analytics") else 9.2)
            elif k=="cards":y+=self.cards(b["entries"],y)
            elif k=="banner":y+=self.banner(b,y)
            elif k=="steps":y+=self.steps(b["entries"],y)
            else:y+=getattr(self,k)(y)
        self.ends[page["id"]]=round(y,2)
        if y>H-70:raise RuntimeError(f"Page {page['id']} overflow: ends {y:.1f}, limit {H-70:.1f}")
        self.footer(page["refs"]);c.showPage()
    def source_pages(self):
        # Sixteen concise references per page, with clickable titles and scope/date.
        for offset in range(0,len(SOURCES),16):
            n=offset//16+1;pg={"label":f"REFERENCE NOTES / {n:02d}","icon":"clipboard","title":"Evidence behind\nthe proposal.","intro":"Clickable primary-source references. Requirements and provider terms must be rechecked before each product, country or campaign goes live."}
            self.c.bookmarkPage(f"sources{n}");self.c.addOutlineEntry(f"Sources {n}",f"sources{n}",level=0)
            y=self.header(pg)
            for key,title,url,checked,scope in SOURCES[offset:offset+16]:
                hh=self.text(f"{key}  {title}",X,y,CW,9.5,TEAL,True)
                self.c.linkURL(url,(X,H-y-hh,W-X,H-y+1),relative=0,thickness=0)
                sh=self.text(f"{checked} | {scope}",X,y+hh+3,CW,8.0,MUTED,leading=10.6)
                y+=hh+sh+11
            if y>H-76:raise RuntimeError(f"Source page {n} overflow {y}")
            if offset+16>=len(SOURCES):
                text="Financial and sales models, hours, tokens and performance targets are project-specific assumptions. No supplier quotes, customer demand study, completed country dossier or provider approvals are implied. ICO references retain their stated indexed-access limitations."
                if y+58<H-76:self.text(text,X,y+5,CW,8.5,MUTED)
            self.footer();self.c.showPage()
    def build(self):
        self.cover()
        for p in C.PAGES:self.page(p)
        self.source_pages();self.c.save()
        return self

def models():
    fx=Decimal("1.25"); other=Decimal("25")/12+Decimal("1.35")+5+20+5+5
    initial=Decimal("9.99")*fx+other;renew=Decimal("24.99")*fx+other
    result={"status":"Illustrative model, not accepted quote or measured capacity","issued":"2026-11-09","assumed_start":C.START.isoformat(),"date_rule":"Phase 1: start + 25 elapsed days; subsequent: prior release + one calendar month + 10 days; no weekend/holiday adjustment","release_dates":[d.isoformat() for d in C.RELEASES],"six_month_trading_review":C.SIX_MONTH.isoformat(),"human_hours":{"low":680,"working":760,"high":880},"ai_million_tokens":{"low":70,"working":110,"high":150,"working_input":95,"working_output":15},"usd_per_gbp_assumption":float(fx),"monthly_usd":{"initial_services":round(float(initial),2),"renewal_services":round(float(renew),2),"initial_with_reserve":round(float(initial+10),2),"renewal_with_reserve":round(float(renew+10),2),"initial_tax_sensitivity_plus_reserve":round(float(initial*Decimal('1.2')+10),2),"renewal_tax_sensitivity_plus_reserve":round(float(renew*Decimal('1.2')+10),2)},"initial_tech_cash_before_tax_reserve_usd":361.05,"development_fee":"Omitted at user's request"}
    assert result["release_dates"]==["2026-12-10","2027-01-20","2027-03-02","2027-04-12"]
    return result

if __name__=="__main__":
    d=Document().build()
    (ROOT/"docs/registers/CLIENT_PROPOSAL_PAGE_MAP.json").write_text(json.dumps({"pages":d.map,"content_bottoms":d.ends,"icons":d.icon_count},indent=2),encoding="utf-8")
    (ROOT/"docs/registers/CLIENT_PROPOSAL_SOURCES.json").write_text(json.dumps([dict(zip(["id","title","url","checked","scope"],r)) for r in SOURCES],indent=2),encoding="utf-8")
    (ROOT/"docs/models/CLIENT_PROPOSAL_MODEL.json").write_text(json.dumps(models(),indent=2),encoding="utf-8")
    print(json.dumps({"pdf":str(OUT),"chapters":len(C.PAGES),"sources":len(SOURCES),"icons":d.icon_count,"bottoms":d.ends},indent=2))
