from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'author': 'Sergey Mironov'})

app.run(host='0.0.0.0')
