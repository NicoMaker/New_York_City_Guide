// ==========================================================================
// main.js — punto di ingresso: carica i JSON e renderizza tutti i
// componenti della guida (hero, nav, giornate, metro, info pratiche).
// ==========================================================================
import { loadAll } from "./core/data.js";
import { buildLineColorMap } from "./core/utils.js";
import { renderHero } from "./hero/hero.js";
import { renderDayNav } from "./nav/nav.js";
import { renderDaySection } from "./day/day.js";
import { renderTransitSection } from "./transit/transit.js";
import { renderPractical } from "./practical/practical.js";
import { bindGalleryClicks } from "./gallery/gallery.js";
import { bindStopToggles, bindPackingChecklist, bindTopButton } from "./interactions/interactions.js";

async function init() {
  let data;
  try {
    data = await loadAll();
  } catch (err) {
    document.getElementById("main").innerHTML =
      `<p class="skeleton">Impossibile caricare i dati della guida (${err.message}).<br>
       Se hai aperto il file direttamente dal disco, avvia un piccolo server locale
       (es. <code>python3 -m http.server</code>) nella cartella del progetto e riapri
       da <code>http://localhost:8000</code> — i browser bloccano il caricamento dei
       file JSON con il protocollo file://.</p>`;
    console.error(err);
    return;
  }

  const { trip, transit, practical, days } = data;
  const lineColorMap = buildLineColorMap(transit);

  renderHero(trip);
  renderDayNav(days);

  const main = document.getElementById("main");
  main.innerHTML = "";
  days.forEach(day => {
    const section = renderDaySection(day, lineColorMap);
    main.appendChild(section);
  });

  renderTransitSection(transit);
  renderPractical(practical);

  // interazioni, da collegare dopo che il DOM e' stato popolato
  bindGalleryClicks(main);
  bindStopToggles(main);
  bindPackingChecklist();
  bindTopButton();
}

init();
