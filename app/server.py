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
    their respective subject counts. Eventually can also return other
    useful calculated metadata.
'''
@app.route("/")
def index():
    cursor = lims.find({"subjects" : { "$exists": True}})
    datasets = []
    for doc in cursor:
        datasets.append({doc["_id"]: len(doc["subjects"])})
    return render_template("index.html", datasets = datasets)

@app.route("/lims_id_request")
def lims_request():
    request_id = request.headers.get("id")
    if (request_id.find("sub-") != -1):
        return url_for("subject", subject_id = request_id)
    else:
        return url_for("dataset", dataset_id = request_id)

@app.route("/dataset")
def dataset():
    dataset_id = request.args.get("dataset_id")
    dataset = lims.find_one({"_id": dataset_id})
    subjects = dataset["subjects"]
    return render_template("dataset_table.html", dataset_id = dataset_id, subjects = subjects)

@app.route("/subject")
def subject():
    subject_id = request.args.get("subject_id")
    subject = lims.find_one({"_id": subject_id})
    # get rid of ID so easier to process derivatives
    subject.pop("_id")
    return render_template("subject_table.html", subject_id = subject_id, subject = subject)


if __name__ == "__main__":
    app.run(debug = True, port = 5000)
