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

token = ""
bot = discord.Bot()
structure_choices = []
item_choices = item
pourcentage_choices = ["60%","40%"]

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
                        color=discord.Color.random())
  for x in range(len(request)):
    if request[x] != []:
      if x == 0:
        embed.add_field(name=f"{request[x][0]*nombre} Scrap",
                        value=":scrap:")
      if x == 1:
        embed.add_field(name=f"{request[x][0]*nombre} Fragments de Métal",
                        value="description of field 1")
      if x == 2:
        embed.add_field(name=f"{request[x][0] * nombre} Métal de Haute Qualité",
                        value="description of field 1")
      if x == 3:
        embed.add_field(name=f"{request[x][0] * nombre} Tissu",
                        value="description of field 1")
      if x == 4:
        embed.add_field(name=f"{request[x][0] * nombre} Bois",
                        value="description of field 1")
      if x == 6:
        embed.add_field(name=f"{request[x][0] * nombre} Engrenages",
                        value="description of field 1")
      if x == 7:
        embed.add_field(name=f"{request[x][0] * nombre} Tech Trash",
                        value="description of field 1")
      if x == 8:
        embed.add_field(name=f"{request[x][0] * nombre} Corde",
                        value="description of field 1")

  embed.set_footer(text="Created By Kaneki")
  #embed.set_image(url="https://static.wikia.nocookie.net/youtube/images/b/bb/Facepunch.jpeg/revision/latest/thumbnail/width/360/height/360?cb=20221110025446")
  #embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

  await ctx.respond(embed=embed)
  #await ctx.respond(f"# Lors que tu recycle {nombre} {item} à {pourcentage} tu obtiens : {response_send}")
  request = ()

bot.run(token)
