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
from dotenv import load_dotenv #gére le token dans un fichier à part
# pour interroger wikidata
from SPARQLWrapper import SPARQLWrapper, JSON

# indique où est le token
load_dotenv(dotenv_path = "config")


class DocBot(discord.Client):
    def __init__(self):
        super().__init__(command_prefix = "!")
        self.endpoint_url = "https://query.wikidata.org/sparql"

    async def on_ready(self):
        print("Le bot est prêt.")
        
    async def on_message(self,message):
        print(message.content)
    
    async def on_message(self,message):
        print("message", message)
               
        if message.content == "Ping":
            await message.channel.send("Pong")
        elif message.content == "communard":
            results = self.get_results(self.requete_tous_les_communards())
            for result in results["results"]["bindings"]:
                await message.channel.send(result)
        elif message.content == "?fin":
            print("fermeture")
            await self.close()      
        else:
            pass
        
        
        message_lu = message.content
        #print(message_lu, type(message_lu))
        
        if "?qui:" in message_lu:
            recherche = message_lu[5:]
            if recherche[0] == " ": 
                recherche = recherche[1:]
            if recherche[-1] == " ": 
                recherche = recherche[:-1]
            print(recherche)
            results = self.get_results(self.requete_une_personne(recherche))
            for result in results["results"]["bindings"]:
                await message.channel.send(result)
        
        
            
    def get_results(self, query):
        """Morceau de code issus de Wikidata Query Service.
        C'est lui qui fait la requete"""
        
        user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
        
        sparql = SPARQLWrapper(self.endpoint_url, agent = user_agent)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()
    
    def requete_tous_les_communards(self):
        """requete permettant d'avoir la liste de toutes les personnes de wikidata aillant  communard comme occupation"""
        
        query = """SELECT ?communard ?communardLabel WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  ?communard wdt:P106 wd:Q1780490.
}
LIMIT 5"""
        return query
    
    def requete_une_personne(self,qui):
        """Requete permettant d'avoir la liste de toutes les personnes de wikidata aillant  communard comme occupation
        et qui contient la chaine de caractère 'qui' dans le libéllé de l'objet"""
        
        query = '''SELECT ?communard ?communardLabel WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }   
  ?communard wdt:P106 wd:Q1780490;  rdfs:label ?communardLabel .
  FILTER(CONTAINS(LCASE(?communardLabel), LCASE("'''+ qui +'''")))
  FILTER (LANG(?communardLabel)="fr") 
}
LIMIT 100'''
        return query
        
if __name__ == "__main__":
    bot = DocBot()
    bot.run(os.getenv("TOKEN"))
