# Team GoodEeevening -- Michelle Tang & Kyle Tau
# SoftDev2 pd 6
# K07 -- Import/Export Bank
# 2019-03-04

'''
Dataset: Pokedex (Pokemon GO Pokedex)
Contents: This dataset contains all the information about Gen 1 Pokemon from the Pokemon GO game including ID number, physical stats, spawn chances, and weaknesses.
Link: https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
Import mechanism: mongoimport --db GoodEeevening --collection poke --jsonArray --file ~/PATH TO/pokemon.json
    **Create database GoodEeevening with collection poke importing from the pokemon.json file**
'''

import pymongo

SERVER_ADDR="104.248.230.23"
connection =pymongo.MongoClient(SERVER_ADDR)
db = connection.GoodEeevening
collection = db.poke


#given a number, return the stats of that pokemon
def query_num(num):
    pokemon = collection.find({'num':num})
    for poke in pokemon:
        print poke

#given a name, return the stats of that pokemon
def query_name(name):
    pokemon = collection.find({'name':name})
    for poke in pokemon:
        print poke

#given a type, return the stats of all the pokemon with that type
def query_type(type):
    pokemon = collection.find({'type':[type]})
    for poke in pokemon:
        print poke

#given a weakness, return the stats of all the pokemon with that single weakness
def query_weakness(type):
    pokemon = collection.find({'type':[type]})
    for poke in pokemon:
        print poke

#given a number, return the stats of all the pokemon with that candy count number
def query_candy_count(num):
    pokemon = collection.find({'candy_count':num})
    for poke in pokemon:
        print poke

print ("Testing query_num")
print (query_num("007"))

print ("Testing query_name")
print (query_name("Blastoise"))

print ("Testing query_type")
print (query_type("Water"))

print ("Testing query_weakness")
print (query_weakness("Water"))

print("Testing query_candy_count")
print (query_candy_count(12))
