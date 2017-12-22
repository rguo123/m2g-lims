# m2g-lims
Laboratory Information Management System for m2g.io data.

# Installation:
## Prequisites:
Have Google Chrome or Chromium installed.  
Have Python3.6 and pip3 package manager installed.

## Setup
1. Clone this repository
2. In cloned repository, run 'pip3 install -r requirements.txt' in terminal.
3. Install MongoDB ([Instructions](https://docs.mongodb.com/manual/installation/))
4. Download [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.34/).
5. Add ChromeDriver to your system PATH. [Tutorial](http://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/)

## Database Setup (see [Dataset Registration](https://nbviewer.jupyter.org/github/rguo123/m2g-lims/blob/master/docs/Dataset_Registration.ipynb))
3. Run 'mkdir data/db/' in cloned git repository.
4. In new terminal window, run: 'mongod --dbpath path/to/git/repo/data/db/'
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
