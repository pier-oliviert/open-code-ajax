#coding: utf8

from flask import Flask, render_template, request, make_response

from models import connect
from models.todo import Todo
from forms.todo import TodoForm

# from formalchemy import FieldSet

todos = Flask(__name__)


@todos.route('/', methods=['GET', 'POST'])
def list():
    """
        Le listing et le formulaire d'ajout de todo
    """
    db_session = connect(True)
    form = TodoForm()

    # GET de base pour obtenir les TODOS au départ
    data = {
        "todos": db_session.query(Todo).filter_by(done=0).all(),
        "form": form
    }

    return render_template("list.html", **data)


@todos.route('/create', methods=['PUT'])
def create():
    # Controller de création d'un todo avec un PUT

    form = TodoForm(request.form)

    if request.method == 'PUT' and form.validate():
        db_session = connect(True)
        newTodo = Todo()
        newTodo.title = form.title.data
        newTodo.done = False

        db_session.add(newTodo)
        db_session.commit()

        todo_data = {
            "id": newTodo.id,
            "title": newTodo.title,
            "done": newTodo.done
        }

        data = {
            "form": form,
            "todo_html": render_template(
                "todo.html",
                **todo_data
            ).replace("\n", "")
        }

        js_response = make_response(
            render_template("list.js", **data).replace("\n", "")
        )
        js_response.headers["Content-Type"] = "text/javascript; charset=utf-8"

        return js_response

    return "", 404


@todos.route('/done/<pk>', methods=['DELETE'])
def done(pk):
    # Controller pour rendre un TODO fait avec un post

    if pk:
        db_session = connect(True)
        current_todo = db_session.query(Todo).filter_by(id=pk).first()

        current_todo.done = True
        db_session.commit()

        data = {
            "id": pk
        }

        js_response = make_response(
            render_template("done.js", **data).replace("\n", "")
        )
        js_response.headers["Content-Type"] = "text/javascript; charset=utf-8"
        return js_response

    return "", 402
