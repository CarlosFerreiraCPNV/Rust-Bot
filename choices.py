import csv

from urllib3 import request

item = []
x = 0


with open('choices.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        temp_tab = []
        if row['Pourcentage'] == "60%":
            item.append(row['Nom'])


def get_a_special_item_recipe(item, pourcentage):
    nom = []
    scrap = []
    fragments_metal = []
    hq = []
    tissu = []
    bois = []
    engrenages = []
    tech = []
    corde = []

    with open('choices.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temp_tab = []
            temp_tab.append(row['Pourcentage'])
            if row['Nom'] == item:
                if temp_tab[-1] == pourcentage:
                    nom.append(row['Nom'])
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

    return scrap, fragments_metal, hq, tissu, bois, engrenages, tech, corde

request = get_a_special_item_recipe("Gears", "60%")