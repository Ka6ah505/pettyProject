from flask import Flask, jsonify, Response
import json

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'id': 'client',
        'author': 'Sergey Mironov'
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.run(host='0.0.0.0')
