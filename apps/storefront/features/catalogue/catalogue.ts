import type { Product } from '@silver-medical/ui/commerce';
import { departmentIcons, type DepartmentIconId } from '@silver-medical/ui/icons';
import { products } from '../home/products';

export interface CatalogueProduct extends Product {
  slug: string;
  sku: string;
  stock: number;
  professional: boolean;
  department: DepartmentIconId;
  family: string;
  variant: string;
  image: string;
  publication: 'sample' | 'approved';
  shoppingFeedApproved: boolean;
}

interface DemoRecord {
  sku: string;
  stock: number;
  variant: string;
  family?: string;
  professional?: boolean;
}

const records: Record<string, DemoRecord> = {
  stethoscope: { sku: 'SM-DG-101', stock: 18, variant: 'Forest green' },
  gloves: { sku: 'SM-CS-201-M', stock: 30, family: 'exam-gloves', variant: 'Medium' },
  'gloves-small': { sku: 'SM-CS-201-S', stock: 12, family: 'exam-gloves', variant: 'Small' },
  otoscope: { sku: 'SM-DG-102', stock: 0, variant: 'Pocket format' },
  monitor: { sku: 'SM-EQ-401', stock: 8, variant: 'Monitor and cuff' },
  gauze: { sku: 'SM-WC-301', stock: 25, variant: 'Dressing pack' },
  instruments: { sku: 'SM-DN-501', stock: 7, variant: 'Three-piece set', professional: true },
  vet: { sku: 'SM-VT-601', stock: 4, variant: 'Forest green' },
  forceps: { sku: 'SM-LB-701', stock: 11, variant: 'Three-piece set' },
  hygiene: { sku: 'SM-IC-801-L', stock: 16, variant: 'Large' },
};

const imageNames = ['stethoscope', 'gloves', 'otoscope', 'monitor', 'gauze', 'instruments'];
const descriptions: Record<string, string> = {
  stethoscope: 'A dual-head stethoscope with forest-green tubing and a silver chestpiece, presented as a single instrument.',
  gloves: 'Blue examination gloves in a dispenser box of 100. Select the required glove size before adding a box to your basket.',
  otoscope: 'A pocket-format otoscope with a silver handle and angled head, presented as a single instrument.',
  monitor: 'An upper-arm monitor with a separate cuff. Each pack contains one monitor-and-cuff set.',
  gauze: 'Woven gauze and bandage presented together in a single dressing pack.',
  instruments: 'Scissors, tweezers and forceps in a three-piece stainless steel set.',
  vet: 'A forest-green examination stethoscope supplied as one instrument in the veterinary selection.',
  forceps: 'A three-piece stainless steel instrument set from the laboratory selection.',
  hygiene: 'Large blue disposable nitrile gloves, presented in a dispenser box of 100.',
};
const smallGloves: Product = {
  ...products.find(product => product.id === 'gloves')!,
  id: 'gloves-small', pack: 'Box of 100 · Small',
  spec: ['Small · Blue', 'Box of 100', 'Illustrative catalogue item'],
};

export const catalogue: CatalogueProduct[] = [...products, smallGloves].map(product => {
  const record = records[product.id];
  const department = departmentIcons.find(item => item.label === product.category);
  if (!department || !record) throw new Error('Incomplete demo catalogue record: ' + product.id);
  return {
    ...product, ...record, slug: product.id, department: department.id,
    description: descriptions[product.id === 'gloves-small' ? 'gloves' : product.id],
    family: record.family ?? product.id, professional: record.professional ?? false,
    image: '/images/catalogue/' + imageNames[product.art] + '.webp',
    publication: 'sample', shoppingFeedApproved: false,
  };
});

export function getProduct(id: string) {
  return catalogue.find(product => product.id === id);
}

export const departmentCopy: Record<DepartmentIconId, string> = {
  diagnostics: 'Explore everyday diagnostic instruments for the examination room.',
  consumables: 'Compare pack sizes for the essentials you replenish most often.',
  'wound-care': 'Browse dressing packs, woven gauze and bandages.',
  equipment: 'Explore equipment and accessories for the clinical workspace.',
  dental: 'Compare instrument sets for the dental practice.',
  veterinary: 'Browse selected examination essentials for veterinary practice.',
  laboratory: 'Explore reusable instruments for the laboratory bench.',
  'infection-control': 'Compare disposable supplies and pack sizes for busy workspaces.',
};
