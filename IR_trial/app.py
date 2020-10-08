from flask import Flask, redirect, url_for, request
from flask import render_template
from main import run
from main import runOne
from flask import json
from urllib import parse
from flask_cors import CORS
# from json import jsonify
app = Flask(__name__)
CORS(app)
def decode(a):
    result = parse.unquote(a)
    return result


@app.route('/search/<name>', methods=['GET', 'OPTIONS']) 
def returnResult(name):
    word = decode(name)
    result = run(word)
    res = json.jsonify(result)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

@app.route('/searchone/<id>') 
def returnOneResult(id): 
    result = runOne(id)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
