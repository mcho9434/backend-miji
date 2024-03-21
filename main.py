from flask import Flask, jsonify
import psycopg
import os

app = Flask(__name__)

# chrome://net-internals/#sockets

@app.route('/')
def index():
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


@app.route('/tester')
def fixer():
    return jsonify({"Choo Choo": "test rioute for tester nest","servicepass":"test"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
