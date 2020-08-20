from flask import render_template, url_for
from app import app
from app import config
from app.graphql import query
from app.utils import deep_get

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/')
@query('index')
@query('layout', 'layout_data')
def index(data, layout_data):
    return render_template('index.html', data=data, layout_data=layout_data)

@app.route('/fonts/<slug>')
@query('font')
@query('layout', 'layout_data')
def font(data, layout_data, slug=None):
    if not deep_get(data, 'viewer.slug.fontCollection'):
        return not_found()

    return render_template('font.html', data=data, layout_data=layout_data)

@app.route('/<slug>')
@query('page')
@query('layout', 'layout_data')
def page(data, layout_data, slug=None):
    if not deep_get(data, 'viewer.slug.page'):
        return not_found()

    return render_template('page.html', data=data, layout_data=layout_data)


def not_found():
    return render_template('404.html'), 404

@app.context_processor
def context_processor():
    return {'fontdue_url': config.FONTDUE_URL}
