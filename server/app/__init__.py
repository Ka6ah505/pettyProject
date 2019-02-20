from flask import Flask, jsonify, Response
import json

app = Flask(__name__)
auth = HTTPBasicAuth()
users = {
    #login:password
    'john': 'hi',
    'susan': 'bye'
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/', methods=['GET'])
@auth.login_required
def index():
    base = Engine()
    data = base.getPerson(id=1)

    data = {
        'id': 'client',
        'author': 'Sergey Mironov'
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
