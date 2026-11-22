"""Construct the second Silver Medical identity collection as portable vector artwork."""
import base64
import math
from functools import lru_cache
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = Path(__file__).resolve().parents[2]
FONTS = Path('C:/Windows/Fonts')
FAMILIES = ['Wordmarks', 'Instrument symbols', 'Supply emblems']
# title, design note, ground, ink, highlight
CONCEPTS = [
 ('Capillary','A fine line leaves the foot of the L and runs beneath the rest of the name, like a capillary channel.','#182b2f','#f5f4dc','#afe2bd'),
 ('Meniscus','A low silver curve sits inside the V. Its shallow dip echoes the surface of liquid in a measuring cylinder.','#eee6dc','#432f39','#ae6147'),
 ('Registration','Two lines of monospaced capitals share one left edge. A stepped registration scale fills the shorter first line.','#eef0de','#20352a','#629049'),
 ('Folded V','Two triangular planes form the V in SILVER. Their crease is the only change of colour within the lettering.','#dce9fd','#183177','#496db9'),
 ('Ligature','The last stroke of a drawn S turns into the stem of the i. The shared stroke makes the opening pair a single letterform.','#442a3e','#fff1e4','#e9adba'),
 ('Cutline','A diagonal incision cuts through tall, closely set capitals. The smaller second line sits flush with the right edge.','#e9e9e5','#202c32','#08756c'),
 ('Baseline','Medical sits on a raised baseline beside a large italic Silver, like a note set beside a specimen name.','#f3e9cf','#453428','#a25534'),
 ('Microprint','Three fine parallel strokes construct every letter in SILVER. At a distance they read as a single band.','#112d48','#eaf2f1','#8ac3cd'),
 ('Counterform','The two words share a solid oval cartouche. Silver is set in italic, with MEDICAL tucked beneath its shoulder.','#e8e5f2','#3b365a','#ebe9f9'),
 ('Index tab','An upright, condensed SILVER sits on an asymmetric tab. Its clipped lower corner leads into MEDICAL.','#efe2d7','#4d2c23','#dc8659'),
 ('Vernier','Two opposing caliper jaws make an open measuring space. A single contrasting rule marks the reading.','#f0ebdc','#233b3e','#aa622f'),
 ('Aperture','Six overlapping blades turn around a clear hexagonal opening, borrowing the geometry of an optical diaphragm.','#252f46','#f0ece0','#a3b5e2'),
 ('Tuning fork','A pair of long tines flows into one stem. Three offset wavelets give the still instrument a sense of resonance.','#e8efdf','#334a35','#698944'),
 ('Pipette','A tapered pipette meets a single suspended drop. The diagonal cut gives the mark its direction.','#203c40','#e4f4e6','#a6e2bd'),
 ('Section plane','A stack of tissue-like contours is interrupted by one straight section line. The cut reveals the inner rings.','#f4e4df','#673445','#c36d69'),
 ('Optical axis','A biconvex lens bends three parallel rays toward one focal point. The point doubles as the symbol’s accent.','#e3eafa','#213b76','#8272b4'),
 ('Retractor','Opposing hooked arms hold a clear central opening. Broad rounded ends soften the instrument silhouette.','#3d2f3d','#f7eee4','#daac9e'),
 ('Microtome','Three progressively thinner slices sit beneath an angled cutting edge. Each slice has its own visible thickness.','#e4ebe7','#243e39','#55897d'),
 ('Dividers','Two compass legs pivot around one hinge. A short arc records the sweep of the movable tip.','#f3eddf','#2c3b49','#b86c41'),
 ('Diffraction','Five apertures open into a widening fan. Their spacing turns a familiar optical pattern into a compact mark.','#202846','#f2ecdc','#b3a5dc'),
 ('Peel tab','A packet corner lifts to reveal a second colour. The diagonal fold gives a square seal a recognisable face.','#eee9d9','#36463a','#abc58e'),
 ('Nest','Three offset tray outlines fit inside one another. An open corner lets the nesting order read at a glance.','#17343e','#ebefe5','#8abfb7'),
 ('Bellows','Alternating faces turn a folded insert into a narrow pleated emblem. Its zigzag edge carries the silhouette.','#eddfd8','#633d36','#c17b5f'),
 ('Breakaway','A perforated strip separates two halves of a pack. One lifted end makes the opening action visible.','#eee9f4','#44365e','#9f87bd'),
 ('Gusset','Four creases converge on the underside of a folded carton. The inset diamond picks out the central seam.','#263728','#f0eed8','#bbcf8e'),
 ('Ampoule tray','Four circular wells sit in a rounded tray. An angled corner marks the orientation of the insert.','#e6eeee','#214954','#68a5ad'),
 ('Pull loop','A doubled loop threads through a short slot. The open tail becomes a simple cue for pulling.','#40313b','#f6e6dc','#e2ad96'),
 ('Lot stamp','A scalloped label holds a staggered array of bars. A missing corner bar gives the stamp its own rhythm.','#ede3ca','#413b29','#a77739'),
 ('Woven wrap','Four broad strips interlace to form a square of woven dressing. Visible breaks establish the over-under pattern.','#e1eae1','#2f4b41','#7c9e82'),
 ('Corner guard','Three nested right angles cradle an open square. The exposed corner reveals how the pieces fit together.','#26394f','#e4edf4','#98c0da')
]

@lru_cache(None)
def face(filename):
    return TTFont(FONTS / filename)

def path(d, color, stroke=0):
    if stroke:
        return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linejoin="round" stroke-linecap="round"/>'
    return f'<path d="{d}" fill="{color}"/>'

def circle(x,y,r,color):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'

def group(inner, transform):
    return f'<g transform="{transform}">{inner}</g>'

def lettering(word,font,box,color,tracking=0,align='left'):
    """Fit actual glyph outlines to a rectangle so the mark travels with the HTML."""
    font=face(font)
    glyphs=font.getGlyphSet()
    cmap=font.getBestCmap()
    cursor=0
    pieces=[]
    bounds=[]
    for char in word:
        glyph=glyphs[cmap[ord(char)]]
        pen=SVGPathPen(glyphs)
        glyph.draw(pen)
        bound=BoundsPen(glyphs)
        glyph.draw(bound)
        if bound.bounds:
            x0,y0,x1,y1=bound.bounds
            bounds.append((x0+cursor,y0,x1+cursor,y1))
            pieces.append(group(path(pen.getCommands(),color),f'translate({cursor} 0)'))
        cursor+=glyph.width+tracking
    left=min(b[0] for b in bounds); bottom=min(b[1] for b in bounds)
    right=max(b[2] for b in bounds); top=max(b[3] for b in bounds)
    x,y,w,h=box
    scale=min(w/(right-left),h/(top-bottom))
    extra=w-(right-left)*scale
    x+= {'center':extra/2,'right':extra,'left':0}[align]
    y+=(h-(top-bottom)*scale)/2
    return group(''.join(pieces),f'translate({x:.2f} {y:.2f}) scale({scale:.6f} {-scale:.6f}) translate({-left} {-top})')

def wordmark(i,bg,ink,ac):
    def letters(word,font,box,color=ink,tracking=0,align='left'):
        return lettering(word,font,box,color,tracking,align)
    def caption(box,align='left'):
        return letters('MEDICAL','corbelb.ttf',box,ink,440,align)
    if i==0:
        return letters('SILVER','corbell.ttf',(100,65,400,89),ink,80,'center')+path('M201 157 V162 H498',ac,2)+caption((100,173,400,20),'center')
    if i==1:
        return letters('SIL','constan.ttf',(94,77,146,85),ink,0,'right')+path('M245 78 L273 158 H280 L311 78 H304 L277 145 L255 78 Z',ink)+path('M257 110 Q276 120 299 108',ac,3)+letters('ER','constan.ttf',(316,77,155,85))+caption((96,178,400,18),'center')
    if i==2:
        return letters('SILVER','consolab.ttf',(115,60,310,67))+letters('MEDICAL','consolab.ttf',(115,145,361,67))+''.join(path(f'M{427+j*8} 125 v{-10-j*4}',ac,3) for j in range(7))
    if i==3:
        return letters('SIL','segoeuib.ttf',(72,73,147,89),ink,-35,'right')+path('M225 76 H252 L276 140 L266 161 H255 Z',ink)+path('M266 161 L293 76 H318 L284 161 Z',ac)+letters('ER','segoeuib.ttf',(323,73,170,89),ink,-35)+caption((100,182,400,18),'center')
    if i==4:
        return path('M177 89 C142 65 95 91 119 112 C134 125 174 124 167 149 C159 174 111 171 102 151 M161 159 Q182 176 193 151 V113',ink,11)+circle(193,94,6,ac)+letters('lver','constani.ttf',(207,77,265,92))+caption((106,188,375,16),'center')
    if i==5:
        return letters('SILVER','bahnschrift.ttf',(97,55,405,117),ink,-50,'center')+path('M93 157 L511 99',bg,3)+letters('M E D I C A L','consola.ttf',(100,189,396,23),ink,20,'right')
    if i==6:
        return letters('Silver','georgiai.ttf',(64,75,304,106))+letters('Medical','constan.ttf',(379,81,150,42))+path('M379 133 H521',ac,2)
    if i==7:
        strokes=['M34 3H13Q2 3 2 12Q2 21 14 21H22Q34 21 34 31Q34 41 23 41H2','M6 3V41','M3 3V41H31','M1 3L17 41L34 3','M32 3H3V41H32 M4 21H26','M3 41V3H21Q34 3 34 14Q34 23 20 23H4 M20 23L35 41']
        xpos=[0,45,61,100,144,185]
        bands=''.join(group(path(d,ink,1.05),f'translate({x} {dy})') for d,x in zip(strokes,xpos) for dy in [0,2.4,4.8])
        return group(bands,'translate(83 66) scale(1.95)')+caption((93,178,414,19),'center')
    if i==8:
        return '<ellipse cx="300" cy="138" rx="212" ry="82" fill="'+ink+'"/>'+letters('Silver','georgiai.ttf',(151,79,290,78),ac,0,'center')+letters('MEDICAL','corbelb.ttf',(211,168,201,18),ac,300,'center')
    return path('M68 62H348V166L320 194H68Z',ink)+letters('SILVER','bahnschrift.ttf',(84,76,247,83),bg,-60,'center')+path('M320 194V166H348Z',ac)+letters('MEDICAL','consolab.ttf',(360,126,174,36),ink,45)

def symbol(i,bg,ink,ac):
    def p(d,col=ink,s=0): return path(d,col,s)
    if i==0: return p('M8 16 H92 V28 H28 V66 L15 81 V28 H8Z')+p('M44 32 H79 V84 L65 68 V43 H44Z',ac)+''.join(p(f'M{x} 17v{6 if x%2 else 4}',bg,1.5) for x in range(31,89,7))
    if i==1: return ''.join(group(p('M50 4 L87 25 L68 32 L51 32 L35 22 Z',ac if j==0 else ink),f'rotate({j*60} 50 50)') for j in range(6))
    if i==2: return p('M20 12 V41 C20 62 50 62 50 41 V12 M35 57V89',ink,9)+p('M63 25 Q72 35 63 46 M73 18 Q89 35 73 53',ac,4)
    if i==3: return p('M55 13L71 29L40 61L23 69L30 48Z')+p('M62 8L78 24 M29 65L22 73',ac,5)+p('M20 75Q8 88 19 92Q30 93 25 82Z',ac)
    if i==4:
        contour='M50 8 C73 6 94 36 85 58 C80 78 64 89 42 87 C20 85 10 69 13 48 C14 30 28 11 50 8Z'
        return ''.join(group(p(contour,ink,4.5),f'translate(50 49) scale({s}) translate(-50 -49)') for s in [1,.73,.47,.23])+p('M12 74L88 22',bg,10)+p('M12 74L88 22',ac,3)
    if i==5: return p('M47 10 Q21 50 47 90 Q73 50 47 10Z',ac)+p('M3 29 H37 L86 51 M3 51 H86 M3 72 H37 L86 51',ink,2.5)+circle(88,51,5,ink)
    if i==6: return p('M18 11V62Q18 76 34 76H44V65H37Q30 65 30 58V11Z')+p('M82 89V38Q82 24 66 24H56V35H63Q70 35 70 42V89Z',ac)+p('M13 12H35 M65 88H87',ink,5)
    if i==7: return p('M8 55L72 12L89 23L25 61Z')+p('M23 65L82 33V40L26 70Z',ac)+p('M25 76L82 49V54L28 80Z')+p('M28 85L82 64V67L30 88Z',ac)
    if i==8: return p('M18 86L47 22L53 22L82 86L57 52L50 37L40 58Z')+circle(50,22,11,ink)+circle(50,22,4,bg)+p('M12 69Q48 94 88 68',ac,3)
    if i==9: return ''.join(p(f'M12 {39+k*5} L87 {5+k*19} L87 {12+k*19} Z',ac if k==2 else ink) for k in range(5))+p('M9 30V70',ink,5)
    if i==10: return p('M13 15H87V58L57 87H13Z')+p('M57 87L58 57L87 58Z',ac)+p('M21 24H73M21 29H56',bg,2)
    if i==11: return ''.join(group(p('M77 16H23Q15 16 15 25V80H73Q83 80 83 70V39',ac if k==1 else ink,6),f'translate({k*14} {k*15}) scale({1-k*.23})') for k in range(3))
    if i==12: return ''.join(p(f'M{9+k*16} {29 if k%2==0 else 12} l16 {(-17 if k%2==0 else 17)} v57 l-16 {(17 if k%2==0 else -17)}Z',ink if k%2==0 else ac) for k in range(5))
    if i==13: return p('M8 30H62V70H8Z')+p('M68 30L92 21V60L68 70Z',ac)+''.join(p(f'M57 {y}V{y+4}',bg,2) for y in range(32,69,8))
    if i==14: return p('M49 7L91 31V69L49 93L8 69V31Z',ink)+p('M9 32L49 56L90 32M49 56V92',bg,3)+p('M26 41L49 27L73 41L49 55Z',ac)+p('M49 9V27',bg,2)
    if i==15: return p('M14 12H65L88 35V86H14Q9 86 9 81V17Q9 12 14 12Z')+''.join(circle(x,y,12,bg) for x,y in [(32,34),(64,40),(32,65),(64,68)])+circle(64,40,6,ac)
    if i==16: return p('M13 62H81V82H13Z',ac)+p('M38 69C34 52 22 23 40 16C71 3 77 39 55 54L38 69L23 90',ink,9)+p('M22 64H30 M53 65H71',bg,3)
    if i==17:
        pts=' '.join(f'{50+math.cos(k*math.pi/40)*(44 if k%2==0 else 41):.2f},{50+math.sin(k*math.pi/40)*(44 if k%2==0 else 41):.2f}' for k in range(80))
        return f'<polygon points="{pts}" fill="{ink}"/>'+''.join(p(f'M{x} {25+(j%2)*8}v{44-(j%2)*8}',bg,s) for j,(x,s) in enumerate([(28,3),(35,5),(44,2),(51,6),(60,3),(68,4)]))+circle(68,25,3,ac)
    if i==18: return p('M15 25H85V40H15Z M15 60H85V75H15Z',ac)+p('M25 15H40V85H25Z M60 15H75V85H60Z')+p('M21 25H44V40H21Z M56 60H80V75H56Z',ac)
    return p('M10 15H82V29H25V87H10Z')+p('M33 36H86V48H45V87H33Z',ac)+p('M52 55H89V65H62V87H52Z')

def artwork(index):
    name,_,bg,ink,accent=CONCEPTS[index]
    if index<10:
        drawing=wordmark(index,bg,ink,accent)
    else:
        local=index-10
        mark=symbol(local,bg,ink,accent)
        fonts=['corbelb.ttf','constan.ttf','georgia.ttf','calibrib.ttf','constanb.ttf','corbel.ttf','georgiai.ttf','bahnschrift.ttf','constan.ttf','corbelb.ttf']
        font=fonts[local%10]
        if local%4==1:
            drawing=group(mark,'translate(246 28) scale(1.08)')
            drawing+=lettering('Silver Medical',font,(74,155,452,61),ink,0,'center')
        elif local%4==2:
            drawing=group(mark,'translate(78 65) scale(1.36)')
            drawing+=lettering('Silver',font,(248,55,278,77),ink)
            drawing+=lettering('Medical',font,(248,144,278,64),ink)
        elif local%4==3:
            drawing=group(mark,'translate(80 70) scale(1.22)')
            drawing+=lettering('SILVER',font,(228,78,290,71),ink,60)
            drawing+=lettering('MEDICAL','corbelb.ttf',(231,165,280,23),ink,480)
        else:
            drawing=group(mark,'translate(41 73) scale(1.18)')
            drawing+=lettering('Silver Medical',font,(172,99,393,64),ink,-25)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270" role="img"><title>Silver Medical | {name}</title><rect width="600" height="270" fill="{bg}"/>{drawing}</svg>'

def build():
    template=(Path(__file__).with_name('silver_medical_collection.html')).read_text('utf-8')
    sections=[]
    hero=[]
    for family,heading in enumerate(FAMILIES):
        cards=[]
        for index in range(family*10,(family+1)*10):
            name,note,bg,ink,accent=CONCEPTS[index]
            code=f'{"ABC"[family]}{index%10+1:02}'
            svg=artwork(index)
            url='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()
            cards.append(f'''<article class="card" data-code="{code}" data-name="{name}">
              <button class="art" data-enlarge aria-label="Enlarge {code} {name}"><img width="600" height="270" src="{url}" alt="Silver Medical, {name} logo"></button>
              <div class="caption"><small>{code}</small><h3>{name}</h3><button class="star" data-save aria-label="Shortlist {code}" aria-pressed="false">☆</button></div><p>{note}</p></article>''')
            if index in [7,15,20]:
                hero.append(f'<a href="#family-{family}"><img src="{url}" width="600" height="270" alt="{name}"><span>{heading} <b>↘</b></span></a>')
        sections.append(f'<section class="family" id="family-{family}"><div class="sectionhead"><h2>{heading}</h2><span>10 concepts</span></div><div class="grid">{"".join(cards)}</div></section>')
    output=ROOT/'deliverables/html/SILVER_MEDICAL_LOGO_PRESENTATION.html'
    output.write_text(template.replace('<!--FAMILIES-->',''.join(sections)).replace('<!--HERO-->',''.join(hero)),encoding='utf-8')
    print(f'{output.name}: {len(CONCEPTS)} concepts, {output.stat().st_size:,} bytes')

if __name__=='__main__':
    build()
