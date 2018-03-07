# -*- coding: utf-8 -*-
import pymongo
import json

class accessDB:
    with open('config.json', 'r') as f:
        datastore = json.load(f)
    
    name = datastore[user][name]
    pwd = datastore[user][pwd]

    def compare(self,company,lst):
        client = pymongo.MongoClient()
        repo = client.repo
        repo.authenticate(name, pwd)

        collectionName = '.' + company + 'list'
        prevLst = repo[name + collectionName].find()
        
        for i in lst:
            if i not in prevLst:
                repo.dropCollection(collectionName)
                repo.createCollection(collectionName)
                return True
            else:
                return False

/* eof */