"""Exercise the client preview and Silver Edit checkout in an isolated Chromium context.

Install Playwright for Python and its Chromium browser. Pass an optional base URL.
"""

import json
import re
import sys
from urllib.parse import urlsplit

from playwright.sync_api import expect, sync_playwright


def run(base, width):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context(viewport={"width": width, "height": 900}, reduced_motion="reduce")
        page = context.new_page()
        errors, outgoing = [], []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("request", lambda request: outgoing.append((request.url, request.post_data or "")))

        def visit(path):
            page.goto(base + path, wait_until="networkidle")

        def click_button(name):
            page.get_by_role("button", name=name, exact=True).click()

        visit("/")
        page.get_by_role("banner").get_by_role("link", name="Design system", exact=True).click()
        expect(page).to_have_url(base + "/design-system")
        expect(page.get_by_role("heading", level=1)).to_contain_text("Silver")
        page.get_by_role("main").get_by_role("link", name=re.compile("^Overlays")).click()
        expect(page).to_have_url(base + "/design-system/overlays")
        page.reload()
        click_button("Open dialog")
        dialog = page.get_by_role("dialog", name="Name your selection")
        expect(dialog).to_be_visible()
        page.keyboard.press("Escape")
        expect(dialog).to_be_hidden()
        page.get_by_role("link", name="View storefront").click()
        expect(page).to_have_url(base + "/")

        visit("/demo")
        click_button("Start a sample basket")
        expect(page).to_have_url(base + "/cart")
        page.reload()
        expect(page.get_by_role("link", name="Dual-head stethoscope").first).to_be_visible()
        page.get_by_role("link", name="Continue to checkout").click()
        click_button("Fill sample details")
        click_button("Continue to payment")
        click_button("Use declined card")
        click_button("Review order")
        page.get_by_role("button", name=re.compile("Place demo order")).click()
        expect(page.get_by_role("alert").filter(has_text="Demo payment declined")).to_be_visible()

        # Manually entering the test digits exercises formatting and validation as well as the fill button.
        page.get_by_label("Demo card number").fill("4242424242424242")
        page.get_by_label("Expiry (MM/YY)", exact=True).fill("1230")
        page.get_by_label("Security code").fill("123")
        click_button("Review order")
        place = page.get_by_role("button", name=re.compile("Place demo order"))
        expect(place).to_contain_text("£42.45")
        place.click()
        page.wait_for_url(re.compile(re.escape(base) + r"/orders/[^/]+$"))
        order_url = page.url
        reference = page.locator(".order-refbar").get_by_text(re.compile(r"^SM-[A-Z0-9]+$")).inner_text()
        expect(page.get_by_role("heading", name="Delivery status")).to_be_visible()
        for action in ["Mark as preparing", "Mark as dispatched", "Mark as delivered", "Request a return",
                       "Confirm return request", "Complete demo refund"]:
            click_button(action)
        page.reload()
        expect(page.locator(".order-status")).to_have_text("Refunded")
        page.get_by_role("link", name="Order messages", exact=True).click()
        page.get_by_label("Message", exact=True).select_option("refunded")
        expect(page.get_by_role("heading", name="Your refund is recorded.")).to_be_visible()
        visit("/track")
        page.get_by_label("Order reference").fill(reference)
        page.get_by_label("Delivery postcode").fill("SW1A 1AA")
        click_button("Track order")
        expect(page).to_have_url(order_url)

        stored = page.evaluate("() => JSON.stringify([Object.entries(localStorage), Object.entries(sessionStorage)])")
        for number in ["4242424242424242", "4000000000000002"]:
            assert number not in stored.replace(" ", ""), "Test card digits present in browser storage"
            assert all(number not in (url + data).replace(" ", "") for url, data in outgoing)
        assert not [u for u, _ in outgoing if urlsplit(u).netloc and urlsplit(u).netloc != urlsplit(base).netloc]
        assert not errors, json.dumps(errors)
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
        context.close()
        browser.close()


if __name__ == "__main__":
    base_url = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:3141").rstrip("/")
    for width in [390, 1440]:
        run(base_url, width)
        print(f"Passed {width}px: design system navigation and dialog, guest basket, decline/retry, checkout, tracking, return, refund and message preview.")

