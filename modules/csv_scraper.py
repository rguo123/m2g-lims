import csv
import urllib, urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def get_csv_links(source):
    browser = webdriver.Chrome()
    browser.get(source)
    time.sleep(2)
    html = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
    browser.close()
    soup = BeautifulSoup(html, "lxml")
    csv_links = []
    for link in soup.find_all("a", href = True, text = True):
        # Two checks to guarantee correct link
        if link["href"].find("csv") != -1 and (link.string).find("csv") != -1:
            csv_links.append(link["href"])
    return csv_links

## data_path shoudl have '/' at end
def download_csvs(csv_links, data_path):
    filenames = []
    for link in csv_links:
        filename = data_path + link.split('/')[-1]
        filenames.append(filename)
        urllib.request.urlretrieve(link, filename)
    return filenames

'''
    Returns list of dictionaries where each dictionary contains subject metadata
'''
def parse_csv(filename):
    metadata_list = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        keys = next(reader)
        # remaining lines are subject metadata
        for row in reader:
            metadata = {}
            for i in range(len(row)):
                ## get corresponding key
                if row[i] == "#":
                    break
                metadata[keys[i]] = row[i]
            metadata_list.append(metadata)
    print(metadata_list)
    return metadata_list

if __name__ == "__main__":
    parse_csv("../data/csv/BNU1.csv")
