

import sys
sys.path.append('src/')

import time
from main import init
from flask import Flask, render_template, request

engine, titles = init()
#pagination
per_page = 10

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', length = 0, time = 0, titles = [])

@app.route("/search", methods = ['GET'])
def response():

    #generation de la réponse
    q = request.args['q']
    start_time = time.time()
    reponse = engine.generateResponse(q, engine.intersect)
    temps = round(time.time() - start_time, 5)
    size_reponse = len(reponse)

    #envoyer juste les 10 premiers résultats
    if per_page < size_reponse:
        pages = reponse[:per_page]
    else:
        pages = reponse

    len_pagination = size_reponse//per_page

    if per_page < len_pagination:
        len_pagination = per_page
    elif size_reponse % 10 != 0:
        len_pagination += 1

    #récuperer les titres à envoyer dans le bon format
    all = [engine.genererLink(titles[id]) for id in pages]
    pages_number = [i+1 for i in range(len_pagination)]

    next = None
    if 2 <= len_pagination:
        next = 2

    return render_template('index.html', q = q, length = size_reponse, time = temps, titles = all, numbers = pages_number, index = 1, next = next)

@app.route("/searchpages", methods = ['GET'])
def pagination():

    try:

        index = int(request.args['page']) - 1
        q = request.args['q']

        #generation de la réponse
        start_time = time.time()
        reponse = engine.generateResponse(q, engine.intersect)
        temps = round(time.time() - start_time, 5)
        size_reponse = len(reponse)

        begin = index*per_page
        end = (index+1)*per_page

        #récuperer les 10 indices prochain liens à envoyer
        pages = reponse[begin:end]

        #mettre à jour les indices de pages
        len_pagination = size_reponse//per_page
        if (index+per_page) < len_pagination:
            len_pagination = index + per_page

        elif size_reponse % 10 != 0:
            len_pagination += 1

        if len_pagination <= index:
            return render_template('index.html', length = 0, time = 0, titles = [])

        pages_number = [i+1 for i in range(index, len_pagination)]
        #récuperer les titres à envoyer dans le bon format
        all = [engine.genererLink(titles[id]) for id in pages]

        next = None
        if 1 < len(pages_number):
            next = index + 2

        return render_template('index.html', q = q, length = size_reponse, time = temps, titles = all, numbers = pages_number, previous = index, index = index + 1, next = next)
    except Exception as e:
        return render_template('index.html', length = 0, time = 0, titles = [])
