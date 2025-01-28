# presentatie.py
def presenteer(dictionary, totaal):
    """
    Presenteer de gegevens van een dictionary op een gestructureerde manier.

    Parameters:
    dictionary (dict): De dictionary met gegevens om te presenteren.
    totaal (int): Het totaalbedrag om weer te geven.

    Returns:
    None
    """
    for key, value in dictionary.items():
        print(f"{key} : {value} euro")
    print("=" * 26)
    print(f"Totaal : {totaal} euro")
