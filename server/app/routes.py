from app import app
from flask import jsonify, render_template

@app.route('/')
@app.route('/index')
def index():
    # user = jsonify({'author': 'Sergey Mironov'})
    user = {'username': 'Sergey Mironov'}
    return render_template('index.html', title='Test App', user=user)
