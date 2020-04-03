#!/bin/py
#   -*-coding:utf-8-*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def return_username(username):
    return 'username is %s'%username

