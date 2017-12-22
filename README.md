# m2g-lims
Laboratory Information Management System for m2g.io data.

# Installation:
## Setup
1. Clone this repository
2. pip3 install -r requirements.txt
3. Install MongoDB ([Instructions](https://docs.mongodb.com/manual/installation/))
4. Download [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.34/) and move it into your path.
## Database Setup (see [Dataset Registration](https://nbviewer.jupyter.org/github/rguo123/m2g-lims/blob/master/docs/Dataset_Registration.ipynb))
3. mkdir data/db/
4. In new terminal window, run: 'mongod --dbpath data/db/'
5. Go into modules directory and run: 'python3 database.py'

## API Setup (see [API Documentation](https://nbviewer.jupyter.org/github/rguo123/m2g-lims/blob/master/docs/API_Documentation.ipynb))
1. Go into app directory
2. Run 'python3 server.py'
3. Open http://localhost:5000/


## Documentation:
[WEB Scraping](https://nbviewer.jupyter.org/github/rguo123/m2g-lims/blob/master/docs/Web_Scraper.ipynb)  
[CSV Scraping](https://nbviewer.jupyter.org/github/rguo123/m2g-lims/blob/master/docs/CSV_Scraper.ipynb)  
[Dataset Registration](https://nbviewer.jupyter.org/github/rguo123/m2g-lims/blob/master/docs/Dataset_Registration.ipynb)  
[LIMS API / Data Querying](https://nbviewer.jupyter.org/github/rguo123/m2g-lims/blob/master/docs/API_Documentation.ipynb)  
