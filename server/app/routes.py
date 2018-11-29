from app import app
from flask import jsonify, render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    # user = jsonify({'author': 'Sergey Mironov'})
    user = {'username': 'Sergey Mironov'}
    return render_template('index.html', title='Test App', user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
