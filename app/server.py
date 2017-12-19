import sys
from flask import Flask, flash, render_template, url_for, \
request, redirect
from pymongo import MongoClient

##### init #####
app = Flask(__name__)
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client.m2gdatabase
    lims = db.lims
except:
    raise "Database not running or not built."

'''
    This route just displays all the datasets in the LIMS and
    their respective subject counts. Eveentually can also return other
    useful calculated metadata.
'''
@app.route("/")
def index():
    cursor = lims.find({"subjects" : { "$exists": True}})
    datasets = []
    for doc in cursor:
        datasets.append({doc["_id"]: len(doc["subjects"])})
    return render_template("index.html", datasets = datasets)

@app.route("/dataset_request")
def dataset_request():
    request_id = request.headers.get("id")
    dataset = lims.find_one({"_id": request_id})
    return render_template("table.html")





if __name__ == "__main__":
    app.run(debug = True, port = 5000)
