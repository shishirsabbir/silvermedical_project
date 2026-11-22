import type { SVGProps } from 'react';

const departmentLabels = {
  diagnostics: 'Diagnostics',
  consumables: 'Consumables',
  'wound-care': 'Wound care',
  equipment: 'Equipment',
  dental: 'Dental',
  veterinary: 'Veterinary',
  laboratory: 'Laboratory',
  'infection-control': 'Infection control',
} as const;

export type DepartmentIconId = keyof typeof departmentLabels;

function iconPath(id: DepartmentIconId) {
  return `/icons/departments/${id}.svg`;
}

type DepartmentIconEntry = {
  id: DepartmentIconId;
  label: (typeof departmentLabels)[DepartmentIconId];
  src: string;
};

export const departmentIcons: readonly DepartmentIconEntry[] = (Object.keys(departmentLabels) as DepartmentIconId[]).map(id => ({
  id,
  label: departmentLabels[id],
  src: iconPath(id),
}));

export interface DepartmentIconProps extends Pick<SVGProps<SVGSVGElement>, 'className' | 'style'> {
  name: DepartmentIconId;
  size?: number | string;
  /** Supply a name when the icon conveys information without adjacent text. */
  label?: string;
}

export function DepartmentIcon({ name, size = 24, label, className, style }: DepartmentIconProps) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 32 32"
      role={label ? 'img' : undefined}
      aria-label={label}
      aria-hidden={label ? undefined : true}
      focusable="false"
      className={className}
      style={style}
    >
      <use href={`${iconPath(name)}#art`} />
    </svg>
  );
}
