import json, os

OUT = "/home/claude/nyc-build/data/days"
os.makedirs(OUT, exist_ok=True)

def stop(time, title, tag, text, addr=None, lat=None, lon=None, img=None, alt=None, link=None):
    d = {"time": time, "title": title, "tag": tag, "text": text}
    if addr: d["address"] = addr
    if lat is not None and lon is not None:
        d["lat"] = lat; d["lon"] = lon
    if img: d["image"] = {"src": img, "alt": alt or title}
    if link: d["mapQuery"] = link
    return d

def link_to(stop_from, stop_to, mode, line, distanceKm, minutes, note=""):
    # connector object placed between two stops
    return {"mode": mode, "line": line, "distanceKm": distanceKm, "minutes": minutes, "note": note}

days = []

# ============================= DAY 0 =============================
d0 = {
  "id": "day0", "num": "00", "color": "#F2B705",
  "title": "Arrivo & Capodanno",
  "date": "Giovedì 31 Dicembre 2026",
  "banner": {"src": "https://commons.wikimedia.org/wiki/Special:FilePath/Times_Square_at_Night_%287823232238%29.jpg?width=1200",
             "alt": "Times Square illuminata di notte"},
  "summary": "Atterri nel giorno più affollato dell'anno a New York. Niente panico: con l'orario di arrivo non hai modo (né bisogno) di infilarti nei recinti di Times Square, che chiudono nel primo pomeriggio. Meglio un Capodanno più semplice e vivibile dopo un volo lungo.",
  "stops": [
    stop("14:40", "Atterraggio a JFK", "LOGISTICA",
         "Metti in conto 45-60 minuti tra controlli e ritiro bagagli. Per il trasferimento in città: AirTrain + subway (~11$, 60-75 min) oppure taxi a tariffa fissa (52$ + pedaggi e mancia verso Manhattan, ~45-60 min senza traffico). La sera di Capodanno il traffico può essere pesante: se puoi, scegli il treno.",
         addr="John F. Kennedy International Airport, Queens", lat=40.6413, lon=-73.7781,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/JFK_Airport_Terminal_4.jpg?width=900",
         alt="Terminal dell'aeroporto JFK di New York", link="JFK+Airport+New+York"),
    stop("16:30", "Check-in in hotel e primo respiro", "RIPOSO",
         "Lascia i bagagli, cambiati e concediti una doccia. Con il jet lag e una città in modalità Capodanno, non forzare il programma: questo primo pomeriggio serve a ricaricare le pile.",
         addr="Hotel a Midtown Manhattan", lat=40.7549, lon=-73.9840),
    stop("19:00", "Cena di Capodanno vicino all'hotel", "CIBO",
         "La sera del 31 molti ristoranti richiedono un menù fisso prenotato con giorni di anticipo. Se non hai prenotato, punta su una pizzeria classica o un diner: sono meno soggetti a menù speciali e restano aperti fino a tardi."),
    stop("23:00", "Mezzanotte: Central Park invece di Times Square", "CONSIGLIO",
         "I recinti ufficiali di Times Square chiudono l'accesso già dal primo pomeriggio e richiedono ore di attesa al freddo senza bagno né possibilità di uscire: sconsigliato se atterri lo stesso giorno. Alternativa più semplice: passeggia verso Columbus Circle o l'angolo sud di Central Park, dove si sente comunque l'energia della città e i fuochi d'artificio sono visibili in lontananza. Oppure, più comodo, un rooftop bar vicino all'hotel. Se preferisci restare tranquilli: guardare il countdown in TV/hotel è un'ottima opzione dopo un volo intercontinentale.",
         addr="Columbus Circle, Manhattan", lat=40.7681, lon=-73.9819,
         link="Columbus+Circle+New+York")
  ],
  "links": [
    link_to(0,1,"treno/taxi", "AirTrain + Subway A / Taxi", 26, 65, "Da JFK all'hotel a Midtown"),
    link_to(1,2,"a piedi", None, 0.4, 6, "Vicino all'hotel"),
    link_to(2,3,"a piedi", None, 1.2, 15, "Verso Columbus Circle / Central Park")
  ]
}
days.append(d0)

# ============================= DAY 1 =============================
d1 = {
  "id": "day1", "num": "01", "color": "#1E5AA8",
  "title": "Lower Manhattan & Statua della Libertà",
  "date": "Venerdì 1 Gennaio 2027 — Capodanno",
  "banner": {"src": "https://commons.wikimedia.org/wiki/Special:FilePath/Statue_of_Liberty%2C_NY.jpg?width=1200",
             "alt": "Statua della Libertà, New York"},
  "summary": "Si parte presto per battere le code al traghetto. Giornata dedicata ai simboli della città vecchia: Statua della Libertà, Ellis Island, Ground Zero, Wall Street e il ponte di Brooklyn al tramonto.",
  "stops": [
    stop("08:30", "Battery Park — imbarco per Liberty Island", "DA PRENOTARE",
         "I traghetti Statue Cruises partono da Battery Park. Prenota online in anticipo (il biglietto Reserve include Statua + Ellis Island); anche a Capodanno il servizio è attivo con orari ridotti.",
         addr="Battery Park, State St, Manhattan", lat=40.7033, lon=-74.0170,
         link="Battery+Park+Statue+Cruises+New+York"),
    stop("09:30", "Statua della Libertà", "ICONA",
         "Passeggia intorno al basamento; se hai prenotato il biglietto per la corona, tieni conto di sicurezza aggiuntiva e limite di oggetti a bordo.",
         addr="Liberty Island", lat=40.6892, lon=-74.0445,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Statue_of_Liberty_7.jpg?width=900",
         alt="Statua della Libertà vista dal basso", link="Statue+of+Liberty+National+Monument"),
    stop("11:15", "Ellis Island — Museo dell'Immigrazione", "STORIA",
         "Il museo racconta la storia dei milioni di migranti entrati negli Stati Uniti da qui tra il 1892 e il 1954. Molto toccante, merita almeno un'ora.",
         addr="Ellis Island", lat=40.6993, lon=-74.0413,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Ellis_Island_2.jpg?width=900",
         alt="Edificio principale di Ellis Island", link="Ellis+Island"),
    stop("13:30", "Pranzo veloce a Financial District", "CIBO",
         "Tornati sulla terraferma, punta su un food hall o un deli intorno a Wall Street.",
         lat=40.7075, lon=-74.0090),
    stop("14:45", "9/11 Memorial & Museum", "MEMORIALE",
         "Le due vasche memoriali sull'impronta delle Torri Gemelle sono ad accesso libero. Il museo sotterraneo è a pagamento e richiede almeno 1h30.",
         addr="180 Greenwich St, Manhattan", lat=40.7115, lon=-74.0134,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/9-11_Memorial_South_Pool.jpg?width=900",
         alt="Vasca memoriale del 9/11 Memorial", link="9/11+Memorial+Museum+New+York"),
    stop("16:15", "Oculus", "ARCHITETTURA",
         "Lo spettacolare hub dei trasporti disegnato da Santiago Calatrava, con la sua struttura a costole bianche che ricorda un uccello in volo: un centro commerciale/stazione da vedere anche solo di passaggio.",
         addr="Westfield World Trade Center, Manhattan", lat=40.7115, lon=-74.0099,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Oculus_interior_2016.jpg?width=900",
         alt="Interno dell'Oculus al World Trade Center", link="Oculus+World+Trade+Center"),
    stop("16:45", "Wall Street — Charging Bull & Federal Hall", "SIMBOLO FINANZIARIO",
         "Il cuore della finanza mondiale: passa dal Charging Bull (il toro di bronzo, meta fotografica classica), ammira la facciata neoclassica della Federal Hall e la sede storica del New York Stock Exchange. La strada è stretta e sempre affollata di turisti in cerca dello scatto col toro.",
         addr="Wall St, Financial District, Manhattan", lat=40.7069, lon=-74.0107,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Charging_Bull_ny.jpg?width=900",
         alt="Charging Bull su Wall Street", link="Wall+Street+Charging+Bull+New+York"),
    stop("17:15", "Ponte di Brooklyn a piedi, al tramonto", "VISTA",
         "La camminata dura circa 25-30 minuti. A inizio gennaio il sole tramonta verso le 16:40, quindi arriverai con la luce blu della sera — porta i guanti, sul ponte tira vento.",
         addr="Brooklyn Bridge, accesso lato Manhattan: Park Row / City Hall", lat=40.7128, lon=-74.0060,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Brooklyn_Bridge_Manhattan.jpg?width=900",
         alt="Ponte di Brooklyn con lo skyline di Manhattan", link="Brooklyn+Bridge+pedestrian+entrance"),
    stop("18:00", "DUMBO, Brooklyn — cena con vista skyline", "CIBO & VISTA",
         "Da Washington St / Water St hai la vista da cartolina sul Manhattan Bridge. Zona piena di ristoranti e la storica Grimaldi's Pizza.",
         addr="Washington St / Water St, DUMBO, Brooklyn", lat=40.7033, lon=-73.9903,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Washington_Street%2C_Dumbo%2C_Brooklyn.jpg?width=900",
         alt="Washington Street a DUMBO con il Manhattan Bridge sullo sfondo", link="DUMBO+Brooklyn+Washington+Street")
  ],
  "links": [
    link_to(0,1,"traghetto", "Statue Cruises", 2.6, 20, "Battery Park → Liberty Island"),
    link_to(1,2,"traghetto", "Statue Cruises", 0.8, 10, "Liberty Island → Ellis Island"),
    link_to(2,3,"traghetto + a piedi", "Statue Cruises → Battery Park", 3.4, 30, "Ritorno a Manhattan e verso Wall St"),
    link_to(3,4,"a piedi", None, 0.9, 12, "Verso il 9/11 Memorial"),
    link_to(4,5,"a piedi", None, 0.3, 4, "Attraversamento verso l'Oculus"),
    link_to(5,6,"a piedi", None, 0.5, 7, "Verso Wall Street"),
    link_to(6,7,"a piedi", None, 0.9, 12, "Da Wall Street all'accesso del ponte"),
    link_to(7,8,"a piedi", None, 1.8, 28, "Attraversamento del Ponte di Brooklyn")
  ]
}
days.append(d1)

# ============================= DAY 2 =============================
d2 = {
  "id": "day2", "num": "02", "color": "#C9962C",
  "title": "Midtown: Empire State & Top of the Rock",
  "date": "Sabato 2 Gennaio 2027",
  "banner": {"src": "https://commons.wikimedia.org/wiki/Special:FilePath/NYC_Empire_State_Building.jpg?width=1200",
             "alt": "Empire State Building al tramonto"},
  "summary": "Giornata verticale: due dei belvedere più famosi del mondo, la Quinta Strada e Rockefeller Center. Consiglio: Empire State al mattino presto (meno coda) e Top of the Rock al tramonto — perché da lì vedi l'Empire State illuminato, cosa che dall'Empire State stesso non puoi fare.",
  "stops": [
    stop("08:30", "Empire State Building", "DA PRENOTARE",
         "Prenota il time-slot online per saltare la fila principale. Sali all'86° piano (terrazza esterna); se vuoi anche il 102° metti in conto un supplemento e altri 15-20 minuti.",
         addr="20 W 34th St, Manhattan", lat=40.7484, lon=-73.9857,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Empire_State_Building_%28aerial_view%29.jpg?width=900",
         alt="Empire State Building visto dall'alto", link="Empire+State+Building"),
    stop("10:30", "Quinta Strada verso nord", "PASSEGGIATA",
         "Vetrine, la New York Public Library con i leoni di pietra, Bryant Park (a inizio gennaio spesso c'è ancora la pista di pattinaggio).",
         addr="5th Ave, Manhattan", lat=40.7532, lon=-73.9822,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/New_York_Public_Library_Lions.jpg?width=900",
         alt="Leone di pietra davanti alla New York Public Library", link="New+York+Public+Library+5th+Avenue"),
    stop("12:30", "Pranzo — Grand Central Market o food hall", "CIBO",
         "Ottimo per assaggiare più cose in un posto solo senza perdere tempo.", lat=40.7527, lon=-73.9772),
    stop("14:00", "MoMA (opzionale)", "FACOLTATIVO",
         "Se ami l'arte moderna, due ore qui volano. Se preferisci più tempo libero per lo shopping, salta questa tappa senza rimpianti — il programma regge comunque.",
         addr="11 W 53rd St, Manhattan", lat=40.7614, lon=-73.9776, link="MoMA+New+York"),
    stop("16:15", "Rockefeller Center & pista di pattinaggio", "ICONA STAGIONALE",
         "L'albero di Natale resta acceso di solito fino ai primi giorni di gennaio: potresti farcela per un pelo. Anche senza albero, la piazza col Prometheus dorato e la pista è molto scenografica.",
         addr="45 Rockefeller Plaza, Manhattan", lat=40.7587, lon=-73.9787, link="Rockefeller+Center"),
    stop("16:45", "Top of the Rock al tramonto", "DA PRENOTARE",
         "Prenota lo slot proprio intorno al tramonto (~16:40 a inizio gennaio) per vedere la città passare dalla luce del giorno alle luci notturne, con l'Empire State come protagonista dello skyline.",
         addr="30 Rockefeller Plaza, Manhattan", lat=40.7588, lon=-73.9797,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Manhattan_from_top_of_the_rock.JPG?width=900",
         alt="Vista su Manhattan dal Top of the Rock", link="Top+of+the+Rock"),
    stop("18:30", "Times Square by night", "DA VEDERE",
         "Ora che il grosso della folla di Capodanno si è diradato, è il momento giusto per vederlo senza il caos del 31.",
         addr="Times Square, Manhattan", lat=40.7580, lon=-73.9855,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Times_Square%2C_New_York_City_%28HDR%29.jpg?width=900",
         alt="Times Square di notte con le insegne luminose", link="Times+Square+New+York"),
    stop("19:30", "Cena a Hell's Kitchen", "CIBO",
         "Zona con altissima densità di ristoranti di ogni tipo e prezzo, a due passi da Times Square.",
         addr="Hell's Kitchen, Manhattan", lat=40.7638, lon=-73.9918)
  ],
  "links": [
    link_to(0,1,"a piedi", None, 1.5, 20, "Da Empire State verso la Quinta Strada"),
    link_to(1,2,"a piedi", None, 0.3, 4, "Verso Grand Central"),
    link_to(2,3,"metro", "B/D/F/M fino a 47-50 Sts", 1.9, 15, "Verso il MoMA"),
    link_to(3,4,"a piedi", None, 0.4, 6, "Verso Rockefeller Center"),
    link_to(4,5,"a piedi", None, 0.1, 2, "Ingresso Top of the Rock"),
    link_to(5,6,"a piedi", None, 0.9, 12, "Verso Times Square"),
    link_to(6,7,"a piedi", None, 0.7, 10, "Verso Hell's Kitchen")
  ]
}
days.append(d2)

# ============================= DAY 3 =============================
d3 = {
  "id": "day3", "num": "03", "color": "#B23A2E",
  "title": "Harlem & Museo di Storia Naturale",
  "date": "Domenica 3 Gennaio 2027",
  "banner": {"src": "https://commons.wikimedia.org/wiki/Special:FilePath/Harlem_-_Apollo_Theater.jpg?width=1200",
             "alt": "Apollo Theater sulla 125th Street a Harlem"},
  "summary": "Mattina a Harlem come richiesto: storia, musica e brunch soul food. Nel primo pomeriggio si scende verso l'Upper West Side per Central Park e l'American Museum of Natural History.",
  "stops": [
    stop("09:00", "Arrivo a Harlem — 125th Street", "QUARTIERE",
         "Prendi la linea A/B/C/D fino a 125 St. La strada è il cuore commerciale e culturale del quartiere.",
         addr="125th St, Harlem, Manhattan", lat=40.8093, lon=-73.9482, link="125th+Street+Harlem+New+York"),
    stop("09:30", "Apollo Theater", "STORIA MUSICALE",
         "Il teatro leggendario dove hanno debuttato Ella Fitzgerald, James Brown e Michael Jackson (all'Amateur Night). Se organizzato in anticipo, i tour guidati raccontano tutta la storia del luogo.",
         addr="253 W 125th St, Harlem", lat=40.8102, lon=-73.9500,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Apollo_Theater_2010.jpg?width=900",
         alt="Facciata dell'Apollo Theater ad Harlem", link="Apollo+Theater+Harlem"),
    stop("10:30", "Studio Museum in Harlem / passeggiata culturale", "ARTE",
         "Dedicato all'arte afroamericana e della diaspora. Se chiuso o in restauro, cammina lungo Malcolm X Blvd ammirando le brownstone d'epoca.",
         addr="Malcolm X Blvd, Harlem", lat=40.8033, lon=-73.9459),
    stop("11:30", "Domenica gospel (facoltativo)", "ESPERIENZA",
         "Essendo domenica, molte chiese storiche di Harlem accolgono visitatori alle funzioni con coro gospel dal vivo. Vestiti in modo sobrio, arriva con anticipo e mantieni un comportamento rispettoso: è un luogo di culto attivo, non uno spettacolo turistico."),
    stop("12:30", "Brunch soul food da Sylvia's", "CIBO ICONICO",
         "Storico ristorante soul food di Harlem: pollo fritto, waffle, mac and cheese. La domenica il brunch con musica dal vivo è molto frequentato: arriva presto o mettiti in lista d'attesa.",
         addr="328 Malcolm X Blvd, Harlem", lat=40.8078, lon=-73.9428, link="Sylvia's+Restaurant+Harlem"),
    stop("14:00", "Central Park — ingresso nord/ovest", "PARCO",
         "Scendendo verso l'Upper West Side, attraversa una fetta di Central Park: in inverno è quasi spoglio ma molto suggestivo, specie intorno al Reservoir.",
         addr="Central Park West, Manhattan", lat=40.7969, lon=-73.9587,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Winter_view_of_the_Bow_Bridge_in_Central_Park.jpg?width=900",
         alt="Central Park innevato in inverno", link="Central+Park+West+110th+Street"),
    stop("15:00", "American Museum of Natural History", "DA PRENOTARE",
         "Uno dei musei di scienze naturali più grandi al mondo: scheletri di dinosauri, la sala degli oceani con la balenottera azzurra, il planetario Hayden. Metti in conto almeno 2 ore, di più se ami i dinosauri.",
         addr="200 Central Park West, Manhattan", lat=40.7813, lon=-73.9740,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/American_Museum_of_Natural_History_02.jpg?width=900",
         alt="Facciata dell'American Museum of Natural History", link="American+Museum+of+Natural+History"),
    stop("18:00", "Cena sull'Upper West Side", "CIBO",
         "Zona residenziale e tranquilla, ottima per una cena rilassata dopo una giornata piena.",
         addr="Upper West Side, Manhattan", lat=40.7870, lon=-73.9754)
  ],
  "links": [
    link_to(0,1,"a piedi", None, 0.2, 3, "Sulla 125th Street"),
    link_to(1,2,"a piedi", None, 0.3, 4, "Lungo Malcolm X Blvd"),
    link_to(2,3,"a piedi", None, 0.3, 4, "Verso la chiesa più vicina"),
    link_to(3,4,"a piedi", None, 0.4, 5, "Verso Sylvia's"),
    link_to(4,5,"metro", "2/3 fino a Central Park North (110 St)", 3.0, 20, "Verso Central Park"),
    link_to(5,6,"a piedi", None, 1.6, 22, "Attraversando il parco verso l'Upper West Side"),
    link_to(6,7,"a piedi", None, 0.7, 10, "Verso il ristorante serale")
  ]
}
days.append(d3)

# ============================= DAY 4 =============================
d4 = {
  "id": "day4", "num": "04", "color": "#6B4E9E",
  "title": "Chelsea, High Line & Greenwich Village",
  "date": "Lunedì 4 Gennaio 2027",
  "banner": {"src": "https://commons.wikimedia.org/wiki/Special:FilePath/Highline_02.jpg?width=1200",
             "alt": "La High Line, parco sopraelevato di Manhattan"},
  "summary": "Giornata più rilassata, tra mercati coperti, quartieri boutique e vita da newyorkesi: la New York meno da cartolina e più autentica.",
  "stops": [
    stop("10:00", "High Line", "PARCO SOPRAELEVATO",
         "Ex ferrovia sopraelevata trasformata in parco lineare, con scorci sull'Hudson e sui grattacieli. In inverno è meno affollata: goditela con calma.",
         addr="Ingresso consigliato: Gansevoort St, Manhattan", lat=40.7397, lon=-74.0081,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Highline_02.jpg?width=900",
         alt="Passerella della High Line tra gli edifici", link="High+Line+Gansevoort+Street"),
    stop("11:15", "Chelsea Market", "CIBO",
         "Mercato coperto con decine di banchi gastronomici: ottimo per il pranzo, prova le ostriche del Lobster Place o il ramen.",
         addr="75 9th Ave, Manhattan", lat=40.7424, lon=-74.0061,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Chelsea_Market_entrance.jpg?width=900",
         alt="Ingresso di Chelsea Market", link="Chelsea+Market"),
    stop("13:00", "Meatpacking District & Whitney Museum (esterno)", "QUARTIERE",
         "Un tempo distretto industriale, oggi zona di boutique e design. Il Whitney Museum of American Art si affaccia proprio sull'ingresso sud della High Line.",
         addr="Meatpacking District, Manhattan", lat=40.7395, lon=-74.0089, link="Whitney+Museum+of+American+Art"),
    stop("14:30", "Greenwich Village & Washington Square Park", "PASSEGGIATA",
         "Stradine alberate, case in mattoni rossi, il celebre arco di Washington Square. Atmosfera molto diversa da Midtown: qui New York si fa bohémien.",
         addr="Washington Square Park, Manhattan", lat=40.7308, lon=-73.9973,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Washington_Square_Arch_NYC.jpg?width=900",
         alt="Arco di Washington Square Park", link="Washington+Square+Park"),
    stop("16:00", "SoHo — shopping e street art", "SHOPPING",
         "Palazzi in ghisa ottocenteschi, negozi di design e boutique. Ottimo posto per gli ultimi regali senza il caos della Quinta Strada.",
         addr="SoHo, Manhattan", lat=40.7233, lon=-74.0030,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Soho_Cast_Iron_Historic_District_(51).JPG?width=900",
         alt="Palazzi in ghisa di SoHo", link="SoHo+Cast+Iron+Historic+District"),
    stop("19:00", "Cena a Little Italy o Nolita", "CIBO",
         "Piccola ma scenografica, a due passi da SoHo. Buona chiusura per l'ultima serata piena in città.",
         addr="Little Italy, Manhattan", lat=40.7191, lon=-73.9973)
  ],
  "links": [
    link_to(0,1,"a piedi", None, 0.6, 9, "Uscita dalla High Line verso Chelsea Market"),
    link_to(1,2,"a piedi", None, 0.5, 7, "Verso il Meatpacking District"),
    link_to(2,3,"a piedi", None, 1.3, 18, "Verso Washington Square Park"),
    link_to(3,4,"a piedi", None, 0.9, 12, "Verso SoHo"),
    link_to(4,5,"a piedi", None, 0.6, 9, "Verso Little Italy")
  ]
}
days.append(d4)

# ============================= DAY 5 =============================
d5 = {
  "id": "day5", "num": "05", "color": "#1F7A6C",
  "title": "Ultima mattina & rientro",
  "date": "Martedì 5 Gennaio 2027 — volo 20:00",
  "banner": {"src": "https://commons.wikimedia.org/wiki/Special:FilePath/Grand_Central_Station_Main_Concourse_Jan_2006.jpg?width=1200",
             "alt": "Sala principale di Grand Central Terminal"},
  "summary": "Giorno di partenza: tempo contato. Con il volo alle 20:00 e l'obiettivo di essere in aeroporto entro le 17:00, hai una mattinata e un primo pomeriggio liberi — da tenere leggeri, vicino all'hotel e ai mezzi per JFK.",
  "stops": [
    stop("09:00", "Colazione con calma & check-out", "LOGISTICA",
         "Chiedi in hotel di lasciare i bagagli in deposito dopo il check-out, così l'ultima mattinata resta libera senza valigie al seguito."),
    stop("10:00", "Grand Central Terminal", "ARCHITETTURA",
         "La grande sala con il soffitto a volta blu dipinto di costellazioni è gratuita e a due passi da Midtown. Da fuori, bella vista sul Chrysler Building.",
         addr="89 E 42nd St, Manhattan", lat=40.7527, lon=-73.9772,
         img="https://commons.wikimedia.org/wiki/Special:FilePath/Grand_Central_Station_Main_Concourse_Jan_2006.jpg?width=900",
         alt="Sala principale di Grand Central Terminal", link="Grand+Central+Terminal"),
    stop("11:00", "Ultimo giro libero / shopping dell'ultimo minuto", "TEMPO LIBERO",
         "Bagel da asporto, un ultimo pretzel per strada, o semplicemente una passeggiata senza meta in una zona che ti è piaciuta particolarmente."),
    stop("13:00", "Pranzo leggero", "CIBO",
         "Meglio qualcosa di rapido: un deli o un food hall vicino a dove recuperi i bagagli."),
    stop("14:00", "Recupero bagagli e partenza verso JFK", "ATTENZIONE ORARI",
         "Per essere in aeroporto entro le 17:00, parti da Manhattan indicativamente tra le 14:00 e le 14:30: in taxi/Uber conta 45-70 minuti (di più con traffico), in AirTrain + subway 70-90 minuti. Meglio abbondare, soprattutto se parti da zone centrali con traffico imprevedibile."),
    stop("17:00", "In aeroporto — check-in e sicurezza", "OBIETTIVO",
         "Con 3 ore di anticipo sul volo delle 20:00 hai margine comodo per check-in, controlli di sicurezza e un ultimo caffè al gate.",
         addr="John F. Kennedy International Airport, Queens", lat=40.6413, lon=-73.7781),
    stop("20:00", "Decollo — si torna a casa", "FINE VIAGGIO",
         "Sei giorni, cinque quartieri, un Capodanno diverso dal solito. Buon rientro.")
  ],
  "links": [
    link_to(0,1,"a piedi", None, 0.4, 6, "Verso Grand Central"),
    link_to(1,2,"a piedi", None, 0.5, 7, "Ultimo giro"),
    link_to(2,3,"a piedi", None, 0.3, 4, "Verso il pranzo"),
    link_to(3,4,"a piedi", None, 0.2, 3, "Recupero bagagli"),
    link_to(4,5,"AirTrain + Subway A / Taxi", "AirTrain + Subway A", 26, 75, "Verso JFK"),
  ]
}
days.append(d5)

for d in days:
    json.dump(d, open(f"{OUT}/{d['id']}.json", "w"), ensure_ascii=False, indent=2)

# index of days (order + colors, for nav)
index = [{"id": d["id"], "num": d["num"], "color": d["color"], "title": d["title"],
          "shortLabel": d["date"].split("—")[0].split(",")[0].strip()} for d in days]
json.dump(index, open("/home/claude/nyc-build/data/days-index.json", "w"), ensure_ascii=False, indent=2)

print("giorni generati:", [d["id"] for d in days])
