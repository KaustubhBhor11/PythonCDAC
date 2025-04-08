import pandas as pd
#
# a=[1,2,3,4]
# x=pd.Series(a,index=["one","two","three","four"],name="Serial Number")
#
# print(x)
# print(x.iloc[0:2])
# print(x.loc['one'])
# print(type(x))
#
# df=pd.DataFrame()
# print(df)
# print(type(df))

emp={"emp_id":[1,2,3,4] , "emp_name":["ram","sham","om","harsh"],"Salary":[1000,200,1200,500]}
df1=pd.DataFrame(emp,index=["one","two","three","four"])
print(df1.emp_name)
print(df1['emp_name'],)
print(df1.loc['one'])
print(df1.iloc[0])
df1.to_csv("Employee.csv")
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
# print(list(my_table.find()))
# excel= pd.read_excel('Employee.xlsx')
# print(excel.head())
# print(excel.describe(()))
# print(excel.emp_id)
# for column in excel.columns[2:]:
#     print(excel[column].count())

emp=pd.read_csv('Employee.csv')
print(emp)
