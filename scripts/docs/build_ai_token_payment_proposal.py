"""Render the source-backed AI development cost explanation and editable text."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import json
import html
import re
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
M = json.loads((ROOT/'docs/models/AI_TOKEN_PAYMENT_MODEL.json').read_text(encoding='utf-8'))
SOURCES = json.loads((ROOT/'docs/registers/AI_TOKEN_PAYMENT_SOURCES.json').read_text(encoding='utf-8'))
D = Decimal
def money(v): return f'{D(v).quantize(D("0.01"), rounding=ROUND_HALF_UP):,.2f}'
budget = D(M['estimated_total_usd'])
reserve = D(M['uncommitted_usage_reserve_usd'])
a = M['workload_assumptions']
cycles = M['minimum_planned_agents'] * M['development_days'] * a['cycles_per_agent_day']
assert cycles == a['total_cycles'] == 5000
assert cycles*a['aggregate_input_tokens_per_cycle'] == a['total_input_tokens']
assert cycles*a['aggregate_output_tokens_per_cycle'] == a['total_output_tokens']
input_m, output_m = D(a['total_input_tokens'])/1000000, D(a['total_output_tokens'])/1000000
rates = {r['id']:r for r in M['rates_usd_per_million_tokens']}
raw_costs = {key: input_m*D(r['input'])+output_m*D(r['output']) for key,r in rates.items()}
costs = {key:value.quantize(D('0.01'),rounding=ROUND_HALF_UP) for key,value in raw_costs.items()}
assert costs['qwen'] == D(M['qwen_base_estimate_usd']) == D('1396.01')
assert costs['qwen']+reserve == budget == D('1555.56')
assert costs['openai_chat']==5835 and costs['claude_opus']==4240
fx = D(M['rmb']['eur_cny'])/D(M['rmb']['eur_usd'])
rmb = budget*fx

PAGES = [
dict(kicker='AI DEVELOPMENT COST / 10 NOVEMBER 2026',title='Build the core.\nThen extend it.',intro='Medical E-commerce | United Kingdom first / Europe next',blocks=[
('hero', 'USD '+money(budget), f'Approximately RMB {money(rmb)} | Developer fee: USD 0', 'Estimated AI cost for the initial 25-day build'),
('stats',[('25 days','Core release target'),('10+ agents','Planned minimum'),('USD 0','Development fee')]),
('h','AI development cost'),
('p',f'The estimated AI cost for the initial 25-day development phase is <b>USD {money(budget)}</b>. This includes modeled API usage and an allowance for additional usage or selective review. My development work carries no professional fee.'),
('call','Qwen for most development',f'Modeled Qwen API usage: <b>USD {money(costs["qwen"])}</b><br/>Additional usage / selective review reserve: <b>USD {money(reserve)}</b><br/>Total estimated AI cost: <b>USD {money(budget)}</b>'),
('h','Most core development belongs in the first 25 days'),
('p','The plan is to build the main commerce foundation and the most important basic features together: shopping, product management, stock, payments, orders and daily administration. Later phases will mainly expand and extend this foundation, rather than start it again.'),
('small','This is the intended shape of the agreed core release, not a measured percentage of the entire future programme. The target still depends on data, timely decisions, integrations and acceptance. Model rates are published facts; token volumes and the reserve are planning assumptions. Actual API costs will depend on measured usage.'),
]),
dict(kicker='01 / WHAT THE FIRST RELEASE ESTABLISHES',title='A substantial foundation\nwithin 25 days.',intro='Twenty planned launch feature groups connect the buyer journey to everyday operations.',blocks=[
('table', ['Core system','Built during the first 25 days','Later extension'],[
['Brand and buying','Brand direction; responsive pages; categories/search; product pages; customer accounts. [F01-F04]','Broader merchandising, richer discovery and additional customer journeys.'],
['Eligibility and checkout','Professional purchase checks; basket/checkout; Revolut/wallets and PayPal; information and service email. [F05-F09]','More approved payment/market routes and reviewed customer-service automation.'],
['Staff and catalogue','SEO/consent foundation; staff MFA/roles; product CRUD/CSV; images and documents. [F10-F13]','More products, improved imports, content workflows and reporting.'],
['Trading operations','Stock/traceability; orders/dispatch; returns/refunds; financial records/exports. [F14-F17]','Deeper purchasing, carrier/accounting connectors and operational automation.'],
['Controlled release','Product/channel approval; hosting and restore; training and launch evidence. [F18-F20]','Capacity tuning, additional eligible categories and country-by-country expansion.']
], [111,235,163]),
('call','Build once; extend the systems','The first phase targets a complete basic receive -> publish -> buy -> ship -> refund workflow. Later work should add depth, scale and new capabilities on top of tested core modules.'),
('h','Practical sequence'),
('p','<b>Days 1-5:</b> design decisions, architecture and a first transaction slice.<br/><b>Days 6-15:</b> connected commerce modules, admin and catalogue intake.<br/><b>Days 16-25:</b> integration, audits, corrections, business acceptance, restore rehearsal and release.'),
('small','Scope follows the existing 20-feature register and 25-day plan. Initial intake targets the reported 250 warehouse products; exact SKUs, lawful sale and evidence remain to be verified. Future full-catalogue ambition continues. Merchant/product approvals and owner-controlled readiness remain release dependencies; AI agents cannot supply them.'),
]),
dict(kicker='02 / TEN AI WORKSTREAMS',title='At least ten agents\nfor the planned workflow.',intro='Developer-led coordination, integration and review remain part of the work.',blocks=[
('p','For the 25-day target, <b>I plan a minimum of ten AI agents</b> across these workstreams. This is a developer capacity assumption; provider quotas and simultaneous-session access still need verification.'),
('roles',M['agents']),
('h','An explicit workload model'),
('table',['Assumed activity','Calculation','Total'],[
['Agent-days','10 agents x 25 days','250'],
['Implementation/review cycles','250 x 20 cycles per agent-day','5,000'],
['Cumulative input tokens','5,000 x 105,000 input tokens','525 million'],
['Cumulative output tokens','5,000 x 21,400 output tokens','107 million'],
['Combined planning volume','525m input + 107m output','632 million']
],[160,229,120]),
('small','A cycle can contain several calls to read files, implement, review and debug. Input is cumulative context; output includes billable reasoning where applicable. These are assumptions, not unique code counts or single-prompt sizes.'),
('call','Illustrative scenario; validate it early','These token quantities are illustrative planning inputs, not measured project consumption. Ten agents alone do not justify 632m tokens. Apply the same quantities to every model and reforecast using actual throughput and spend on Day 5.'),
]),
dict(kicker='03 / SEPARATE API BILLING COMPARISONS',title='What the same token\nvolume would cost.',intro='Illustrative scenario: 525m input + 107m output | standard uncached text API assumptions',blocks=[
('call','The API billing formula','<b>Cost = (input tokens / 1,000,000 x input rate)<br/>+ (output tokens / 1,000,000 x output rate)</b>'),
('table',['Selected model','Input / 1m','Output / 1m','Project scenario'],[
['ChatGPT API: chat-latest [S2]','USD 5.00','USD 30.00','USD '+money(costs['openai_chat'])],
['Claude Opus 5.5 [S3]','USD 4.00','USD 20.00','USD '+money(costs['claude_opus'])],
['Qwen 3.8 Max [S1]','USD 1.65','USD 4.951','USD '+money(costs['qwen'])],
['OpenAI GPT-6.1 Sol [S2]','USD 2.00','USD 10.00','USD '+money(costs['openai_sol'])],
['Claude Sonnet 5.5 [S3]','USD 2.00','USD 10.00','USD '+money(costs['claude_sonnet'])]
],[203,89,95,122]),
('h','OpenAI / ChatGPT calculation'),
('p',f'<b>525 x USD 5 + 107 x USD 30 = USD {money(costs["openai_chat"])}.</b><br/>This illustrative scenario uses the <b>chat-latest API</b> rate; it is not a ChatGPT subscription price or an incurred bill. [S2]'),
('h','Claude calculation'),
('p',f'<b>525 x USD 4 + 107 x USD 20 = USD {money(costs["claude_opus"])}.</b><br/>This illustrative scenario uses <b>Claude Opus 5.5</b> standard base-token rates, not a measured project bill. [S3]'),
('bars', [('ChatGPT API',costs['openai_chat']),('Claude Opus 5.5',costs['claude_opus']),('Qwen base estimate',costs['qwen'])]),
('small','Illustrative scenarios, not measured bills or provider minimum prices. Cheaper alternatives are shown. Equal tokens do not establish equal quality; tokenizers and retries differ. No cache/batch/credit savings, tax or tool fees are assumed. OpenAI: standard short context. Qwen: Frankfurt/global <=1m input/request. [S1-S3]'),
]),
dict(kicker='04 / QWEN COST AND RMB CONVERSION',title='USD 1,555.56, explained.',intro='Qwen is the main development API; the usage allowance covers extra tokens or selective review.',blocks=[
('table',['Cost component','Calculation','USD'],[
['Qwen input','525m x USD 1.65 / million',money(input_m*D(rates['qwen']['input']))],
['Qwen output','107m x USD 4.951 / million',money(output_m*D(rates['qwen']['output']))],
['Modeled Qwen usage','Input + output',money(costs['qwen'])],
['Additional usage reserve','Total estimate less Qwen base',money(reserve)],
['Developer professional fee','No charge','0.00'],
['Total estimated AI cost',money(costs['qwen'])+' + '+money(reserve),money(budget)]
],[165,235,109]),
('p',f'The reserve is <b>{reserve/costs["qwen"]*100:.2f}% of the modeled Qwen base</b>, included in the total cost estimate. It is an allowance, rather than an incurred provider charge or measured contingency. It covers potential additional tokens, tier/rate changes or selective OpenAI/Claude review. The base includes no separate premium-review token allocation.'),
('call',f'Indicative RMB equivalent: RMB {money(rmb)}',f'ECB reference date: <b>9 November 2026</b>.<br/>CNY per USD = 7.4689 / 1.1193 = <b>{fx:.5f}</b>.<br/>USD 1,555.56 x {fx:.5f} = approximately <b>RMB {money(rmb)}</b>. Calculation uses the unrounded cross rate. [S6-S7]'),
('h','Direct RMB API pricing is a separate route'),
('p',f'Aliyun lists Qwen 3.8 Max at <b>RMB 12 input / RMB 36 output per million</b> for its Frankfurt/global or Beijing RMB billing route. The same assumed volume would be <b>525 x 12 + 107 x 36 = RMB 10,152</b> before any reserve. Account eligibility and settlement must be checked. This tariff is not mixed into the USD {money(costs["qwen"])} baseline. [S4]'),
('h','How actual usage affects the estimate'),
('p',f'Compare actual usage and provider charges with this model on Days 5, 15 and 25. If base usage rises 25%, the Qwen estimate becomes <b>USD {money(raw_costs["qwen"]*D("1.25"))}</b>, exceeding the total estimate shown here. Update the forecast as measured token volumes, model choices and billing rates become available.'),
('small','RMB is indicative, not a settlement quote. Hosting, stock, domains, paid image generation, other tools, maintenance and later phases are separate. Tax/FX/transfer fees are uncalculated.'),
]),
dict(kicker='05 / PRICING CHANGES AND SOURCE NOTES',title='Current rates.\nHonest cost exposure.',intro='Sources checked 10 November 2026. Published tariffs establish prices, not the project workload.',blocks=[
('h','Where bills can increase'),
('p','<b>Qwen:</b> Singapore Coder Flash rises from USD 0.30/1.50 per million input/output at <=32K input to USD 0.50/2.50 at 32K-128K: a <b>66.7% tier uplift</b>. This is a context-based cost increase, not a recent across-the-board tariff rise. [S1]'),
('p','<b>OpenAI / ChatGPT:</b> GPT-6.1 Sol standard rates are USD 2/10 per million input/output; Fast rates are USD 4/20, a <b>100% speed-tier uplift</b>. Model, context and region also affect billing. This is not a claim that the standard tariff recently doubled. [S2]'),
('p','<b>Claude:</b> Anthropic says newer tokenizers may produce about 30% more tokens for the same text, affecting bills. It also cancelled the planned September 2026 Sonnet 5 price increase; the announced USD 3/15 tariff did not take effect. A blanket claim that all Claude prices rose would be inaccurate. [S3, S5]'),
('h','Dated, scoped references'),
('sources',SOURCES),
('small','Provider accounts, rates, limits, model availability and tax treatment need verification before API use. This is a cost explanation based on published rates and assumed usage; actual charges will depend on consumption. Prepared by Shishir Sabbir | shishirsabbir.github.io | shishir.sabbir@gmail.com'),
])
]

OUT = ROOT/'deliverables/pdf/UK_MEDICAL_ECOMMERCE_AI_TOKEN_PAYMENT_PROPOSAL.pdf'
TMP = ROOT/'.local/pdfs/ai_token_payment_v2'
OUT.parent.mkdir(parents=True,exist_ok=True); TMP.mkdir(parents=True,exist_ok=True)
for name,file in [('Body','arial.ttf'),('Bold','arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold')
W,H,L,CW = 595.28,841.89,43,509.28
FOREST,INK,MUTED,PALE,LINE,CREAM,CORAL = map(HexColor,['#153e35','#203b35','#66776e','#eaf2e9','#d5dfd3','#fbfaf5','#c76244'])
c=canvas.Canvas(str(OUT),pagesize=(W,H))
c.setTitle('Medical E-commerce | AI development cost | USD 1,555.56')
c.setAuthor('Shishir Sabbir')
markdown=['# Medical E-commerce | AI development cost','',f'10 November 2026 | Revision {M["revision"]} | Cost explanation with usage assumptions','']

def strip(t):
    return html.unescape(re.sub('<[^>]+>','',t.replace('<br/>','\n')))

def paragraph(t,top,x=L,width=CW,size=10.2,color=INK,bold=False):
    p=Paragraph(t,ParagraphStyle('body',fontName='Bold' if bold else 'Body',fontSize=size,leading=size*1.38,textColor=color))
    _,height=p.wrap(width,2000)
    if top-height<64: raise ValueError(f'Overflow page {c.getPageNumber()}: {strip(t)[:70]} / {top-height:.1f}')
    p.drawOn(c,x,top-height)
    return top-height

def table(header,rows,widths,top):
    cells=[]
    for i,row in enumerate([header]+rows):
        cells.append([Paragraph(html.escape(str(v)),ParagraphStyle('cell',fontName='Bold' if i==0 else 'Body',fontSize=9,leading=12.5,textColor=white if i==0 else INK)) for v in row])
    t=Table(cells,colWidths=widths)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),FOREST),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,PALE]),('LINEBELOW',(0,1),(-1,-1),0.4,LINE)]))
    _,height=t.wrap(CW,2000)
    if top-height<64: raise ValueError(f'Table overflow page {c.getPageNumber()}: {top-height}')
    t.drawOn(c,L,top-height)
    markdown.extend(['| '+' | '.join(header)+' |','|'+'|'.join(['---']*len(header))+'|']+['| '+' | '.join(map(str,r))+' |' for r in rows]+[''])
    return top-height-16

for number,page in enumerate(PAGES,1):
    c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(FOREST);c.rect(0,H-10,W,10,fill=1,stroke=0)
    c.setFillColor(CORAL);c.circle(W-L-8,H-42,5,fill=1,stroke=0)
    y=paragraph(page['kicker'],H-35,size=8,color=CORAL,bold=True)-16
    y=paragraph(page['title'].replace('\n','<br/>'),y,size=29,color=FOREST,bold=True)-10
    y=paragraph(page['intro'],y,size=10,color=MUTED)-22
    markdown.extend(['## '+page['title'].replace('\n',' '),'',page['intro'],''])
    c.bookmarkPage(f'p{number}');c.addOutlineEntry(page['title'].replace('\n',' '),f'p{number}')
    for block in page['blocks']:
        kind=block[0]
        if kind in ('p','small','h'):
            size=13 if kind=='h' else 8.7 if kind=='small' else 10.2
            y=paragraph(block[1],y,size=size,color=MUTED if kind=='small' else FOREST if kind=='h' else INK,bold=kind=='h')-(8 if kind=='h' else 15)
            markdown.extend([('### ' if kind=='h' else '')+strip(block[1]),''])
        elif kind=='hero':
            c.setFillColor(FOREST);c.roundRect(L,y-138,CW,138,9,fill=1,stroke=0)
            paragraph(block[3],y-16,L+18,CW-36,9,HexColor('#c0d5c4'))
            paragraph(block[1],y-39,L+18,CW-36,38,white,True)
            paragraph(block[2],y-105,L+18,CW-36,10,white)
            y-=156;markdown.extend([block[1],block[2],block[3],''])
        elif kind=='stats':
            for j,(value,label) in enumerate(block[1]):
                x=L+j*173
                c.setFillColor(PALE);c.roundRect(x,y-64,163,64,5,fill=1,stroke=0)
                paragraph(value,y-10,x+12,139,18,FOREST,True)
                paragraph(label,y-39,x+12,139,8.5,MUTED)
                markdown.append(value+' | '+label)
            y-=83;markdown.append('')
        elif kind=='call':
            # Measure both paragraphs before painting the accent panel.
            ps=ParagraphStyle('measure',fontName='Body',fontSize=10,leading=13.8)
            body=Paragraph(block[2],ps);_,bh=body.wrap(CW-32,2000)
            title=Paragraph(block[1],ParagraphStyle('measuretitle',fontName='Bold',fontSize=11,leading=15));_,th=title.wrap(CW-32,2000)
            height=bh+th+31
            if y-height<64: raise ValueError(f'Callout overflow {number}: top {y}, height {height}')
            c.setFillColor(PALE);c.roundRect(L,y-height,CW,height,6,fill=1,stroke=0)
            c.setFillColor(CORAL);c.rect(L,y-height,3,height,fill=1,stroke=0)
            yy=paragraph(block[1],y-12,L+16,CW-32,11,FOREST,True)-6
            paragraph(block[2],yy,L+16,CW-32,10,INK)
            y-=height+18;markdown.extend(['### '+block[1],'',strip(block[2]),''])
        elif kind=='table': y=table(block[1],block[2],block[3],y)
        elif kind=='roles':
            for j,role in enumerate(block[1]):
                col=j%2;row=j//2;x=L+col*259;top=y-row*31
                c.setFillColor(CORAL);c.circle(x+9,top-9,8,fill=1,stroke=0)
                c.setFont('Bold',7);c.setFillColor(white);c.drawCentredString(x+9,top-11.5,str(j+1))
                paragraph(html.escape(role),top,x+24,226,9,INK)
                markdown.append(f'{j+1}. {role}')
            y-=170;markdown.append('')
        elif kind=='bars':
            for label,value in block[1]:
                paragraph(label,y,size=8.8,color=MUTED)
                c.setFillColor(LINE);c.roundRect(L,y-24,CW,8,4,fill=1,stroke=0)
                c.setFillColor(CORAL if 'Qwen' not in label else FOREST);c.roundRect(L,y-24,float(value/max(v for _,v in block[1]))*CW,8,4,fill=1,stroke=0)
                c.setFont('Bold',9);c.setFillColor(FOREST);c.drawRightString(W-L,y-8,'USD '+money(value))
                y-=36
            y-=10
        elif kind=='sources':
            labels={
                'S1':'Qwen USD: Frankfurt/global 1.65/4.951; context tiers and region differences.',
                'S2':'OpenAI: chat-latest 5/30 and GPT-6.1 Sol 2/10, standard USD per million.',
                'S3':'Claude: Opus 5.5 4/20; Sonnet 5.5 2/10; tokenizer and cache billing notes.',
                'S4':'Aliyun RMB: Qwen 3.8 Max, Frankfurt/global or Beijing, RMB 12/36 per million.',
                'S5':'Sonnet 5: August 10 edit cancels the planned September price increase.',
                'S6':'ECB, 9 Nov 2026: EUR 1 = CNY 7.4689. Indicative reference rate.',
                'S7':'ECB, 9 Nov 2026: EUR 1 = USD 1.1193. Used for the RMB cross rate.'}
            for s in block[1]:
                line=f'<b>[{s["id"]}]</b> <link href="{html.escape(s["url"],quote=True)}" color="#153e35">{html.escape(s["title"])}</link> - {labels[s["id"]]}'
                y=paragraph(line,y,size=8.2,color=MUTED)-8
                markdown.extend([f'[{s["id"]}] [{s["title"]}]({s["url"]}) | Checked {s["checked"]} | {s["scope"]} | Limit: {s["limit"]}',''])
    if y<61: raise ValueError(f'Page {number} bottom {y}')
    c.setStrokeColor(LINE);c.line(L,49,W-L,49)
    c.setFont('Body',7.2);c.setFillColor(MUTED)
    c.drawString(L,33,'SHISHIR SABBIR / AI DEVELOPMENT COST / 10 NOV 2026')
    c.drawRightString(W-L,33,f'{number:02d} / {len(PAGES):02d}')
    c.showPage()
c.save()

doc=pymupdf.open(OUT)
assert len(doc)==6
text=''.join(p.get_text() for p in doc)
for required in (money(budget),money(costs['qwen']),money(reserve),money(costs['openai_chat']),money(costs['claude_opus']),'525 million','107 million'):
    assert required in text,required
for i,page in enumerate(doc):
    page.get_pixmap(matrix=pymupdf.Matrix(1.35,1.35)).save(TMP/f'page-{i+1}.png')
    for word in page.get_text('words'):
        assert word[0]>=L-1 and word[2]<=W-L+1, (i,word)
(ROOT/'docs/plans/UK_MEDICAL_ECOMMERCE_AI_TOKEN_PAYMENT_PROPOSAL.md').write_text('\n'.join(markdown),encoding='utf-8')
computed={'revision':M['revision'],'source_checked':'2026-11-10','cycles':cycles,'input_millions':str(input_m),'output_millions':str(output_m),'costs_usd':{k:money(v) for k,v in costs.items()},'reserve_usd':money(reserve),'total_usd':money(budget),'fx_cny_per_usd':str(fx),'rmb_equivalent':money(rmb),'pages':len(doc)}
(ROOT/'docs/models/AI_TOKEN_PAYMENT_CALCULATED.json').write_text(json.dumps(computed,indent=2)+'\n',encoding='utf-8')
print(json.dumps(computed,indent=2))
