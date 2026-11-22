import type { ReactNode } from 'react';
import { BookOpen, Box, Check, ClipboardList, Grid2X2, Heart } from 'lucide-react';
import { LinkButton } from '@silver-medical/ui/controls';
import { Accordion } from '@silver-medical/ui/navigation';
import { CollectionTile } from '@silver-medical/ui/commerce';
import Link from 'next/link';
import { guides } from './guides';
import { BannerPicture } from '../assets/banner-picture';
import { collectionBanners, homepageBanner } from '../assets/banners';

export function SectionHeading({ eyebrow, title, children, action }: {
  eyebrow: string; title: string; children?: ReactNode; action?: ReactNode;
}) {
  return (
    <div className="edit-section-heading">
      <div>
        <p className="edit-eyebrow">{eyebrow}</p>
        <h2>{title}</h2>
        {children && <p className="edit-section-description">{children}</p>}
      </div>
      {action}
    </div>
  );
}

export function Hero() {
  return (
    <>
      <section className="edit-hero" aria-labelledby="edit-title">
        <BannerPicture asset={homepageBanner} className="edit-hero__photo" priority />
        <div className="edit-shell edit-hero__inner">
          <div className="edit-hero__copy">
            <p className="edit-eyebrow">The art of being prepared</p>
            <h1 id="edit-title">Behind every<br />moment of<br /><em>care.</em></h1>
            <p className="edit-hero__lede">
              A considered collection of medical essentials.<br /> For the people who make a difference, every day.
            </p>
            <LinkButton href="#browse" variant="light">Discover the collection</LinkButton>
          </div>
        </div>
      </section>
      <div className="edit-shell edit-statement">
        <span className="edit-eyebrow">Purpose in every detail</span>
        <p>Precision in your instruments.<br /><em>Simplicity in your everyday.</em></p>
        <a className="edit-link" href="#practice">Explore our approach</a>
      </div>
    </>
  );
}

export function Collections() {
  return (
    <section className="edit-shell edit-section" id="browse" aria-label="Collections">
      <SectionHeading eyebrow="Considered collections" title="Made for the way you work."
        action={<a className="edit-link" href="/shop">Browse all products</a>}>
        The tools, supplies and equipment behind the everyday.
      </SectionHeading>
      <div className="edit-collections">
        <CollectionTile title={'A closer look.\nA clearer picture.'} eyebrow="The diagnostic collection"
          action="Explore diagnostics" variant="feature" href="/departments/diagnostics"
          media={<BannerPicture asset={collectionBanners.diagnostics} alt="" />} />
        <CollectionTile title={'Small essentials.\nA big part of your day.'} eyebrow="The everyday collection"
          action="Shop consumables" variant="split" href="/departments/consumables"
          media={<BannerPicture asset={collectionBanners.everyday} alt="" />} />
        <CollectionTile title="A place for better care." eyebrow="The clinical workspace"
          action="Explore equipment" variant="scene" href="/departments/equipment"
          media={<BannerPicture asset={collectionBanners.workspace} alt="" />} />
      </div>
    </section>
  );
}

export function PracticeStory() {
  const benefits = [
    { Icon: Grid2X2, title: 'One considered catalogue', body: 'Explore across clinical specialties' },
    { Icon: Box, title: 'Clear pack information', body: 'Compare quantities at a glance' },
    { Icon: Heart, title: 'A list that works for you', body: 'Save essentials as you browse' },
    { Icon: BookOpen, title: 'Room for informed choices', body: 'Practical guides for your practice' },
  ];
  return (
    <>
      <section className="edit-practice" id="practice" aria-labelledby="practice-title">
        <img src="/images/clinic.webp" width={1536} height={1024} loading="lazy"
          alt="Daylight falls across a clinical workspace with sage cabinetry and an examination couch" />
        <div className="edit-practice__copy">
          <p className="edit-eyebrow">For the whole practice</p>
          <h2 id="practice-title">Every room.<br />Every routine.<br /><em>Everyday care.</em></h2>
          <p>From setting up a treatment room to replenishing the supply cupboard, bring your practice essentials together in one place.</p>
          <ul>
            {['Browse by department', 'Compare pack sizes', 'Save your shortlist'].map((point) => (
              <li key={point}><Check aria-hidden size={17} />{point}</li>
            ))}
          </ul>
          <LinkButton href="#browse" variant="light">Explore practice supplies</LinkButton>
        </div>
      </section>
      <ul className="edit-shell edit-benefits">
        {benefits.map(({ Icon, title, body }) => (
          <li key={title}>
            <Icon aria-hidden size={27} strokeWidth={1.5} />
            <div><strong>{title}</strong><span>{body}</span></div>
          </li>
        ))}
      </ul>
    </>
  );
}

const journalIcons = { packs: Box, room: Grid2X2, list: ClipboardList };

export function Journal() {
  return (
    <section className="edit-shell edit-section" id="guides" aria-label="Buying guides">
      <SectionHeading eyebrow="The practice journal" title="A little clarity goes a long way.">
        Practical ideas for a more organised working day.
      </SectionHeading>
      <div className="edit-guides">
        {guides.map((guide) => {
          const Icon = journalIcons[guide.id];
          return (
            <article className="edit-guide" key={guide.id}>
              <div className={`edit-guide__art edit-guide__art--${guide.id}`} aria-hidden>
                <Icon strokeWidth={0.85} size={64} />
              </div>
              <div className="edit-guide__copy">
                <p className="edit-eyebrow">{guide.label}</p>
                <h3>{guide.title}</h3>
                <p>{guide.summary}</p>
                <Link className="edit-link" href={'/journal/' + guide.id} aria-label={'Read ' + guide.title}>Read the guide</Link>
              </div>
            </article>
          );
        })}
      </div>
    </section>
  );
}

export function Help() {
  const questions = [
    { value: 'search', title: 'How do I find supplies for my practice?', content: 'Start with a department or search for a product name. Narrow the selection using the category filters and compare items by price.' },
    { value: 'save', title: 'Can I save items for another look?', content: 'Use the heart on a product to add it to your saved list. Open Saved in the header to revisit those products while you browse.' },
    { value: 'packs', title: 'Where can I compare pack sizes?', content: 'Pack information appears beneath each product name. Open a product for more detail before adding it to your basket.' },
    { value: 'orders', title: 'Are these products and prices available to order?', content: 'This storefront uses sample stock and prices. Try a guest or account checkout with a test card, then follow your order through delivery.' },
  ];
  return (
    <section className="edit-shell edit-help" id="help">
      <SectionHeading eyebrow="A little help" title="Good questions. Clear answers.">
        Find your way around the catalogue.
      </SectionHeading>
      <Accordion items={questions} />
    </section>
  );
}
