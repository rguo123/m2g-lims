.. NeuroData LIMS documentation master file, created by
   sphinx-quickstart on Sun Oct 15 23:15:51 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to NeuroDataDesign-AVATR LIMS's documentation!
================================================

1. Clone annotation repo. In Terminal type:
    ``git clone https://github.com/rguo123/m2g-lims.git``

2. Install dependences by typing: ``pip3 install -r requirements.txt``

3. Scrape m2g for the data by typing: ``python3 modules/scraper.py``

4. Start the MongoDB server by typing ``mongod --dbpath path/to/db``, where path/to/DB is the path to you database folder.
An example could be ``mongod --dbpath ~/Envs/NDD/m2g-lims/DB/``:

5. Start the LIMS server by typing ``python server.py``.

6. Navigate to ``http://localhost:5000`` in a web browser.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
