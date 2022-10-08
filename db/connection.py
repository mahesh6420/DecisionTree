import pymongo
from config import MONGO_URL

class Database:

    def get_database(self):
        db_client = pymongo.MongoClient('mongodb+srv://admin:gBeCjN6Gm9thjsP9@cluster0.ecsej3g.mongodb.net/?retryWrites=true&w=majority')
        return db_client.irisdb