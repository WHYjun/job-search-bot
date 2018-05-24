# -*- coding: utf-8 -*-
import pymongo
import json
import os.path


def compare(company, jobs):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'config.json')
    with open(filename) as f:
        datastore = json.load(f)

    client = pymongo.MongoClient()
    repo = client.repo

    collectionName = company + 'list'
    try:
        prevLst = repo[collectionName].find_one()
        prevLst = prevLst['lst']
    except:
        prevLst = []

    for job in jobs:
        if job not in prevLst:
            repo.drop_collection(collectionName)
            repo.create_collection(collectionName)
            dic = {}
            dic['lst'] = jobs
            repo[collectionName].insert(dic)
            return True
    return False
