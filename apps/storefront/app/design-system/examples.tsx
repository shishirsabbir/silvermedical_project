import { BrandExamples, TypeExamples } from './foundations';
import { AssetExamples } from './asset-examples';
import { ActionExamples, FeedbackExamples, FormExamples } from './control-examples';
import { NavigationExamples, OverlayExamples } from './pattern-examples';
import { CommerceExamples } from './commerce-examples';
import type { Section } from './library';

export function Examples({ section }: { section: Section }) {
  switch (section) {
    case 'brand': return <BrandExamples/>;
    case 'assets': return <AssetExamples/>;
    case 'typography': return <TypeExamples/>;
    case 'actions': return <ActionExamples/>;
    case 'forms': return <FormExamples/>;
    case 'navigation': return <NavigationExamples/>;
    case 'overlays': return <OverlayExamples/>;
    case 'feedback': return <FeedbackExamples/>;
    case 'products': return <CommerceExamples/>;
    default: return null;
  }
}
