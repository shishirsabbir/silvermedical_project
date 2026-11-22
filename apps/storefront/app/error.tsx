'use client';
import { Button, LinkButton } from '@silver-medical/ui/controls';
export default function ErrorPage({ reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return <main id="main" className="store-page store-system-state"><h1>Something interrupted this page.</h1><p className="lede">Try loading the page again, or return to the homepage.</p><Button onClick={reset}>Try again</Button>{' '}<LinkButton href="/" variant="secondary">Go to homepage</LinkButton></main>;
}

