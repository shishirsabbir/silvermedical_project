export const helpTopics = {
  delivery: {
    title: 'Delivery & tracking',
    summary: 'Choose delivery and follow your order through dispatch.',
    sections: [
      { title: 'Delivery at checkout', body: 'Demo delivery covers England, Scotland and Wales. Standard delivery takes 3–5 working days and costs £3.95, or is free on baskets of £50 or more. Express delivery takes 1–2 working days and costs £6.95. Your choice and totals appear before confirmation.' },
      { title: 'Follow an order', body: 'Open the confirmation link or select Order history in your account. On the tracking page, enter your order reference and delivery postcode. You can also explore a sample shipment there.' },
      { title: 'Try a delivery update', body: 'The tracking page includes demo controls to advance an order through preparation, dispatch and delivery. All updates apply to the order in this browser.' },
    ],
    action: { text: 'Track an order', href: '/track' },
  },
  returns: {
    title: 'Returns & refunds', summary: 'Try a return and view the outcome on the order timeline.',
    sections: [
      { title: 'Find your order', body: 'Open the order from your tracking link or account history. Check the reference, items and order status before requesting a return.' },
      { title: 'Request a demo return', body: 'Once the demo order is marked delivered, use the return action on its detail page. You can follow its progress on the same timeline.' },
      { title: 'Review a refund', body: 'A simulated refund updates the order in this browser. This preview does not collect or refund money, arrange collections or issue physical return labels.' },
    ],
    action: { text: 'Find an order', href: '/track' },
  },
  contact: {
    title: 'Contact the team', summary: 'Prepare a sample enquiry about a product, order or account.',
    sections: [], action: { text: 'Browse customer care', href: '/help' },
  },
  privacy: {
    title: 'Privacy in the demo', summary: 'See which information is kept on your device.',
    sections: [
      { title: 'Use fictional details', body: 'The demonstration accepts example account, practice and checkout information. Avoid entering private clinical information, real passwords, personal identity documents or payment credentials.' },
      { title: 'Browser storage', body: 'Account records, address books, baskets, saved products, demo orders and preferences use browser storage. Account passwords are stored as salted hashes. Verification is simulated in a browser inbox. Signing out closes your account session on this tab.' },
      { title: 'Manage your information', body: 'Edit your profile or remove saved addresses in Your account. You can clear this site’s browser storage to remove the local demo records on your device, including sample order history. Only do this if you want to erase that history.' },
    ],
    action: { text: 'Manage preferences', href: '/cookies' },
  },
  terms: {
    title: 'Terms of the demo', summary: 'Understand how the preview catalogue and checkout work.',
    sections: [
      { title: 'A preview of the store', body: 'Silver Medical showcases a proposed medical-supplies shopping experience. Catalogue descriptions, prices, stock, delivery estimates, tax calculations and service options are illustrative.' },
      { title: 'Demo transactions', body: 'The payment, verification, professional review and delivery steps simulate a shopping journey. Use the sample payment information shown at checkout. Completing an order creates a local demonstration record.' },
      { title: 'Commercial information', body: 'Live selling will require confirmed operator and contact details, approved product records and the terms for the actual destination and order. This demo provides no route to purchase real products.' },
    ],
    action: { text: 'Explore the catalogue', href: '/shop' },
  },
} as const;
export type HelpTopic = keyof typeof helpTopics;
export const topicKeys = Object.keys(helpTopics) as HelpTopic[];
export function isHelpTopic(value: string): value is HelpTopic { return Object.hasOwn(helpTopics, value); }
