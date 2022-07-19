#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

# pour interroger wikidata
from SPARQLWrapper import SPARQLWrapper, JSON

class Cog_Communard_data(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.endpoint_url = "https://query.wikidata.org/sparql"
        
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
    
    async def qui(self,message):
        message_lu =  message.content
        print("message", message_lu)
        
        
        recherche = message_lu[5:]
        if recherche[0] == " ": 
            recherche = recherche[1:]
        if recherche[-1] == " ": 
            recherche = recherche[:-1]
        print(recherche)
        results = self.get_results(self.requete_une_personne(recherche))
        for result in results["results"]["bindings"]:
            await message.channel.send(result) 
    
    @commands.command()
    async def communard(self,ctx):
        results = self.get_results(self.requete_tous_les_communards())
        for result in results["results"]["bindings"]:
            await message.channel.send(result)