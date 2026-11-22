export const sections = [
  { slug: 'overview', title: 'Overview', group: 'Foundations', summary: 'Explore the Silver Edit component library.' },
  { slug: 'brand', title: 'Brand & colour', group: 'Foundations', summary: 'Logo artwork, surfaces and functional colours.' },
  { slug: 'assets', title: 'Asset library', group: 'Foundations', summary: 'Preview and download the photography, department icons and brand artwork used across Silver Medical.' },
  { slug: 'typography', title: 'Type & spacing', group: 'Foundations', summary: 'A serif for editorial moments and a sans serif for working interfaces.' },
  { slug: 'actions', title: 'Buttons & links', group: 'Components', summary: 'Primary actions, secondary actions, links and icon buttons.' },
  { slug: 'forms', title: 'Form controls', group: 'Components', summary: 'Collect input, search the catalogue and choose a value.' },
  { slug: 'navigation', title: 'Navigation', group: 'Components', summary: 'Move between sections, browse results and reveal related content.' },
  { slug: 'overlays', title: 'Overlays', group: 'Components', summary: 'Menus, contextual help, dialogs and drawers.' },
  { slug: 'feedback', title: 'Feedback & states', group: 'Components', summary: 'Acknowledge an action and explain loading, empty and error states.' },
  { slug: 'products', title: 'Products & basket', group: 'Storefront', summary: 'Browse product cards and list items, compare packs and adjust a basket.' },
] as const;

export type Section = (typeof sections)[number]['slug'];
export const sectionPath = (slug: Section) => slug === 'overview' ? '/design-system' : '/design-system/' + slug;

