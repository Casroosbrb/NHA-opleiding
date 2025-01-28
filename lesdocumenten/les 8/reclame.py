# Importeren van de functie uit 'algemene_functies.py'
from algemene_functies import mijn_functie_2

# functie 1: aanbieding_1
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."

# functie 2: inkomsten_totaal
def inkomsten_totaal(inkomsten, btw=0):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

# functie 3: laag_en_hoog
def laag_en_hoog(mijn_lijst):
    return [min(mijn_lijst), max(mijn_lijst)]

# functie 4: gemiddelde
def gemiddelde(mijn_lijst):
    gemiddelde_bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag} euro."

# functie 5: meervoudig
def meervoudig(invoer_lijst):
    laag_hoog = laag_en_hoog(invoer_lijst)
    return laag_hoog

# functie 6: combinatie
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])

## prints 

from reclame import aanbieding_1, inkomsten_totaal, laag_en_hoog, gemiddelde, meervoudig, combinatie

# Test aanbieding_1
print(aanbieding_1("aardbei", 4, 0.1))

# Test inkomsten_totaal
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

# Test laag_en_hoog
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

# Test gemiddelde
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

# Test meervoudig
print(meervoudig([10, 5, 3, 2, 1, 2, 9]))

# Test combinatie
print(combinatie([220, 430, 125, 160, 205, 90, 345]))
