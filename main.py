"""
Carlos Ferreira
"""

import time
import discord
from discord.ext import commands

token = ""
bot = discord.Bot()

@bot.slash_command()
async def raid(ctx, structure: discord.Option(str, choices=["mur en pierre", "mur en metal"]), nombre: int):
  await ctx.respond(f"Pour détruire {nombre} {structure} il faut 40 bombes.")

@bot.slash_command()
async def recycle(ctx, item: discord.Option(str, choices=["Caméra", "SMG Body"]), nombre: int):
  await ctx.respond(f"Pour détruire {nombre} {item} il faut 40 bombes.")

bot.run(token)
