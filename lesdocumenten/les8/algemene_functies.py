# Importeer mijn_functie_2 uit algemene_functies.py
from algemene_functies import mijn_functie_2

# Functie 1: aanbieding_1
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."

# Functie 2: inkomsten_totaal
def inkomsten_totaal(inkomsten, btw=0):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."

# Functie 3: laag_en_hoog
def laag_en_hoog(mijn_lijst):
    return [min(mijn_lijst), max(mijn_lijst)]

# Functie 4: gemiddelde
def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    gemiddelde_bedrag = totaal / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag:.2f} euro."

# Functie 5: meervoudig
def meervoudig(invoer_lijst):
    laag_en_hoog_lijst = laag_en_hoog(invoer_lijst)
    return laag_en_hoog_lijst

# Functie 6: combinatie
def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0])  # Aannemende dat de eerste waarde het argument is voor mijn_functie_2
