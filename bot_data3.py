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

# Pour le bon fonctionnement
import discord
from discord.ext import commands
from dotenv import load_dotenv #gére le token dans un fichier à part

#import communards

# indique où est le token
load_dotenv(dotenv_path = "config")

class DocBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix = "!")

    async def on_ready(self):
        print(f"{self.user.display_name} est prêt. Il est connecté.")
        
    async def on_message(self,message):
        print(message.content)

    async def on_message(self, message):
        if(message.content.startswith("!ping")):
            await message.channel.send("Pong")
            
        if(message.content.startswith("!fin")):
            print("fermeture")
            await self.close()    
        
if __name__ == "__main__":
    bot = DocBot()
    #bot.add_cog(communards.Cog_Communard_data(bot))
    bot.run(os.getenv("TOKEN"))
