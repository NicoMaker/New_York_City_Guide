import json, os

OUT = "/home/claude/nyc-build/data"
os.makedirs(OUT + "/days", exist_ok=True)

# ---------------------------------------------------------------
# trip.json — hero, voli, numeri "at a glance"
# ---------------------------------------------------------------
trip = {
  "badge": "ARRIVO LA NOTTE DI CAPODANNO",
  "titleLines": ["NEW YORK", "CITY"],
  "sub": "31 Dicembre 2026 → 5 Gennaio 2027",
  "lead": "6 giorni tra Manhattan, Harlem e Brooklyn: dal Capodanno appena atterrati fino all'ultimo caffè prima del volo di rientro.",
  "flights": [
    {"label": "✈ ANDATA — ARRIVO A NEW YORK", "route": "Volo internazionale → JFK",
     "time": "14:40", "date": "Giovedì 31 Dicembre 2026"},
    {"label": "✈ RITORNO — PARTENZA DA NEW YORK", "route": "JFK → volo internazionale",
     "time": "20:00", "date": "Martedì 5 Gennaio 2027 · check-in entro le 17:00"}
  ],
  "glance": [
    {"num": "6", "label": "giorni a New York"},
    {"num": "5", "label": "quartieri esplorati"},
    {"num": "~2°C", "label": "media inizio gennaio"},
    {"num": "01", "label": "notte di Capodanno inclusa"}
  ]
}
json.dump(trip, open(f"{OUT}/trip.json", "w"), ensure_ascii=False, indent=2)

# ---------------------------------------------------------------
# transit.json — linee metro usate nel viaggio + guida OMNY
# ---------------------------------------------------------------
transit = {
  "intro": "New York si gira quasi tutta in subway: rete attiva 24/7, pagamento contactless con OMNY (carta o smartphone) direttamente ai tornelli, tariffa fissa a corsa indipendentemente dalla distanza percorsa.",
  "fare": "2,90$ a corsa con OMNY o MetroCard. Dopo 12 corse pagate in una settimana (lun-dom) le successive sono gratuite fino a domenica.",
  "lines": [
    {"codes": ["A", "C", "E"], "color": "#2850AD", "name": "8th Avenue Line",
     "note": "Collega JFK (via AirTrain + Howard Beach) a Lower Manhattan, West Village, Chelsea e Harlem (125 St)."},
    {"codes": ["1", "2", "3"], "color": "#EE352E", "name": "Broadway–7th Avenue Line",
     "note": "South Ferry/Battery Park, Times Square, Chelsea, Harlem — la dorsale del lato ovest."},
    {"codes": ["4", "5", "6"], "color": "#00933C", "name": "Lexington Avenue Line",
     "note": "Grand Central, Union Square, Wall St, 125 St lato est — molto trafficata nelle ore di punta."},
    {"codes": ["N", "Q", "R", "W"], "color": "#FCCC0A", "name": "Broadway Line",
     "note": "Times Square, Herald Square, Union Square: utile per Midtown e SoHo."},
    {"codes": ["B", "D", "F", "M"], "color": "#FF6319", "name": "6th Avenue Line",
     "note": "Rockefeller Center (47-50 Sts), Herald Square, 125 St lato ovest."},
    {"codes": ["L"], "color": "#A7A9AC", "name": "14th Street Line",
     "note": "Attraversa Manhattan su 14th St, utile per Union Square–Meatpacking."}
  ],
  "airport": {
    "title": "Dall'aeroporto in città",
    "options": [
      {"mode": "AirTrain + Subway", "cost": "~11$ totali (8$ AirTrain + 2,90$ subway)",
       "time": "60-75 min", "note": "Prendi AirTrain fino a Howard Beach o Jamaica Station, poi linea A o LIRR verso Manhattan."},
      {"mode": "Taxi giallo", "cost": "52$ tariffa fissa verso Manhattan + pedaggi e mancia",
       "time": "45-60 min senza traffico", "note": "La sera di Capodanno il traffico può essere pesante."},
      {"mode": "Uber / Lyft", "cost": "Variabile con la domanda, simile al taxi",
       "time": "45-70 min", "note": "Comodo con bagagli ma prezzo meno prevedibile."}
    ]
  }
}
json.dump(transit, open(f"{OUT}/transit.json", "w"), ensure_ascii=False, indent=2)

# ---------------------------------------------------------------
# practical.json — info pratiche + checklist bagaglio
# ---------------------------------------------------------------
practical = {
  "title": "Info pratiche",
  "lead": "Tutto quello che serve sapere prima di partire, in una pagina sola.",
  "cards": [
    {"title": "Meteo — inizio gennaio",
     "text": "Temperature medie tra -2°C e 5°C, spesso ventoso soprattutto vicino all'acqua (Battery Park, ponti, High Line). Possibili nevicate leggere. Vestiti a strati: piumino, sciarpa, guanti e scarpe impermeabili con suola buona sono più utili di un solo cappotto pesante."},
    {"title": "Muoversi in metro",
     "text": "Usa OMNY (pagamento contactless con carta o smartphone direttamente ai tornelli): non serve comprare una MetroCard. Tariffa singola fissa indipendentemente dalla distanza; dopo 12 corse in una settimana il resto è gratuito."},
    {"title": "Dall'aeroporto in città",
     "text": "AirTrain JFK (8$) + subway (2,90$): economico ma più lento. Taxi giallo: tariffa fissa 52$ verso Manhattan + pedaggi e mancia (15-20%). Uber/Lyft simile al taxi, prezzo variabile con la domanda."},
    {"title": "Mance (tipping)",
     "text": "Al ristorante 18-20% sul conto prima delle tasse è lo standard. Per i taxi 15-20%. Per il servizio in camera d'hotel 2-5$ al giorno. Non è opzionale come in Europa: è parte integrante dello stipendio di chi lavora nel settore."},
    {"title": "Prenotazioni da fare in anticipo",
     "text": "Empire State Building, Top of the Rock, Statua della Libertà/Ellis Island e American Museum of Natural History vendono biglietti a orario: prenotali online almeno una settimana prima, soprattutto per il periodo di Capodanno."},
    {"title": "Cosa assaggiare",
     "text": "Bagel con cream cheese a colazione, una fetta di pizza newyorkese piegata a metà, un pastrami sandwich, un pretzel caldo da un carretto, cioccolata calda dopo una giornata fredda in giro."}
  ],
  "packing": {
    "title": "Checklist bagaglio inverno NYC",
    "sub": "Tocca una voce per segnarla come fatta — il progresso si aggiorna in tempo reale.",
    "items": [
      "Piumino / cappotto invernale", "Guanti e sciarpa", "Berretto",
      "Scarpe impermeabili", "Maglioni / strati termici", "Documenti + ESTA/visto",
      "Adattatore per prese USA", "Carta contactless per OMNY",
      "Prenotazioni stampate/salvate", "Power bank",
      "Crema idratante (aria secca da riscaldamento)", "Zaino pieghevole per le giornate in giro"
    ]
  }
}
json.dump(practical, open(f"{OUT}/practical.json", "w"), ensure_ascii=False, indent=2)

print("trip/transit/practical OK")
