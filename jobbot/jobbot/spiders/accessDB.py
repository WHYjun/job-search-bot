# -*- coding: utf-8 -*-
import pymongo
import json
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'config.json')
with open(filename) as f:
    datastore = json.load(f)

name = datastore['user']['name']
pwd = datastore['user']['pwd']

def compare(company,urls):
    client = pymongo.MongoClient()
    repo = client.repo
    repo.authenticate(name, pwd)

    collectionName = company + 'list'
    prevLst = repo[name + '.' + collectionName].find()
    
    lst = []
    for url in urls:
        lst.append(str(url))

    # Debugging only
    # with open(os.path.join(scriptpath, 'debug.txt'), 'w') as d:
    #     for i in lst:
    #         d.write(i)
    #         d.write('\n')

    for i in lst:
        if i not in prevLst:
            repo.drop_collection(collectionName)
            repo.create_collection(collectionName)
            return True
        else:
            return False
