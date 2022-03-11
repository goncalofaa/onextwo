leagues_fte = {"UEFA Champions League",
               "EredivisieNetherlands",
               "Super LeagueSwitzerland",
               "Serie AItaly",
               "La LigaSpain",
               "Premier LeagueEngland",
               "First Division ABelgium",
               "BundesligaGermany",
               "Ligue 1France",
               "Primeira LigaPortugal",
               "First Division ABelgium",
               "SuperligaDenmark",
               "PremiershipScotland",
               "Süper LigTurkey",
               "Liga MXMexico",
               "MLSUSA",
               "BrasileirãoBrazil",
               "ChampionshipEngland",
               "UEFA Europa League",
               "AllsvenskanSweden",
               "J1 LeagueJapan",
               "Ligue 2France",
               "2. BundesligaGermany",
               "La Liga 2Spain",
               "Serie BItaly",
               "Super LeagueGreece",
               "Premier LeagueRussia",
               "BundesligaAustria",
               }

months = {"Jan": "/01",
          "Feb": "/02",
          "Mar": "/03",
          "Apr": "/04",
          "May": "/05",
          "Oct": "/10",
          "Nov": "/11",
          "Dec": "/12"}

comps = {"UEFA Champions League": "UCL",
         "Eredivisie": "Nl1",
         "Super League": "Ch1",
         "First Division A": "Be1",
         "Serie A": "It1",
         "Ligue 1": "Fr1",
         "La Liga": "Es1",
         "Primeira Liga": "Pt1",
         "Superliga": "Dk1",
         "Premiership": "Sc1",
         "Süper Lig": "Tr1",
         "Liga MX": "Mx1",
         "MLS": "Us1",
         "Brasileirão": "Br1",
         "Championship":"CH",
         "UEFA Europa League":"UEL",
         "Allsvenskan":"Se1",
         "J1 League":"Jp1",
         "Ligue 2":"Fr2",
         "2. Bundesliga":"De2",
         "La Liga 2":"Es2",
         "Serie B":"It2",}

leagues = {"Es1",
           "De1",
           "Fr1",
           "Pt1",
           "It1",
           "UCL",
           "Be1",
           "Ch1",
           "Nl1",
           "EPL",
           "Dk1",
           "Sc1",
           "Tr1",
           "Mx1",
           "Us1",
           "Br1",
           "CH",
           "Se1",
           "Fr2",
           "De2",
           "Es2",
           "It2",
           "Gr1",
           "Ru1",
           "At1"}

links = {"https://www.forebet.com/en/predictions-europe/uefa-champions-league",
         "https://www.forebet.com/en/football-tips-and-predictions-for-england/premier-league",
         "https://www.forebet.com/en/football-tips-and-predictions-for-spain/primera-division",
         "https://www.forebet.com/en/football-tips-and-predictions-for-germany/Bundesliga",
         "https://www.forebet.com/en/football-tips-and-predictions-for-france/ligue1",
         "https://www.forebet.com/en/football-tips-and-predictions-for-italy/serie-a",
         "https://www.forebet.com/en/football-tips-and-predictions-for-portugal-superliga/primeira-liga",
         "https://www.forebet.com/en/football-tips-and-predictions-for-belgium/jupiler-pro-league",
         "https://www.forebet.com/en/football-tips-and-predictions-for-switzerland-super-league",
         "https://www.forebet.com/en/football-tips-and-predictions-for-netherlands/eredivisie",
         "https://www.forebet.com/en/football-tips-and-predictions-for-usa-major-league-soccer",
         "https://www.forebet.com/en/football-tips-and-predictions-for-scotland",
         "https://www.forebet.com/en/football-tips-and-predictions-for-brazil",
         "https://www.forebet.com/en/football-tips-and-predictions-for-denmark-superliga",
         "https://www.forebet.com/en/football-tips-and-predictions-for-mexico",
         "https://www.forebet.com/en/football-tips-and-predictions-for-turkey",
         "https://www.forebet.com/en/football-tips-and-predictions-for-england/championship",
         "https://www.forebet.com/en/predictions-europe/uefa-europa-league",
         "https://www.forebet.com/en/football-tips-and-predictions-for-sweden/allsvenskan"
         "https://www.forebet.com/en/football-tips-and-predictions-for-japan-j-league/j-league",
         "https://www.forebet.com/en/football-tips-and-predictions-for-france/ligue2",
         "https://www.forebet.com/en/football-tips-and-predictions-for-germany/2-Bundesliga",
         "https://www.forebet.com/en/football-tips-and-predictions-for-spain/segunda-division",
         "https://www.forebet.com/en/football-tips-and-predictions-for-italy/serie-b",
         "https://www.forebet.com/en/football-tips-and-predictions-for-greece/super-league",
         "https://www.forebet.com/en/football-tips-and-predictions-for-russia-premier-league",
         "https://www.forebet.com/en/football-tips-and-predictions-for-austria/bundesliga"}

leagues_to_links={"UCL":"https://www.forebet.com/en/predictions-europe/uefa-champions-league",
                  "EPL":"https://www.forebet.com/en/football-tips-and-predictions-for-england/premier-league",
                  "Es1":"https://www.forebet.com/en/football-tips-and-predictions-for-spain/primera-division",
                  "De1":"https://www.forebet.com/en/football-tips-and-predictions-for-germany/Bundesliga",
                  "Fr1": "https://www.forebet.com/en/football-tips-and-predictions-for-france/ligue1",
                  "It1":"https://www.forebet.com/en/football-tips-and-predictions-for-italy/serie-a",
                  "Pt1":"https://www.forebet.com/en/football-tips-and-predictions-for-portugal-superliga/primeira-liga",
                  "Be1":"https://www.forebet.com/en/football-tips-and-predictions-for-belgium/jupiler-pro-league",
                  "Ch1":"https://www.forebet.com/en/football-tips-and-predictions-for-switzerland-super-league",
                  "Nl1":"https://www.forebet.com/en/football-tips-and-predictions-for-netherlands/eredivisie",
                  "Us1":"https://www.forebet.com/en/football-tips-and-predictions-for-usa-major-league-soccer",
                  "Sc1":"https://www.forebet.com/en/football-tips-and-predictions-for-scotland",
                  "Br1":"https://www.forebet.com/en/football-tips-and-predictions-for-brazil",
                  "Dk1":"https://www.forebet.com/en/football-tips-and-predictions-for-denmark-superliga",
                  "Mx1":"https://www.forebet.com/en/football-tips-and-predictions-for-mexico",
                  "Tr1":"https://www.forebet.com/en/football-tips-and-predictions-for-turkey",
                  "CH":"https://www.forebet.com/en/football-tips-and-predictions-for-england/championship",
                  "UEL":"https://www.forebet.com/en/predictions-europe/uefa-europa-league",
                  "Se":"https://www.forebet.com/en/football-tips-and-predictions-for-sweden/allsvenskan",
                  "Jp1":"https://www.forebet.com/en/football-tips-and-predictions-for-japan-j-league/j-league",
                  "Fr2":"https://www.forebet.com/en/football-tips-and-predictions-for-france/ligue2",
                  "De2":"https://www.forebet.com/en/football-tips-and-predictions-for-germany/2-Bundesliga",
                  "Es2":"https://www.forebet.com/en/football-tips-and-predictions-for-spain/segunda-division",
                  "It2":"https://www.forebet.com/en/football-tips-and-predictions-for-italy/serie-b",
                  "Gr1":"https://www.forebet.com/en/football-tips-and-predictions-for-greece/super-league",
                  "Ru1":"https://www.forebet.com/en/football-tips-and-predictions-for-russia-premier-league",
                  "At1":"https://www.forebet.com/en/football-tips-and-predictions-for-austria/bundesliga"}


teams = {"Zenit": "Zenit",
         "Beşiktaş": "Besiktas JK",
         "Shakhtar": "Shakhtar Donetsk",
         "Sheriff": "Sheriff Tiraspol",
         "Celtic": "Celtic FC",
         "Ferencváros": "Ferencvaros TC",
         "1. FC Köln": "1.FC Köln",
         "AC Milan": "AC Milan",
         "Angers": "Angers SCO",
         "Arminia": "Arminia Bielefeld",
         "Arsenal": "Arsenal",
         "Monaco": "AS Monaco",
         "Roma": "AS Roma",
         "St Étienne": "AS Saint-Étienne",
         "Aston Villa": "Aston Villa",
         "Atalanta": "Atalanta Bergamo",
         "Athletic Bilbao": "Athletic Bilbao",
         "Atlético Madrid": "Atlético Madrid",
         "Leverkusen": "Bayer Leverkusen",
         "Bayern Munich": "Bayern München",
         "Belenenses": "Os Belenenses SAD",
         "Boavista": "Boavista FC",
         "Bologna": "Bologna FC",
         "Dortmund": "Borussia Dortmund",
         "Brentford": "Brentford",
         "Brighton": "Brighton",
         "Burnley": "Burnley",
         "Osasuna": "CA Osasuna",
         "Cádiz": "Cadiz CF",
         "Cagliari": "Cagliari Calcio",
         "Santa Clara": "CD Santa Clara",
         "Tondela": "CD Tondela",
         "Celta Vigo": "Celta de Vigo",
         "Chelsea": "Chelsea",
         "Clermont": "Clermont Foot",
         "Crystal Palace": "Crystal Palace",
         "Alavés": "Deportivo Alavés",
         "Eintracht": "Eintracht Frankfurt",
         "Elche": "Elche CF",
         "Empoli": "Empoli FC",
         "Everton": "Everton",
         "Arouca": "FC Arouca",
         "FC Augsburg": "FC Augsburg",
         "Barcelona": "FC Barcelona",
         "Famalicão": "FC Famalicão",
         "Lorient": "FC Lorient",
         "Metz": "FC Metz",
         "Nantes": "FC Nantes",
         "Porto": "FC Porto",
         "Vizela": "FC Vizela",
         "Fiorentina": "Fiorentina",
         "Estoril": "GD Estoril",
         "Genoa": "Genoa",
         "Getafe": "Getafe CF",
         "Gil Vicente": "Gil Vicente",
         "Bordeaux": "Girondins Bordeaux",
         "Granada": "Granada CF",
         "Greuther Fürth": "Greuther Fürth",
         "Verona": "Hellas Verona",
         "Hertha BSC": "Hertha BSC",
         "Hoffenheim": "Hoffenheim",
         "Inter Milan": "Inter Milano",
         "Juventus": "Juventus FC",
         "Lazio": "Lazio",
         "Leeds United": "Leeds United",
         "Leicester": "Leicester City",
         "Levante": "Levante UD",
         "Lille": "Lille OSC",
         "Liverpool": "Liverpool",
         "Lyon": "Lyon",
         "Mainz": "Mainz",
         "Man. City": "Manchester City",
         "Man. United": "Manchester United",
         "Marítimo": "Marítimo",
         "Gladbach": "Mönchengladbach",
         "Montpellier": "Montpellier HSC",
         "Moreirense": "Moreirense FC",
         "Newcastle": "Newcastle United",
         "Norwich": "Norwich City",
         "Nice": "OGC Nice",
         "Marseille": "Olympique Marseille",
         "Paços Ferreira": "Paços de Ferreira",
         "PSG": "Paris St. Germain",
         "Portimonense": "Portimonense SC",
         "Rayo Vallecano": "Rayo Vallecano",
         "RB Leipzig": "RB Leipzig",
         "Lens": "RC Lens",
         "Espanyol": "RCD Espanyol",
         "Real Betis": "Real Betis",
         "Real Madrid": "Real Madrid",
         "Mallorca": "Real Mallorca",
         "Real Sociedad": "Real Sociedad",
         "Salernitana": "Salernitana",
         "Sampdoria": "Sampdoria",
         "Sassuolo": "Sassuolo Calcio",
         "SC Freiburg": "SC Freiburg",
         "Sevilla": "Sevilla FC",
         "Benfica": "SL Benfica",
         "Southampton": "Southampton",
         "Spezia": "Spezia Calcio",
         "Braga": "Sporting Braga",
         "Sporting": "Sporting CP",
         "Napoli": "SSC Napoli",
         "Brest": "Stade Brestois",
         "Reims": "Stade Reims",
         "Rennes": "Stade Rennais",
         "Strasbourg": "Strasbourg",
         "Torino": "Torino FC",
         "Tottenham": "Tottenham",
         "Troyes": "Troyes AC",
         "Udinese": "Udinese Calcio",
         "Union Berlin": "Union Berlin",
         "Valencia": "Valencia CF",
         "Venezia": "Venezia FC",
         "VfB Stuttgart": "VfB Stuttgart",
         "VfL Bochum": "VfL Bochum",
         "Wolfsburg": "VfL Wolfsburg",
         "Villarreal": "Villarreal CF",
         "Guimarães": "Vitória Guimarães",
         "Watford": "Watford",
         "West Ham": "West Ham",
         "Wolves": "Wolverhampton",
         "Union SG": "Union Saint-Gilloise",
         "Club Brugge": "Club Brugge",
         "Antwerp": "Royal Antwerp",
         "Anderlecht": "Anderlecht",
         "Charleroi": "Sporting Charleroi",
         "Gent": "KAA Gent",
         "Cercle Brugge": "Cercle Brugge",
         "Kortrijk": "KV Kortrijk",
         "Mechelen": "KV Mechelen",
         "Genk": "Racing Genk",
         "Standard Liège": "Standard Liège",
         "Sint-Truidense": "Sint-Truiden",
         "OH Leuven": "OH Leuven",
         "Eupen": "Eupen",
         "Oostende": "KV Oostende",
         "Zulte Waregem": "Zulte Waregem",
         "Seraing": "FC Seraing",
         "Beerschot": "Beerschot Wilrijk",
         "Young Boys": "BSC Young Boys",
         "Zürich": "FC Zürich",
         "Basel": "FC Basel",
         "Lugano": "FC Lugano",
         "Servette": "Servette FC",
         "Grasshoppers": "Grasshoppers",
         "Sion": "FC Sion",
         "St. Gallen": "St. Gallen",
         "Luzern": "FC Luzern",
         "Lausanne-Sport": "Lausanne-Sport",
         "Ajax": "AFC Ajax",
         "PSV": "PSV Eindhoven",
         "Feyenoord": "Feyenoord",
         "Twente": "FC Twente",
         "AZ Alkmaar": "AZ Alkmaar",
         "Vitesse": "Vitesse Arnhem",
         "Utrecht": "FC Utrecht",
         "Cambuur": "SC Cambuur",
         "NEC": "NEC Nijmegen",
         "Heerenveen": "SC Heerenveen",
         "Groningen": "FC Groningen",
         "RKC": "RKC Waalwijk",
         "Go Ahead": "Go Ahead Eagles",
         "Heracles": "Heracles Almelo",
         "Willem II": "Willem II Tilburg",
         "Sparta": "Sparta Rotterdam",
         "Fortuna Sittard": "Fortuna Sittard",
         "PEC Zwolle": "PEC Zwolle",
         "RB Salzburg": "RB Salzburg",
         "Rangers": "Rangers FC",
         "Olympiacos": "Olympiacos FC",
         "Dinamo Zagreb": "Dinamo Zagreb",
         "Livingston": "Livingston FC",
         "St Johnstone": "St Johnstone",
         "Motherwell": "Motherwell FC",
         "Aberdeen": "Aberdeen FC",
         "Hibernian": "Hibernian FC",
         "Dundee Utd": "Dundee FC",
         "Ross County": "Ross County",
         "Hearts": "Hearts FC",
         "SønderjyskE": "SønderjyskE",
         "Odense": "Odense BK",
         "AaB": "AaB Aalborg",
         "Vejle": "Vejle BK",
         "Silkeborg": "Silkeborg FC",
         "Brøndby": "Brøndby I",
         "AGF Aarhus": "AGF Aarhus",
         "Nordsjælland": "FC Nordsjælland",
         "Dundee": "Dundee FC",
         "St Mirren": "St. Mirren",
         "Austin FC": "Austin FC",
         "Inter Miami": "Inter Miami CF",
         "LAFC": "Los Angels FC",
         "Portland": "Portland Timbers",
         "NYCFC": "New York City FC",
         "Montréal": "Montreal Impact",
         "Columbus": "Columbus Crew",
         "Toronto FC": "Toronto FC",
         "Seattle": "Seattle Sounders",
         "LA Galaxy": "Los Angeles Galaxy",
         "Houston": "Houston Dynamo",
         "Vancouver": "Vancouver Whitecaps",
         "New England": "New England Revolution",
         "Real Salt Lake": "Real Salt Lake",
         "D.C. United": "DC United",
         "Chicago": "Chicago Fire",
         "Orlando City": "Orlando City SG",
         "FC Cincinnati": "FC Cincinnati",
         "Philadelphia": "Philadelphia Union",
         "San Jose": "San Jose Earthquakes",
         "FC Dallas": "FC Dallas",
         "Nashville": "Nashville SG",
         "Colorado": "Colorado Rapids",
         "Sporting KC": "Sporting Kansas City",
         "Atlanta": "Atlanta United",
         "Charlotte FC": "Charlotte FC",
         "NY Red Bulls": "New York Red Bulls",
         "Karagümrükspor": "	Fatih Karagümrük",
         "Altay": "Altay SK Izmir",
         "Fenerbahçe": "	Fenerbahçe SK",
         "Trabzonspor": "Trabzonspor",
         "Antalyaspor": "Antalyaspor",
         "Sivasspor": "Sivasspor",
         "Alanyaspor": "Alanyaspor",
         "Hatayspor": "Hatayspor",
         "Başakşehir": "Istanbul Basaksehir",
         "Y. Malatyaspor": "Yeni Malatyaspor",
         "Kasımpaşa": "Kasımpaşa SK",
         "Rizespor": "Rizespor",
         "Göztepe": "Göztepe Izmir",
         "Kayserispor": "Kayserispor",
         "Konyaspor": "Konyaspor",
         "Randers": "Randers FC",
         "Viborg": "Viborg FF",
         "Demirspor": "Adana Demirspor",
         "Midtjylland": "FC Midtjylland",
         "Copenhagen": "	FC København",
         "Minnesota": "Minnesota United",
         "Galatasaray": "Galatasaray SK",
         "Giresunspor": "Giresunspor",
         "GFK": "Gaziantep B.B.",
         "Mazatlán":"Mazatlan FC",
         "Pachuca":"Pachuca CF",
         "Tigres UANL":"Tigres UANL",
         "Tijuana":"Club Tijuana",
         "Monterrey":"CF Monterrey",
         "FC Juárez":"FC Juárez",
         "Necaxa":"Club Necaxa",
         "Querétaro":"Querétaro FC",
         "León":"Club León",
         "Cruz Azul":"Cruz Azul",
         "Pumas UNAM":"	UNAM Pumas",
         "Guadalajara":"Guadalajara Chivas",
         "Club América":"Club América",
         "Toluca":"Deportivo Toluca",
         "Pachuca":"Pachuca CF",
         "San Luis":"Atlético San Luis",
         "Puebla":"Puebla FC",
         "Santos Laguna":"Santos Laguna",
         "Red Star":"FK Crvena Zvezda",
         "Akhmat Grozny":"Akhmat Grozny",
         "FC Khimki":"FK Khimki",
         "Sochi":"PFC Sochi",
        "Krylia Sovetov":"Krylia Sovetov",
        "Spartak Moscow":"Spartak Moscow",
        "Krasnodar":"FK Krasnodar",
        "Rubin Kazan":"Rubin Kazan",
        "Rostov":"FK Rostov",
         "Zaragoza":"Real Zaragoza",
         "Fuenlabrada":"CF Fuenlabrada",
         "Júbilo Iwata":"Jubilo Iwata",
         "Gamba Osaka":"Gamba Osaka",
         "Yokohama FM":"Yokohama Marinos",
         "Shimizu S-Pulse":"Shimizu S-Pulse",
        "Cerezo Osaka":"Cerezo Osaka",
        "Shonan":"Shonan Bellmare",
        "Kyoto Purple Sanga":"Kyoto Sanga",
        "FC Tokyo":"FC Tokyo",
        "Kashiwa Reysol":"Kashiwa Reysol",
        "Avispa Fukuoka":"Avispa Fukuoka",
        "Kawasaki":"Kashima Antlers",
        "Nagoya":"Nagoya Grampus",
        "SC Paderborn":"Paderborn",
        "Fortuna":"Fortuna Düsseldorf",
        "Hamburger SV":"Hamburger SV",
        "Erzgebirge Aue":"Erzgebirge Aue",
        "Dynamo Dresden":"Dynamo Dresden",
        "FC St. Pauli":"St. Pauli",
        "Barnsley":"Barnsley",
        "Fulham":"Fulham",
         "Mirandés":"CD Mirandés",
         "Cartagena":"FC Cartagena",
         "Ibiza":"Ibiza-Eivissa",
         "Leganés":"CD Leganes",
         "Almería":"UD Almería",
         "Lugo":"CD Lugo",
         "Las Palmas":"UD Las Palmas",
         "Girona":"Girona FC",
         "Málaga":"Málaga CF",
         "Ponferradina":"SD Ponferradina",
         "Burgos":"Burgos CF",
         "Real Sociedad B":"Real Sociedad B",
         "Sporting Gijón":"Sporting Gijón",
         "Tenerife":"CD Tenerife",
         "Eibar":"SD Eibar",
         "Amorebieta":"SD Amorebieta",
         "Oviedo":"Real Oviedo",
         "Valladolid":"Real Valladolid",
         "Alcorcón":"Alcorcón",
         "Huesca":"SD Huesca",
         "Reggina":"Reggina Calcio",
         "Perugia":"Perugia Calcio",
         "Lecce":"US Lecce",
         "Brescia":"Brescia Calcio",
         "Ternana":"Ternana Calcio",
         "Cosenza":"Cosenza Calcio",
         "AC Ajaccio":"AC Ajaccio",
         "Bastia":"	SC Bastia",
         "Auxerre":"AJ Auxerre",
         "Sochaux":"FC Sochaux",
         "Nottm Forest":"Nottingham Forest",
         "Reading":"Reading",
         "Birmingham":"Birmingham City",
         "Hull City":"Hull City",
         "Blackburn":"Blackburn Rovers",
         "Bristol City":"Bristol City",
         "Blackpool":"Blackpool",
         "Swansea City":"Swansea City",
         "Peterborough":"Peterborough",
         "Stoke City":"Stoke City",
         "Coventry City":"Coventry City",
         "Sheffield Utd":"Sheffield United",
         "Millwall":"Millwall",
         "Middlesbrough":"Middlesbrough",
         "Bournemouth":"Bournemouth",
         "Derby County":"Derby County",
         "Cardiff City":"Cardiff City",
         "Preston":"Preston North End",
         "SPAL":"SPAL 1907",
         "Ascoli":"Ascoli",
         "Frosinone":"Frosinone",
         "Alessandria":"Alessandria",
         "Monza":"Monza",
         "Vicenza":"Vicenza Calcio",
         "Pordenone":"Pordenone",
         "Como":"Calcio Como",
         "Benevento":"Benevento Calcio",
         "Crotone":"FC Crotone",
         "Le Havre":"Le Havre AC",
         "Nîmes":"Nîmes Olympique",
         "Amiens":"Amiens SC",
         "Nancy":"AS Nancy",
         "Guingamp":"Guingamp",
         "US Quevilly":"US Quevilly",
         "Paris FC":"Paris FC",
         "Niort":"Chamois Niortais",
         "Dunkerque":"USL Dunkerque",
         "Pau":"Pau FC",
         "Grenoble":"Grenoble",
         "Rodez":"Rodez AF",
         "Caen":"SM Caen",
         "Toulouse":"Toulouse FC",
         "Valenciennes":"Valenciennes FC",
         "Dijon FCO":"Dijon FCO",
         "Heidenheim":"	Heidenheim",
         "Werder Bremen":"Werder Bremen",
         "Luton Town":"Luton Town",
         "QPR":"QPR",
         "Karlsruher SC":"Karlsruher SC",
         "Regensburg":"	Jahn Regensburg",
         "Hannover 96":"Hannover 96",
         "Nürnberg":"Nürnberg",
         "Ingolstadt":"Ingolstadt",
         "Schalke 04":"	Schalke 04",
         "Pisa":"AC Pisa",
         "Cremonese":"Cremonese",
         "Vissel Kobe":"Vissel Kobe",
         "Kashima Antlers":"Kashima Antlers",
         "Hansa Rostock":"Hansa Rostock",
         "Holstein Kiel":"Holstein Kiel",
         "Darmstadt 98":"SV Darmstadt",
         "SV Sandhausen":"SV Sandhausen",
         "Parma":"Parma FC",
         "Cittadella":"Cittadella",
         "West Brom":"West Bromwich",
         "Huddersfield":"Huddersfield",
         "Atlas":"Club Atlas",
         "Consa":"Consadole Sapporo",
         "Sanfrecce":"Sanfrecce",
         "Ufa":"FK Ufa",
         "Nizhny Novgorod":"FK Nizhny Novgorod",
         "Arsenal Tula":"Arsenal Tula",
         "Dinamo Moscow":"Dynamo Moscow",
         "Lokomotiv":"Lokomotiv Moscow",
         "CSKA Moscow":"CSKA Moscow",
         "Sagan Tosu":"Sagan Tosu",
         "Urawa Reds":"Urawa Red Diamonds",
         "Ural":"FK Ural",
         "Rheindorf Altach":"SCR Altach",
         "Hartberg":"Hartberg",
         "Admira":"Admira",
         "Ried":"SV Ried",
         "LASK Linz":"LASK Linz",
         "WSG Tirol":"WSG Wattens",
         "SK Austria":"Austria Klagenfurt",
         "Rapid Vienna":"Rapid Wien",
         "Austria Vienna":"Austria Wien",
         "Wolfsberg":"Wolfsberger AC",
         "Sturm Graz":"Sturm Graz"
}
