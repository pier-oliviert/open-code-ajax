#coding: utf-8

from wtforms import Form, BooleanField, TextField, validators


class TodoForm(Form):
    title = TextField('title', [validators.Length(min=1, max=100)])
    done = BooleanField('Done')
