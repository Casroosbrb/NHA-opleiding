import time
import requests

# Vervang met je Discord-webhook URL
webhook_url = "https://discord.com/api/webhooks/1300955703036481588/VDib7Oc885pLWfSBKCQx7tOvfCklqvFB63P0KpzKI86ep5Q-cYlKcQvdlVRX8oxKYdk_"
user_id = "768480560619978772"  # ID van de gebruiker om te taggen
duration = 250  # Duur in seconden
interval = 1  # Interval in seconden

# Bereken het aantal meldingen dat verstuurd zal worden
num_messages = duration // interval

for _ in range(num_messages):
    data = {
        "content": f"<@{user_id}> Dit is een melding met legitiem doel!",
    }
    
    # Verstuur de webhook-melding
    response = requests.post(webhook_url, json=data)
    
    # Controleer of de melding succesvol is verzonden
    if response.status_code == 204:
        print("Bericht verzonden.")
    else:
        print("Er is iets misgegaan met het versturen van het bericht:", response.status_code)

    # Wacht de ingestelde intervaltijd
    time.sleep(interval)

print("Alle meldingen zijn verstuurd.")
