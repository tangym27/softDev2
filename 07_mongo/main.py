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


#given a number, return a pokemon
def query_num(num):
    pokemon = collection.find({'num':num})
    for poke in pokemon:
        print poke

def query_name(name):
    pokemon = collection.find({'name':name})
    for poke in pokemon:
        print poke

def query_type(type):
    pokemon = collection.find({'type':[type]})
    for poke in pokemon:
        print poke

def query_weakness(type):
    pokemon = collection.find({'type':[type]})
    for poke in pokemon:
        print poke

def query_candy_count(num):
    pokemon = collection.find({'candy_count':num})
    for poke in pokemon:
        print poke

print ("Testing\n\n\n\n")
print (query_num("007"))
print ("Testing\n\n\n\n")

print (query_name("Blastoise"))
print ("Testing\n\n\n\n")

print (query_type("Water"))
print (query_weakness("Water"))
print (query_candy_count(12))
