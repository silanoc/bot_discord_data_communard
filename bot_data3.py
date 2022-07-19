#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

"""-----------------------------------------------------------------
Bot discord spécialisé sur la commune de Paris 1871.
Il utilise wikidata, et autres projets de mediawiki comme base de données

date de création : 18 juillet 2018
autair : silanoc
version : 0.0.1
-------------------------------------------------------------------"""

# Standard
import os
import sys
# Pour le bon fonctionnement
import discord
from discord.ext import commands
from dotenv import load_dotenv #gére le token dans un fichier à part
# pour interroger wikidata
from SPARQLWrapper import SPARQLWrapper, JSON

import communards

# indique où est le token
load_dotenv(dotenv_path = "config")

class DocBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix = "!")
        self.add_commands()
        
    async def on_ready(self):
        print(f"{self.user.display_name} est prêt. Il est connecté.")
        
    async def on_message(self,message):
        print(message.content)
    
    def add_commands(self):
        @self.command(name="Ping", pass_context=True)
        async def Ping(self, ctx):
            await ctx.channel.send("Pong")

        @self.command(name="fin")
        async def fin(self, ctx):
            print("fermeture")
            await self.close()    
        
if __name__ == "__main__":
    bot = DocBot()
    bot.add_cog(communards.Cog_Communard_data(bot))
    bot.run(os.getenv("TOKEN"))
