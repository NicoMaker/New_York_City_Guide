// ==========================================================================
// render-nav.js — barra sticky con le "linee" (giornate) del viaggio.
// Tutte le giornate sono raggiungibili: click sui bottoni, frecce ← →,
// drag col mouse, swipe col dito su mobile e frecce della tastiera.
// ==========================================================================
import { esc } from "../core/utils.js";

export function renderDayNav(days) {
  const dayNav = document.getElementById("dayNav");
  const wrap = dayNav.closest(".day-nav");

  // struttura: [freccia sinistra] [viewport con fade + scroll] [freccia destra]
  wrap.innerHTML = `
    <div class="day-nav-row">
      <button class="day-nav-arrow" type="button" data-dir="-1" aria-label="Giornata precedente">‹</button>
      <div class="day-nav-viewport">
        <div class="day-nav-fade left"></div>
        <div class="day-nav-scroll" id="dayNav" tabindex="0"></div>
        <div class="day-nav-fade right"></div>
      </div>
      <button class="day-nav-arrow" type="button" data-dir="1" aria-label="Giornata successiva">›</button>
    </div>`;

  const scroller = document.getElementById("dayNav");
  const prevBtn = wrap.querySelector('[data-dir="-1"]');
  const nextBtn = wrap.querySelector('[data-dir="1"]');
  const fadeLeft = wrap.querySelector(".day-nav-fade.left");
  const fadeRight = wrap.querySelector(".day-nav-fade.right");

  scroller.innerHTML = days.map(d => `
    <button data-target="${esc(d.id)}" style="color:${esc(d.color)}">
      <span class="chip"></span>${esc(d.date.split("—")[0].split(",")[0].trim().toUpperCase())} · ${esc(d.title.split(" ")[0].toUpperCase())}
    </button>`).join("");

  const buttons = [...scroller.querySelectorAll("button")];
  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      document.getElementById(btn.dataset.target)?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  // ------- frecce: scorrono la barra di uno "schermo" alla volta -------
  function scrollByStep(dir) {
    scroller.scrollBy({ left: dir * scroller.clientWidth * 0.8, behavior: "smooth" });
  }
  prevBtn.addEventListener("click", () => scrollByStep(-1));
  nextBtn.addEventListener("click", () => scrollByStep(1));

  // le frecce si attivano/disattivano da sole in base alla posizione di scroll
  function updateEdges() {
    const max = scroller.scrollWidth - scroller.clientWidth - 1;
    const atStart = scroller.scrollLeft <= 0;
    const atEnd = scroller.scrollLeft >= max;
    prevBtn.disabled = atStart;
    nextBtn.disabled = atEnd || max <= 0;
    fadeLeft.classList.toggle("visible", !atStart);
    fadeRight.classList.toggle("visible", !atEnd && max > 0);
  }
  scroller.addEventListener("scroll", updateEdges, { passive: true });
  window.addEventListener("resize", updateEdges);

  // ------- drag col mouse (desktop): clicca e trascina la barra -------
  let isDown = false, dragged = false, startX = 0, startScroll = 0;
  scroller.addEventListener("mousedown", (e) => {
    isDown = true; dragged = false;
    startX = e.pageX;
    startScroll = scroller.scrollLeft;
    scroller.classList.add("dragging");
  });
  window.addEventListener("mousemove", (e) => {
    if (!isDown) return;
    const delta = e.pageX - startX;
    if (Math.abs(delta) > 4) dragged = true;
    scroller.scrollLeft = startScroll - delta;
  });
  window.addEventListener("mouseup", () => {
    isDown = false;
    scroller.classList.remove("dragging");
  });
  // se e' stato un trascinamento, non far scattare il click sul bottone sottostante
  scroller.addEventListener("click", (e) => {
    if (dragged) { e.stopPropagation(); e.preventDefault(); }
    dragged = false;
  }, true);

  // ------- frecce della tastiera quando la barra e' focus -------
  scroller.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") { scrollByStep(1); e.preventDefault(); }
    if (e.key === "ArrowLeft") { scrollByStep(-1); e.preventDefault(); }
  });

  // il touch/swipe col dito su mobile funziona nativamente grazie a
  // overflow-x:auto + touch-action:pan-x, nessun listener aggiuntivo serve.

  updateEdges();

  // scrollspy: evidenzia il bottone della giornata visibile e la scorre in vista
  const sections = days.map(d => document.getElementById(d.id)).filter(Boolean);
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const activeBtn = buttons.find(b => b.dataset.target === entry.target.id);
        buttons.forEach(b => b.classList.toggle("active", b === activeBtn));
        if (activeBtn) activeBtn.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
      }
    });
  }, { rootMargin: "-40% 0px -55% 0px", threshold: 0 });

  sections.forEach(s => observer.observe(s));
}
