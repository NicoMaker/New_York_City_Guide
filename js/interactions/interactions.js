// ==========================================================================
// interactions.js — comportamenti dopo il rendering: apertura/chiusura
// delle tappe, progresso checklist bagaglio, pulsante "torna su".
// ==========================================================================

export function bindStopToggles(root) {
  root.querySelectorAll(".stop-head").forEach((head) => {
    head.addEventListener("click", () => {
      head.parentElement.classList.toggle("open");
    });
  });
}

export function bindPackingChecklist() {
  const list = document.getElementById("packingList");
  const bar = document.getElementById("packingBar");
  if (!list || !bar) return;

  const items = [...list.querySelectorAll("li")];

  function updateProgress() {
    const checked = items.filter((li) =>
      li.classList.contains("checked"),
    ).length;
    bar.style.width = `${(checked / items.length) * 100}%`;
  }

  items.forEach((li) => {
    li.addEventListener("click", () => {
      li.classList.toggle("checked");
      updateProgress();
    });
  });

  updateProgress();
}

export function bindTopButton() {
  const btn = document.getElementById("topBtn");
  if (!btn) return;

  window.addEventListener(
    "scroll",
    () => {
      btn.classList.toggle("show", window.scrollY > 600);
    },
    { passive: true },
  );

  btn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}
