import scraper
from pymongo import MongoClient

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
def build_derivative(lims, datatype, derivative, links):
    for link_list in links:
        subject = get_subject(links[0])
        lims.
