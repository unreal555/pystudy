#!/bin/py
#   -*-coding:utf-8-*-

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class User(db.Model):  # 表名将会是 user（ 自动生成， 小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份


db.create_all()
# db.drop_all()

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

use1 = User(name='Greyli')
db.session.add(use1)
db.session.commit()
for i in movies:
    movie = Movie(title=i['title'], year=i['year'])
    db.session.add(movie)
    db.session.commit()
