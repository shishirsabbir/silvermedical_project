import type { Metadata } from 'next';
import { ServiceCrumbs } from '../../features/support/service-crumbs';
import { Preferences } from '../../features/support/preferences';
import '../../features/support/service.css';

export const metadata: Metadata = { title: 'Cookie preferences', description: 'Choose how optional analytics and marketing preferences are saved on this browser.', alternates: { canonical: '/cookies' } };
export default function CookiesPage() {
  return <main className="se-service-shell" id="main"><ServiceCrumbs title="Cookie preferences"/>
    <header className="se-service-heading"><h1>Cookie <em>preferences.</em></h1><p>Choose the optional settings for this browser. You can change them here at any time.</p></header>
    <Preferences/>
  </main>;
}
