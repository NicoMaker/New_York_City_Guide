/* ==========================================================================
   NYC TRIP GUIDE — interactions
   1) Accordion sulle tappe della timeline
   2) Day-nav sticky con scrollspy (evidenzia il giorno visibile)
   3) Checklist bagaglio con barra di avanzamento
   4) Pulsante "torna su"
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* ---------------------------------------------------------------
     1) ACCORDION — click su una tappa per espandere/richiudere
     --------------------------------------------------------------- */
  document.querySelectorAll('.stop-head').forEach(head => {
    head.addEventListener('click', () => {
      const stop = head.closest('.stop');
      stop.classList.toggle('open');
    });
  });

  /* ---------------------------------------------------------------
     2) DAY NAV — click per scrollare + scrollspy per evidenziare
     --------------------------------------------------------------- */
  const navButtons = Array.from(document.querySelectorAll('.day-nav button'));
  const daySections = navButtons
    .map(btn => document.getElementById(btn.dataset.target))
    .filter(Boolean);

  navButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = document.getElementById(btn.dataset.target);
      if (!target) return;
      const navHeight = document.querySelector('.day-nav').offsetHeight;
      const top = target.getBoundingClientRect().top + window.scrollY - navHeight - 4;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });

  function setActiveByIndex(idx){
    navButtons.forEach((b, i) => b.classList.toggle('active', i === idx));
    // keep the active pill scrolled into view on mobile
    const activeBtn = navButtons[idx];
    if (activeBtn){
      const container = document.getElementById('dayNav');
      const btnLeft = activeBtn.offsetLeft;
      const btnRight = btnLeft + activeBtn.offsetWidth;
      if (btnLeft < container.scrollLeft || btnRight > container.scrollLeft + container.clientWidth){
        container.scrollTo({ left: btnLeft - 24, behavior: 'smooth' });
      }
    }
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting){
        const idx = daySections.findIndex(s => s.id === entry.target.id);
        if (idx !== -1) setActiveByIndex(idx);
      }
    });
  }, {
    root: null,
    rootMargin: '-45% 0px -50% 0px', // trigger when section is roughly centered
    threshold: 0
  });

  daySections.forEach(section => observer.observe(section));
  if (navButtons.length) setActiveByIndex(0);

  /* ---------------------------------------------------------------
     3) PACKING CHECKLIST — toggle + progress bar
     --------------------------------------------------------------- */
  const packingList = document.getElementById('packingList');
  const packingBar = document.getElementById('packingBar');

  function updatePackingProgress(){
    if (!packingList) return;
    const items = packingList.querySelectorAll('li');
    const checked = packingList.querySelectorAll('li.checked');
    const pct = items.length ? Math.round((checked.length / items.length) * 100) : 0;
    if (packingBar) packingBar.style.width = pct + '%';
  }

  if (packingList){
    packingList.querySelectorAll('li').forEach(li => {
      li.addEventListener('click', () => {
        li.classList.toggle('checked');
        updatePackingProgress();
      });
    });
  }

  /* ---------------------------------------------------------------
     4) SCROLL TO TOP
     --------------------------------------------------------------- */
  const topBtn = document.getElementById('topBtn');
  if (topBtn){
    window.addEventListener('scroll', () => {
      topBtn.classList.toggle('show', window.scrollY > 600);
    });
    topBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

});
