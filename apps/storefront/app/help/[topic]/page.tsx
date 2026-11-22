import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { ArrowRight } from 'lucide-react';
import { helpTopics, isHelpTopic, topicKeys } from '../../../features/support/help-topics';
import { ContactForm } from '../../../features/support/contact-form';
import { ServiceCrumbs } from '../../../features/support/service-crumbs';
import '../../../features/support/service.css';

type Route = { params: Promise<{ topic: string }> };
export const dynamicParams = false;
export function generateStaticParams() { return topicKeys.map(topic => ({ topic })); }
export async function generateMetadata({ params }: Route): Promise<Metadata> {
  const { topic } = await params;
  if (!isHelpTopic(topic)) return {};
  return { title: helpTopics[topic].title, description: helpTopics[topic].summary, alternates: { canonical: '/help/' + topic } };
}
export default async function HelpTopicPage({ params }: Route) {
  const { topic } = await params;
  if (!isHelpTopic(topic)) notFound();
  const item = helpTopics[topic];
  return <main className="se-service-shell" id="main">
    <ServiceCrumbs title={item.title} inHelp/>
    <header className="se-service-heading"><h1>{item.title}</h1><p>{item.summary}</p></header>
    <div className="se-account-layout"><aside className="se-account-nav">
      <nav aria-label="Customer care topics">{topicKeys.map(key => <Link key={key} href={'/help/' + key} aria-current={key === topic ? 'page' : undefined}>{helpTopics[key].title}</Link>)}
        <Link href="/cookies">Cookie preferences</Link></nav></aside>
      <section className="se-service-card se-help-article">
        {topic === 'contact' ? <ContactForm/> : <>{item.sections.map(section => <section key={section.title}><h2>{section.title}</h2><p>{section.body}</p></section>)}
          <Link href={item.action.href} className="se-arrow-link">{item.action.text} <ArrowRight size={17}/></Link></>}
      </section></div>
  </main>;
}
