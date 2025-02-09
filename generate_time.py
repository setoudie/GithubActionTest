from datetime import datetime

# Génère un fichier avec la date et l'heure actuelles
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("current_time.txt", "a") as file:
    file.write(f"La date et l'heure actuelles sont : {current_time}\n")

print("Fichier current_time.txt mis à jour avec succès !")
