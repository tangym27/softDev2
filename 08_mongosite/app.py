# Team MONGOnificient: Michelle Tang & Jabir Chowdhury & Sarar Aseer
# Softdev pd6
# K#08: Ay Mon, Go Git It From Yer Flask
# 2019-03-07

import os

from flask import Flask, request, render_template, session, redirect

from util import nobelprize

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def __init__():
    return  render_template('index.html')

@app.route('/process' , methods = ["POST"])
def __process__():
    ip = request.form.get("ip")
    nobelprize.rebuild(ip)
    return  render_template('query.html' , data = [])

@app.route('/query' , methods = ["POST"])
def __query__():
    query = request.form.get('topic')
    type = request.form.get("type")
    if type == "year":
        lst = nobelprize.find_year(query)
    elif type == "category":
        lst = nobelprize.find_category(query)
    else:
        lst = nobelprize.find_topic(query)
    return render_template('query.html', data = lst)

if __name__ == "__main__":
    app.debug = True
    app.run()
