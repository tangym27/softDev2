# Team MONGOnificient: Michelle Tang & Jabir Chowdhury & Sarar Aseer
# Softdev pd6
# K#08: Ay Mon, Go Git It From Yer Flask
# 2019-03-07

'''
dataset name: Nobel Prizes

description: Contains a record of all nobel prizes given
in the years 1901-2018 in the categories: physics, chemistry, medicine,
peace, economics, and literature.

Link to dataset: http://api.nobelprize.org/v1/prize.json

Import mechanism:
   1) saved the contents of the dataset in nobelprize.json
   2) created a function called insertData which opens nobelprize.json
   3) used json.load(file) on the opened file
   4) since the dataset contains a single list which contains all the data,
      the insert_many() function was used on the list to import all the data
      into the mongodb database
   5) Called insertData() once
'''

from pymongo import MongoClient
import json


SERVER_ADDR='104.248.227.121' # change to IP you want to start with
client = MongoClient(SERVER_ADDR, 27017)
db = client.huMONGOus
collection = db.nobelprize



def rebuild(address):
    '''
    function to import data from json file and insert into database
    '''

    global SERVER_ADDR
    global client
    global db
    global collection

    client.close()
    #dropping and recreating database on specified server
    if address != "":
        SERVER_ADDR = address
    client = MongoClient(SERVER_ADDR, 27017)
    client.drop_database( "huMONGOus")
    db = client['huMONGOus']
    collection = db['nobelprize']
    insertData()

def insertData():
    '''
    function to import data from json file and insert into database
    only called once
    '''
    with open('data/nobelprize.json') as f:
        data = json.load(f)
        collection.insert_many(data["prizes"])

def find_year(year):
    '''
    returns all nobel prizes given in all categories in the given year
    '''
    ret = []
    for doc in collection.find({"year" : year}):
        ret.append(doc)
    return ret

def find_category(category):
    '''
    returns all nobel prizes given in all years in the given category
    '''
    ret = []
    for doc in collection.find({"category" : category}):
        ret.append(doc)
    return ret

def find_year_category(year, category):
    '''
    returns all nobel prizes given in the given year and category
    '''
    ret = []
    for doc in collection.find({"year" : year, "category" : category}):
        ret.append(doc)
    return ret

def find_category_num(category , num):
    '''
    returns all nobel prizes given in the given category where there were num laureates
    '''
    ret = []
    for doc in collection.find({"category" : category, "laureates" : {'$size':  num}}):
        ret.append(doc)
    return ret

def find_topic(topic):
    '''
    returns all nobel prizes that were given for progress in the given topic
    '''
    ret = []
    for doc in collection.find({"laureates.motivation" : { "$regex" : ".*" + topic + ".*" , "$options" : "i"}}):
        ret.append(doc)
    return ret

# insertData() #already called, no need to call again
# print("###########################")
# print("testing find_year()")
# print("###########################")
# print(find_year("2018"))
# print("###########################")
# print("testing find_category()")
# print("###########################")
# print(find_category("physics"))
# print("###########################")
# print("testing find_year_category()")
# print("###########################")
# print(find_year_category("2018", "chemistry"))
# print("###########################")
# print("testing find_category_num()")
# print("###########################")
# print(find_category_num("peace", 3))
# print("###########################")
# print("testing find_topic()")
# print("###########################")
# print(find_topic("middle east"))
