"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 1
Numéro d'équipe :  15
Noms et matricules : Thomas Doucet (2370464), Savanh Phengsai (2374918)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici

import csv
import datetime

bibliotheque = {}

file_collection = 'collection_bibliotheque.csv'

with open(file_collection, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:

        cote_rangement = row['cote_rangement']


        bibliotheque[cote_rangement] = {
            'titre': row['titre'],
            'auteur': row['auteur'],
            'date_publication': row['date_publication']
        }


print(f' \n Bibliotheque initiale : {bibliotheque} \n')



########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

file_nouvelle_collection = 'nouvelle_collection.csv'

with open(file_nouvelle_collection, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)


    for row in reader:

        cote_rangement = row['cote_rangement']

        if cote_rangement not in bibliotheque:


            bibliotheque[cote_rangement] = {
                'titre': row['titre'],
                'auteur': row['auteur'],
                'date_publication': row['date_publication']
            }
            print(f"Le livre {row['cote_rangement']}, {row['titre']} par {row['auteur']} a été ajouté avec succès")

        else:
            print(f"Le livre {row['cote_rangement']}, {row['titre']} par {row['auteur']} est déja présent dans la bibliothèque")



########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

cotes_a_modifier = []

for cote_rangement, info_livre in bibliotheque.items():
    if info_livre['auteur'] == 'William Shakespeare':

        nouvelle_cote = 'WS' + cote_rangement[1:]

        cotes_a_modifier.append((cote_rangement, nouvelle_cote, info_livre))


for ancienne_cote, nouvelle_cote, info in cotes_a_modifier:
    bibliotheque[nouvelle_cote] = info
    del bibliotheque[ancienne_cote]


print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')



########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

for cote_rangement, info_livre in bibliotheque.items():
    info_livre['emprunts'] = 'disponible'

file_emprunts = 'emprunts.csv'

with open(file_emprunts, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)


    for row in reader:

        cote_rangement = row['cote_rangement']


        if cote_rangement in bibliotheque:
            bibliotheque[cote_rangement]['emprunts'] = 'emprunté'
            bibliotheque[cote_rangement]['date_emprunt'] = row['date_emprunt']



print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')




########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici

today = datetime.date.today()

with open(file_emprunts, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)


    for row in reader:

        cote_rangement = row['cote_rangement']
        date_emprunt = datetime.date(int(row['date_emprunt'][:4]),int(row['date_emprunt'][5:7]),int(row['date_emprunt'][8:10]) )

        difference_temps = today - date_emprunt
        difference_date = difference_temps.days


        if cote_rangement in bibliotheque and difference_date > 30:
            frais = (difference_date - 30) * 2
            if frais <= 100:
                bibliotheque[cote_rangement]['frais_retard'] = str(frais) + '$'
            if frais > 100:
                bibliotheque[cote_rangement]['frais_retard'] = "100$"

            if difference_date > 365:
                bibliotheque[cote_rangement]['livre_perdus'] = 'perdus'

print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')



