# New York City Guide — versione a componenti

Guida di viaggio (31 Dic 2026 – 5 Gen 2027) riorganizzata a componenti:
HTML minimo + CSS modulare + JS a moduli + dati in JSON.

## Struttura

```
index.html              guscio della pagina, contiene solo i contenitori vuoti
css/
  base/variables.css     design tokens (colori, font, spaziature)
  hero/hero.css          header, voli, striscia "at a glance"
  nav/nav.css            barra sticky di navigazione tra le giornate
  day/day.css            intestazione giornata, banner, riepilogo
  gallery/gallery.css    galleria foto scrollabile sopra la timeline
  timeline/timeline.css  tappe (accordion) di ogni giornata
  transit/transit.css    chip linee metro + sezione "come muoversi"
  practical/practical.css info pratiche + checklist bagaglio
  footer/footer.css      footer e pulsante "torna su"
js/
  main.js                 punto di ingresso: carica i dati e chiama i render
  core/data.js             carica tutti i JSON (fetch)
  core/utils.js            helper: link mappe, embed OpenStreetMap, chip metro
  hero/hero.js             costruisce header e "at a glance"
  nav/nav.js               costruisce la barra di navigazione + scrollspy
  gallery/gallery.js       costruisce la galleria foto di ogni giornata
  stop/stop.js             costruisce una singola tappa + il connettore
                           "come arrivare alla tappa successiva"
  day/day.js               assembla l'intera sezione di una giornata
  transit/transit.js       sezione dedicata "Come muoversi in metro"
  practical/practical.js   info pratiche + checklist bagaglio
  interactions/interactions.js  apertura tappe, checklist, pulsante "torna su"
data/
  trip.json               hero, voli, numeri "at a glance"
  transit.json             linee metro usate nel viaggio + guida OMNY/aeroporto
  practical.json           info pratiche + checklist bagaglio
  days-index.json          elenco ordinato delle giornate (id, colore, titolo)
  days/day0.json … day5.json   tappe di ogni giornata, con per ciascuna tappa:
                           orario, titolo, testo, indirizzo, coordinate
                           (lat/lon) per la mappa OpenStreetMap incorporata,
                           immagine, link a Google Maps; e un array "links"
                           con il collegamento alla tappa successiva
                           (mezzo, linea metro, distanza in km, minuti,
                           nota).
```

## Come aprirla

I moduli JS usano `fetch()` per leggere i file JSON: i browser bloccano
questo tipo di richiesta se apri `index.html` direttamente da disco
(protocollo `file://`). Serve un piccolo server locale:

```bash
cd cartella-del-progetto
python3 -m http.server 8000
```

poi apri `http://localhost:8000` nel browser.

Se invece pubblichi il sito (es. GitHub Pages, come l'originale
`nicomaker.github.io/New_York_City_Guide/`), funziona senza alcuna
configurazione aggiuntiva: basta caricare tutta la cartella così com'è.

## Cosa è stato aggiunto rispetto all'originale

- **Metro**: sezione dedicata "Come muoversi in metro" con le linee
  reali (A/C/E, 1/2/3, 4/5/6, N/Q/R/W, B/D/F/M, L) rappresentate con
  chip colorati come sulla segnaletica MTA, tariffe OMNY e opzioni per
  arrivare dall'aeroporto.
- **Connettori tra tappe**: tra una tappa e la successiva, un piccolo
  blocco mostra il mezzo consigliato, la linea metro (se rilevante),
  la distanza approssimativa e il tempo di percorrenza.
- **Galleria scrollabile**: sopra i dati/timeline di ogni giornata,
  una striscia di foto orizzontalmente scorrevole con le tappe che
  hanno un'immagine; toccando una foto si apre la tappa corrispondente.
- **OpenStreetMap incorporato**: ogni tappa con coordinate note mostra
  una mini-mappa OSM incorporata oltre al link a Google Maps.
- **Wall Street e Ponte di Brooklyn** come tappe autonome e complete
  (indirizzo, immagine, mappa), non più solo accennate nel testo.
- **Componentizzazione completa**: CSS diviso per area funzionale, JS
  diviso in moduli con responsabilità singola, dati separati dal
  markup in file JSON, per essere facilmente modificabili senza
  toccare il codice.

Orari, prezzi e tempi di percorrenza sono indicativi: verifica sempre
sui siti ufficiali prima di partire.
