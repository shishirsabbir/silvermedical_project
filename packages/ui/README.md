# The Silver Edit UI

`@silver-medical/ui` contains the reusable React components and CSS tokens for Silver Medical. The homepage and gallery both consume this workspace package directly. To see each component's states and interactions, start the storefront and open the [design system](http://localhost:3000/design-system). [Setup and build commands](../../apps/storefront/README.md).

| Import path | Components |
|---|---|
| `@silver-medical/ui/brand` | `BrandLogo` with light, reversed, mark and stacked variants |
| `@silver-medical/ui/icons` | Eight department marks. Use `<DepartmentIcon name="dental" />` alongside a visible label, or supply `label="Dental"` when the symbol stands alone. Each mark has a matching SVG download in the asset library. |
| `@silver-medical/ui/controls` | Buttons and links, labelled fields, textareas, search, native select, searchable combobox, checkboxes, radio groups, switches, quantity controls, status messages, empty states and skeletons |
| `@silver-medical/ui/navigation` | Dropdown menus, tabs, breadcrumbs, pagination and accordions |
| `@silver-medical/ui/overlays` | Dialogs, drawers, popovers, tooltips and toasts |
| `@silver-medical/ui/commerce` | Product cards and list items, pack information, GBP prices, product photography, collection tiles, basket rows and catalogue controls |

## Using the components

Load the CSS in the app layout. Place the provider around the routes where a component calls `useToast()`. The storefront [root layout](../../apps/storefront/app/layout.tsx) already includes this setup.

```tsx
import type { ReactNode } from 'react';
import { ToastProvider } from '@silver-medical/ui/overlays';
import '@silver-medical/ui/tokens.css';
import '@silver-medical/ui/controls.css';
import '@silver-medical/ui/navigation.css';
import '@silver-medical/ui/overlays.css';
import '@silver-medical/ui/commerce.css';

export function Providers({ children }: { children: ReactNode }) {
  return <ToastProvider>{children}</ToastProvider>;
}
```

Components expose native events where they wrap native inputs. Custom selections report the committed value through `onValueChange`. Keep application state in the caller and use a client component when passing event handlers.

```tsx
'use client';

import { useState } from 'react';
import { Button, Select } from '@silver-medical/ui/controls';
import { useToast } from '@silver-medical/ui/overlays';

const packSizes = [
  { label: 'Box of 50', value: '50' },
  { label: 'Box of 100', value: '100' },
];

export function PackSelector() {
  const [pack, setPack] = useState('50');
  const { toast } = useToast();

  return (
    <>
      <Select label="Pack size" options={packSizes} value={pack}
        onChange={event => setPack(event.currentTarget.value)} />
      <Button onClick={() => toast({ title: `Selected box of ${pack}`, tone: 'success' })}>
        Confirm pack size
      </Button>
    </>
  );
}
```

## Design and interaction

- Change colour roles, body and display fonts, spacing, radii, focus colour and motion in [tokens.css](src/tokens.css). Manrope is the interface face. Cormorant Garamond is the editorial display face.
- Use `Button` for an action and `LinkButton` for a destination. Provide a descriptive `label` for icon buttons. A loading button disables repeat activation.
- Give each form control a label. Use `hideLabel` when the surrounding layout supplies the visual context. The field primitives generate linked IDs for hints and errors, and set the invalid state when an error is present.
- A native `Select` suits a short value list. A `Combobox` lets a user type to filter, move with the arrow keys and press Enter to commit. Escape dismisses the choices, and Tab leaves the control. Use a `DropdownMenu` for actions.
- Use a focusable `Button` or `IconButton` as an overlay trigger. Give dialogs, drawers and popovers a descriptive title. Dialogs and drawers keep keyboard focus inside while open. Escape closes the surface and returns focus to its opener. Provide a visible route to important information on touch devices as well as tooltip text.
- Use `StatusMessage` for a persistent inline message and `useToast()` for a brief announcement after an action. Use the empty, disabled and loading examples in the gallery when building the corresponding states on a new page.
- The [storefront asset guide](../../apps/storefront/README.md) covers the local fonts and their licenses, original logo files and illustrative product photography. A new host app should supply the same public asset paths when it uses these brand and commerce components.
