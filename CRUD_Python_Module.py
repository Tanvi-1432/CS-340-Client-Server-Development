# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from urllib.parse import quote_plus

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        # Initialize MongoDB connection
        

        self.client = MongoClient(
            host=HOST,
            port=PORT,
            username=username,
            password=password,
            authSource="admin"
        )
        
        self.database = self.client[DB]
        self.collection = self.database[COL]


    # Create a document in MongoDB

    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Error inserting document:", e)
                return False
        else:
            return False
            
    # Read documents from MongoDB
    def read(self, query):
        if query is not None:
            try:
                documents = self.collection.find(query)
                return list(documents)
            except Exception as e:
                print("Error reading documents:", e)
                return []
        else:
            return []
    
    # Update documents that match the query
    def update(self, query, new_data):
        try:
            result = self.collection.update_many(
                query,
                {"$set": new_data}
            )
            return result.modified_count
        except Exception as e:
            print("Error updating documents:", e)
            return 0

    # Delete documents that match the query
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Error deleting documents:", e)
            return 0