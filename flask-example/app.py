#coding: utf8

from flask import Flask, render_template

todos = Flask(__name__)

@todos.route('/', methods = ['GET'])
def list():
    # Controller du listing des TODOS
    return render_template("list.html")

@todos.route('/create', methods = ['PUT'])
def create():
    # Controller de création d'un todo avec un PUT
    return "create"

@todos.route('/done', methods = ['POST'])
def done():
    # Controller pour rendre un TODO fait avec un post
    return "done"