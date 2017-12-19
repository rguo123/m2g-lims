import csv
import urllib, urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time

SOURCE_URL = "http://m2g.io"

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
    for link in csv_links:
        filename = data_path + link.split('/')[-1]
        urllib.request.urlretrieve(link, filename)

if __name__ == "__main__":
    csv_links = get_csv_links(SOURCE_URL)
    download_csvs(csv_links, "../data/csv/")
