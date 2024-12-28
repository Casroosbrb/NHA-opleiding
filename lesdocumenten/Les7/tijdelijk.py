prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}

aanbieding = prijzen["aardbei"] * 0.8
aanbieding2 = prijzen["vanille"] * 0.8
aanbieding3 = prijzen["chocolade"] * 0.8

reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding:.2f}"
reclame_tekst2 = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding2:.2f}"
reclame_tekst3 = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding3:.2f}"



print(reclame_tekst)
print(reclame_tekst2)
print(reclame_tekst3)