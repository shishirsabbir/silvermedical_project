"""Prepare the dated references used by the technical specification."""
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[2]
old = {s['id']: s for s in json.loads((ROOT/'docs/registers/CLIENT_PROPOSAL_SOURCES.json').read_text(encoding='utf-8'))}
for row in runpy.run_path(str(ROOT/'docs/content/project_plan_content.py'))['SOURCES']:
    old.setdefault(row[0], dict(zip(('id','title','url','checked','scope'), row)))

NEW = [
('NX01','Next.js self-hosting','https://nextjs.org/docs/app/guides/self-hosting','Self-hosted App Router, proxy, cache and deployment behaviour'),
('NE01','NestJS Fastify adapter','https://docs.nestjs.com/techniques/performance','Official HTTP adapter and compatibility guidance'),
('VI01','Vite guide','https://vite.dev/guide/','Frontend build tooling; exact compatible versions to be pinned'),
('DB01','PostgreSQL explicit locking','https://www.postgresql.org/docs/current/explicit-locking.html','Database concurrency and row-lock behaviour'),
('DB02','Prisma transactions','https://www.prisma.io/docs/orm/fundamentals/transactions','Transaction patterns; selected runtime/adapter needs verification'),
('DB03','PostgreSQL continuous archiving','https://www.postgresql.org/docs/current/continuous-archiving.html','Base backups, WAL archiving and point-in-time recovery'),
('JB01','pg-boss official repository','https://github.com/timgit/pg-boss','PostgreSQL-backed job processing; external side effects still need idempotency'),
('IM01','Sharp documentation','https://sharp.pixelplumbing.com/','Upload-time image resizing and encoding'),
('AU01','Better Auth Fastify integration','https://better-auth.com/docs/integrations/fastify','Library integration; proposed Nest/dual-realm design needs a spike'),
('AU02','Better Auth sessions','https://better-auth.com/docs/concepts/session-management','Database sessions and optional cookie cache; custom policy is project-specific'),
('AU03','Better Auth email/password','https://better-auth.com/docs/authentication/email-password','Verification, password reset and account-enumeration configuration'),
('AU04','Better Auth security','https://better-auth.com/docs/reference/security','Scrypt and library security features; deployment configuration remains required'),
('AU05','Better Auth two-factor plugin','https://better-auth.com/docs/plugins/2fa','TOTP and backup-code capabilities; mandatory staff enforcement is application policy'),
('AU06','Better Auth cookies','https://better-auth.com/docs/concepts/cookies','Session identifiers, cookie configuration and cache distinction'),
('OW01','OWASP session management','https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html','General web-session engineering guidance; numeric limits here are proposals'),
('OW02','OWASP authentication','https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html','Authentication, password and recovery engineering guidance'),
('OW03','OWASP CSRF prevention','https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html','Cookie-based web request protection'),
('SEO01','Core Web Vitals','https://web.dev/articles/vitals','Field LCP, INP and CLS thresholds at the 75th percentile'),
('SEO02','Lighthouse scoring','https://github.com/GoogleChrome/lighthouse/blob/main/docs/scoring.md','Automated category scoring; not a search-ranking score'),
('SEO03','Lighthouse performance scoring','https://developer.chrome.com/docs/lighthouse/performance/performance-scoring','Lab metric weighting and score interpretation'),
('SEO04','Google page experience','https://developers.google.com/search/docs/appearance/page-experience','Search page-experience guidance; no single overall ranking score'),
('SEO05','Google product structured data','https://developers.google.com/search/docs/appearance/structured-data/product','Product search presentation; rich-result appearance is not guaranteed'),
('SEO06','Ecommerce URL structure','https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites','Canonical URLs, navigation and ecommerce crawling'),
('SEO07','Google noindex guidance','https://developers.google.com/search/docs/crawling-indexing/block-indexing','Crawl/index controls; robots.txt is not access control'),
('A11Y01','WCAG 2.2','https://www.w3.org/TR/WCAG22/','Accessibility recommendation; AA is a proposed implementation target'),
('QA01','Playwright documentation','https://playwright.dev/docs/intro','Browser automation for functional and journey verification'),
('QA02','Grafana k6 test types','https://grafana.com/docs/k6/latest/testing-guides/test-types/','Load-test design; workload and thresholds are project assumptions'),
('CF01','R2 public buckets','https://developers.cloudflare.com/r2/buckets/public-buckets/','Public media custom domain; private evidence must remain separate'),
('CF02','R2 pricing','https://developers.cloudflare.com/r2/pricing/','Standard storage and operation allowances; usage, region/tax and provider terms matter'),
('PAY01','Revolut Merchant API','https://developer.revolut.com/docs/api/merchant/2026-03-12','Merchant integration contracts; account/catalogue acceptance is a separate dependency'),
('PAY02','PayPal webhooks','https://developer.paypal.com/api/rest/webhooks/','Payment-event integration; verify current account/API version'),
('PAY03','PayPal REST webhook verification','https://developer.paypal.com/api/rest/webhooks/rest/','Authenticity verification and webhook handling'),
]
for sid,title,url,scope in NEW:
    old[sid] = dict(id=sid,title=title,url=url,checked='9 Nov 2026',scope=scope)
sections=runpy.run_path(str(ROOT/'docs/content/technical_spec_content.py'))['SECTIONS']
used=sorted({r for s in sections for r in s['refs']})
assert all(s in old for s in used)
(ROOT/'docs/registers/TECHNICAL_SPEC_SOURCES.json').write_text(json.dumps([old[s] for s in used],indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'{len(used)} dated references prepared.')
