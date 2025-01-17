"""
Carlos Ferreira
"""

# Importation des bibliothèques nécessaires
import discord
from TOKEN import bot_token

from requests import *

# Configuration de l'activité du bot
activity = discord.CustomActivity("Created by Kaneki")
token = bot_token
bot = discord.Bot(activity=activity)

# Définition des choix et des ressources utilisées dans les commandes
structure_choices = raid
item_choices = item
pourcentage_choices = ["60%","40%"]
scrap_emoji = "<:scrap:1319640356094214175>" # Emoji utilisé pour représenter la ferraille

# Commande pour effectuer un raid
@bot.slash_command()
async def raid(ctx, structure: discord.Option(str, choices=structure_choices), nombre: int):
    """
        Cette commande génère une liste des éléments nécessaires pour effectuer un raid
        sur une structure donnée, en fonction de son type et de sa quantité.
    """
    request = get_a_special_raid_structure(structure)
    embed = discord.Embed(title=f"Faire un RAID sur {nombre} {structure}",
                        description=f"Voici les éléments que vous pouvez utiliser pour détruire {nombre} {structure} :",
                        color=discord.Colour.from_rgb(87,0,0))

    # Ajout d'une image descriptive au message
    embed.set_image(url="https://i.ytimg.com/vi/ujGRaqlTZBQ/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLC3sXh_zns3d9kkF6e5wKbfDYk4LA")

    # Génération des ressources nécessaires pour chaque type de structure
    for x in range(len(request)):

        if x == 0:
            Cquatre_recipe = f"""*Souffre : {2200 * int(request[x][0])} 
                                    Charbon : {3000 * int(request[x][0])} 
                                    Metal Fragments : {200 * int(request[x][0])} 
                                    Low Grade : {60 * int(request[x][0])} 
                                    Tech Trash : {2 * int(request[x][0])}*"""

            embed.add_field(name=f"{request[x][0]*nombre} C4",
                            value=Cquatre_recipe)
        # Ajout des autres recettes pour chaque type d'arme/explosif...
        # (Les autres blocs `if` suivent une logique similaire)
        if x == 1:
            Explo_recipe = f"""*Souffre : {int(50 /2 * int(request[x][0]))} 
                                Charbon : {int(60 /2 * int(request[x][0]))} 
                                Metal Fragments : {int(10 /2 * int(request[x][0]))}*"""

            embed.add_field(name=f"{request[x][0]*nombre} Explosive 5.56 Rifle Ammo",
                            value=Explo_recipe)
        if x == 2:
            satchel_recipe = f"""*Souffre : {480 * int(request[x][0])} 
                                 Charbon : {720 * int(request[x][0])} 
                                 Metal Fragments : {80 * int(request[x][0])} 
                                 Tissu : {10 * int(request[x][0])} 
                                 Corde : {1 * int(request[x][0])}*"""

            embed.add_field(name=f"{request[x][0]*nombre} Satchel Charge",
                            value=satchel_recipe)
        if x == 3:
            beancan_recipe = f"""*Souffre : {120 * int(request[x][0])} 
                                 Charbon : {180 * int(request[x][0])} 
                                 Metal Fragments : {20 * int(request[x][0])}*"""

            embed.add_field(name=f"{request[x][0]*nombre} Beancan Greanade",
                            value=beancan_recipe)
        if x == 4:
            rocket_recipe = f"""*Souffre : {1400 * int(request[x][0])} 
                                 Charbon : {1950 * int(request[x][0])} 
                                 Metal Fragments : {100 * int(request[x][0])} 
                                 Low Grade : {32 * int(request[x][0])} 
                                 Metal Pipe : {2 * int(request[x][0])}*"""

            embed.add_field(name=f"{request[x][0]*nombre} Rocket",
                            value=rocket_recipe)
        if x == 5:
            Hrocket_recipe = f"""*Souffre : {200 * int(request[x][0])} 
                                 Charbon : {300 * int(request[x][0])} 
                                 Metal Pipe : {1 * int(request[x][0])}*"""

            embed.add_field(name=f"{request[x][0]*nombre} High Velocity Rocket",
                            value=Hrocket_recipe)
        if x == 6:
            grenade_recipe = f"""*Souffre : {60 * int(request[x][0])} 
                                 Charbon : {90 * int(request[x][0])} 
                                 Metal Fragments : {25 * int(request[x][0])}*"""

            embed.add_field(name=f"{request[x][0]*nombre} F1 Grenade",
                            value=grenade_recipe)
        if x == 7:
            mlrs_recipe = f"""*Pas Craftable"""

            embed.add_field(name=f"{request[x][0]*nombre} MLRS Rocket",
                            value=mlrs_recipe)
        if x == 8:
            hegrenade_recipe = f"""*Pas Craftable"""

            embed.add_field(name=f"{request[x][0]*nombre} 40mm HE Greanade",
                            value=hegrenade_recipe)
        if x == 9:
            molo_recipe = f"""*Tissu : {10 * int(request[x][0])} 
                                 Low Grade : {50 * int(request[x][0])}*"""

            embed.add_field(name=f"{request[x][0]*nombre} Cocktail Molotov",
                            value=molo_recipe)

    # Répond au contexte avec l'embed créé
    await ctx.respond(embed=embed)

# Commande pour recycler des objets
@bot.slash_command()
async def recycle(ctx, item: discord.Option(str, choices=item_choices), nombre: int, pourcentage: discord.Option(str, choices=pourcentage_choices)):
    """
        Cette commande indique les ressources obtenues en recyclant un objet spécifique
        en fonction de la quantité et du pourcentage de rendement choisi.
    """
    request = get_a_special_item_recipe(item,pourcentage)
    embed = discord.Embed(title=f"Recyclage de {nombre} {item} ({pourcentage} de rendement)",
                        description=f"En recyclant {nombre} {item}, vous obtiendrez :",
                        color=discord.Colour.from_rgb(87,0,0))

    # Initialisation des états des ressources obtenues
    scrap_state = False
    fragments_metal_state = False
    hq_state = False
    tissu_state = False
    bois_state = False
    engrenages_state = False
    tech_state = False
    corde_state = False

    # Parcours des ressources pour ajouter les informations à l'embed
    for x in range(len(request)):
        if request[x] != []:
            if x == 0:
                embed.add_field(name=f"{request[x][0]*nombre} Scrap",
                                value="")
                scrap_state = True
            # Autres ressources (similaire au bloc précédent)
            if x == 1:
                embed.add_field(name=f"{request[x][0]*nombre} Fragments de Métal",
                                value="")
                fragments_metal_state = True
            if x == 2:
                embed.add_field(name=f"{request[x][0]*nombre} Métal de Haute Qualité",
                                value="")
                hq_state = True
            if x == 3:
                embed.add_field(name=f"{request[x][0]*nombre} Tissu",
                                value="")
                tissu_state = True
            if x == 4:
                embed.add_field(name=f"{request[x][0]*nombre} Bois",
                                value="")
                bois_state = True
            if x == 5:
                embed.add_field(name=f"{request[x][0]*nombre} Engrenages",
                                value="")
                engrenages_state = True
            if x == 6:
                embed.add_field(name=f"{request[x][0]*nombre} Tech Trash",
                                value="")
                tech_state = True
            if x == 7:
                embed.add_field(name=f"{request[x][0]*nombre} Corde",
                                value="")
                corde_state = True

    # Ajout d'une image spécifique selon les ressources recyclées
    # only scrap
    if scrap_state == True and fragments_metal_state == False and hq_state == False and tissu_state == False and bois_state == False and engrenages_state == False and tech_state == False and corde_state == False:
        embed.set_image(url="https://media.discordapp.net/attachments/1186623630277365870/1319740653227217029/scrap.png?ex=677e2203&is=677cd083&hm=6c61a1dace6ecf2507dcd94a926df38bfdc65351d209bacb00aebf7a28b92039&=&format=webp&quality=lossless&width=887&height=628")

    # Autres cas pour afficher les images correspondantes
    # scrap + frags
    if scrap_state == True and fragments_metal_state == True and hq_state == False and tissu_state == False and bois_state == False and engrenages_state == False and tech_state == False and corde_state == False:
        embed.set_image(url="https://media.discordapp.net/attachments/1186623630277365870/1319740653839847535/scrapfrags.png?ex=677e2203&is=677cd083&hm=4e4e3438216a41360d0437b7c2ef176ad2b31416f68f36a9e3456efb54191869&=&format=webp&quality=lossless&width=686&height=486")

    # scrap + frags + hq
    if scrap_state == True and fragments_metal_state == True and hq_state == True and tissu_state == False and bois_state == False and engrenages_state == False and tech_state == False and corde_state == False:
        embed.set_image(url="https://media.discordapp.net/attachments/1186623630277365870/1319740655026569236/srapfragshq.png?ex=677e2203&is=677cd083&hm=055c177a290ab23c69d9eea97e4687edd55042abe378113234f30e3126548f48&=&format=webp&quality=lossless&width=686&height=486")

    # scrap + hq
    if scrap_state == True and fragments_metal_state == False and hq_state == True and tissu_state == False and bois_state == False and engrenages_state == False and tech_state == False and corde_state == False:
        embed.set_image(url="https://media.discordapp.net/attachments/1186623630277365870/1319740654498218034/scraphq.png?ex=677e2203&is=677cd083&hm=9ad6868a638fc4fcc501196f3397a8ffd270d29f0ae0e496b53ec2bf9bd84a9d&=&format=webp&quality=lossless&width=686&height=486")

    # Tech + hq
    if scrap_state == False and fragments_metal_state == False and hq_state == True and tissu_state == False and bois_state == False and engrenages_state == False and tech_state == True and corde_state == False:
        embed.set_image(url="https://media.discordapp.net/attachments/1186623630277365870/1319740655605387314/techhq.png?ex=677e2203&is=677cd083&hm=e346fd2945731bc799a7fe5102b0bd596e9de979fdf8f224619b94fac2b45362&=&format=webp&quality=lossless&width=887&height=628")

    # frags + Tech + hq
    if scrap_state == False and fragments_metal_state == True and hq_state == True and tissu_state == False and bois_state == False and engrenages_state == False and tech_state == True and corde_state == False:
        embed.set_image(url="https://media.discordapp.net/attachments/1186623630277365870/1319740656196780042/techhqfrags.png?ex=677e2204&is=677cd084&hm=425a00d59aa2287dde36eb19bd1a343fb58c1bab9b13dc9f3a4512210280e2c6&=&format=webp&quality=lossless&width=686&height=486")

    # Tissu + Corde
    if scrap_state == False and fragments_metal_state == False and hq_state == False and tissu_state == True and bois_state == False and engrenages_state == False and tech_state == False and corde_state == True:
        embed.set_image(url="https://media.discordapp.net/attachments/1186623630277365870/1319740652774359060/clothrope.png?ex=677e2203&is=677cd083&hm=550ff55bdab93284306d95466f992a96a37ff0160cf696c5bc936d0bda687816&=&format=webp&quality=lossless&width=698&height=494")

    # Réponse au contexte avec l'embed créé
    await ctx.respond(embed=embed)

# Commande pour afficher des commandes utiles
@bot.slash_command()
async def commands(ctx):
    """
        Cette commande affiche une liste de commandes utiles pour les joueurs de Rust.
    """
    embed = discord.Embed(title="Voici quelques commandes utiles :",
                          description='''
                          🔸  Se suicider et respawn directement sur un bag, Idéal en cas de RAID pour réapparaître rapidement.
                          
                          ```bind [KEY] kill;respawn_sleepingbag [ID]```
                          
                          🔸  Zoomer, Permet d’augmenter temporairement votre champ de vision.
                          
                          ```bind [KEY] "lookatradius 20;+fov 90;fov 70;lookatradius 0.01"```
                          
                          🔸  Afficher des informations utiles dans la console, Active automatiquement des commandes pratiques à chaque ouverture de la console.

                          ```input.bind F1 client.consoletoggle; combatlog; client.ping```
                          ''',
                          colour=discord.Colour.from_rgb(87,0,0))

    await ctx.respond(embed=embed)

# Commande pour afficher un guide d'utilisation
@bot.slash_command()
async def help(ctx):
    """
        Cette commande affiche un guide détaillé pour utiliser les fonctionnalités du bot.
    """
    embed = discord.Embed(title="Bienvenue dans le guide d'utilisation du Sensei Of Rust ! Voici comment utiliser les commandes disponibles :",
                          description='''
                          🔹 Commandes spécifiques
                          
                          1. ```/raid```

                          **Explique les moyens de détruire des structures (ex. murs en pierre, portes métalliques).**
                          
                          *Exemple : /raid [structure] [nombre de structure à casser].*
                          
                          2. ```/recycle```

                          **Indique ce que vous pouvez obtenir en recyclant des objets spécifiques.**
                          
                          *Exemple : /recycle [item] [nombre d'items à recycler] [pourcentage].*
                          
                          3. ```/commands```

                          **Affiche des commandes utiles.**
                          
                          *Exemple : /commands.*
                          
                          🔹 Besoin d'aide supplémentaire ?

                          Si vous avez des questions ou rencontrez des problèmes, n'hésitez pas à demander à un administrateur ou à consulter la documentation liée au bot.
                          ''',
                          colour=discord.Colour.from_rgb(87, 0, 0))

    await ctx.respond(embed=embed)

print("Connecté")
# Démarrage du bot avec le token
bot.run(token)
