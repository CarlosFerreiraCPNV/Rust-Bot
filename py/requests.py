# Importation des bibliothèques nécessaires
import csv

# Initialisation des listes pour stocker les données des fichiers CSV

item = []  # Liste des objets récupérés depuis 'choices.csv'
raid = []  # Liste des structures récupérées depuis 'raid.csv'
x = 0

# Chargement des objets depuis 'recyclables.csv' pour un pourcentage spécifique
with open('../data/recyclables.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile) # Lecture du fichier en tant que dictionnaire
    for row in reader:
        temp_tab = []
        # Si l'objet a un pourcentage de "60%", il est ajouté à la liste 'item'
        if row['Pourcentage'] == "60%":
            item.append(row['Nom'])

# Fonction pour récupérer la recette d'un objet spécifique en fonction du pourcentage
def get_a_special_item_recipe(item, pourcentage):
    """
        Récupère les ressources nécessaires pour un objet spécifique en fonction de son rendement.
        :param item: Nom de l'objet.
        :param pourcentage: Pourcentage de rendement (ex. "60%" ou "40%").
        :return: Une liste contenant les quantités des ressources nécessaires.
    """
    # Initialisation des listes pour chaque ressource
    nom = []
    scrap = []
    fragments_metal = []
    hq = []
    tissu = []
    bois = []
    engrenages = []
    tech = []
    corde = []

    with open('../data/recyclables.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile) # Lecture du fichier en tant que dictionnaire
        for row in reader:
            temp_tab = []
            temp_tab.append(row['Pourcentage'])
            # Vérifie si l'objet correspond au nom et au pourcentage souhaités
            if row['Nom'] == item:
                if temp_tab[-1] == pourcentage:
                    nom.append(row['Nom'])
                    # Ajoute les ressources aux listes respectives si elles sont > 0
                    if int(row['Scrap']) > 0:
                        scrap.append(int(row['Scrap']))

                    if int(row['Fragments metal']) > 0:
                        fragments_metal.append(int(row['Fragments metal']))

                    if int(row['HQ']) > 0:
                        hq.append(int(row['HQ']))

                    if int(row['Tissu']) > 0:
                        tissu.append(int(row['Tissu']))

                    if int(row['Bois']) > 0:
                        bois.append(int(row['Bois']))

                    if int(row['Engrenages']) > 0:
                        engrenages.append(int(row['Engrenages']))

                    if int(row['Tech']) > 0:
                        tech.append(int(row['Tech']))

                    if int(row['Corde']) > 0:
                        corde.append(int(row['Corde']))

    # Retourne les quantités pour chaque ressource
    return scrap, fragments_metal, hq, tissu, bois, engrenages, tech, corde

# Chargement des structures depuis 'structures.csv'
with open('../data/structures.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile) # Lecture du fichier en tant que dictionnaire
    for row in reader:
        # Ajoute chaque structure à la liste 'raid'
        raid.append(row['Nom'])


# Fonction pour récupérer les ressources nécessaires pour détruire une structure spécifique
def get_a_special_raid_structure(structure):
    """
        Récupère les ressources nécessaires pour détruire une structure spécifique.
        :param structure: Nom de la structure.
        :return: Une liste contenant les quantités des différents explosifs nécessaires.
    """

    # Initialisation des listes pour chaque type d'explosif
    Cquatre = []
    explo = []
    satchel = []
    beancan = []
    rocket = []
    HVrocket = []
    grenade = []
    mlrs = []
    HEgrenade = []
    Cocktail = []

    with open('../data/structures.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile) # Lecture du fichier en tant que dictionnaire
        for row in reader:
            if row['Nom'] == structure:
                # Ajoute les quantités des explosifs pour la structure correspondante
                Cquatre.append(int(row['C4']))
                explo.append(int(row['Explo 5.56']))
                satchel.append(int(row['Satchel']))
                beancan.append(int(row['Beancan']))
                rocket.append(int(row['Rocket']))
                HVrocket.append(int(row['High Velocity Rocket']))
                grenade.append(int(row['F1 Grenade']))
                mlrs.append(int(row['MLRS']))
                HEgrenade.append(int(row['40mm HE Grenade']))
                Cocktail.append(int(row['Cocktail']))

    # Retourne les quantités pour chaque explosif
    return  Cquatre, explo, satchel, beancan, rocket, HVrocket, grenade, mlrs, HEgrenade, Cocktail