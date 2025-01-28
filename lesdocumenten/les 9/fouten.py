import math

def discriminant(a, b, c):
    """
    Bereken de oplossingen D1 en D2 van een kwadratische vergelijking.

    Parameters:
    a (float): Coëfficiënt van x^2
    b (float): Coëfficiënt van x
    c (float): Constante term

    Returns:
    list: Een lijst met de oplossingen D1 en D2, of 'geen oplossing' als er een fout optreedt.
    """
    try:
        D1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
        D2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
        uitvoer = [D1, D2]
    except (ValueError, ZeroDivisionError):
        uitvoer = ["geen oplossing", "geen oplossing"]
    return uitvoer

# Hoofdcode
print("Voor de formule ax^2 + bx + c, geef a, b en c:")
try:
    a = int(input("Geef de waarde van a: "))
    b = int(input("Geef de waarde van b: "))
    c = int(input("Geef de waarde van c: "))
    
    uitkomst = discriminant(a, b, c)
    D1 = uitkomst[0]
    D2 = uitkomst[1]

    print(f"Voor a={a}, b={b}, c={c}, zijn de oplossingen:")
    print(f"D1 = {D1}")
    print(f"D2 = {D2}")
except ValueError:
    print("Ongeldige invoer. Zorg ervoor dat je hele getallen invoert voor a, b en c.")
