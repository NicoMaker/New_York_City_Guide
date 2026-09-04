// ==========================================================================
// utils.js — funzioni di supporto condivise dai moduli di rendering
// ==========================================================================

/** Escapa testo per l'inserimento sicuro in innerHTML */
export function esc(str) {
  if (str == null) return "";
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

/** Link a Google Maps a partire da una query testuale o da lat/lon */
export function googleMapsLink({ mapQuery, lat, lon }) {
  if (mapQuery)
    return `https://maps.google.com/?q=${encodeURIComponent(mapQuery)}`;
  if (lat != null && lon != null)
    return `https://maps.google.com/?q=${lat},${lon}`;
  return null;
}

/** URL embed di OpenStreetMap centrato su lat/lon con marker */
export function osmEmbedUrl(lat, lon, delta = 0.006) {
  const bbox = [lon - delta, lat - delta, lon + delta, lat + delta].join("%2C");
  return `https://www.openstreetmap.org/export/embed.html?bbox=${bbox}&layer=mapnik&marker=${lat}%2C${lon}`;
}

/** Link "apri su OpenStreetMap" (fuori dall'iframe, per il tap da mobile) */
export function osmLink(lat, lon) {
  return `https://www.openstreetmap.org/?mlat=${lat}&mlon=${lon}#map=16/${lat}/${lon}`;
}

/**
 * Costruisce una mappa { codiceLinea: colore } a partire da transit.json,
 * cosi' ogni componente puo' colorare i chip delle linee metro in modo coerente.
 */
export function buildLineColorMap(transitData) {
  const map = {};
  for (const group of transitData.lines) {
    for (const code of group.codes) map[code] = group.color;
  }
  return map;
}

/** Genera l'HTML di una riga di chip circolari colorati per una stringa tipo "A/B/C/D" o "4/5/6" */
export function lineChipsHTML(lineString, lineColorMap) {
  if (!lineString) return "";
  const codes = lineString
    .split(/[\/,\s]+/)
    .filter(Boolean)
    .filter((c) => lineColorMap[c]);
  if (!codes.length) return "";
  const chips = codes
    .map((c) => {
      const color = lineColorMap[c] || "#555";
      return `<span class="line-chip" style="background:${color}" title="Linea ${esc(c)}">${esc(c)}</span>`;
    })
    .join("");
  return `<span class="line-chip-row">${chips}</span>`;
}

/** Icona testuale per modalita' di spostamento nel connettore tra tappe */
export function modeIcon(mode = "") {
  const m = mode.toLowerCase();
  if (m.includes("metro")) return "🚇";
  if (m.includes("traghetto")) return "⛴";
  if (m.includes("piedi")) return "🚶";
  if (m.includes("taxi") || m.includes("treno")) return "🚕";
  if (m.includes("airtrain") || m.includes("subway")) return "🚆";
  return "➜";
}

/** Formatta la distanza in stringa leggibile */
export function fmtDistance(km) {
  if (km == null) return "";
  if (km < 1) return `${Math.round(km * 1000)} m`;
  return `${km.toFixed(1)} km`;
}
