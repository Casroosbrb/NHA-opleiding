import time


prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}

aanbieding = prijzen["aardbei"] * 0.8
aanbieding2 = prijzen["vanille"] * 0.8
aanbieding3 = prijzen["chocolade"] * 0.8

reclame_tekst1 = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding:.2f}"
reclame_tekst2 = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding2:.2f}"
reclame_tekst3 = f"Vandaag in de aanbieding: chocolade-ijs, 1 liter – slechts € {aanbieding3:.2f}"
reclame_tekst4 = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding:.2f}".upper()
reclame_tekst5 = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding2:.2f}".upper()
reclame_tekst6 = f"Vandaag in de aanbieding: chocolade-ijs, 1 liter – slechts € {aanbieding3:.2f}".upper()
flyer1 = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding:.2f}".lower()
flyer2 = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding2:.2f}".lower()
flyer3 = f"Vandaag in de aanbieding: chocolade-ijs, 1 liter – slechts € {aanbieding3:.2f}".lower()
reclame_teksten = [
    reclame_tekst1,
    reclame_tekst2,
    reclame_tekst3,
    reclame_tekst4,
    reclame_tekst5,
    reclame_tekst6,
]

for i, tekst in enumerate(reclame_teksten, start=1):
    print(f"Reclame tekst {i}: {tekst}")
    time.sleep(10)