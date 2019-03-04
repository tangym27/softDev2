# Team GoodEeevening
import pymongo

SERVER_ADDR="104.248.230.23"
connection =pymongo.MongoClient(SERVER_ADDR)
db = connection.GoodEeevening
collection = db.poke

# mongoimport --db GoodEeevening --collection poke --jsonArray --file ~/softDev2/07_mongo/db.json

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
print (query_name("Blastoise"))
print (query_type("Water"))
print (query_weakness("Water"))
print (query_candy_count(12))
