"""
Carlos Ferreira
"""

import time
from random import choices

import discord
from discord.types import embed
from pygame.examples.cursors import image

from choices import item, get_a_special_item_recipe
from discord.ext import commands

activity = discord.CustomActivity("Created by Kaneki")
token = ""
bot = discord.Bot(activity=activity)
structure_choices = []
item_choices = item
pourcentage_choices = ["60%","40%"]
scrap_emoji = "<:scrap:1319640356094214175>"

scrap = 0
fragments_metal = 1
hq = 2
tissu = 3
bois = 4
engrenages = 5
tech = 6
corde = 7



@bot.slash_command()
async def raid(ctx, structure: discord.Option(str, choices=structure_choices), nombre: int):
  await ctx.respond(f"Pour détruire {nombre} {structure} il faut 40 bombes.")

@bot.slash_command()
async def recycle(ctx, item: discord.Option(str, choices=item_choices), nombre: int, pourcentage: discord.Option(str, choices=pourcentage_choices)):
  request = get_a_special_item_recipe(item,pourcentage)
  embed = discord.Embed(title=f"Recyclage de {nombre} {item} dans un recycleur à {pourcentage}",
                        description=f"Voici ce que vous obtenez en recyclant {nombre} {item}.",
                        color=discord.Colour.from_rgb(87,0,0))

  scrap_state = False
  fragments_metal_state = False
  hq_state = False
  tissu_state = False
  bois_state = False
  engrenages_state = False
  tech_state = False
  corde_state = False

  for x in range(len(request)):
    if request[x] != []:
      if x == 0:
        embed.add_field(name=f"{request[x][0]*nombre} Scrap",
                        value="")
        scrap_state = True
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

  # only scrap
  if scrap_state == True and fragments_metal_state == False and hq_state == False and tissu_state == False and bois_state == False and engrenages_state == False and tech_state == False and corde_state == False:
      embed.set_image(url="https://media.discordapp.net/attachments/1186623630277365870/1319740653227217029/scrap.png?ex=677e2203&is=677cd083&hm=6c61a1dace6ecf2507dcd94a926df38bfdc65351d209bacb00aebf7a28b92039&=&format=webp&quality=lossless&width=887&height=628")

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
      embed.set_image(
          url="https://media.discordapp.net/attachments/1186623630277365870/1319740655605387314/techhq.png?ex=677e2203&is=677cd083&hm=e346fd2945731bc799a7fe5102b0bd596e9de979fdf8f224619b94fac2b45362&=&format=webp&quality=lossless&width=887&height=628")

  # frags + Tech + hq
  if scrap_state == False and fragments_metal_state == True and hq_state == True and tissu_state == False and bois_state == False and engrenages_state == False and tech_state == True and corde_state == False:
      embed.set_image(
          url="https://media.discordapp.net/attachments/1186623630277365870/1319740656196780042/techhqfrags.png?ex=677e2204&is=677cd084&hm=425a00d59aa2287dde36eb19bd1a343fb58c1bab9b13dc9f3a4512210280e2c6&=&format=webp&quality=lossless&width=686&height=486")

  # Tissu + Corde
  if scrap_state == False and fragments_metal_state == False and hq_state == False and tissu_state == True and bois_state == False and engrenages_state == False and tech_state == False and corde_state == True:
      embed.set_image(
          url="https://media.discordapp.net/attachments/1186623630277365870/1319740652774359060/clothrope.png?ex=677e2203&is=677cd083&hm=550ff55bdab93284306d95466f992a96a37ff0160cf696c5bc936d0bda687816&=&format=webp&quality=lossless&width=698&height=494")

  await ctx.respond(embed=embed)


bot.run(token)
