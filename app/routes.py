from flask import render_template
from app import app
from app.graphql import query
from app.utils import deep_get

@app.route('/')
@query('index')
def index(data):
    return render_template('index.html', data=data)

@app.route('/fonts/<slug>')
@query('font')
def font(data, slug=None):
    if not deep_get(data, 'viewer.slug.fontCollection'):
        return not_found()

    return render_template('font.html', data=data)

@app.route('/<slug>')
@query('page')
def page(data, slug=None):
    if not deep_get(data, 'viewer.slug.page'):
        return not_found()

    return render_template('page.html', data=data)


def not_found():
    return render_template('404.html'), 404
