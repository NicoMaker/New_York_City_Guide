// ==========================================================================
// data.js — caricamento di tutti i file JSON della guida
// ==========================================================================

async function fetchJSON(path) {
  const res = await fetch(path, { cache: "no-store" });
  if (!res.ok)
    throw new Error(`Impossibile caricare ${path} (HTTP ${res.status})`);
  return res.json();
}

/**
 * Carica trip.json, transit.json, practical.json e l'indice delle giornate,
 * poi tutti i data/days/dayN.json in parallelo.
 * Ritorna { trip, transit, practical, days } pronto per il rendering.
 */
export async function loadAll() {
  const [trip, transit, practical, daysIndex] = await Promise.all([
    fetchJSON("data/trip.json"),
    fetchJSON("data/transit.json"),
    fetchJSON("data/practical.json"),
    fetchJSON("data/days-index.json"),
  ]);

  const days = await Promise.all(
    daysIndex.map((d) => fetchJSON(`data/days/${d.id}.json`)),
  );

  return { trip, transit, practical, days };
}
