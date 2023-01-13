# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:32:44 2023

@author: mato
"""

from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect , session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,FileField
from wtforms.widgets import PasswordInput
from wtforms.validators import DataRequired, Email
import email_validator
from collections import Counter
import re
from dash import Dash, dcc, html


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'
dash_app = Dash(
    __name__,
    server=app,
    url_base_pathname='/yourprofile/EDA/'
)

@app.route('/')
def test_boot( ):
   return render_template('welcome.html', title="GeoIA")


class NameForm(FlaskForm):
    name = StringField('Username', validators=[ DataRequired() ])
    password = StringField('Password', widget=PasswordInput(hide_value=False))
    submit = SubmitField("Submit")
    
class FileForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField("Submit")


@app.route('/sign/', methods=['GET', 'POST'])
def sign():
    global name
    name = None
    global password
    password =None
    global form
    form = NameForm()
    if form.validate_on_submit():
       name = form.name.data    
       password = form.password.data 
       session['name']= name

       print(session['name'] )
       return redirect(url_for("yourprofile"))
    # Gérer les valeurs saisies
    return render_template("sign.html", form=form, name=name, password=password)


@app.route('/yourprofile/',methods=['GET', 'POST'])
def yourprofile():
   form = FileForm()
   if form.validate_on_submit():
       uploaded_file = form.file.data
       if uploaded_file.filename != '':
           uploaded_file.save( uploaded_file.filename)
   # Faire le traitement sur le fichier
   return render_template("yourprofile.html", form=form,title="GeoIA")


@app.route('/project/',methods=['GET', 'POST'])
def project():
   # Faire le traitement sur le fichier
   return render_template("project.html", title="GeoIA")


dash_app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])
    
])




# Run le dashboard sur le server http://127.0.0.1:5000/
if __name__ == "__main__":
    app.run(debug=True) #♣mode debug pour modifier et mettre a jour en même temps