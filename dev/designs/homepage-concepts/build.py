from pathlib import Path
from base64 import b64encode
import json
import re
from zipfile import ZIP_DEFLATED, ZipFile
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
OUT=ROOT/'deliverables/html/SILVER_MEDICAL_HOMEPAGE_MOCKUPS.html'
def data(path,mime):return 'data:'+mime+';base64,'+b64encode(path.read_bytes()).decode()
assets={n:data(HERE/'assets'/f'{n}.webp','image/webp') for n in ['editorial','clinic','products','diagnostics']}
for n in ['silver-medical-reversed','silver-medical-mark']:
 assets[n]=data(ROOT/'apps/storefront/public/brand'/f'{n}.svg','image/svg+xml')
for n in ['manrope','cormorant']:assets[n]=data(HERE/'assets'/f'{n}-variable.woff2','font/woff2')
assets['cormorant-italic']=data(HERE/'assets/cormorant-italic.woff2','font/woff2')
ICONS={
 'search':'<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 4.5 4.5"/>',
 'bag':'<path d="M5 7h14l1 14H4L5 7Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
 'heart':'<path d="M20.6 5.4a5 5 0 0 0-7.1 0L12 7l-1.5-1.6a5 5 0 0 0-7.1 7.1L12 21l8.6-8.5a5 5 0 0 0 0-7.1Z"/>',
 'plus':'<path d="M12 5v14M5 12h14"/>','minus':'<path d="M5 12h14"/>','close':'<path d="m6 6 12 12M18 6 6 18"/>',
 'chevron':'<path d="m6 9 6 6 6-6"/>','grid':'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 'check':'<path d="m5 12 4 4L19 6"/>','book':'<path d="M12 5v16M3 3c4-1 7 0 9 2 2-2 5-3 9-2v16c-4-1-7 0-9 2-2-2-5-3-9-2V3Z"/>',
 'box':'<path d="m12 3 9 5v9l-9 5-9-5V8l9-5Zm0 9 9-4M12 12 3 8m9 4v10M7.5 5.5l9 5v5"/>',
 'steth':'<path d="M4 3v5a5 5 0 0 0 10 0V3M3 3h3m6 0h3M9 13v3a5 5 0 0 0 10 0v-3"/><circle cx="19" cy="10" r="3"/>',
 'cross':'<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6V3Z"/>',
 'shield':'<path d="M12 3 4 6v6c0 5 8 10 8 10s8-5 8-10V6l-8-3Z"/><path d="m8 12 3 3 5-6"/>',
 'lab':'<path d="M9 3h6M10 3v7L4 20a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1l-6-10V3M7 16h10"/>',
 'tooth':'<path d="M12 5C4-2 1 5 4 11c2 5 1 11 4 10 1-1 1-6 4-6s3 5 4 6c3 1 2-5 4-10 3-6 0-13-8-6Z"/>',
 'paw':'<ellipse cx="8" cy="6" rx="2" ry="3"/><ellipse cx="16" cy="6" rx="2" ry="3"/><ellipse cx="3.5" cy="12" rx="2" ry="2.5"/><ellipse cx="20.5" cy="12" rx="2" ry="2.5"/><path d="M6 19c0-3 3-7 6-7s6 4 6 7c0 4-4 1-6 1s-6 3-6-1Z"/>',
 'menu':'<path d="M4 6h16M4 12h16M4 18h16"/>','sliders':'<path d="M4 7h9m4 0h3M4 17h3m4 0h9"/><circle cx="15" cy="7" r="2"/><circle cx="9" cy="17" r="2"/>',
}
def icon(n):return f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'
def logo():return f'<a class="logo" href="#top" aria-label="Silver Medical home"><img src="@@silver-medical-reversed@@" alt="Silver Medical UK" width="300" height="300"></a>'
def photo(n,alt,cls='',eager=False):return f'<img class="photo {cls}" src="@@{n}@@" alt="{alt}" width="1536" height="1024" {"fetchpriority=high" if eager else "loading=lazy"}>'
def art(n,cls=''):return f'<div class="product-art art-{n} {cls}" role="img" aria-label="Illustrative medical product photograph"></div>'
def btn(text,target='browse',cls='primary'):return f'<a class="button {cls}" href="#{target}">{text}</a>'
CATS=[('Diagnostics','steth','Instruments for every examination',0),('Consumables','box','Everyday supplies for your practice',1),('Wound care','cross','Dressings, gauze and instruments',4),('Equipment','sliders','Equip your clinical workspace',3),('Dental','tooth','Essentials for the treatment room',5),('Veterinary','paw','Supplies for animal care',0),('Laboratory','lab','Sample handling essentials',3),('Infection control','shield','Keep your workspace prepared',1)]
PRODUCTS=[
 {'id':'stethoscope','name':'Dual-head stethoscope','category':'Diagnostics','pack':'Single instrument','price':38.5,'art':0,'tag':'Diagnostic essentials','description':'A familiar format for the examination room. Compare instrument construction, size and manufacturer information before selecting a model.','spec':['Forest green finish','Single instrument','Illustrative catalogue item']},
 {'id':'gloves','name':'Nitrile examination gloves','category':'Consumables','pack':'Box of 100 · Medium','price':5.95,'art':1,'tag':'Everyday essentials','description':'A staple for your supply cupboard. Pack count and size are shown together to make comparing your order easier.','spec':['Medium · Blue','Box of 100','Illustrative catalogue item']},
 {'id':'otoscope','name':'Pocket diagnostic otoscope','category':'Diagnostics','pack':'Single instrument','price':59.0,'art':2,'tag':'Diagnostic essentials','description':'A compact diagnostic instrument concept. The final product page will include verified model details, compatibility and manufacturer documentation.','spec':['Pocket format','Single instrument','Illustrative catalogue item']},
 {'id':'monitor','name':'Upper-arm blood pressure monitor','category':'Equipment','pack':'Monitor & cuff','price':42.0,'art':3,'tag':'Practice equipment','description':'A monitor and cuff presented together for easy comparison. The eventual catalogue will identify the exact model and included accessories.','spec':['Monitor with cuff','One set','Illustrative catalogue item']},
 {'id':'gauze','name':'Gauze dressings & bandage','category':'Wound care','pack':'Dressing pack','price':4.8,'art':4,'tag':'Treatment essentials','description':'A dressing pack concept for browsing the wound-care range. Pack contents and dimensions will be confirmed against the selected supplier product.','spec':['Gauze and bandage','One dressing pack','Illustrative catalogue item']},
 {'id':'instruments','name':'Stainless steel instrument set','category':'Dental','pack':'Set of 3 instruments','price':24.5,'art':5,'tag':'Treatment essentials','description':'A three-piece instrument selection for comparing catalogue layouts. Final use and handling information must come from the actual manufacturer.','spec':['Scissors, tweezers & forceps','Set of 3','Illustrative catalogue item']},
 {'id':'vet','name':'Veterinary examination stethoscope','category':'Veterinary','pack':'Single instrument','price':42.0,'art':0,'tag':'Veterinary essentials','description':'An illustrative instrument listing for the veterinary practice selection. Exact models and specifications will be supplied for the live catalogue.','spec':['Forest green finish','Single instrument','Illustrative catalogue item']},
 {'id':'forceps','name':'Laboratory instrument set','category':'Laboratory','pack':'Set of 3 instruments','price':22.0,'art':5,'tag':'Laboratory essentials','description':'A sample instrument selection for the laboratory category. Check exact model, materials and intended use in the final supplier record.','spec':['Stainless steel finish','Set of 3','Illustrative catalogue item']},
 {'id':'hygiene','name':'Disposable nitrile gloves','category':'Infection control','pack':'Box of 100 · Large','price':6.25,'art':1,'tag':'Workspace essentials','description':'A second pack size for comparing everyday supplies. Review the final supplier information to match the glove to your workflow.','spec':['Large · Blue','Box of 100','Illustrative catalogue item']},
]
def search():return f'<form class="search" role="search" data-search><label for="search-input" class="sr">Search the catalogue</label>{icon("search")}<input id="search-input" type="search" placeholder="Search medical essentials" autocomplete="off"><button type="submit" aria-label="Search products">{icon("search")}</button></form>'
def header():
 return f'''<header class="site-header"><div class="utility"><div class="shell"><span>Medical supplies. Thoughtfully selected.</span><div><a href="#guides">Buying guides</a><span>UK · GBP £</span></div></div></div><div class="shell masthead">{logo()}{search()}<div class="header-actions"><button class="icon-button" data-open="saved" aria-label="Saved products">{icon('heart')}<span class="desktop-label">Saved</span></button><button class="basket-button" data-open="basket" aria-label="Open basket">{icon('bag')}<span class="desktop-label">Basket</span><span data-count>0</span></button></div></div><div class="navigation"><div class="shell nav-inner"><details class="departments"><summary>{icon('grid')}<span>All departments</span>{icon('chevron')}</summary><div class="mega"><div><p class="eyebrow">Explore the catalogue</p><h2>Find your essentials.</h2><p>From the first examination to the everyday restock.</p>{btn('View all products','products','secondary')}</div><div class="mega-links">{''.join(f'<a href="#products" data-category="{n}">{icon(i)}<span>{n}<small>{desc}</small></span></a>' for n,i,desc,_ in CATS)}</div></div></details><nav aria-label="Primary navigation"><a href="#browse">The collections</a><a href="#products">Selected essentials</a><a href="#practice">For your practice</a><a href="#guides">Journal &amp; guides</a></nav><a class="nav-support" href="#help">Need a hand?</a></div></div></header>'''
def features():
 return f'<div class="benefit-strip shell">'+''.join(f'<div>{icon(i)}<span><strong>{t}</strong><small>{s}</small></span></div>' for i,t,s in [('grid','One considered catalogue','Explore across clinical specialties'),('box','Clear pack information','Compare quantities at a glance'),('heart','A list that works for you','Save essentials as you browse'),('book','Room for informed choices','Practical guides for your practice')])+'</div>'
def sectionhead(kicker,title,copy='',action='Browse all products'):
 return f'<div class="section-head"><div><p class="eyebrow">{kicker}</p><h2>{title}</h2>{f"<p>{copy}</p>" if copy else ""}</div>{f"<a class=underlink href=#products>{action}</a>" if action else ""}</div>'
def collections():
    return f'''<section class="shell section premium-collections" id="browse">{sectionhead('Considered collections','Made for the way you work.','The tools, supplies and equipment behind the everyday.')}<div class="editorial-grid"><a class="collection-large" href="#products" data-category="Diagnostics">{photo('diagnostics','Green stethoscope and silver diagnostic instruments')}<div><span class="eyebrow">The diagnostic collection</span><h3>A closer look.<br>A clearer picture.</h3><span class="underlink">Explore diagnostics</span></div></a><a class="collection-small supplies" href="#products" data-category="Consumables">{art(1)}<div><span class="eyebrow">The everyday collection</span><h3>Small essentials.<br>A big part of your day.</h3><span class="underlink">Shop consumables</span></div></a><a class="collection-small equipment" href="#products" data-category="Equipment">{photo('clinic','Sage green cabinetry and an examination couch')}<div><span class="eyebrow">The clinical workspace</span><h3>A place for better care.</h3><span class="underlink">Explore equipment</span></div></a></div></section>'''

def product_section():
    return f'''<section class="shell section products-section" id="products">{sectionhead('Selected essentials','Considered down to the detail.','Explore the sample catalogue, compare packs and build your list.','')}<div class="product-toolbar"><div class="filter-tabs" role="group" aria-label="Product categories"><button data-filter="All" aria-pressed="true">All essentials</button><button data-filter="Diagnostics" aria-pressed="false">Diagnostics</button><button data-filter="Consumables" aria-pressed="false">Consumables</button><button data-filter="Wound care" aria-pressed="false">Wound care</button><button data-filter="Equipment" aria-pressed="false">Equipment</button></div><label class="sort"><span class="sr">Sort products</span><select data-sort><option value="featured">Featured</option><option value="low">Price: low to high</option><option value="high">Price: high to low</option><option value="az">Name: A to Z</option></select>{icon('chevron')}</label></div><div class="result-line"><p data-results aria-live="polite"></p><button class="underlink" data-reset>Clear filters</button></div><div class="product-grid" data-products></div><div class="empty-state" data-empty hidden>{icon('search')}<h3>No matching essentials.</h3><p>Try a broader search or return to the full selection.</p><button class="button primary" data-reset>Show all essentials</button></div><div class="product-more"><button class="button secondary" data-more>Explore all essentials</button><span data-shown></span></div></section>'''

def practice():
 return f'''<section class="practice-story" id="practice"><div class="practice-photo">{photo('clinic','A light-filled clinical room with an examination couch and sage green cabinetry')}<span class="image-caption">Spaces that support your working day.</span></div><div class="practice-copy"><p class="eyebrow">For the whole practice</p><h2>Every room.<br>Every routine.<br><em>Everyday care.</em></h2><p>From setting up a treatment room to replenishing the supply cupboard, bring your practice essentials together in one place.</p><div class="practice-points"><span>{icon('check')} Browse by specialty</span><span>{icon('check')} Compare pack sizes</span><span>{icon('check')} Save your shortlist</span></div>{btn('Explore practice supplies','browse')}</div></section>'''
def guide_section():
 guides=[('packs','Purchasing essentials','The right pack. The right quantity.','A simple approach to comparing your everyday supplies.','box'),('room','Practice planning','A workspace, thoughtfully equipped.','Build a room-by-room list before you start your order.','grid'),('list','An easier restock','Make your next order a little simpler.','Keep a considered list of the things you use most.','book')]
 return f'''<section class="shell section guides" id="guides">{sectionhead('The practice journal','A little clarity goes a long way.','Practical ideas for a more organised working day.','')}<div class="guide-grid">{''.join(f'<button class="guide-card" data-guide="{id}"><div class="guide-visual guide-{id}">{icon(ic)}<span>{label}</span></div><div class="guide-text"><p class="eyebrow">{label} · 2 min read</p><h3>{title}</h3><p>{desc}</p><span class="underlink">Read the guide</span></div></button>' for id,label,title,desc,ic in guides)}</div></section>'''
def faq():
 items=[('How do I find supplies for my practice?','Start with a department or specialty, or search for a product name. You can narrow the selection using the category tabs and compare items by price.'),('Can I save items for another look?','Use the heart on a product card to add it to your saved list. Open Saved in the header to revisit those products. Your list stays available while you switch between desktop and mobile.'),('Where can I compare pack sizes?','Pack information appears directly beneath each product name. Open a product for a closer look at the sample details before adding it to your basket.'),('Are these products and prices available to order?','This is a design preview with illustrative products, photography and prices. The live catalogue, delivery options and ordering will be confirmed during implementation.')]
 return f'''<section class="shell faq-section" id="help"><div><p class="eyebrow">A little help</p><h2>Good questions.<br>Clear answers.</h2><p>Find your way around the catalogue.</p></div><div class="faq-list">{''.join(f'<details><summary>{q}{icon("plus")}</summary><p>{a}</p></details>' for q,a in items)}</div></section>'''
def footer():
 return f'''<section class="support-band"><div class="shell"><div><p class="eyebrow">Ready for your next working day</p><h2>Find the essentials.<br>Focus on the care.</h2></div>{btn('Explore the catalogue','products','light')}</div></section><footer><div class="shell footer-main"><div class="footer-brand">{logo()}<p>Medical supplies and equipment.<br>Thoughtfully brought together.</p><span>silvermedical.co.uk</span></div><div><h3>Explore</h3><a href="#products">All essentials</a><a href="#browse">Departments</a><a href="#practice">For your practice</a></div><div><h3>Departments</h3>{''.join(f'<a href="#products" data-category="{n}">{n}</a>' for n in ['Diagnostics','Consumables','Equipment','Wound care'])}</div><div><h3>Here to help</h3><a href="#guides">Buying guides</a><a href="#help">Common questions</a><button data-open="saved">Your saved products</button><button data-open="basket">Your basket</button></div></div><div class="shell footer-bottom"><span>© Silver Medical UK</span><span>Concept preview · Illustrative products, photography and prices.</span><a href="#top">Back to top</a></div></footer><dialog class="drawer" id="basket-dialog" aria-labelledby="basket-heading"><div class="dialog-head"><div><p class="eyebrow">Your selection</p><h2 id="basket-heading">Your basket <span data-count>0</span></h2></div><button class="icon-button" data-close aria-label="Close basket">{icon('close')}</button></div><div data-basket-lines></div><div class="basket-summary"><div><span>Sample subtotal</span><strong data-total>£0.00</strong></div><p>Illustrative prices. Delivery and tax are not calculated. This preview does not accept orders.</p><button class="button primary" data-close>Continue browsing</button></div></dialog><dialog class="drawer" id="saved-dialog" aria-labelledby="saved-heading"><div class="dialog-head"><div><p class="eyebrow">Your shortlist</p><h2 id="saved-heading">Saved essentials</h2></div><button class="icon-button" data-close aria-label="Close saved products">{icon('close')}</button></div><div data-saved-lines></div></dialog><dialog class="quick-dialog" id="quick-dialog" aria-labelledby="quick-heading"><button class="icon-button float-close" data-close aria-label="Close product details">{icon('close')}</button><div data-quick></div></dialog><dialog class="guide-dialog" id="guide-dialog" aria-labelledby="guide-heading"><button class="icon-button float-close" data-close aria-label="Close guide">{icon('close')}</button><div data-guide-content></div></dialog><div class="toast" role="status" data-toast hidden></div>'''

def hero():
    return f'''<section class="premium-hero">{photo('editorial','Silver diagnostic instruments, green stethoscope and gauze on emerald plinths','premium-hero-photo',True)}<div class="shell"><div class="premium-copy"><p class="eyebrow">The art of being prepared</p><h1>Behind every<br>moment of<br><em>care.</em></h1><p>A considered collection of medical essentials. <br>For the people who make a difference, every day.</p>{btn('Discover the collection','browse','light')}<div class="premium-hero-label"><span>Silver Medical UK</span><span>Care starts with the details.</span></div></div></div></section><div class="editorial-statement shell"><p class="eyebrow">Purpose in every detail</p><p>Precision in your instruments.<br><em>Simplicity in your everyday.</em></p><a class="underlink" href="#practice">Explore our approach</a></div>'''

def embed_assets(content):
    return re.sub(r'@@([a-z-]+)@@', lambda match: assets[match[1]], content)


def script_json(value):
    return json.dumps(value, ensure_ascii=False).replace('<', r'\u003c')


def build_storefront():
    styles = embed_assets((HERE / 'store.css').read_text(encoding='utf-8-sig'))
    script = (HERE / 'store.js').read_text(encoding='utf-8-sig')
    data = script_json({
        'products': PRODUCTS,
        'icons': {name: icon(name) for name in ICONS},
    })
    sections = hero() + collections() + product_section() + practice() + features() + guide_section() + faq()
    body = embed_assets(header() + f'<main id="main">{sections}</main>' + footer())
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<meta name="description" content="The Silver Edit, the selected Silver Medical homepage design.">
<title>Silver Medical | The Silver Edit</title>
<link rel="icon" href="{assets['silver-medical-mark']}">
<style>{styles}</style>
</head>
<body class="premium" id="top">
<a class="skip" href="#main">Skip to content</a>
{body}
<script>window.CONCEPT_DATA = {data};</script>
<script>{script}</script>
</body>
</html>"""


def main():
    review = (HERE / 'review.html').read_text(encoding='utf-8-sig')
    font_licenses = '\n\n'.join(
        (HERE / 'assets' / f'{name}-LICENSE.txt').read_text(encoding='utf-8')
        for name in ('manrope', 'cormorantgaramond')
    )
    presentation = review.replace('../../../apps/storefront/public/brand/silver-medical-mark.svg', assets['silver-medical-mark'])
    presentation = presentation.replace('/*STOREFRONT*/', script_json(build_storefront()))
    presentation = presentation.replace('<!-- FONT LICENSES -->', f'<!--\n{font_licenses}\n-->')
    OUT.write_text(presentation, encoding='utf-8')
    client_zip = OUT.parent.parent / 'Silver-Medical-Homepage-Mockups.zip'
    with ZipFile(client_zip, 'w', compression=ZIP_DEFLATED) as archive:
        archive.write(OUT, 'Silver Medical - The Silver Edit.html')
        archive.write(HERE / 'Start Here.txt', 'Start Here.txt')
    print(f'Built {OUT} and {client_zip.name}')


if __name__ == '__main__':
    main()
