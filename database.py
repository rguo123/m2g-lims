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


def build_dataset(db):
    pass


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

        # insert if needed
        lims.update_one(
            filter = {_id: subject}, #query
            update = { "$setOnInsert": { datatype: { derivative: {} } } },
            upsert = True
        )
        #insert url to derivative list
        #NOTE: no upsert option exists
        lims.update_one(
            filter = {_id: subject}, #query
            update = {
                "$push": { datatype + "." + derivative: {url: ""} }
            }
        )

def upsert_dataset(lims, dataset, subject):
    # add subject to proper dataset
    lims.update_one(
        filter = {_id: dataset},
        update = { "addToSet": {}}
    )



def get_subject(link_header):
    return link_header.split("_")[0]
