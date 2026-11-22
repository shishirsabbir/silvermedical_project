import { LibraryShell } from './library-shell';
import type { ReactNode } from 'react';
import './library.css';

export default function DesignSystemLayout({ children }: { children: ReactNode }) {
  return <LibraryShell>{children}</LibraryShell>;
}
