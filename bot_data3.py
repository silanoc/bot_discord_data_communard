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
        """Contrôle : affiche tous les messages dans le terminal."""
        print(message.content)

    async def on_message(self, message):
        """simple test de vérification de connection"""
        if(message.content.startswith("!ping")):
            await message.channel.send("Pong")
        
        """pour se déconnecter proprement"""    
        if(message.content.startswith("!fin")):
            print("fermeture")
            await self.close()    
        
if __name__ == "__main__":
    bot = DocBot()
    #bot.add_cog(communards.Cog_Communard_data(bot))
    bot.load_extension("ext_communards")
    bot.run(os.getenv("TOKEN"))
    #communards.Cog_Communard_data.communard()
