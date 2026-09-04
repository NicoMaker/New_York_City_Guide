// ==========================================================================
// render-gallery.js — striscia foto orizzontale scrollabile, mostrata
// sopra i dati/timeline di ogni giornata. Click su una foto -> scrolla
// e apre la tappa corrispondente nella timeline sottostante.
// ==========================================================================
import { esc } from "../core/utils.js";

export function renderDayGallery(day) {
  const withImages = day.stops
    .map((s, i) => ({ ...s, index: i }))
    .filter((s) => s.image);

  if (!withImages.length) return "";

  const thumbs = withImages
    .map(
      (s) => `
    <button class="gallery-thumb" data-stop-index="${s.index}" data-day="${esc(day.id)}" type="button">
      <span class="gt-time">${esc(s.time)}</span>
      <img src="${esc(s.image.src)}" alt="${esc(s.image.alt)}" loading="lazy">
      <span class="gt-caption">${esc(s.title)}</span>
    </button>`,
    )
    .join("");

  return `
    <div class="day-gallery">
      <p class="day-gallery-label">Scorri le foto della giornata</p>
      <div class="day-gallery-scroll">${thumbs}</div>
    </div>`;
}

/** Collega il click sulle miniature all'apertura/scroll della tappa corrispondente */
export function bindGalleryClicks(root) {
  root.querySelectorAll(".gallery-thumb").forEach((btn) => {
    btn.addEventListener("click", () => {
      const day = btn.dataset.day;
      const idx = btn.dataset.stopIndex;
      const stopEl = document.querySelector(
        `#${day} .stop[data-index="${idx}"]`,
      );
      if (!stopEl) return;
      stopEl.classList.add("open");
      stopEl.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  });
}
