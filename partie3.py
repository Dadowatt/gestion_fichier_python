import os
import json

# Fichier du compteur
fichier = "compteur.json"
etat_defaut = {"compteur": 0}

# --- Chargement du fichier ---
try:
    if os.path.exists(fichier):
        with open(fichier, 'r', encoding='utf-8') as f:
            contenu = f.read().strip()
            if contenu == "":
                data = etat_defaut
            else:
                data = json.loads(contenu) 
    else:
        data = etat_defaut
except json.JSONDecodeError:
    print("Le fichier JSON est mal formé, réinitialisation du compteur.")
    data = etat_defaut

# Assurer que la clé compteur existe
data.setdefault("compteur", 0)
compteur = data['compteur']

# Affichage du compteur actuel
print(f"Compteur actuel : {compteur}")

# --- Interaction utilisateur ---
while True:
    print("\nQue voulez-vous faire ?")
    print("1. Augmenter le compteur")
    print("0. Diminuer le compteur")
    choix = input("Choisir une option : ").strip()
    if choix == "1":
        compteur += 1
    elif choix == "0":
        compteur -= 1
    else:
        print("Saisie incorrecte, veuillez choisir 1 ou 2")

# Mise à jour en mémoire
    data["compteur"] = compteur

# Sauvegarde du fichier
    with open(fichier, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Compteur mis à jour : {compteur}")
