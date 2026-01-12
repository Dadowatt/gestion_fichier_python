#Partie 2 — Fichier JSON
import json

personne = {
    "nom": "Watt",
    "prenom": "Dado",
    "matricule": "P9"
}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(personne, f, indent=4, ensure_ascii=False)

#Lire le fichier JSON et afficher les données.
with open('data.json', 'r', encoding='utf-8') as f:
    personne = json.load(f)

for c, v in personne.items():
    print(f"{c} : {v}")

#Modifier une valeur (ex : matricule).
with open('data.json', 'r', encoding='utf-8') as f:
    personne = json.load(f)

personne['prenom'] = 'Thilaye'

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(personne, f, indent=4, ensure_ascii=False)