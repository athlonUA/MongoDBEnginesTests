import sys
import pymongo
import datetime

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.testEngines
collection = db.insertOperation

if len(sys.argv) > 1:
    numberDocuments = int(sys.argv[1])

    try:
        array = []
        for i in range(0, numberDocuments):
            array.append({'i': i})

        ts = datetime.datetime.now()

        collection.insert_many(array)

        tf = datetime.datetime.now()
        te = tf - ts
        print te
    except Exception as e:
        print "insert failed:", e

