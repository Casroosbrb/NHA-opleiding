# boekhouding.py
from helper import *  # Importeer alles uit helper.py
from presentatie import *  # Importeer alles uit presentatie.py
import csv

# Definieer de dictionary 'inkomsten'
inkomsten = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

# Bereken totaal inkomsten met de functie som() uit helper.py
totaal_inkomsten = som(inkomsten)

# Presenteer de gegevens met de functie presenteer() uit presentatie.py
presenteer(inkomsten, totaal_inkomsten)

# Schrijf de inkomsten naar een CSV-bestand
with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key, value])
