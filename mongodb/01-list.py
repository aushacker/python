import pymongo

from pymongo import MongoClient

client = MongoClient()

for db in client.list_databases():
  print(db)

db = client.local

for c in db.list_collections():
  print(c)
