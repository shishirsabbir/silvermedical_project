"use client";

import {
  cloneElement,
  forwardRef,
  useEffect,
  useId,
  useRef,
  useState,
  type AnchorHTMLAttributes,
  type ButtonHTMLAttributes,
  type CSSProperties,
  type InputHTMLAttributes,
  type KeyboardEvent,
  type ReactElement,
  type ReactNode,
  type SelectHTMLAttributes,
  type TextareaHTMLAttributes,
} from "react";
import {
  AlertCircle, Check, CheckCircle2, ChevronDown, Info,
  LoaderCircle, Minus, Plus, Search, TriangleAlert,
} from "lucide-react";

export type ButtonVariant = "primary" | "secondary" | "ghost" | "light" | "danger";
export type ControlSize = "sm" | "md" | "lg";

type ButtonAppearance = { variant?: ButtonVariant; size?: ControlSize };
export type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & ButtonAppearance & { loading?: boolean };

function classes(...values: Array<string | undefined | false>) {
  return values.filter(Boolean).join(" ");
}

export function buttonClass(variant: ButtonVariant, size: ControlSize, className?: string) {
  return classes("sm-button", `sm-button--${variant}`, `sm-button--${size}`, className);
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(function Button(
  { children, variant = "primary", size = "md", loading = false, disabled, className, type = "button", ...props },
  ref,
) {
  return (
    <button {...props} type={type} ref={ref} className={buttonClass(variant, size, className)}
      disabled={disabled || loading} aria-busy={loading || props["aria-busy"]}>
      {loading && <LoaderCircle aria-hidden="true" className="sm-spinner" />}
      {children}
    </button>
  );
});

export type LinkButtonProps = AnchorHTMLAttributes<HTMLAnchorElement> & ButtonAppearance & { href: string };
export const LinkButton = forwardRef<HTMLAnchorElement, LinkButtonProps>(function LinkButton(
  { variant = "primary", size = "md", className, ...props }, ref,
) {
  return <a {...props} ref={ref} className={buttonClass(variant, size, className)} />;
});

export type IconButtonProps = Omit<ButtonProps, "aria-label"> & { label: string };
export const IconButton = forwardRef<HTMLButtonElement, IconButtonProps>(function IconButton(
  { label, variant = "ghost", className, children, loading, ...props }, ref,
) {
  return (
    <Button {...props} ref={ref} variant={variant} loading={loading} aria-label={label} className={classes("sm-icon-button", className)}>
      {!loading && <span aria-hidden="true" className="sm-icon-button__glyph">{children}</span>}
    </Button>
  );
});

type FieldMetadata = {
  label: ReactNode;
  hint?: ReactNode;
  error?: ReactNode;
  hideLabel?: boolean;
};

type FieldAttributes = Pick<InputHTMLAttributes<HTMLInputElement>, "id" | "aria-invalid" | "aria-describedby"> & {
  id: string;
};
export type FieldProps = FieldMetadata & {
  id?: string;
  "aria-describedby"?: string;
  "aria-invalid"?: FieldAttributes["aria-invalid"];
  children: ReactElement<FieldAttributes> | ((attributes: FieldAttributes) => ReactNode);
};

/** Associates a single form control with its visible label, hint and validation message. */
export function Field({ id, label, hint, error, hideLabel, children, ...aria }: FieldProps) {
  const generated = useId();
  const childAria = typeof children === "function" ? undefined : children.props;
  const controlId = id ?? childAria?.id ?? generated;
  const hintId = hint ? controlId + "-hint" : undefined;
  const errorId = error ? controlId + "-error" : undefined;
  const control: FieldAttributes = {
    id: controlId,
    "aria-invalid": error ? true : aria["aria-invalid"] ?? childAria?.["aria-invalid"],
    "aria-describedby": classes(hintId, errorId, aria["aria-describedby"], childAria?.["aria-describedby"]) || undefined,
  };
  return (
    <div className="sm-field">
      <label id={controlId + "-label"} className={hideLabel ? "sm-control-sr" : "sm-field__label"} htmlFor={controlId}>{label}</label>
      {typeof children === "function" ? children(control) : cloneElement(children, control)}
      {hint && <div className="sm-field__hint" id={hintId}>{hint}</div>}
      {error && <div className="sm-field__error" id={errorId}>{error}</div>}
    </div>
  );
}

export type TextInputProps = InputHTMLAttributes<HTMLInputElement> & FieldMetadata;
export const TextInput = forwardRef<HTMLInputElement, TextInputProps>(function TextInput(
  { id, label, hint, error, hideLabel, className, type = "text", ...props }, ref,
) {
  return (
    <Field {...{ id, label, hint, error, hideLabel }}>
      <input {...props} ref={ref} type={type} className={classes("sm-input", className)} />
    </Field>
  );
});

export type TextareaProps = TextareaHTMLAttributes<HTMLTextAreaElement> & FieldMetadata;
export const Textarea = forwardRef<HTMLTextAreaElement, TextareaProps>(function Textarea(
  { id, label, hint, error, hideLabel, className, rows = 4, ...props }, ref,
) {
  return (
    <Field {...{ id, label, hint, error, hideLabel }}>
      <textarea {...props} ref={ref} rows={rows} className={classes("sm-input", "sm-textarea", className)} />
    </Field>
  );
});

export type ControlOption = { value: string; label: string; disabled?: boolean };
export type SelectProps = SelectHTMLAttributes<HTMLSelectElement> & FieldMetadata & { options?: readonly ControlOption[] };
export const Select = forwardRef<HTMLSelectElement, SelectProps>(function Select(
  { id, label, hint, error, hideLabel, options, className, children, ...props }, ref,
) {
  return (
    <Field {...{ id, label, hint, error, hideLabel }} aria-describedby={props["aria-describedby"]} aria-invalid={props["aria-invalid"]}>
      {(control) => (
        <div className="sm-select">
          <select {...props} {...control} ref={ref} className={classes("sm-input", className)}>
            {children ?? options?.map((option) => (
              <option key={option.value} value={option.value} disabled={option.disabled}>{option.label}</option>
            ))}
          </select>
          <ChevronDown className="sm-select__chevron" size={16} aria-hidden="true" />
        </div>
      )}
    </Field>
  );
});

export type SearchFieldProps = Omit<TextInputProps, "type"> & {
  onSearch?: (value: string) => void;
  submitLabel?: string;
};
export function SearchField({
  id, label, hint, error, hideLabel, className, disabled, onKeyDown, onSearch, submitLabel = "Search", ...props
}: SearchFieldProps) {
  const input = useRef<HTMLInputElement>(null);
  function handleKeyDown(event: KeyboardEvent<HTMLInputElement>) {
    onKeyDown?.(event);
    if (event.key === "Enter" && onSearch && !event.nativeEvent.isComposing && !event.defaultPrevented) {
      event.preventDefault();
      onSearch(event.currentTarget.value);
    }
  }
  return (
    <Field {...{ id, label, hint, error, hideLabel }} aria-describedby={props["aria-describedby"]} aria-invalid={props["aria-invalid"]}>
      {(control) => (
        <div className={classes("sm-search", className)} role="search">
          <Search className="sm-search__icon" size={18} aria-hidden="true" />
          <input {...props} {...control} type="search" ref={input} className="sm-input" disabled={disabled} onKeyDown={handleKeyDown} />
          {onSearch && (
            <Button size="sm" disabled={disabled} onClick={() => onSearch(input.current?.value ?? "")}>
              {submitLabel}
            </Button>
          )}
        </div>
      )}
    </Field>
  );
}

export type ComboboxProps = FieldMetadata & {
  id?: string;
  name?: string;
  options: readonly ControlOption[];
  value: string;
  onValueChange: (value: string) => void;
  placeholder?: string;
  disabled?: boolean;
  emptyText?: string;
};

/** Editable single-select. Typing narrows options, and selection commits the value. */
export function Combobox({
  id, label, hint, error, hideLabel, name, options, value, onValueChange,
  placeholder = "Search options", disabled = false, emptyText = "No matches",
}: ComboboxProps) {
  const generated = useId();
  const inputId = id ?? generated;
  const listId = inputId + "-options";
  const input = useRef<HTMLInputElement>(null);
  const list = useRef<HTMLUListElement>(null);
  const [expanded, setExpanded] = useState(false);
  const [above, setAbove] = useState(false);
  const [query, setQuery] = useState<string | null>(null);
  const [activeValue, setActiveValue] = useState<string | undefined>(undefined);
  const selected = options.find(option => option.value === value);
  const visible = options.filter(option => option.label.toLocaleLowerCase().includes((query ?? "").trim().toLocaleLowerCase()));
  const choices = visible.filter(option => !option.disabled);
  const activeIndex = visible.findIndex(option => option.value === activeValue && !option.disabled);
  const open = expanded && !disabled;

  useEffect(() => {
    if (!open || !list.current || activeIndex < 0) return;
    const current = list.current.children[activeIndex] as HTMLElement | undefined;
    if (!current) return;
    const listBounds = list.current.getBoundingClientRect();
    const bounds = current.getBoundingClientRect();
    if (bounds.top < listBounds.top) list.current.scrollTop -= listBounds.top - bounds.top;
    if (bounds.bottom > listBounds.bottom) list.current.scrollTop += bounds.bottom - listBounds.bottom;
  }, [activeIndex, open]);

  function show() {
    const bounds = input.current?.getBoundingClientRect();
    if (bounds) setAbove(window.innerHeight - bounds.bottom < 220 && bounds.top > window.innerHeight - bounds.bottom);
    setExpanded(true);
  }
  function close() {
    setExpanded(false);
    setQuery(null);
    setActiveValue(undefined);
  }
  function commit(option: ControlOption) {
    onValueChange(option.value);
    close();
  }
  function handleKey(event: KeyboardEvent<HTMLInputElement>) {
    if (event.nativeEvent.isComposing) return;
    if (event.key === "Escape" && open) {
      event.preventDefault();
      event.stopPropagation();
      close();
    } else if (event.key === "ArrowDown" || event.key === "ArrowUp") {
      event.preventDefault();
      show();
      if (!choices.length) return;
      const step = event.key === "ArrowDown" ? 1 : -1;
      const current = choices.findIndex(option => option.value === activeValue);
      const next = current < 0 ? (step > 0 ? 0 : choices.length - 1) : (current + step + choices.length) % choices.length;
      setActiveValue(choices[next]?.value);
    } else if (event.key === "Enter" && open) {
      event.preventDefault();
      if (activeIndex >= 0) commit(visible[activeIndex]);
      else if (choices.length === 1) commit(choices[0]);
      else close();
    }
  }

  return (
    <Field id={inputId} {...{ label, hint, error, hideLabel }}>
      {(control) => (
        <div className="sm-combobox" onBlur={event => {
          if (!event.currentTarget.contains(event.relatedTarget as Node | null)) close();
        }}>
          {name && <input type="hidden" name={name} value={value} disabled={disabled} />}
          <input {...control} ref={input} className="sm-input" role="combobox" type="text" autoComplete="off"
            aria-autocomplete="list" aria-expanded={open} aria-controls={open ? listId : undefined}
            aria-activedescendant={open && activeIndex >= 0 ? listId + "-" + activeIndex : undefined}
            value={query ?? selected?.label ?? ""} placeholder={placeholder} disabled={disabled}
            onClick={show} onFocus={event => { event.currentTarget.select(); show(); }}
            onChange={event => { setQuery(event.target.value); setActiveValue(undefined); show(); }} onKeyDown={handleKey} />
          <button type="button" className="sm-combobox__toggle" tabIndex={-1} disabled={disabled}
            aria-label={open ? "Close options" : "Show options"}
            onMouseDown={event => event.preventDefault()} onClick={() => {
              if (open) close();
              else { input.current?.focus(); show(); }
            }}>
            <ChevronDown size={17} aria-hidden="true" />
          </button>
          {open && (
            <ul ref={list} id={listId} role="listbox" aria-labelledby={inputId + "-label"}
              className="sm-combobox__list" data-above={above}>
              {visible.map((option, index) => (
                <li id={listId + "-" + index} key={option.value} role="option"
                  aria-selected={option.value === value} aria-disabled={option.disabled || undefined}
                  className={classes("sm-combobox__option", index === activeIndex && "sm-combobox__option--active")}
                  onMouseDown={event => event.preventDefault()}
                  onPointerMove={() => { if (!option.disabled) setActiveValue(option.value); }}
                  onClick={() => { if (!option.disabled) commit(option); }}>
                  {option.label}
                  {option.value === value && <Check size={16} aria-hidden="true" />}
                </li>
              ))}
              {!visible.length && <li role="option" aria-selected={false} aria-disabled="true" className="sm-combobox__empty">{emptyText}</li>}
            </ul>
          )}
        </div>
      )}
    </Field>
  );
}

export type CheckboxProps = Omit<TextInputProps, "type" | "hideLabel">;
export const Checkbox = forwardRef<HTMLInputElement, CheckboxProps>(function Checkbox(
  { id, label, hint, error, className, ...props }, ref,
) {
  const generated = useId();
  const controlId = id ?? generated;
  const hintId = hint ? controlId + "-hint" : undefined;
  const errorId = error ? controlId + "-error" : undefined;
  return (
    <div className={classes("sm-choice", className)}>
      <label htmlFor={controlId} className="sm-choice__label">
        <input {...props} ref={ref} id={controlId} type="checkbox" className="sm-choice__input"
          aria-invalid={error ? true : props["aria-invalid"]}
          aria-describedby={classes(props["aria-describedby"], hintId, errorId) || undefined} />
        <span>{label}</span>
      </label>
      {hint && <div className="sm-field__hint" id={hintId}>{hint}</div>}
      {error && <div className="sm-field__error" id={errorId}>{error}</div>}
    </div>
  );
});

export type RadioGroupProps = Omit<FieldMetadata, "hideLabel"> & {
  id?: string;
  name?: string;
  options: readonly ControlOption[];
  value: string;
  onValueChange: (value: string) => void;
  disabled?: boolean;
  required?: boolean;
};
export function RadioGroup({ id, name, label, hint, error, options, value, onValueChange, disabled, required }: RadioGroupProps) {
  const generated = useId();
  const groupId = id ?? generated;
  const hintId = hint ? groupId + "-hint" : undefined;
  const errorId = error ? groupId + "-error" : undefined;
  return (
    <fieldset id={groupId} disabled={disabled} className="sm-radio-group"
      aria-describedby={classes(hintId, errorId) || undefined} aria-invalid={error ? true : undefined}>
      <legend className="sm-field__label">{label}</legend>
      {options.map(option => (
        <label className="sm-choice__label" key={option.value}>
          <input type="radio" className="sm-choice__input" name={name ?? groupId} value={option.value}
            checked={value === option.value} disabled={option.disabled} required={required}
            onChange={() => onValueChange(option.value)} />
          <span>{option.label}</span>
        </label>
      ))}
      {hint && <div className="sm-field__hint" id={hintId}>{hint}</div>}
      {error && <div className="sm-field__error" id={errorId}>{error}</div>}
    </fieldset>
  );
}

export type SwitchProps = {
  id?: string;
  name?: string;
  label: ReactNode;
  checked: boolean;
  onCheckedChange: (checked: boolean) => void;
  disabled?: boolean;
  hint?: ReactNode;
};
export function Switch({ id, name, label, checked, onCheckedChange, disabled, hint }: SwitchProps) {
  const generated = useId();
  const controlId = id ?? generated;
  return (
    <div className="sm-switch">
      <label htmlFor={controlId} className="sm-choice__label">
        <input id={controlId} name={name} type="checkbox" role="switch" className="sm-switch__input"
          checked={checked} disabled={disabled} onChange={event => onCheckedChange(event.currentTarget.checked)}
          aria-describedby={hint ? controlId + "-hint" : undefined} />
        <span>{label}</span>
      </label>
      {hint && <div id={controlId + "-hint"} className="sm-field__hint">{hint}</div>}
    </div>
  );
}

export type QuantityControlProps = {
  label: string;
  value: number;
  onValueChange: (quantity: number) => void;
  min?: number;
  max?: number;
  disabled?: boolean;
};
export function QuantityControl({ label, value, onValueChange, min = 1, max = 99, disabled }: QuantityControlProps) {
  return (
    <div className="sm-quantity" role="group" aria-label={label}>
      <IconButton label={`Decrease ${label}`} size="sm" disabled={disabled || value <= min}
        onClick={() => onValueChange(Math.max(min, value - 1))}><Minus size={15} /></IconButton>
      <output aria-label={label} aria-live="polite">{value}</output>
      <IconButton label={`Increase ${label}`} size="sm" disabled={disabled || value >= max}
        onClick={() => onValueChange(Math.min(max, value + 1))}><Plus size={15} /></IconButton>
    </div>
  );
}

export type StatusTone = "info" | "success" | "warning" | "error";
export type StatusMessageProps = { tone?: StatusTone; title?: ReactNode; children?: ReactNode };
export function StatusMessage({ tone = "info", title, children }: StatusMessageProps) {
  const StatusIcon = { info: Info, success: CheckCircle2, warning: TriangleAlert, error: AlertCircle }[tone];
  return (
    <div className={`sm-status-message sm-status-message--${tone}`} role={tone === "error" ? "alert" : "status"}>
      <StatusIcon size={19} aria-hidden="true" />
      <div>{title && <strong>{title}</strong>}{children && <div>{children}</div>}</div>
    </div>
  );
}

export type EmptyStateProps = { title: ReactNode; description?: ReactNode; action?: ReactNode; icon?: ReactNode };
export function EmptyState({ title, description, action, icon }: EmptyStateProps) {
  return (
    <div className="sm-empty-state">
      {icon && <span aria-hidden="true" className="sm-empty-state__icon">{icon}</span>}
      <h3>{title}</h3>
      {description && <p>{description}</p>}
      {action && <div className="sm-empty-state__action">{action}</div>}
    </div>
  );
}

export type SkeletonProps = {
  width?: CSSProperties["width"];
  height?: CSSProperties["height"];
  label?: string;
  className?: string;
};
export function Skeleton({ width, height, label, className }: SkeletonProps) {
  return (
    <span className={classes("sm-skeleton", className)} style={{ width, height }}
      role={label ? "status" : undefined} aria-hidden={!label || undefined}>
      {label && <span className="sm-control-sr">{label}</span>}
    </span>
  );
}
