"""db.py: connect to Postgres database and create tables"""
import os

from flask import Flask

# create the flask application & connect to db)
app = Flask(__name__, 
            template_folder = os.path.join(os.getcwd(), 'templates'), 
            static_folder=os.path.join(os.getcwd(), 'static'))
