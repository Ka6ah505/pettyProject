from app import app
from flask import jsonify, render_template,flash, redirect
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    # user = jsonify({'author': 'Sergey Mironov'})
    user = {'username': 'Sergey Mironov'}
    return render_template('index.html', title='Test App', user=user)


@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me {}'. fromat(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
