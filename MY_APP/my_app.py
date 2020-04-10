#!/bin/py
#   -*-coding:utf-8-*-
# set FLASK_ENV=development
# set FLASK_ENV=my_app
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

name = 'GreyLi'
movies = [
    {'title': 'MyNeighborTotoro', 'year': '1988'},
    {'title': 'DeadPoetsSociety', 'year': '1989'},
    {'title': 'APerfectWorld', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'SwallowtailButterfly', 'year': '1996'},
    {'title': 'KingofComedy', 'year': '1999'},
    {'title': 'DevilsontheDoorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'ThePorkofMusic', 'year': '2012'},
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', name=name, movies=movies)
