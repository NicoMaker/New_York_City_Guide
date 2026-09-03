// ==========================================================================
// render-day.js — assembla l'intera sezione di una giornata:
// intestazione, banner, riepilogo, galleria scrollabile, timeline con
// tappe e connettori "come arrivare" tra una tappa e l'altra.
// ==========================================================================
import { esc } from "../core/utils.js";
import { renderDayGallery } from "../gallery/gallery.js";
import { renderStop, renderConnector } from "../stop/stop.js";

export function renderDaySection(day, lineColorMap) {
  const section = document.createElement("section");
  section.className = "day-section";
  section.id = day.id;
  section.style.setProperty("--line-color", day.color);

  const linksByFromIndex = {};
  (day.links || []).forEach((l, i) => { linksByFromIndex[i] = l; });

  const stopsHTML = day.stops.map((stop, i) => {
    const stopHTML = renderStop(stop, i, lineColorMap);
    const isLast = i === day.stops.length - 1;
    const connectorHTML = isLast ? "" : renderConnector(linksByFromIndex[i], lineColorMap);
    return stopHTML + connectorHTML;
  }).join("");

  // Se il giorno è "00", lo trasformiamo in "31"
  const dayNumDisplay = day.num === "00" ? "31" : day.num;

  section.innerHTML = `
    <div class="day-head">
      <div class="day-num">${esc(dayNumDisplay)}</div>
      <div class="day-info">
        <h2>${esc(day.title)}</h2>
        <div class="day-date">${esc(day.date)}</div>
      </div>
    </div>
    <div class="day-banner-wrap">
      <img src="${esc(day.banner.src)}" alt="${esc(day.banner.alt)}" loading="lazy">
    </div>
    <p class="day-summary">${esc(day.summary)}</p>
    ${renderDayGallery(day)}
    <div class="timeline">${stopsHTML}</div>
  `;

  return section;
}