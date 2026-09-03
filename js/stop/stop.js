// ==========================================================================
// render-stop.js — una singola tappa della timeline (accordion) e il
// connettore "come arrivare alla prossima tappa" (distanza/tempo/mezzo).
// ==========================================================================
import { esc, googleMapsLink, osmEmbedUrl, osmLink, lineChipsHTML, modeIcon, fmtDistance } from "../core/utils.js";

export function renderStop(stop, index, lineColorMap) {
  const mapsUrl = googleMapsLink(stop);
  const hasCoords = stop.lat != null && stop.lon != null;

  const addrHTML = stop.address ? `<p class="stop-addr">${esc(stop.address)}</p>` : "";

  const linksHTML = `
    ${mapsUrl ? `<a class="map-link" href="${mapsUrl}" target="_blank" rel="noopener">Apri su Google Maps</a>` : ""}
    ${hasCoords ? `<a class="map-link" href="${osmLink(stop.lat, stop.lon)}" target="_blank" rel="noopener">Apri su OpenStreetMap</a>` : ""}
  `;

  const osmEmbed = hasCoords
    ? `<iframe class="osm-embed" loading="lazy" src="${osmEmbedUrl(stop.lat, stop.lon)}" title="Mappa OpenStreetMap — ${esc(stop.title)}"></iframe>`
    : "";

  const imgHTML = stop.image
    ? `<img class="stop-img" src="${esc(stop.image.src)}" alt="${esc(stop.image.alt)}" loading="lazy">`
    : "";

  const noteClass = stop.tag === "ATTENZIONE ORARI" ? " note" : "";

  return `
    <div class="stop${noteClass}" data-index="${index}">
      <div class="stop-head">
        <span class="stop-time">${esc(stop.time)}</span>
        <span class="stop-title">${esc(stop.title)}</span>
        <span class="stop-toggle">＋</span>
      </div>
      <div class="stop-body"><div class="stop-body-inner">
        <span class="stop-tag">${esc(stop.tag)}</span>
        <p>${esc(stop.text)}</p>
        ${addrHTML}
        ${linksHTML}
        ${imgHTML}
        ${osmEmbed}
      </div></div>
    </div>`;
}

/** Riga di collegamento tra una tappa e la successiva: mezzo, linea, distanza, tempo */
export function renderConnector(link, lineColorMap) {
  if (!link) return "";
  const chips = lineChipsHTML(link.line, lineColorMap);
  const modeLabel = link.line && chips ? "" : (link.line ? esc(link.line) : "");
  return `
    <div class="stop-connector">
      <span class="sc-icon">${modeIcon(link.mode)}</span>
      <span class="sc-mode">${esc(link.mode)}</span>
      ${chips}
      ${modeLabel ? `<span class="sc-meta">${modeLabel}</span>` : ""}
      <span class="sc-meta">${fmtDistance(link.distanceKm)} · ~${link.minutes} min</span>
      ${link.note ? `<span class="sc-note">${esc(link.note)}</span>` : ""}
    </div>`;
}
