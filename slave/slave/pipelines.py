import pymongo as pm

host = 'localhost'
port = 27017
client = pm.MongoClient(host,port)
db = client.demo.tongcheng

class SlavePipeline(object):
    def process_item(self, item, spider):
        db.insert(dict(item))
