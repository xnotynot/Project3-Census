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
title = "Project 3 - Data and Visualization"
heading = "Insurance Data Analysis"

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_map_url = os.path.join(SITE_ROOT, "static/assets", "FinalData.json")
map_dataJSON = json.load(open(json_map_url))

client = MongoClient(Mongoserver)
db = client["CensusData"]

# Get List of States------------------------------
states = db.states
state_list = [p['STATE'] for p in states.find()]

#total population-------------------------------------
total_population_json = db.popincome_data.aggregate(
    [{"$group": { "_id": "null", "TotalPop": { "$sum": "$Population"}}}])
# Get list of counties
for value in total_population_json:
    total_population = int(value["TotalPop"] / 3)

#Insured Banner---------------------
total_insured_json = db.insurance_data.aggregate([
        {"$group": { "_id": "null", "TotalInsured": { "$sum": "$NIC_PT"}}}])

for value in total_insured_json:
    total_insured = int(value["TotalInsured"] / 3 )
    
#UnInsured Banner----------------------
total_uninsured_json = db.insurance_data.aggregate([
        {"$group": { "_id": "null", "TotalUnInsured": { "$sum": "$NUI_PT"}}}])

for value in total_uninsured_json:
    total_uninsured = int(value["TotalUnInsured"] / 3)

#data gap---------------------
total_unknown = total_population - (total_insured + total_uninsured)

#Plotly Data
total_pop_plotly_df = DataFrame(list(db.popincome_data.aggregate(
    [{"$group": { "_id": "$Year", "TotalPop": { "$sum": "$Population"}}}])))
pop_fig = px.bar(total_pop_plotly_df, x="_id", y="TotalPop", barmode="stack")

total_pinco_plotly_df = DataFrame(list(db.popincome_data.aggregate(
    [{"$group": { "_id": "$Year", "PerCapitaIncome": { "$sum": "$Per Capita Income"}}}])))
pinco_fig = px.bar(total_pinco_plotly_df, x="_id", y="PerCapitaIncome", barmode="stack")

total_pop_plotlyJSON = json.dumps(pop_fig, cls=plotly.utils.PlotlyJSONEncoder)
total_pinco_plotlyJSON = json.dumps(pinco_fig,cls=plotly.utils.PlotlyJSONEncoder)

#Get County GeoJson
counties = db.counties_geocoding
counties_collected = []

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
	return render_template('index.html',a2=a2,states=state_list,t=title,h=heading,
                            total_pop=total_population,
                            total_insured=total_insured,
                            total_uninsured=total_uninsured,
                            total_unknown = total_unknown,
                            total_pop_plotlyJSON = total_pop_plotlyJSON,
                            total_pinco_plotlyJSON=total_pinco_plotlyJSON,
                            map_dataJSON = map_dataJSON)

@app.route('/state', methods=['POST', 'GET'])
def switch_state():
    if request.method == 'POST':
        selected_state = request.form.get('state_pick')
        return render_template('index.html',t=title,h=heading,states=state_list,state_pick=selected_state)

# @app.route("/list")
# def lists ():
# 	#Display the all Tasks
# 	# todos_l = todos.find()
# 	a1="active"
# 	return render_template('index.html',a1=a1,states=state_list,t=title,h=heading)

# @app.route("/completed")
# def completed ():
# 	#Display the Completed Tasks
# 	todos_l = todos.find({"done":"yes"})
# 	a3="active"
# 	return render_template('index.html',a3=a3,todos=todos_l,t=title,h=heading)

# @app.route("/done")
# def done ():
# 	#Done-or-not ICON
# 	id=request.values.get("_id")
# 	task=todos.find({"_id":ObjectId(id)})
# 	if(task[0]["done"]=="yes"):
# 		todos.update_one({"_id":ObjectId(id)}, {"$set": {"done":"no"}})
# 	else:
# 		todos.update_one({"_id":ObjectId(id)}, {"$set": {"done":"yes"}})
# 	redir=redirect_url()	

# 	return redirect(redir)

# @app.route("/action", methods=['POST'])
# def action ():
# 	#Adding a Task
# 	name=request.values.get("name")
# 	desc=request.values.get("desc")
# 	date=request.values.get("date")
# 	pr=request.values.get("pr")
# 	todos.insert_one({ "name":name, "desc":desc, "date":date, "pr":pr, "done":"no"})
# 	return redirect("/list")

# @app.route("/remove")
# def remove ():
# 	#Deleting a Task with various references
# 	key=request.values.get("_id")
# 	todos.delete_one({"_id":ObjectId(key)})
# 	return redirect("/")

# @app.route("/update")
# def update ():
# 	id=request.values.get("_id")
# 	task=todos.find({"_id":ObjectId(id)})
# 	return render_template('update.html',tasks=task,h=heading,t=title)

# @app.route("/action3", methods=['POST'])
# def action3 ():
# 	#Updating a Task with various references
# 	name=request.values.get("name")
# 	desc=request.values.get("desc")
# 	date=request.values.get("date")
# 	pr=request.values.get("pr")
# 	id=request.values.get("_id")
# 	todos.insert_one({"_id":ObjectId(id)}, {'$set':{ "name":name, "desc":desc, "date":date, "pr":pr }})
# 	return redirect("/")

# @app.route("/search", methods=['GET'])
# def search():
# 	#Searching a Task with various references

# 	key=request.values.get("key")
# 	refer=request.values.get("refer")
# 	if(key=="_id"):
# 		todos_l = todos.find({refer:ObjectId(key)})
# 	else:
# 		todos_l = todos.find({refer:key})
# 	return render_template('searchlist.html',todos=todos_l,t=title,h=heading)

if __name__ == "__main__":
    app.run(debug=True)