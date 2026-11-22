export const workflowLabels = { basket: 'Basket', card: 'Payment', parcel: 'Delivery', account: 'Account', receipt: 'Order messages', return: 'Returns' } as const;
export type WorkflowIconName = keyof typeof workflowLabels;
export function WorkflowIcon({ name, size = 32 }: { name: WorkflowIconName; size?: number }) {
  return <svg viewBox="0 0 32 32" width={size} height={size} aria-hidden="true" focusable="false"><use href={'/icons/shopping.svg#' + name}/></svg>;
}

