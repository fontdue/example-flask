from flask import render_template
from app import app
from app.graphql import query

@app.route('/')
@query('index')
def index(data={}):
    return render_template('index.html', title='Home', data=data)

@app.route('/fonts/<id>')
@query('font')
def font(data={}, id=id):
    return render_template('font.html', data=data)
