// ==========================================================================
// render-practical.js — griglia info pratiche + checklist bagaglio
// ==========================================================================
import { esc } from "../core/utils.js";

export function renderPractical(practical) {
  const el = document.getElementById("practicalSection");

  const cardsHTML = practical.cards
    .map(
      (c) => `
    <div class="info-card">
      <h3>${esc(c.title)}</h3>
      <p>${esc(c.text)}</p>
    </div>`,
    )
    .join("");

  const itemsHTML = practical.packing.items
    .map(
      (label) => `
    <li><span class="box"></span><span class="label">${esc(label)}</span></li>`,
    )
    .join("");

  el.innerHTML = `
    <h2 class="section-title">${esc(practical.title)}</h2>
    <p class="section-lead">${esc(practical.lead)}</p>
    <div class="info-grid">${cardsHTML}</div>
    <div class="packing">
      <h3>${esc(practical.packing.title)}</h3>
      <p class="packing-sub">${esc(practical.packing.sub)}</p>
      <div class="packing-progress"><div class="packing-progress-bar" id="packingBar"></div></div>
      <ul class="packing-list" id="packingList">${itemsHTML}</ul>
    </div>
  `;
}
