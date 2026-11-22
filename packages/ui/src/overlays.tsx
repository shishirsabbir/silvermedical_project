'use client';

import {
  createContext,
  useCallback,
  useContext,
  useId,
  useMemo,
  useRef,
  useState,
  type ReactElement,
  type ReactNode,
} from 'react';
import {
  Dialog as DialogPrimitive,
  Popover as PopoverPrimitive,
  Toast as ToastPrimitive,
  Tooltip as TooltipPrimitive,
} from 'radix-ui';
import { CircleAlert, CircleCheck, Info, X } from 'lucide-react';
import './overlays.css';

type Side = 'top' | 'right' | 'bottom' | 'left';

export interface TooltipProps {
  children: ReactElement;
  content: string;
  side?: Side;
}

export function Tooltip({ children, content, side = 'top' }: TooltipProps) {
  return (
    <TooltipPrimitive.Provider delayDuration={350}>
      <TooltipPrimitive.Root>
        <TooltipPrimitive.Trigger asChild>{children}</TooltipPrimitive.Trigger>
        <TooltipPrimitive.Portal>
          <TooltipPrimitive.Content
            className="sm-tooltip"
            side={side}
            sideOffset={7}
            collisionPadding={10}
          >
            {content}
            <TooltipPrimitive.Arrow className="sm-tooltip-arrow" width={10} height={5} />
          </TooltipPrimitive.Content>
        </TooltipPrimitive.Portal>
      </TooltipPrimitive.Root>
    </TooltipPrimitive.Provider>
  );
}

export interface PopoverProps {
  trigger: ReactElement;
  title: string;
  children: ReactNode;
  side?: Side;
  align?: 'start' | 'center' | 'end';
  open?: boolean;
  onOpenChange?: (open: boolean) => void;
}

export function Popover({
  trigger, title, children, side = 'bottom', align = 'start', open, onOpenChange,
}: PopoverProps) {
  const titleId = useId();
  return (
    <PopoverPrimitive.Root open={open} onOpenChange={onOpenChange}>
      <PopoverPrimitive.Trigger asChild>{trigger}</PopoverPrimitive.Trigger>
      <PopoverPrimitive.Portal>
        <PopoverPrimitive.Content
          className="sm-popover"
          aria-labelledby={titleId}
          side={side}
          align={align}
          sideOffset={8}
          collisionPadding={12}
        >
          <div className="sm-popover-header">
            <h3 id={titleId}>{title}</h3>
            <PopoverPrimitive.Close className="sm-overlay-close" aria-label="Close popover">
              <X size={17} aria-hidden="true" />
            </PopoverPrimitive.Close>
          </div>
          <div className="sm-popover-body">{children}</div>
        </PopoverPrimitive.Content>
      </PopoverPrimitive.Portal>
    </PopoverPrimitive.Root>
  );
}

export interface DialogProps {
  title: string;
  description?: string;
  trigger?: ReactElement;
  open?: boolean;
  defaultOpen?: boolean;
  onOpenChange?: (open: boolean) => void;
  children: ReactNode;
  footer?: ReactNode;
}

type ModalKind = 'dialog' | 'drawer';

function ModalSurface({
  title, description, trigger, open, defaultOpen, onOpenChange, children, footer, kind,
}: DialogProps & { kind: ModalKind }) {
  const previousFocus = useRef<HTMLElement | null>(null);
  return (
    <DialogPrimitive.Root open={open} defaultOpen={defaultOpen} onOpenChange={onOpenChange}>
      {trigger && <DialogPrimitive.Trigger asChild>{trigger}</DialogPrimitive.Trigger>}
      <DialogPrimitive.Portal>
        <DialogPrimitive.Overlay className="sm-overlay-backdrop" />
        <DialogPrimitive.Content
          className={'sm-modal-surface sm-' + kind}
          {...(description ? {} : { 'aria-describedby': undefined })}
          onOpenAutoFocus={() => {
            previousFocus.current = document.activeElement instanceof HTMLElement
              ? document.activeElement
              : null;
          }}
          onCloseAutoFocus={(event) => {
            // With an external opener Radix has no Trigger reference to return focus to.
            if (!trigger && previousFocus.current?.isConnected) {
              event.preventDefault();
              previousFocus.current.focus({ preventScroll: true });
            }
          }}
        >
          <div className="sm-modal-header">
            <div>
              <DialogPrimitive.Title className="sm-modal-title">{title}</DialogPrimitive.Title>
              {description && <DialogPrimitive.Description className="sm-modal-description">{description}</DialogPrimitive.Description>}
            </div>
            <DialogPrimitive.Close className="sm-overlay-close" aria-label={'Close ' + title}>
              <X size={20} aria-hidden="true" />
            </DialogPrimitive.Close>
          </div>
          <div className="sm-modal-body">{children}</div>
          {footer && <div className="sm-modal-footer">{footer}</div>}
        </DialogPrimitive.Content>
      </DialogPrimitive.Portal>
    </DialogPrimitive.Root>
  );
}

export function Dialog(props: DialogProps) {
  return <ModalSurface {...props} kind="dialog" />;
}

export function Drawer(props: DialogProps) {
  return <ModalSurface {...props} kind="drawer" />;
}

export interface ToastMessage {
  title: string;
  description?: string;
  tone?: 'success' | 'info' | 'error';
}

interface ToastEntry extends ToastMessage {
  id: number;
}

interface ToastController {
  toast: (message: ToastMessage) => void;
}

const ToastContext = createContext<ToastController | null>(null);
const toastSymbols = { success: CircleCheck, info: Info, error: CircleAlert };

export function ToastProvider({ children }: { children: ReactNode }) {
  const [messages, setMessages] = useState<ToastEntry[]>([]);
  const nextId = useRef(0);
  const toast = useCallback((message: ToastMessage) => {
    const entry = { ...message, id: ++nextId.current };
    setMessages((current) => [...current, entry]);
  }, []);
  const controller = useMemo(() => ({ toast }), [toast]);
  return (
    <ToastContext.Provider value={controller}>
      <ToastPrimitive.Provider swipeDirection="right" duration={5500} label="Notification">
        {children}
        {messages.slice(0, 3).map(({ id, title, description, tone = 'info' }) => {
          const Symbol = toastSymbols[tone];
          return (
            <ToastPrimitive.Root
              key={id}
              className="sm-toast"
              data-tone={tone}
              onOpenChange={(isOpen) => {
                if (!isOpen) setMessages((current) => current.filter((entry) => entry.id !== id));
              }}
            >
              <Symbol className="sm-toast-icon" size={20} aria-hidden="true" />
              <div className="sm-toast-copy">
                <ToastPrimitive.Title className="sm-toast-title">{title}</ToastPrimitive.Title>
                {description && <ToastPrimitive.Description className="sm-toast-description">{description}</ToastPrimitive.Description>}
              </div>
              <ToastPrimitive.Close className="sm-overlay-close" aria-label="Dismiss notification">
                <X size={16} aria-hidden="true" />
              </ToastPrimitive.Close>
            </ToastPrimitive.Root>
          );
        })}
        <ToastPrimitive.Viewport className="sm-toast-viewport" />
      </ToastPrimitive.Provider>
    </ToastContext.Provider>
  );
}

export function useToast(): ToastController {
  const controller = useContext(ToastContext);
  if (!controller) throw new Error('useToast must be used inside ToastProvider.');
  return controller;
}
