import type { ReactNode } from 'react';

export function Specimen({ title, description, children, usage }: {
  title: string;
  description?: string;
  children: ReactNode;
  usage?: string;
}) {
  return <section className="lib-specimen">
    <div className="lib-specimen-head"><h2>{title}</h2>{description && <p>{description}</p>}</div>
    <div className="lib-specimen-stage">{children}</div>
    {usage && <details className="lib-usage"><summary>View React example</summary><pre><code>{usage}</code></pre></details>}
  </section>;
}
