import pymongo as mongo

# Create connection to db
db = mongo.MongoClient("mongodb://localhost:27017/")
print(db.list_database_names())

# Select database
mydb = db["employee"]

# List the collections in db
x = mydb.list_collection_names()
print(x)

# select collection in table amd print
my_table = mydb["demo"]
print(my_table)

# Insert document in collection
document = {
    "emp_id": 111,
    "name": "Sham",
    "salary": 75000,
    "manager": True
}
my_table.insert_one(document)
# my_table.update_many()
# list document in collection
print(list(my_table.find()))
