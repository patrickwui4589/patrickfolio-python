import csv

with open("fichier.csv", newline='', encoding='utf-8') as csvfile:
    lecteur = csv.reader(csvfile)
    for ligne in lecteur:
        print(ligne)
