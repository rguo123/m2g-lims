import scraper
from pymongo import MongoClient
import pickle
import csv_scraper

'''
SCHEMA:
Dataset:
{
    _id = dataset_name
    _subjects = [list of subject document ids]
}

Subject:
{
    _id = subject id
    datatype = {
        derivative: {
            {link : neuroglancer link},
            {link : neuroglancer link},
            ...
        }
    }
}

'''
## tracker
scan_count = 0

### DATA_DIRECTORY
SOURCE_URL = "http://m2g.io"
DATA_PATH = "../data/csv/"

### init MongoDB ###
def init_database():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        # specify database
        db = client.m2gdatabase
        # specify collection
        lims = db.lims
        return lims
    except:
        raise "MongoDB not running."

def build_database():
    #scrape = scraper.m2g_scrape('https://m2g.io')
    #data = scraper.m2g_data_scrape(scrape)
    data = pickle.load(open("../data/tmp/data.pickle", "rb"))
    lims = init_database()
    for datatype in data.keys():
        for dataset in data[datatype].keys():
            build_dataset(lims, dataset)
            for derivative in data[datatype][dataset].keys():
                ## ignore graph QA plots since not subject based
                ## TODO: think of fix for this
                if (derivative == "QA.graphs"):
                    continue
                links = data[datatype][dataset][derivative]
                build_derivative(lims, dataset, datatype, derivative, links)
    #build_metadata()


def build_dataset(lims, dataset):
    lims.update_one(
        filter = {"_id": dataset},
        update = {"$setOnInsert": { "subjects": [] }},
        upsert = True
    )

def update_dataset(lims, dataset, subject):
    lims.update_one(
        filter = {"_id": dataset},
        update = {"$addToSet": { "subjects": subject }}
    )

'''
    lims: MongoDB collection
    datatype: fMRI or DWI
    derivative: Aligned Images, Tensors, Fibers...
    links: list of lists formatted as [[link_header, link], [link_header, link], ...]
'''
def build_derivative(lims, dataset, datatype, derivative, links):

    global scan_count
    for link_list in links:
        scan_count += 1
        link_header = link_list[0]
        ## invalid parse
        ## TODO: get better fix
        if (link_header.find("sub") < 0 or link_header.find("_") < 0):
            continue
        url = encode_url(link_list[1])

        subject = get_subject(link_header)
        update_dataset(lims, dataset, subject)
        # insert  and subject dataype if needed

        write_result = lims.update_one(
            filter = {"_id": subject},
            update = {"$setOnInsert": { datatype + "." + derivative: [{url: ""}]}},
            upsert = True
        )

        if (write_result.upserted_id is not None):
            print("Upsert and added Scan #" + str(scan_count))
            continue

        lims.update_one(
            filter = {"_id": subject, datatype + "." + derivative: {"$exists": False}},
            update = { "$set": { datatype + "." + derivative: [] }},
        )
        #insert url to derivative list
        #NOTE: no upsert option exists
        lims.update_one(
            filter = {"_id": subject}, #query
            update = {
                "$push": { datatype + "." + derivative: {url: ""} }
            }
        )
        print("Added Scan #" + str(scan_count))


def build_metadata():
    ## Get metadata CSV
    try:
        links = get_csv_links(SOURCE_URL)
        filenames = download_csvs(links, DATA_PATH)
        metadata_list = parse_csv(filenames)
    except:
        raise "Could not access/download CSVs"

    for metadata in metadata_list:
        subid = metadata.pop("SUBID")
        for key, value in metadata.items():
            try:
                lims.update_one(
                    filter = {"_id": "sub-" + subid},
                    update = {"$set": {"metadata." + key: value}}
                )
            except:
                raise "Error adding metadata"


def get_subject(link_header):
    return link_header.split("_")[0]

def encode_url(url):
    return url.replace(".", "$$$")

def decode_url(encoded_url):
    return encoded_url.replace("$$$", ".")

if __name__ == "__main__":
    build_database()
