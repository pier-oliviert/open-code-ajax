#coding: utf8

from flask import Flask, render_template, request

from models import connect
from models.todo import Todo

from formalchemy import FieldSet

todos = Flask(__name__)

@todos.route('/', methods = ['GET', 'POST'])
def list():
    """
        Le listing et le formulaire d'ajout de todo
    """
    db_session = connect(True)
    
    data = {
        "todos" : db_session.query(Todo).all()
        , "form" : FieldSet(Todo)
    }

    if request.method == 'POST':
        form = FieldSet(Todo, data = request.form)

        if form.validate():
            form.sync()
            db_session.commit()

    return render_template("list.html", **data)

@todos.route('/create', methods = ['PUT'])
def create():
    # Controller de création d'un todo avec un PUT
    return "create"

@todos.route('/done', methods = ['POST'])
def done():
    # Controller pour rendre un TODO fait avec un post
    return "done"