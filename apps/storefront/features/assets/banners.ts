import { departmentIcons, type DepartmentIconId } from '@silver-medical/ui/icons';
import artDirection from './art-direction.json';

type CollectionId = 'diagnostic-collection' | 'everyday-collection' | 'clinical-workspace';
export type BannerId = 'homepage' | CollectionId | DepartmentIconId;
type BannerKind = 'Homepage' | 'Collection' | 'Department';

interface Crop {
  src: string;
  width: number;
  height: number;
}

export interface BannerAsset {
  id: BannerId;
  title: string;
  kind: BannerKind;
  alt: string;
  desktop: Crop;
  mobile: Crop;
}

function banner(id: BannerId, title: string, kind: BannerKind, alt: string): BannerAsset {
  const base = '/images/banners/' + id;
  const profile = artDirection.shots[id].profile as keyof typeof artDirection.profiles;
  const { desktop, mobile } = artDirection.profiles[profile];
  return {
    id, title, kind, alt,
    desktop: { src: base + '-desktop.webp', width: desktop[0], height: desktop[1] },
    mobile: { src: base + '-mobile.webp', width: mobile[0], height: mobile[1] },
  };
}

export const homepageBanner = banner('homepage', 'Behind every moment of care', 'Homepage',
  'A silver and emerald stethoscope and folded ivory gauze on dark green plinths.');

export const collectionBanners = {
  diagnostics: banner('diagnostic-collection', 'The diagnostic collection', 'Collection',
    'An emerald stethoscope with silver diagnostic instruments.'),
  everyday: banner('everyday-collection', 'The everyday collection', 'Collection',
    'Examination gloves, cotton pads and paper tape on a pale green studio block.'),
  workspace: banner('clinical-workspace', 'The clinical workspace', 'Collection',
    'A daylight-filled consultation room with sage cabinetry and an examination couch.'),
};

const departmentDescriptions: Record<DepartmentIconId, string> = {
  diagnostics: 'An aneroid pressure gauge with its cuff and inflation bulb.',
  consumables: 'Pleated paper cups and folded gauze on a pale work surface.',
  'wound-care': 'A woven gauze roll unfurls beside a stack of dressing pads.',
  equipment: 'A green examination couch in a sunlit consulting room.',
  dental: 'A polished dental mirror and tweezers on a textured green bib.',
  veterinary: 'A veterinary weighing scale and green slip lead on an examination counter.',
  laboratory: 'Light passes through glass test tubes in a small metal rack.',
  'infection-control': 'A pump dispenser and folded wipes on a sage counter.',
};

export const departmentBanners = departmentIcons.map(({ id, label }) =>
  banner(id, label, 'Department', departmentDescriptions[id])
);

export const banners = [homepageBanner, ...Object.values(collectionBanners), ...departmentBanners];
