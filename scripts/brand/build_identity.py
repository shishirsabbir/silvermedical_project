"""Render the storefront identity assets from its original logo and local fonts.

Requires Pillow, Playwright and its Chromium browser. Run from any directory.
"""

import base64
import io
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[2]
PUBLIC = ROOT / "apps" / "storefront" / "public"
IDENTITY = PUBLIC / "brand" / "identity"
FONTS = PUBLIC / "fonts"
EMERALD = "#082f26"
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def original(filename, viewbox, x, y, width, height, *, flat=False):
    svg = ET.parse(PUBLIC / "brand" / filename).getroot()
    svg.attrib = {
        "viewBox": viewbox, "x": str(x), "y": str(y),
        "width": str(width), "height": str(height),
    }
    if flat:
        for path in svg.iter(f"{{{SVG_NS}}}path"):
            path.set("fill", "#edf2ee")
    return ET.tostring(svg, encoding="unicode")


def icon(*, maskable=False, favicon=False):
    # The safe area uses the mark's optical centre and leaves space for OS masks.
    inset = 12 if maskable else 0
    mark = original("silver-medical-mark.svg", "-4.076 -0.548 120 120",
                    inset, inset, 120 - 2 * inset, 120 - 2 * inset, flat=favicon)
    radius = 23 if favicon else 0
    return f'''<svg xmlns="{SVG_NS}" width="120" height="120" viewBox="0 0 120 120">
  <title>Silver Medical</title>
  <rect width="120" height="120" rx="{radius}" fill="{EMERALD}"/>
  {mark}
</svg>'''


def font_face(filename, family, italic=False):
    payload = base64.b64encode((FONTS / filename).read_bytes()).decode("ascii")
    style = "italic" if italic else "normal"
    return (f"@font-face {{font-family:'{family}';font-style:{style};font-weight:200 800;"
            f"src:url(data:font/woff2;base64,{payload}) format('woff2');}}")


def social_art():
    typefaces = "".join([
        font_face("manrope-variable.woff2", "Manrope"),
        font_face("cormorant-variable.woff2", "Cormorant"),
        font_face("cormorant-italic.woff2", "Cormorant", italic=True),
    ])
    wordmark = original("silver-medical.svg", "0 0 300 67", 66, 56, 244, 55)
    emblem = original("silver-medical-mark.svg", "-4.076 -0.548 120 120",
                      707, 77, 480, 480)
    return f'''<svg xmlns="{SVG_NS}" width="1200" height="630" viewBox="0 0 1200 630">
  <title>The Silver Edit from Silver Medical UK</title>
  <defs>
    <style>{typefaces}</style>
    <linearGradient id="paper" x2="1" y2="1" gradientUnits="objectBoundingBox">
      <stop stop-color="#fafbf7"/><stop offset="1" stop-color="#e8eee5"/>
    </linearGradient>
    <radialGradient id="green" cx=".30" cy=".20" r=".97">
      <stop stop-color="#2b5548"/><stop offset=".65" stop-color="#123a30"/><stop offset="1" stop-color="#06281f"/>
    </radialGradient>
    <linearGradient id="plate" x1="0" y1="0" x2=".92" y2="1" gradientUnits="objectBoundingBox">
      <stop stop-color="#335e4f"/><stop offset=".48" stop-color="#183f32"/><stop offset="1" stop-color="#07291f"/>
    </linearGradient>
    <filter id="relief" x="-12%" y="-12%" width="135%" height="135%">
      <feDropShadow dx="0" dy="2" stdDeviation=".7" flood-color="#051f18" flood-opacity=".75"/>
      <feDropShadow dx="3" dy="8" stdDeviation="7" flood-color="#051f18" flood-opacity=".4"/>
    </filter>
    <clipPath id="art"><rect x="678" width="522" height="630"/></clipPath>
  </defs>
  <rect width="1200" height="630" fill="url(#paper)"/>
  {wordmark}
  <g fill="#123e33" font-family="Cormorant" font-weight="500">
    <text x="61" y="291" font-size="126" letter-spacing="-5">The Silver</text>
    <text x="61" y="415" font-size="158" font-style="italic" letter-spacing="-6">Edit.</text>
  </g>
  <text x="67" y="477" font-family="Manrope" font-size="23" font-weight="500" fill="#435c50">Instruments &amp; practice essentials</text>
  <path d="M67 531H610" stroke="#a5b3a4"/>
  <text x="67" y="574" font-family="Manrope" font-size="19" font-weight="600" fill="#173a31">silvermedical.co.uk</text>
  <g clip-path="url(#art)">
    <rect x="678" width="522" height="630" fill="url(#green)"/>
    <g fill="none" stroke="#adc8b4" stroke-width="1">
      <circle cx="947" cy="317" r="317" opacity=".20"/>
      <circle cx="947" cy="317" r="304" opacity=".16"/>
      <circle cx="947" cy="317" r="291" opacity=".12"/>
    </g>
    <circle cx="947" cy="317" r="234" fill="url(#plate)" stroke="#789481" stroke-width="1.15"/>
    <circle cx="947" cy="317" r="228" fill="none" stroke="#6d8a76" stroke-width=".75"/>
    <g filter="url(#relief)">{emblem}</g>
  </g>
</svg>'''


def render(page, svg, width, height, *, transparent=False):
    page.set_viewport_size({"width": width, "height": height})
    page.set_content("<style>*{margin:0}body>svg{display:block;width:100vw;height:100vh}</style>" + svg)
    page.evaluate("document.fonts.ready")
    return Image.open(io.BytesIO(page.screenshot(omit_background=transparent))).copy()


def main():
    IDENTITY.mkdir(exist_ok=True, parents=True)
    favicon = icon(favicon=True)
    (IDENTITY / "favicon.svg").write_text(favicon, encoding="utf-8")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(device_scale_factor=1)
        browser_mark = render(page, favicon, 512, 512, transparent=True)
        browser_mark.save(PUBLIC / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
        for name, size, maskable in [
            ("apple-touch-icon", 180, False), ("app-icon-192", 192, False),
            ("app-icon-512", 512, False), ("app-icon-maskable-512", 512, True),
        ]:
            tile = render(page, icon(maskable=maskable), size, size)
            tile.convert("RGB").save(IDENTITY / f"{name}.png", optimize=True)
        social = render(page, social_art(), 1200, 630)
        social.convert("RGB").save(IDENTITY / "silver-edit-social.png", optimize=True)
        browser.close()


if __name__ == "__main__":
    main()
