from flask import Flask, render_template,request,redirect,url_for, flash # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
from bson.json_util import dumps
from config import Mongoserver
import os
import json
import plotly
import plotly.express as px

from pandas import DataFrame

app = Flask(__name__)
title = "Project 3 - Leaflet Visualizer"
heading = "State and County Info"

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_map_url = os.path.join(SITE_ROOT, "static/assets", "FinalData.json")
map_dataJSON = json.load(open(json_map_url))


def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')

@app.route("/")
# @app.route("/uncompleted")
def tasks ():
	#Display the Uncompleted Tasks
	#counties_l = counties.find({"state_id":"PA"})
	a2="active"
	return render_template('countyMap.html',
                                map_dataJSON = map_dataJSON)

if __name__ == "__main__":
    app.run(debug=True)