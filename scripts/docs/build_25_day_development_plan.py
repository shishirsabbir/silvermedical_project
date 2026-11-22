"""Build the collaborative, 250-product launch plan and editable tracking records."""
from pathlib import Path
from io import BytesIO
import json
import html
import runpy

from reportlab.pdfgen import canvas
from reportlab.platypus import Flowable, Table, TableStyle
from reportlab.lib.colors import HexColor, white
import pymupdf

ROOT=Path(__file__).resolve().parents[2]
C=runpy.run_path(str(ROOT/'docs/content/development_25_day_content.py'))
R=runpy.run_path(str(ROOT/'scripts/docs/build_technical_spec.py'))
W,H,L,RIGHT,CW=[R[n] for n in ('W','H','L','R','CW')]
NAVY,TEAL,INK,MUTED,PALE,LINE,FONT,BOLD=[R[n] for n in ('NAVY','TEAL','INK','MUTED','PALE','LINE','FONT','BOLD')]
para,put,icon,flows=[R[n] for n in ('para','put','icon','flows')]
OUT=ROOT/'deliverables/pdf/UK_MEDICAL_ECOMMERCE_25_DAY_DEVELOPMENT_PLAN.pdf'
SOURCES={s['id']:s for s in C['SOURCES']}

class DayCard(Flowable):
    def __init__(self,b):
        Flowable.__init__(self);self.b=b;self.width=CW
        self.title=para(b['title'],10.4,color=NAVY,bold=True)
        self.rows=[]
        for label,key in [('BUILD','build'),('CLIENT','client'),('PROOF','evidence')]:
            self.rows.append((label,para(b[key],8.9,11.6,color=TEAL if key=='evidence' else INK)))
        self.title_h=self.title.wrap(CW-123,1000)[1]
        self.heights=[p.wrap(CW-76,1000)[1] for _,p in self.rows]
        self.height=19+max(self.title_h,23)+sum(self.heights)+12
    def draw(self):
        c=self.canv;h=self.height
        c.setFillColor(PALE);c.setStrokeColor(LINE);c.roundRect(0,0,CW,h,6,stroke=1,fill=1)
        c.setFillColor(TEAL);c.roundRect(10,h-31,46,21,4,stroke=0,fill=1)
        c.setFillColor(white);c.setFont(BOLD,9.4);c.drawCentredString(33,h-24,'DAY '+str(self.b['day']))
        self.title.drawOn(c,67,h-10-self.title_h)
        c.setFont(FONT,7);c.setFillColor(MUTED);c.drawRightString(CW-10,h-20,self.b['date'])
        y=h-16-max(self.title_h,23)
        for (label,p),ph in zip(self.rows,self.heights):
            c.setFillColor(TEAL if label=='PROOF' else MUTED);c.setFont(BOLD,7.1);c.drawString(12,y-8,label)
            p.drawOn(c,65,y-ph);y-=ph+4

def build(target,known=None,total=None):
    c=canvas.Canvas(target,pagesize=(W,H),pageCompression=1)
    c.setTitle('Medical E-commerce | 25-day development and launch plan')
    c.setAuthor('Shishir Sabbir')
    c.setSubject('Collaborative branding, 250-product launch, first-release features and daily delivery plan')
    pages={}
    def footer(refs=()):
        c.setStrokeColor(LINE);c.line(L,53,RIGHT,53)
        c.setFont(FONT,7);c.setFillColor(MUTED)
        c.drawString(L,25,'25-DAY DEVELOPMENT PLAN  /  9 NOV 2026  /  PROPOSED DELIVERY BASELINE')
        c.drawRightString(RIGHT,25,f'{c.getPageNumber():02d}'+(f' / {total:02d}' if total else ''))
        if refs:
            c.setFont(FONT,6.8);c.drawString(L,41,'Sources:');x=L+33
            for sid in refs:
                label=sid+'  ';c.setFillColor(TEAL);c.drawString(x,41,label)
                width=c.stringWidth(label,FONT,6.8);c.linkURL(SOURCES[sid]['url'],(x,38,x+width,49),thickness=0);x+=width
    def heading(s):
        c.setFillColor(NAVY);c.rect(0,H-8,W,8,stroke=0,fill=1)
        c.setFillColor(TEAL);c.setFont(BOLD,7.8);c.drawString(L,H-35,s['group'].upper())
        names={'01':'cart','02':'layers','03':'check','04':'data','05':'server','06':'check','07':'layers'}
        icon(c,names.get(s['group'][:2],'layers'),RIGHT-24,H-70,24)
        y=H-55;hh=put(c,s['title'],L,y,CW-40,23,NAVY,True);y-=hh+12
        hh=put(c,s['intro'],L,y,CW,10.5,MUTED);return y-hh-16

    # Cover.
    c.setFillColor(NAVY);c.rect(0,343,W,H-343,stroke=0,fill=1)
    c.setFillColor(TEAL);c.roundRect(L,H-61,330,27,13,stroke=0,fill=1)
    c.setFont(BOLD,8.8);c.setFillColor(white);c.drawString(L+15,H-51,'UNITED KINGDOM FIRST / EUROPE NEXT')
    put(c,'Medical E-commerce',L,H-100,CW,28,white,True)
    put(c,'25-day development',L,H-155,CW,33,HexColor('#90e0d6'),True)
    put(c,'and launch plan',L,H-199,CW,33,HexColor('#90e0d6'),True)
    put(c,'Choose the brand together. Build the selling workflow.\nLaunch with reviewed warehouse stock.'.replace('\n',' '),L,H-266,CW-28,13.2,HexColor('#c7dfe9'))
    for i,(val,label) in enumerate([('DAY 1','Collaborative design'),('250','Product intake target'),('20','Launch feature groups')]):
        x=L+i*177;c.setFillColor(HexColor('#1a4057'));c.roundRect(x,382,157,77,7,stroke=0,fill=1)
        put(c,val,x+12,444,133,23,white,True);put(c,label,x+12,409,133,8.8,HexColor('#bcdce5'))
    c.setFont(FONT,8);c.setFillColor(HexColor('#a7c8d6'));c.drawString(L,360,'A practical delivery plan for the owners and the developer')
    y=311
    for n,title,text in [('layers','A team experience','AI-assisted design choices, shared reviews and clear client decisions from the first development day.'),('cart','Ready to transact','Catalogue, accounts, checkout, payments, stock, dispatch, refunds and everyday admin workflows.'),('check','Ready to grow','A reviewed path to add products after launch, with daily deliverables and evidence-based release gates.')]:
        icon(c,n,L,y-25,25);put(c,title,L+40,y,CW-40,11,NAVY,True);put(c,text,L+40,y-21,CW-40,10,MUTED);y-=72
    c.setStrokeColor(LINE);c.line(L,83,RIGHT,83)
    put(c,'Prepared by Shishir Sabbir',L,70,300,9.8,NAVY,True)
    put(c,'shishirsabbir.github.io  |  shishir.sabbir@gmail.com',L,51,CW,8.5,MUTED)
    c.linkURL('https://shishirsabbir.github.io',(L,36,L+175,52),thickness=0)
    c.showPage()

    for s in C['SECTIONS']:
        pages[s['id']]=c.getPageNumber();c.bookmarkPage(s['id']);c.addOutlineEntry(s['title'],s['id'],0,False)
        y=heading(s)
        for b in s['blocks']:
            items=[(DayCard(b),9)] if b['kind']=='day' else flows(b)
            for f,gap in items:
                _,hh=f.wrap(CW,1000)
                if y-hh<68:raise RuntimeError(f"Page overflow: {s['id']} / {b['kind']}: bottom {y-hh:.1f}")
                f.drawOn(c,L,y-hh);y-=hh+gap
        footer(s.get('refs',[]));c.showPage()
    s=dict(group='07 / SOURCES AND STATUS',title='References and working assumptions',intro='Official guidance supports the project controls below. The day allocations, asset quantities, feature packages and effort estimates are proposed delivery choices, not external guarantees.')
    pages['sources']=c.getPageNumber();c.bookmarkPage('sources');c.addOutlineEntry('References and working assumptions','sources',0,False)
    y=heading(s)
    for src in C['SOURCES']:
        hh=put(c,src['id']+' / '+src['title'],L,y,CW,10,NAVY,True);y-=hh+3
        hh=put(c,'Checked '+src['checked']+' | '+src['scope'],L,y,CW,8.9,MUTED);y-=hh+4
        link=para('<link href="'+html.escape(src['url'],quote=True)+'" color="#087f83">'+html.escape(src['url'])+'</link>',7.8,10.5,raw=True)
        _,hh=link.wrap(CW,1000);link.drawOn(c,L,y-hh);y-=hh+15
    y-=5
    hh=put(c,'Project references and authority',L,y,CW,11,NAVY,True);y-=hh+6
    hh=put(c,'The existing client proposal, full project plan and technical specification provide the broader operating model and engineering detail. This plan adds the Day 1 co-design workshop and a 250-product initial intake. It does not claim that stock, licences, product permissions, merchant accounts or Google approval have been verified.',L,y,CW,9.5);y-=hh+10
    hh=put(c,'Date note: 15 November 2026 is the retained illustrative Day 0; the daily plan runs 16 November-10 December. No start date, working pattern or 24/7 support commitment is booked. The new brand/legal operator remains to be confirmed. This document prepares future work; no store or brand asset has been published through it.',L,y,CW,9.5);y-=hh
    assert y>=68,y
    footer();total=c.getPageNumber();c.save()
    return pages,total

def export_md(pages):
    lines=['# Medical E-commerce — 25-day development and launch plan','',f"Prepared by Shishir Sabbir. {C['DATE']}. Proposed delivery baseline.",'']
    for s in C['SECTIONS']:
        lines += ['## '+s['title'],'',s['group']+f" · PDF page {pages[s['id']]}",'',s['intro'],'']
        for b in s['blocks']:
            k=b['kind']
            if k=='p':lines += [b['text'],'']
            elif k=='h':lines += ['### '+b['text'],'']
            elif k=='callout':lines += ['> **'+b['title']+'** — '+b['text'],'']
            elif k=='table':
                esc=lambda x:str(x).replace('|','\\|').replace('\n','<br>')
                lines+=['| '+' | '.join(esc(x) for x in b['headers'])+' |','| '+' | '.join('---' for _ in b['headers'])+' |']
                lines+=['| '+' | '.join(esc(x) for x in row)+' |' for row in b['rows']]+['']
            elif k=='day':
                lines += [f"### Day {b['day']} · {b['date']} · {b['title']}",'','**Build:** '+b['build'],'','**Client:** '+b['client'],'','**Completion evidence:** '+b['evidence'],'']
        if s['refs']:lines+=['Sources: '+', '.join('['+sid+']('+SOURCES[sid]['url']+')' for sid in s['refs'])+'.','']
    lines+=['## Dated source register','']
    for r in C['SOURCES']:lines += [f"- **{r['id']}** [{r['title']}]({r['url']}) — {r['checked']}. {r['scope']}"]
    (ROOT/'docs/plans/UK_MEDICAL_ECOMMERCE_25_DAY_DEVELOPMENT_PLAN.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    features=[dict(zip(('id','name','deliverable','planned_days','acceptance'),row),status='planned',evidence=None) for row in C['FEATURES']]
    days=[dict(b,status='planned') for s in C['SECTIONS'] for b in s['blocks'] if b['kind']=='day']
    for name,obj in [('DAY_25_FEATURE_REGISTER.json',features),('DAY_25_DAILY_PLAN.json',days),('DAY_25_DEVELOPMENT_SOURCES.json',C['SOURCES'])]:
        (ROOT/'docs/registers'/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

if __name__=='__main__':
    out=BytesIO();pages,total=build(out)
    pages2,total2=build(str(OUT),pages,total)
    assert pages==pages2 and total==total2
    export_md(pages)
    (ROOT/'docs/registers/DAY_25_DEVELOPMENT_PAGE_MAP.json').write_text(json.dumps(dict(pages=total,sections=pages),indent=2)+'\n')
    d=pymupdf.open(OUT);txt='\n'.join(p.get_text() for p in d)
    assert all(f[0] in txt for f in C['FEATURES'])
    assert all('DAY '+str(i) in txt for i in range(1,26))
    print(json.dumps(dict(pdf=str(OUT),pages=len(d),features=len(C['FEATURES']),days=len(C['DAYS']),links=sum(len(p.get_links()) for p in d)),indent=2))
