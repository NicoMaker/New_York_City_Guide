// ==========================================================================
// render-hero.js — header con badge, titolo, voli, e striscia "at a glance"
// ==========================================================================
import { esc } from "../core/utils.js";

export function renderHero(trip) {
  const header = document.getElementById("heroSection");
  header.innerHTML = `
    <div class="wrap">
      <div class="hero-badge"><span class="dot"></span> ${esc(trip.badge)}</div>
      <h1>${trip.titleLines.map(esc).join("<br>")}</h1>
      <p class="sub">${esc(trip.sub)}</p>
      <p class="lead">${esc(trip.lead)}</p>
      <div class="flight-cards">
        ${trip.flights.map(f => `
          <div class="flight-card">
            <div class="fc-label">${esc(f.label)}</div>
            <div class="fc-route">${esc(f.route)}</div>
            <div class="fc-time">${esc(f.time)}</div>
            <div class="fc-date">${esc(f.date)}</div>
          </div>`).join("")}
      </div>
    </div>`;

  const glance = document.getElementById("glanceSection");
  glance.innerHTML = `
    <div class="wrap glance-row">
      ${trip.glance.map(g => `
        <div class="glance-item">
          <div class="gi-num">${esc(g.num)}</div>
          <div class="gi-label">${esc(g.label)}</div>
        </div>`).join("")}
    </div>`;
}
