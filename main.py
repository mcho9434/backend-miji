from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app Git test 🚅"})

@app.route('/tester')
def index():
    return jsonify({"Choo Choo": "test rioute for tester nest"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
