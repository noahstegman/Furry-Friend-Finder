from flask import Flask, render_template, request
import requests, requests_cache
from finder import find

requests_cache.install_cache(cache_name='petfinder_cache', backend='sqlite', expire_after=2000)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lookup")
def lookup():
    age = "age=" + request.args.get('age')
    location = "location=" + request.args.get('location')
    distance = "distance=" + request.args.get('distance')
    results = find(location, distance, age)
    
    return render_template("search.html", results=results)