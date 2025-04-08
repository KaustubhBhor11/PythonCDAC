import pymongo as mongo
import pandas as pd
# Create connection to db
db = mongo.MongoClient("mongodb://localhost:27017/")
print(db.list_database_names())

# Select database
mydb = db["employee"]

# select collection in table amd print
my_table = mydb["demo"]

# list document in collection
# print(list(my_table.find()))
df1=pd.DataFrame(list(my_table.find()))

df1.drop('_id',axis=1,inplace=True)
df1.drop_duplicates(inplace=True)
# print(df1['salary'].mean())
# print(df1)
for i in df1['salary']:
    print(i)
