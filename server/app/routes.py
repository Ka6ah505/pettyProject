from app import app
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    # user = jsonify({'author': 'Sergey Mironov'})
    user = {'username': 'Sergey Mironov'}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''