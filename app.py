

import sys
sys.path.append('src/')

import time
from main import init
from flask import Flask, render_template, request

engine, titles = init()
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', length = 0, time = 0, titles = [])

@app.route("/search", methods = ['GET'])
def response():
    start_time = time.time()
    q = request.args['search']
    response = engine.generateResponse(q, engine.merge)
    temps = round(time.time() - start_time, 4)
    return render_template('index.html', q = q ,length=len(response),time = temps, titles = [engine.genererLink(titles[id]) for id in response])
