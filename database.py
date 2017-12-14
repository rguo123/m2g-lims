import scraper
from pymongo import MongoClient

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

### init MongoDB ###
def init_database():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        # specify database
        db = client.database
        # specify collection
        lims = db.lims
        return lims
    except:
        raise "MongoDB not running."

def build_database():
    scrape = scraper.m2g_scrape('https://m2g.io')
    data = scraper.m2g_data_scrape(scrape)
    lims = init_database()
    for datatype in data.keys():
        for dataset in data[datatype].keys():
            build_dataset(lims, dataset)
            for derivative in data[dataset][datatype].keys():
                links = data[datatype][dataset][derivative]
                build_derivative(lims, dataset, datatype, derivative, links)


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
    for link_list in links:

        link_header = link_list[0]
        url = link_list[1]

        subject = get_subject(link_header)
        update_dataset(lims, dataset, subject)
        # insert  and subject dataype if needed

        lims.update_one(
            filter = {"_id": subject, datatype + "." + derivative: {"$exists": False}},
            update = { "$set": { datatype + "." + derivative: [] }},
            upsert = True
        )
        #insert url to derivative list
        #NOTE: no upsert option exists
        lims.update_one(
            filter = {"_id": subject}, #query
            update = {
                "$push": { datatype + "." + derivative: {url: ""} }
            }
        )

def get_subject(link_header):
    return link_header.split("_")[0]

if __name__ == "__main__":
    build_database()
