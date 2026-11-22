export interface Guide {
  id: 'packs' | 'room' | 'list';
  label: string;
  title: string;
  summary: string;
  sections: Array<{ title: string; body: string }>;
}

export const guides: Guide[] = [
  {
    id: 'packs',
    label: 'Purchasing essentials',
    title: 'The right pack. The right quantity.',
    summary: 'A simple approach to comparing your everyday supplies.',
    sections: [
      { title: 'Start with the unit', body: 'A box, a case and a single item are different ways of buying. Read the pack description first, then compare the quantity with the way you use the product.' },
      { title: 'Compare like for like', body: 'Keep pack size, dimensions and the exact product variant together in your shortlist. A lower pack price is only useful when you understand what the pack contains.' },
      { title: 'Build a considered list', body: 'Save the items you want to compare, then review them together before adding quantities to your basket.' },
    ],
  },
  {
    id: 'room',
    label: 'Practice planning',
    title: 'A workspace, thoughtfully equipped.',
    summary: 'Build a room-by-room list before you start your order.',
    sections: [
      { title: 'Walk through the room', body: 'Start with the activities that take place in each space. Note the instruments, consumables, storage and equipment already in use, and identify the gaps.' },
      { title: 'Separate equipment from replenishment', body: 'Keep durable equipment and repeat supplies on separate lists. It makes a room setup easier to review and the next restock easier to plan.' },
      { title: 'Keep the details with the decision', body: 'Record dimensions, model references, accessory requirements and intended use when comparing equipment. Confirm those details against the manufacturer information.' },
    ],
  },
  {
    id: 'list',
    label: 'An easier restock',
    title: 'Make your next order a little simpler.',
    summary: 'Keep a considered list of the things you use most.',
    sections: [
      { title: 'Start with the cupboard', body: 'Make a short list of the products your practice reaches for regularly. Include the exact pack size and variant so the next review starts from the same place.' },
      { title: 'Keep a shortlist as you browse', body: 'Use the heart on a product to save it. Your saved list brings those items into one view, ready for comparing packs or adding them to a basket.' },
      { title: 'Review before ordering', body: 'Compare the list with your current stock and planned activity. Check quantities and product details before placing an order.' },
    ],
  },
];
