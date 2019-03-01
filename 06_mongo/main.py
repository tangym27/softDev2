import pymongo
SERVER_ADDR = " "
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db.restaurants

#All restaurants in a specified borough.
def query_borough(borough):
	restaurants = collection.find({"borough": borough})
	for restaurant in restaurants:
		print(restaurant)

# All restaurants in a specified zip code.
def query_zipcode(zip):
    zip = str(zip)
	restaurants = collection.find({"address.zipcode": zip})
	for restaurant in restaurants:
		print(restaurant)

# All restaurants in a specified zip code and with a specified grade.
def query_zipcode_grade(zip, grade):
    zip = str(zip)
	restaurants =  collection.find({'$and': [{"address.zipcode": zip },{"grades.0.grade": grade}]})
	for restaurant in restaurants:
		print(restaurant)

# All restaurants in a specified zip code with a score below a specified threshold.
def query_threshold(zip, score):
    zip = str(zip)
	restaurants = collection.find({'$and': [{"address.zipcode": zip},{"grades.0.score":{ '$lt': score }}]});
	for restaurant in restaurants:
		print(restaurant)
