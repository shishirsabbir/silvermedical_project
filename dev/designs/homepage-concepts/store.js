(() => {
'use strict';
const {products,icons}=window.CONCEPT_DATA;
const $=s=>document.querySelector(s);
const $$=s=>[...document.querySelectorAll(s)];
const money=n=>new Intl.NumberFormat('en-GB',{style:'currency',currency:'GBP'}).format(n);
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const product=id=>products.find(p=>p.id===id);
const art=p=>`<div class="product-art art-${p.art}" role="img" aria-label="Illustrative ${escape(p.name)} photograph"></div>`;
const cart={};
const saved=new Set();
let category='All',term='',sort='featured',limit=4;
let timer;
function announce(message){$('[data-toast]').textContent=message;$('[data-toast]').hidden=false;clearTimeout(timer);timer=setTimeout(()=>{$('[data-toast]').hidden=true;},2600);}
function persist(){
  $$('[data-count]').forEach(el=>el.textContent=Object.values(cart).reduce((a,b)=>a+b,0));
  $$('[data-save]').forEach(el=>{const active=saved.has(el.dataset.save);el.setAttribute('aria-pressed',String(active));el.setAttribute('aria-label',`${active?'Unsave':'Save'} ${product(el.dataset.save).name}`);});
}
function card(p){return `<article class="product-card" data-product="${p.id}"><div class="product-image"><button data-quick="${p.id}" aria-label="View ${escape(p.name)}">${art(p)}</button><button class="save-button" data-save="${p.id}" aria-pressed="${saved.has(p.id)}" aria-label="Save ${escape(p.name)}">${icons.heart}</button><span class="quick-label">Take a closer look</span></div><p class="product-meta">${escape(p.tag)}</p><h3 class="product-title"><button data-quick="${p.id}">${escape(p.name)}</button></h3><p class="pack">${escape(p.pack)}</p><div class="product-bottom"><strong class="price">${money(p.price)}<small>Sample price</small></strong><button class="add-button" data-add="${p.id}" aria-label="Add ${escape(p.name)} to basket"><span>Add</span>${icons.plus}</button></div></article>`;}
function renderProducts(){
  const words=term.toLowerCase().trim().split(/\s+/).filter(Boolean);
  let matches=products.filter(p=>(category==='All'||p.category===category)&&words.every(w=>`${p.name} ${p.category} ${p.pack}`.toLowerCase().includes(w)));
  if(sort==='low')matches.sort((a,b)=>a.price-b.price);if(sort==='high')matches.sort((a,b)=>b.price-a.price);if(sort==='az')matches.sort((a,b)=>a.name.localeCompare(b.name));
  const shown=matches.slice(0,limit);
  $('[data-products]').innerHTML=shown.map(card).join('');
  $('[data-empty]').hidden=matches.length>0;
  $('[data-results]').textContent=term?`${matches.length} results for “${term}”`:category==='All'?'A selection of practice essentials':`${matches.length} ${category.toLowerCase()} ${matches.length===1?'essential':'essentials'}`;
  $('[data-shown]').textContent=`Showing ${shown.length} of ${matches.length} sample products`;
  $('[data-more]').hidden=shown.length>=matches.length;
  $('.product-more').hidden=matches.length===0;
  $('.result-line [data-reset]').hidden=category==='All'&&!term;
  $$('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.filter===category)));
  persist();
}
function filter(next){category=next;term='';$('#search-input').value='';limit=category==='All'?4:products.length;renderProducts();}
function openDialog(id){const dialog=document.getElementById(id);if(!dialog.open)dialog.showModal();}
function lineItem(p,qty,savedMode=false){return `<div class="line-item" data-line="${p.id}">${art(p)}<div><h3>${escape(p.name)}</h3><p>${escape(p.pack)}</p><div class="line-row"><strong>${money(p.price*(savedMode?1:qty))}</strong>${savedMode?`<button class="add-button" data-add="${p.id}">Add ${icons.plus}</button>`:`<div class="quantity"><button data-quantity="${p.id}" data-delta="-1" aria-label="Decrease ${escape(p.name)} quantity">${icons.minus}</button><span aria-live="polite">${qty}</span><button data-quantity="${p.id}" data-delta="1" aria-label="Increase ${escape(p.name)} quantity">${icons.plus}</button></div>`}</div><button class="underlink" ${savedMode?'data-remove-saved':'data-remove'}="${p.id}">Remove</button></div></div>`;}
function empty(kind){return `<div class="drawer-empty">${icons[kind==='basket'?'bag':'heart']}<h3>${kind==='basket'?'Your basket is waiting.':'A place for your essentials.'}</h3><p>${kind==='basket'?'Add a few essentials and bring your next order together.':'Tap the heart on a product to keep it in your shortlist.'}</p><button class="button primary" data-close>Explore the catalogue</button></div>`;}
function renderBasket(){const ids=Object.keys(cart).filter(id=>product(id)&&cart[id]>0);$('[data-basket-lines]').innerHTML=ids.length?ids.map(id=>lineItem(product(id),cart[id])).join(''):empty('basket');$('[data-total]').textContent=money(ids.reduce((sum,id)=>sum+product(id).price*cart[id],0));persist();}
function renderSaved(){const ids=[...saved].filter(id=>product(id));$('[data-saved-lines]').innerHTML=ids.length?ids.map(id=>lineItem(product(id),1,true)).join(''):empty('saved');persist();}
function add(id){const p=product(id);if(!p)return;cart[id]=Math.min(99,(cart[id]||0)+1);renderBasket();announce(`${p.name} added to your basket.`);}
function quick(id){const p=product(id);if(!p)return;document.querySelector('#quick-dialog [data-quick]').innerHTML=`<div class="quick-layout"><div class="quick-art">${art(p)}</div><div class="quick-copy"><p class="eyebrow">${escape(p.category)}</p><h2 id="quick-heading">${escape(p.name)}</h2><p>${escape(p.description)}</p><ul>${p.spec.map(s=>`<li>${escape(s)}</li>`).join('')}</ul><strong class="price">${money(p.price)}<small>Sample price · ${escape(p.pack)}</small></strong><button class="button primary" data-add="${p.id}">${icons.bag} Add to basket</button><p class="disclaimer">Illustrative product and photography for design review.</p></div></div>`;openDialog('quick-dialog');}
const guides={
 packs:{label:'Purchasing essentials',title:'The right pack. The right quantity.',sections:[['Start with the unit','A box, a case and a single item are different ways of buying. Read the pack description first, then compare the quantity with the way you use the product.'],['Make like-for-like comparisons','Keep pack size, dimensions and the exact product variant together in your shortlist. A lower pack price is only useful when you understand what the pack contains.'],['Build a considered list','Save the items you want to compare, then review them together before adding quantities to your basket. This keeps the decision separate from the order.']]},
 room:{label:'Practice planning',title:'A workspace, thoughtfully equipped.',sections:[['Walk through the room','Start with the activities that take place in each space. Note the instruments, consumables, storage and equipment already in use, and identify the gaps.'],['Separate equipment from replenishment','Keep durable equipment and repeat supplies on separate lists. It makes a room setup easier to review and the next restock easier to plan.'],['Keep the details with the decision','Record dimensions, model references, accessory requirements and intended use when comparing equipment. Confirm those details against the final manufacturer information.']]},
 list:{label:'An easier restock',title:'Make your next order a little simpler.',sections:[['Start with the cupboard','Make a short list of the products your practice reaches for regularly. Include the exact pack size and variant so that the next review starts from the same place.'],['Keep a shortlist as you browse','Use the heart on a product to save it. Your saved list brings those items into one view, ready for comparing packs or adding them to a basket.'],['Review before ordering','Compare the list with your current stock and planned activity. Check quantities and exact product details before placing an order when the live storefront is available.']]}
};
function guide(id){const g=guides[id];if(!g)return;$('[data-guide-content]').innerHTML=`<p class="eyebrow">${escape(g.label)} · The practice journal</p><h2 id="guide-heading">${escape(g.title)}</h2>${g.sections.map(([h,p])=>`<h3>${escape(h)}</h3><p>${escape(p)}</p>`).join('')}<button class="button primary" data-close>Continue exploring</button>`;openDialog('guide-dialog');}
$('[data-search]').addEventListener('submit',e=>{e.preventDefault();term=$('#search-input').value.trim();category='All';limit=products.length;renderProducts();$('#products').scrollIntoView();});
$('[data-sort]').addEventListener('change',e=>{sort=e.target.value;renderProducts();});
document.addEventListener('click',e=>{
 const target=e.target.closest('button,a');if(!target)return;
 if(target.hasAttribute('data-category')){filter(target.dataset.category);$('.departments').open=false;}
 if(target.hasAttribute('data-filter'))filter(target.dataset.filter);
 if(target.hasAttribute('data-reset'))filter('All');
 if(target.hasAttribute('data-more')){limit=products.length;renderProducts();const next=$$('.product-card')[4];next?.querySelector('button')?.focus({preventScroll:true});}
 if(target.hasAttribute('data-save')){const id=target.dataset.save;saved.has(id)?saved.delete(id):saved.add(id);persist();announce(saved.has(id)?'Added to your saved essentials.':'Removed from your saved essentials.');}
 if(target.hasAttribute('data-add'))add(target.dataset.add);
 if(target.hasAttribute('data-open')){if(target.dataset.open==='basket')renderBasket();else renderSaved();openDialog(`${target.dataset.open}-dialog`);}
 if(target.hasAttribute('data-close'))target.closest('dialog')?.close();
 if(target.hasAttribute('data-quick'))quick(target.dataset.quick);
 if(target.hasAttribute('data-guide'))guide(target.dataset.guide);
 if(target.hasAttribute('data-quantity')){const id=target.dataset.quantity;cart[id]=Math.max(0,Math.min(99,(cart[id]||0)+Number(target.dataset.delta)));if(!cart[id])delete cart[id];const delta=target.dataset.delta;renderBasket();const next=$(`[data-quantity="${id}"][data-delta="${delta}"]`);(next||$('#basket-dialog [data-close]')).focus({preventScroll:true});}
 if(target.hasAttribute('data-remove')){delete cart[target.dataset.remove];renderBasket();$('#basket-dialog [data-close]').focus();}
 if(target.hasAttribute('data-remove-saved')){saved.delete(target.dataset.removeSaved);renderSaved();$('#saved-dialog [data-close]').focus();}
 if(target.closest('.mega')&&target.tagName==='A')$('.departments').open=false;
});
document.addEventListener('click',e=>{if(!e.target.closest('.departments'))$('.departments').open=false;});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&$('.departments').open){$('.departments').open=false;$('.departments summary').focus();}});
$$('dialog').forEach(d=>d.addEventListener('click',e=>{if(e.target!==d)return;const r=d.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)d.close();}));
renderProducts();renderBasket();
})();
