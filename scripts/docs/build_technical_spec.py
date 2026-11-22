"""Render the editable technical specification into a designed, linked PDF."""
from pathlib import Path
from io import BytesIO
import html
import json
import re
import runpy
import math

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle, Flowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
CONTENT = runpy.run_path(str(ROOT/'docs/content/technical_spec_content.py'))
SECTIONS = CONTENT['SECTIONS']
SOURCES = {s['id']:s for s in json.loads((ROOT/'docs/registers/TECHNICAL_SPEC_SOURCES.json').read_text(encoding='utf-8'))}
OUT = ROOT/'deliverables/pdf/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
W,H=A4
L,R=42,W-42
CW=R-L
NAVY,INK,TEAL,MUTED,PALE,LINE,GOLD = map(HexColor,['#112e43','#273e50','#087f83','#5f7585','#eef6f8','#d8e4eb','#e9b65d'])
FONT,BOLD,MONO='Tech','Tech-Bold','Tech-Mono'
for name,file in [(FONT,'segoeui.ttf'),(BOLD,'segoeuib.ttf'),(MONO,'consola.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily(FONT,normal=FONT,bold=BOLD,italic=FONT,boldItalic=BOLD)

def rich(s):
    return re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',html.escape(str(s)))

def para(s,size=9.65,leading=None,color=INK,bold=False,raw=False,mono=False):
    return Paragraph(s if raw else rich(s),ParagraphStyle('p',fontName=MONO if mono else BOLD if bold else FONT,fontSize=size,leading=leading or size*1.36,textColor=color,splitLongWords=True))

def put(c,s,x,y,w,size=10,color=INK,bold=False):
    p=para(s,size,color=color,bold=bold)
    _,ph=p.wrap(w,1000); p.drawOn(c,x,y-ph)
    return ph

def icon(c,name,x,y,size=22,color=TEAL):
    c.saveState(); c.translate(x,y); c.scale(size/24,size/24)
    c.setStrokeColor(color);c.setLineWidth(1.55);c.setLineCap(1);c.setLineJoin(1)
    if name=='shield':
        p=c.beginPath();p.moveTo(12,22);p.lineTo(21,18);p.lineTo(20,9);p.curveTo(19,4,15,2,12,1);p.curveTo(9,2,5,4,4,9);p.lineTo(3,18);p.close();c.drawPath(p)
        c.line(8,12,11,9);c.line(11,9,16,15)
    elif name=='data':
        c.ellipse(3,16,21,22);c.line(3,19,3,5);c.line(21,19,21,5);c.arc(3,2,21,8,180,180);c.arc(3,9,21,15,180,180)
    elif name=='cart':
        c.line(2,21,5,21);c.line(5,21,8,7);c.line(8,7,20,7);c.line(6,17,22,17);c.line(22,17,20,10);c.line(20,10,7,10);c.circle(10,3,1.4);c.circle(18,3,1.4)
    elif name=='chart':
        c.line(3,22,3,3);c.line(3,3,22,3);c.line(6,7,11,12);c.line(11,12,15,10);c.line(15,10,21,19);c.line(16,19,21,19);c.line(21,19,21,14)
    elif name=='server':
        for y0 in (3,14):
            c.roundRect(2,y0,20,8,2);c.circle(6,y0+4,.8);c.line(12,y0+4,18,y0+4)
    elif name=='check':
        c.circle(12,12,10);c.line(6,12,10,8);c.line(10,8,18,17)
    else:
        for yy in (3,11,19):
            c.roundRect(3,yy,18,4,1)
    c.restoreState()

DIAGRAM_TEXT={
'architecture':'Customers and staff use separate hostnames. Both reach the API through a controlled reverse proxy. PostgreSQL stays private; only approved media is public.',
'storefront':'Illustrative desktop and mobile storefront: prominent search, browsable categories, clear pack prices, basket and account access. Final branding is still to be selected.',
'product':'Illustrative product view: image, exact identity, pack size, price including applicable VAT, availability, purchase eligibility, evidence and delivery terms.',
'customer-auth':'Register -> generic response -> verify email -> sign in -> opaque customer session. Every commerce request then passes server-side ownership and eligibility checks.',
'staff-auth':'Controlled invitation -> verify and set password -> confirm TOTP -> complete MFA sign-in -> staff session -> permission and fresh-auth checks.',
'admin':'Illustrative admin: task queues, catalogue, stock, orders, compliance and reporting, with permission-controlled actions and an audit trail.',
'media':'Upload -> private quarantine -> validation/scan -> worker optimises -> prepared public variants. Evidence remains private and is accessed only after authorisation.',
'data':'Products have variants and evidence; variants link lots/stock and order lines. Customers link orders and entitlements; orders link payments, shipments and returns. Audit/outbox records support the transactions.',
'order-state':'Commercial, payment, review and fulfilment states are separate. Capture and release happen only after eligibility/stock checks; failures enter an operator-visible exception path.',
'outbox':'One database transaction stores the business change plus outbox event. A worker performs the external action, then acknowledges; retries require idempotency and reconciliation.',
'scores':'Public-template targets: Lighthouse SEO100, performance90+ mobile/95+ desktop, manual WCAG2.2AA. Field p75 LCP<=2.5s, INP<=200ms, CLS<=0.1 when enough data exists.'}

class Diagram(Flowable):
    def __init__(self,name):
        Flowable.__init__(self);self.name=name;self.width=CW
        self.height={'architecture':240,'storefront':239,'product':211,'customer-auth':130,'staff-auth':140,'admin':218,'media':170,'data':195,'order-state':177,'outbox':150,'scores':123}[name]
    def draw(self):
        c=self.canv;hh=self.height
        c.setFillColor(PALE);c.setStrokeColor(LINE);c.roundRect(0,0,CW,hh,8,stroke=1,fill=1)
        def box(x,y,w,h,label='',body='',dark=False):
            c.setFillColor(NAVY if dark else white);c.setStrokeColor(LINE)
            c.roundRect(x,hh-y-h,w,h,5,stroke=not dark,fill=1)
            if label: put(c,label,x+9,hh-y-8,w-18,8.8,white if dark else NAVY,True)
            if body: put(c,body,x+9,hh-y-25,w-18,7.65,HexColor('#d6e9f1') if dark else MUTED)
        def txt(s,x,y,w,size=8,color=MUTED,bold=False): return put(c,s,x,hh-y,w,size,color,bold)
        def arrow(x1,y1,x2,y2):
            c.setStrokeColor(TEAL);c.setLineWidth(1.05);c.line(x1,hh-y1,x2,hh-y2)
            angle=math.atan2(y2-y1,x2-x1)
            for d in (-.55,.55):
                c.line(x2,hh-y2,x2-5*math.cos(angle+d),hh-y2+5*math.sin(angle+d))
        n=self.name
        if n=='architecture':
            box(14,15,150,46,'CUSTOMER','www.<domain> / Next.js')
            box(178,15,150,46,'STAFF','admin.<domain> / React')
            box(346,15,151,46,'EXTERNAL SERVICES','Payments / email / carriers')
            arrow(89,61,89,80);arrow(253,61,253,80)
            box(14,80,314,40,'CLOUDFLARE + NGINX','TLS / allowlisted hosts / same-origin API',True)
            arrow(88,120,88,137)
            box(14,137,148,46,'API / PRIVATE NETWORK','Auth, policy and transactions',True)
            box(179,137,149,46,'WORKER','Jobs, feeds and reconciliation',True)
            c.setStrokeColor(TEAL);c.line(421,hh-61,421,hh-100);arrow(421,100,328,100)
            box(346,137,151,46,'R2 STORAGE','Public media / private evidence')
            arrow(88,183,88,202);arrow(253,183,253,202)
            box(14,202,314,26,'POSTGRESQL  /  No public database port')
            txt('External callbacks enter only verified API routes.',346,196,151,7.8)
        elif n=='storefront':
            box(13,14,347,211)
            box(26,26,321,24,'BRAND    |    Search product name, brand or SKU',dark=True)
            txt('Products     Clinical supplies     Equipment     Guides',28,57,315,7.2)
            box(26,76,321,47,'Supplies for everyday care','Browse approved categories. Clear pack sizes and availability.')
            for i,label in enumerate(['Dressings','Diagnostics','Hygiene']):
                x=26+i*109;box(x,134,103,77,label,'Product image\nPack / price / stock')
                c.setFillColor(TEAL);c.roundRect(x+9,hh-201,84,12,3,stroke=0,fill=1)
            box(377,14,120,211)
            box(386,26,102,23,'BRAND     Cart',dark=True)
            box(386,58,102,24,'Search products')
            box(386,91,102,44,'Shop supplies','Explore categories')
            box(386,144,102,66,'Product card','Image / pack price\nStock / add to basket')
        elif n=='product':
            box(14,15,215,179,'PRODUCT IMAGE','Prepared, responsive variants')
            c.setStrokeColor(LINE);c.roundRect(67,hh-142,108,88,8);c.line(84,hh-112,111,hh-84);c.line(111,hh-84,155,hh-127)
            box(245,15,252,179,'Clear product title','Brand / manufacturer reference / GTIN')
            txt('Correct pack size + variant selector',258,66,224,9,NAVY,True)
            txt('Total price incl. applicable VAT\nAvailability / approved buyer restriction',258,89,224,9)
            c.setFillColor(TEAL);c.roundRect(258,hh-148,225,25,4,stroke=0,fill=1)
            txt('Quantity     |     Add to basket',271,128,196,8.8,white,True)
            txt('Delivery  /  Documents  /  Returns',258,164,224,8)
        elif n=='customer-auth':
            labels=[('REGISTER','Email + password'),('VERIFY EMAIL','Single-use link'),('SIGN IN','Opaque session'),('API CHECKS','Owner + eligibility')]
            for i,(a,b) in enumerate(labels):
                x=14+i*125;box(x,15,108,59,a,b,i==3)
                if i<3:arrow(x+108,44,x+123,44)
            txt('RESET PATH',16,91,85,7.5,TEAL,True)
            txt('Generic request -> short-lived link -> new password -> revoke previous sessions',104,91,389,8.3)
        elif n=='staff-auth':
            steps=[('INVITE','Owner controlled'),('VERIFY','Email + password'),('ENROL MFA','Confirm TOTP')]
            for i,(a,b) in enumerate(steps):
                x=14+i*169;box(x,12,145,45,a,b)
                if i<2:arrow(x+145,36,x+165,36)
            arrow(425,57,425,73)
            box(14,73,314,44,'STAFF API GUARD','Correct realm + permission + completed MFA',True)
            box(352,73,145,44,'MFA SIGN-IN','Every new staff session')
            arrow(352,96,329,96)
            txt('Sensitive actions additionally require fresh authentication within five minutes.',16,125,481,7.6)
        elif n=='admin':
            box(14,14,483,190)
            c.setFillColor(NAVY);c.roundRect(14,hh-204,111,190,5,stroke=0,fill=1)
            txt('OPERATIONS',25,29,89,8.5,white,True)
            for i,t in enumerate(['Overview','Orders','Catalogue','Stock / lots','Product approval','Customers','Reports']):txt(t,25,58+i*18,90,7.8,HexColor('#d5e7ee'))
            txt('Today / needs attention',139,26,332,12,NAVY,True)
            for i,(a,b) in enumerate([('Orders','Ready to pick'),('Stock','Low / expiring'),('Review','Evidence due')]):box(139+i*116,53,108,50,a,b)
            box(139,114,344,76,'WORK QUEUE','Reference       Status        Owner        Next action')
            c.setStrokeColor(LINE)
            for yy in (150,166,182):c.line(150,hh-yy,472,hh-yy)
        elif n=='media':
            for i,(a,b) in enumerate([('UPLOAD','Private quarantine'),('VALIDATE','Size / type / scan'),('OPTIMISE','Sharp worker')]):
                x=14+i*169;box(x,20,145,48,a,b)
                if i<2:arrow(x+145,44,x+165,44)
            arrow(424,68,424,90)
            box(267,90,230,53,'PUBLIC MEDIA','320 / 640 / 1280 widths; immutable keys',True)
            box(14,90,230,53,'PRIVATE EVIDENCE','Authorise access; short-lived signed URL')
            txt('Originals and private documents are never exposed by a public bucket rule.',16,151,481,7.8)
        elif n=='data':
            box(14,15,144,49,'CUSTOMERS','Accounts / entitlements')
            box(184,15,144,49,'ORDERS','Immutable line snapshots',True)
            box(354,15,143,49,'PAYMENTS','Attempts / events / refunds')
            arrow(158,40,184,40);arrow(328,40,354,40)
            box(14,89,144,49,'PRODUCTS','Variants / market evidence')
            box(184,89,144,49,'STOCK','Lots / moves / reservations',True)
            box(354,89,143,49,'FULFILMENT','Shipments / returns / recalls')
            arrow(158,114,184,114);arrow(256,64,256,89);arrow(328,114,354,114)
            box(14,148,483,31,'CROSS-CUTTING   Audit log / webhook inbox / transactional outbox')
        elif n=='order-state':
            rows=[('ORDER','Pending payment  ->  Confirmed  ->  Completed / cancelled'),('PAYMENT','Created  ->  Pending  ->  Captured / failed / refunded'),('REVIEW','Pending evidence  ->  Approved / rejected / expired'),('FULFILMENT','Unallocated  ->  Reserved  ->  Picked  ->  Shipped / returned')]
            for i,(a,b) in enumerate(rows):
                box(14,14+i*34,111,27,a,dark=i==0)
                txt(b,139,20+i*34,351,8.2)
            txt('Exceptions: late capture, price conflict, recall, short stock, duplicate/late event.',16,155,481,8,TEAL)
        elif n=='outbox':
            box(14,20,150,63,'DATABASE TRANSACTION','Business change + event\nCommit together',True)
            box(190,20,135,63,'WORKER','Claim -> act -> acknowledge')
            box(352,20,145,63,'EXTERNAL SERVICE','Provider idempotency\nVerified response')
            arrow(164,51,190,51);arrow(325,51,352,51)
            txt('RETRY SAFELY',16,105,98,8,TEAL,True)
            txt('A crash can repeat delivery. Store business keys, compare state, reconcile and surface failures.',120,103,373,8.4)
        elif n=='scores':
            for i,(a,b) in enumerate([('100','SEO / public pages'),('90+','Mobile performance'),('95+','Desktop performance'),('AA','Manual accessibility')]):
                x=14+i*125;box(x,12,108,65)
                txt(a,x+10,19,88,22,TEAL,True);txt(b,x+10,53,90,7.5)
            txt('FIELD TARGETS',17,89,97,7.7,TEAL,True)
            txt('LCP <=2.5s    INP <=200ms    CLS <=0.1  /  p75',121,87,375,10,NAVY,True)
            txt('Technical acceptance targets; not a ranking or sales guarantee.',17,109,480,7.5)

def flows(block):
    k=block['kind']
    if k=='p': return [(para(block['text']),9)]
    if k=='h': return [(para(block['text'],12.1,color=NAVY,bold=True),7)]
    if k=='diagram':return [(Diagram(block['name']),14)]
    if k=='table':
        ratios=block.get('widths') or [1/len(block['headers'])]*len(block['headers'])
        cells=[[para(s,8.8,color=white,bold=True) for s in block['headers']]]
        cells += [[para(s,9,12.1) for s in row] for row in block['rows']]
        t=Table(cells,colWidths=[CW*r for r in ratios],repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[PALE,white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,1),(-1,-1),.4,LINE)]))
        return [(t,12)]
    if k in ('callout','requirement'):
        requirement=k=='requirement';amber=block.get('tone')=='amber'
        title=(block['id']+'  /  '+block['phase']+' acceptance') if requirement else block['title']
        items=[para(title,9.3,color=TEAL,bold=True)]
        if requirement:items += [para(block['text'],9.5,bold=True),para(block['acceptance'],9.25)]
        else:items += [para(block['text'],9.4)]
        t=Table([[items]],colWidths=[CW],hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),HexColor('#fff7e8') if amber else HexColor('#eaf6f3')),('LINEBEFORE',(0,0),(0,-1),3,GOLD if amber else TEAL),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),11)]))
        return [(t,12)]
    if k=='code':
        text='<br/>'.join(html.escape(line).replace(' ','&#160;') for line in block['text'].splitlines())
        t=Table([[para(text,8.1,11.3,color=HexColor('#d7ecf2'),raw=True,mono=True)]],colWidths=[CW])
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),NAVY),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),12),('BOTTOMPADDING',(0,0),(-1,-1),12)]))
        return [(t,12)]
    raise ValueError(k)

def build(target,known=None,total=None):
    c=canvas.Canvas(target,pagesize=A4,pageCompression=1)
    c.setTitle('Medical E-commerce | Detailed Technical Specification')
    c.setAuthor('Shishir Sabbir')
    c.setSubject('Proposed implementation baseline: storefront, identity, API, data, commerce, SEO and operations')
    page_map={};section_pages={}
    def footer(refs=()):
        c.setStrokeColor(LINE);c.line(L,54,R,54)
        c.setFont(FONT,7);c.setFillColor(MUTED)
        c.drawString(L,25,'TECHNICAL SPECIFICATION  /  9 NOV 2026  /  PROPOSED BASELINE')
        c.drawRightString(R,25,f'{c.getPageNumber():02d}'+(f' / {total:02d}' if total else ''))
        if refs:
            c.setFont(FONT,6.5);c.drawString(L,41,'References:');x=L+40
            for sid in refs:
                label=sid+'  ';w=pdfmetrics.stringWidth(label,FONT,6.5)
                c.setFillColor(TEAL);c.drawString(x,41,label);c.linkURL(SOURCES[sid]['url'],(x,38,x+w,49),thickness=0);x+=w
    def heading(s,continued=False):
        c.setFillColor(NAVY);c.rect(0,H-8,W,8,stroke=0,fill=1)
        c.setFont(BOLD,7.6);c.setFillColor(TEAL);c.drawString(L,H-35,s['group'].upper())
        typ={'01':'server','02':'cart','03':'shield','04':'layers','05':'data','06':'layers','07':'chart','08':'shield','09':'server','10':'check'}.get(s['group'][:2],'layers')
        icon(c,typ,R-24,H-71,24)
        title=s['title']+(' / continued' if continued else '')
        ph=put(c,title,L,H-55,CW-42,21 if continued else 24,NAVY,True)
        y=H-55-ph-12
        if not continued:y-=put(c,s['intro'],L,y,CW,10.5,MUTED)+17
        return y
    def newpage(s,continued=True):
        footer(s.get('refs',[]));c.showPage();return heading(s,continued)
    def render(s):
        start=c.getPageNumber();page_map[s['id']]=start
        c.bookmarkPage(s['id']);c.addOutlineEntry(s['title'],s['id'],0,False)
        y=heading(s)
        for b in s['blocks']:
            for f,gap in flows(b):
                if b['kind']=='h' and y<150:y=newpage(s)
                pending=[f]
                while pending:
                    flow=pending.pop(0);_,fh=flow.wrap(CW,1000)
                    if fh<=y-71:
                        flow.drawOn(c,L,y-fh);y-=fh+gap
                    else:
                        parts=flow.split(CW,y-71) if isinstance(flow,Table) and b['kind']=='table' else []
                        if parts and len(parts)>1:
                            first=parts.pop(0);_,hh=first.wrap(CW,1000);first.drawOn(c,L,y-hh)
                            y=newpage(s);pending=parts+pending
                        else:
                            y=newpage(s);_,fh=flow.wrap(CW,1000)
                            if fh>y-71:raise RuntimeError(f"Unsplit block too tall: {s['id']} {b['kind']} {fh}")
                            flow.drawOn(c,L,y-fh);y-=fh+gap
        section_pages[s['id']]=list(range(start,c.getPageNumber()+1))
        footer(s.get('refs',[]));c.showPage()

    # Cover uses deliberate hierarchy and a vector platform motif.
    c.setFillColor(NAVY);c.rect(0,380,W,H-380,stroke=0,fill=1)
    c.setFillColor(TEAL);c.roundRect(L,H-61,328,27,13,stroke=0,fill=1)
    c.setFillColor(white);c.setFont(BOLD,8.9);c.drawString(L+15,H-51,'UNITED KINGDOM FIRST / EUROPE NEXT')
    put(c,'Medical E-commerce',L,H-104,CW,37,white,True)
    put(c,'Technical\nspecification'.replace('\n',' '),L,H-161,CW,31,HexColor('#8ce0d5'),True)
    put(c,'A detailed blueprint for the customer experience, secure operations and a maintainable commerce platform.',L,H-218,438,13.5,HexColor('#c4dce6'))
    xs=[L,L+177,L+354]
    for x,n,title,desc in zip(xs,['cart','shield','data'],['CUSTOMER','COMMERCE CORE','OPERATIONS'],['Discover / buy / reorder','Identity / API / data','Admin / stock / fulfilment']):
        icon(c,n,x,H-340,30,HexColor('#87dcd3'));put(c,title,x,H-357,158,9.4,white,True);put(c,desc,x,H-378,158,8.6,HexColor('#bfd7e1'))
    c.setFillColor(HexColor('#94b7ca'));c.setFont(FONT,8);c.drawString(L,402,'VERSION 1.0  /  9 NOVEMBER 2026  /  FOR TECHNICAL REVIEW')
    y=350
    for n,title,body in [('layers','What this specification defines','39 sections covering framework choices, screen behaviour, authentication, data contracts, transactions, integrations, deployment and release evidence.'),('chart','Measurable quality targets','Lighthouse SEO 100 on public templates, performance budgets, manual accessibility checks and real-user Core Web Vitals.'),('check','A phased, testable delivery baseline','A complete first-selling workflow after 25 elapsed days, with later releases for operating depth, B2B growth and country expansion.')]:
        icon(c,n,L,y-27,25);ph=put(c,title,L+39,y,CW-39,11,NAVY,True);put(c,body,L+39,y-ph-5,CW-39,9.7,MUTED);y-=82
    c.setStrokeColor(LINE);c.line(L,91,R,91)
    put(c,'Prepared for the new medical-supplies business',L,78,320,9,NAVY,True)
    put(c,'Shishir Sabbir  |  shishirsabbir.github.io',L,61,400,8.6,MUTED)
    c.linkURL('https://shishirsabbir.github.io',(L,47,L+300,63),thickness=0)
    c.showPage()

    for idx,subset in enumerate([SECTIONS[:23],SECTIONS[23:]]):
        s=dict(group='READING GUIDE / '+str(idx+1)+' OF 2',title='Contents' if idx==0 else 'Contents / continued',intro='Navigate by topic. Every section contains a requirement and acceptance evidence. Diagrams are proposed designs, not screenshots of a deployed store.')
        y=heading(s);previous=None
        for item in subset:
            if item['group']!=previous:
                previous=item['group'];y-=7
                c.setFont(BOLD,8);c.setFillColor(TEAL);c.drawString(L,y,previous.upper());y-=21
            c.setFillColor(INK);c.setFont(FONT,9.4);c.drawString(L+8,y,item['title'])
            if known:
                c.setFont(BOLD,9.4);c.drawRightString(R,y,str(known[item['id']]))
                c.linkRect('',item['id'],(L,y-4,R,y+12),thickness=0)
            y-=18
        if idx==1:
            y-=14;c.setFont(BOLD,8);c.setFillColor(TEAL);c.drawString(L,y,'REFERENCE APPENDIX');y-=20
            c.setFont(FONT,9.4);c.setFillColor(INK);c.drawString(L+8,y,'Official sources, check dates and scope')
            if known:c.drawRightString(R,y,str(known['sources']));c.linkRect('','sources',(L,y-4,R,y+12),thickness=0)
            y-=38
            notes=[('CONFIRMED','User decisions: operating model, storefront/admin direction, database, hosting and payment preferences.'),('PROPOSED','Frameworks, numerical policies, performance budgets and diagrams require implementation validation.'),('DEPENDENT','Product, provider and country eligibility require external evidence and owner approval.')]
            for a,b in notes:
                put(c,a,L,y,100,8.2,TEAL,True);hh=put(c,b,L+102,y,CW-102,9.3,MUTED);y-=hh+15
        footer();c.showPage()
    for s in SECTIONS:render(s)

    page_map['sources']=c.getPageNumber();c.bookmarkPage('sources');c.addOutlineEntry('Sources, dates and scope','sources',0,False)
    s=dict(group='REFERENCE APPENDIX',title='Sources, dates and scope',intro='Official references were checked on the dates below. Project policies and numerical targets are proposed engineering decisions. Earlier regulatory access limitations remain recorded in the source register.',refs=[])
    y=heading(s)
    for sid,src in SOURCES.items():
        blocks=[para(sid+'  /  '+src['title'],10.1,color=NAVY,bold=True),para('Checked '+src['checked']+' | '+src['scope'],8.7,color=MUTED),para('<link href="'+html.escape(src['url'],quote=True)+'" color="#087f83">'+html.escape(src['url'])+'</link>',7.8,10.6,raw=True)]
        heights=[b.wrap(CW,1000)[1] for b in blocks];need=sum(heights)+26
        if y-need<71:y=newpage(s)
        for b,hh in zip(blocks,heights):b.drawOn(c,L,y-hh);y-=hh+4
        y-=8;c.setStrokeColor(LINE);c.line(L,y+1,R,y+1)
    footer();count=c.getPageNumber();c.save()
    return page_map,section_pages,count

def markdown(page_map):
    lines=['# Medical E-commerce — Detailed Technical Specification','',CONTENT['VERSION'],'',f"Dated {CONTENT['DATE']}. Prepared by Shishir Sabbir. Proposed requirements, not an implemented system.",'','PDF: deliverables/pdf/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.pdf','']
    for s in SECTIONS:
        lines += ['## '+s['title'],'',s['group']+f" · PDF page {page_map[s['id']]}",'',s['intro'],'']
        for b in s['blocks']:
            k=b['kind']
            if k=='p':lines += [b['text'],'']
            elif k=='h':lines += ['### '+b['text'],'']
            elif k=='diagram':lines += ['> **Design diagram:** '+DIAGRAM_TEXT[b['name']],'']
            elif k=='code':lines += ['```text',b['text'],'```','']
            elif k=='callout':lines += ['> **'+b['title']+'** — '+b['text'],'']
            elif k=='requirement':lines += ['**'+b['id']+' · '+b['phase']+' — '+b['text']+'**','','Acceptance: '+b['acceptance'],'']
            elif k=='table':
                def esc(x):return str(x).replace('|','\\|').replace('\n','<br>')
                lines += ['| '+' | '.join(esc(x) for x in b['headers'])+' |','| '+' | '.join('---' for _ in b['headers'])+' |']
                lines += ['| '+' | '.join(esc(x) for x in row)+' |' for row in b['rows']]+['']
        if s['refs']:lines += ['Sources: '+', '.join('['+sid+']('+SOURCES[sid]['url']+')' for sid in s['refs'])+'.','']
    lines += ['## Sources, dates and scope','']
    for sid,s in SOURCES.items():lines += [f"- **{sid}** [{s['title']}]({s['url']}) — checked {s['checked']}. {s['scope']}"]
    (ROOT/'docs/plans/UK_MEDICAL_ECOMMERCE_TECHNICAL_SPECIFICATION.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

if __name__=='__main__':
    first=BytesIO();mapping,pages,total=build(first)
    second_map,pages,second_total=build(str(OUT),mapping,total)
    assert second_map==mapping and second_total==total
    markdown(mapping)
    requirements=[dict(section=s['id'],**b) for s in SECTIONS for b in s['blocks'] if b['kind']=='requirement']
    (ROOT/'docs/registers/TECHNICAL_SPEC_REQUIREMENTS.json').write_text(json.dumps(requirements,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (ROOT/'docs/registers/TECHNICAL_SPEC_PAGE_MAP.json').write_text(json.dumps(dict(total_pages=total,sections=pages,sources_start=mapping['sources']),indent=2)+'\n',encoding='utf-8')
    doc=pymupdf.open(OUT)
    text='\n'.join(p.get_text() for p in doc)
    assert len(doc)==total and all(r['id'] in text for r in requirements)
    assert len(set(r['id'] for r in requirements))==len(requirements)
    print(json.dumps(dict(pdf=str(OUT),pages=total,sections=len(SECTIONS),requirements=len(requirements),sources=len(SOURCES),links=sum(len(p.get_links()) for p in doc)),indent=2))
