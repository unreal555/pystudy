#!/bin/py
#   -*-coding:utf-8-*-
# set FLASK_ENV=development
# set FLASK_ENV=my_app
from flask import Flask
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

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


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.context_processor
def inject_name():
    name = User.query.first()
    return dict(name=name.name)


@app.context_processor
def inject_movies():
    movies = Movie.query.all()
    return dict(movies=movies)
