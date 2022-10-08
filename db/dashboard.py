from db.connection import Database
import json

class DashboardDb:
    def __init__(self):
        self.db = Database().get_database()

    def insertRecord(self, obj):
        try:
            self.db.classifications.insert_one(json.loads(json.dumps(obj)))
        except(e):
            return 'Cannot Insert'
        else:
            return ''
    
    def getAll(self):
        try:
            return list(self.db.classifications.find({}))
        except(e):
            return 'Error returning data'
        else:
            return ''