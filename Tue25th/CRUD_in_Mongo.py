import pymongo as mongo


class MongoCRUD:
    def __init__(self, db_url):
        self.connection = mongo.MongoClient(db_url)
        self.used_database = None

    def list_db(self):
        return self.connection.list_database_names()

    def use_database(self, database_name):
        self.used_database = self.connection[database_name]
        return True

    def list_collections(self):
        return self.used_database.list_collection_names()

    def select_collection(self, collection_name):
        self.collection = self.used_database[collection_name]
        return self.collection

    def insert_documents(self, document):
        self.collection.insert_many(document)
        return True

    def read_document(self):
        return list(self.collection.find())

    def update_document(self,query,new_values):
        self.collection.update_many(query,new_values)
        return True




if __name__ == "__main__":
    db = MongoCRUD('mongodb://localhost:27017/')

    print(db.list_db())
    print(db.use_database("employee"))
    print(db.list_collections())
    my_collection = db.select_collection('demo')
    document = [{
        "emp_id": 349,
        "name": "Sasuke",
        "salary": 89020,
        "manager": True
    }
    ]
    print(db.insert_documents(document))
    print(db.read_document())
    myquery = {"name": "Sasuke"}
    newvalues = {"$set": {"name": "Minnie"}}
    db.update_document(myquery,newvalues)