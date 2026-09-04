// ==========================================================================
// render-transit.js — sezione "Come muoversi in metro", con le linee
// realmente utilizzate nell'itinerario e le opzioni dall'aeroporto.
// ==========================================================================
import { esc } from "../core/utils.js";

export function renderTransitSection(transit) {
  const el = document.getElementById("transitSection");

  const linesHTML = transit.lines
    .map(
      (l) => `
    <div class="transit-line-row">
      <span class="line-chip-row">
        ${l.codes.map((c) => `<span class="line-chip" style="background:${esc(l.color)}">${esc(c)}</span>`).join("")}
      </span>
      <span class="tlr-name">${esc(l.name)}</span>
      <span class="tlr-note">${esc(l.note)}</span>
    </div>`,
    )
    .join("");

  const airportHTML = transit.airport.options
    .map(
      (o) => `
    <div class="airport-option">
      <div class="ao-mode">${esc(o.mode)}</div>
      <div class="ao-time">${esc(o.time)}</div>
      <div class="ao-cost">${esc(o.cost)}</div>
      <div class="ao-note">${esc(o.note)}</div>
    </div>`,
    )
    .join("");

  el.innerHTML = `
    <h2 class="section-title">Come muoversi in metro</h2>
    <p class="section-lead">${esc(transit.intro)}</p>
    <div class="transit-fare-box"><strong>Tariffe:</strong> ${esc(transit.fare)}</div>
    <div class="transit-lines">${linesHTML}</div>
    <h3 style="max-width:var(--content-w);margin:0 auto 14px;font-family:var(--font-display);font-size:19px;color:var(--white)">${esc(transit.airport.title)}</h3>
    <div class="airport-options">${airportHTML}</div>
  `;
}
