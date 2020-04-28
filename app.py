

import sys
sys.path.append('src/')

import time
from main import init
from flask import Flask, render_template, request

engine, titles = init()
#pagination
per_page = 10

app = Flask(__name__)

#pagination per_page
def getPagination(index, reponse, size_reponse, per_page=per_page):
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

    return pages, len_pagination


#generation de la réponse
def getResponse(request):

    q = request.args['q']
    opt = request.args['opt']
    f = request.args['f']
    start_time = time.time()
    reponse = engine.fusion_not(engine.generateResponse(q, engine.options[opt]), engine.generateResponse(f, engine.merge))
    temps = round(time.time() - start_time, 5)
    size_reponse = len(reponse)

    return q, opt, f, reponse, temps, size_reponse

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', length = 0, time = 0, titles = [])

@app.route("/search", methods = ['GET'])
def response():

    #reponse
    q, opt, f, reponse, temps, size_reponse = getResponse(request)

    #envoyer juste les 10 premiers résultats
    pages, len_pagination = getPagination(0, reponse, size_reponse)

    #récuperer les titres à envoyer dans le bon format
    all = [engine.genererLink(titles[id]) for id in pages]
    pages_number = [i+1 for i in range(len_pagination)]

    next = None
    if 2 <= len_pagination:
        next = 2

    return render_template('index.html', q = q, length = size_reponse, time = temps, titles = all, numbers = pages_number, index = 1, next = next, opt = opt, f = f)

@app.route("/searchpages", methods = ['GET'])
def pagination():

    try:
        #index pour la pagination
        index = int(request.args['page']) - 1

        #reponse
        q, opt, f, reponse, temps, size_reponse = getResponse(request)

        #recuperer les prochains indices et pages à envoyer
        pages, len_pagination = getPagination(index, reponse, size_reponse)

        if len_pagination <= index:
            return render_template('index.html', length = 0, time = 0, titles = [])

        pages_number = [i+1 for i in range(index, len_pagination)]
        #récuperer les titres à envoyer dans le bon format
        all = [engine.genererLink(titles[id]) for id in pages]

        next = None
        if 1 < len(pages_number):
            next = index + 2

        return render_template('index.html', q = q, length = size_reponse, time = temps, titles = all, numbers = pages_number, previous = index, index = index + 1, next = next, opt = opt, f = f)

    except Exception as e:
        return render_template('index.html', length = 0, time = 0, titles = [])
