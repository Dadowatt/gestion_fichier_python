# Partie 1 — Fichier texte (TXT)
# Lire le contenu du fichier et l’afficher dans le terminal.

fichier = open('notes.txt', 'r', encoding='utf-8')
contenu = fichier.read()
print(contenu)
fichier.close()

#Ajouter une nouvelle ligne sans supprimer les précédentes.
with open('notes.txt', 'a', encoding='utf-8') as f:
    f.write('voici la nouvelle ligne ajouté\n')

with open('notes.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# Supprimer la dernière ligne du fichier
with open('notes.txt', 'r', encoding='utf-8') as f:
    ligne = f.readlines()

with open('notes.txt', 'w', encoding='utf-8') as f:
    f.writelines(ligne[:-1])


# Gérer le cas ou le fichier n'existe pas
try:
    with open('notes.txt', 'r', encoding='utf-8') as f:
        ligne = f.readlines()

    with open('notes.txt', 'w', encoding='utf-8') as f:
        f.writelines(ligne[:-1])
        
except FileNotFoundError:
    print("le fichier n'existe pas")



