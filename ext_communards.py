#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

from ast import alias
from asyncio import events
import sys
import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(Cog_Communard_data(bot))

class Cog_Communard_data(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.endpoint_url = "https://query.wikidata.org/sparql"
        print("Cog_initialisé")
        self.test = "test"
        
    @commands.command()
    async def coucou(self, ctx):
        await ctx.send("Coucou !")
        await ctx.send("Comment allez vous ?")