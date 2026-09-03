// ==========================================================================
// render-nav.js — barra sticky con le 6 "linee" (giornate) del viaggio
// ==========================================================================
import { esc } from "../core/utils.js";

export function renderDayNav(days) {
  const nav = document.getElementById("dayNav");
  nav.innerHTML = days.map(d => `
    <button data-target="${esc(d.id)}" style="color:${esc(d.color)}">
      <span class="chip"></span>${esc(d.date.split("—")[0].split(",")[0].trim().toUpperCase())} · ${esc(d.title.split(" ")[0].toUpperCase())}
    </button>`).join("");

  const buttons = [...nav.querySelectorAll("button")];
  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      document.getElementById(btn.dataset.target)?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  // scrollspy: evidenzia il bottone della giornata visibile
  const sections = days.map(d => document.getElementById(d.id)).filter(Boolean);
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        buttons.forEach(b => b.classList.toggle("active", b.dataset.target === entry.target.id));
      }
    });
  }, { rootMargin: "-40% 0px -55% 0px", threshold: 0 });

  sections.forEach(s => observer.observe(s));
}
