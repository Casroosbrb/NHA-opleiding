# helper.py
def som(dictionary):
    """
    Bereken de som van alle waarden in een dictionary.

    Parameters:
    dictionary (dict): De dictionary waarvan de waarden worden opgeteld.

    Returns:
    int: De som van alle waarden in de dictionary.
    """
    return sum(dictionary.values())
