from flask import Flask, redirect, url_for, request
from flask import render_template
from main import run
from main import runOne
from flask import json
from urllib import parse
# from json import jsonify
app = Flask(__name__)


def decode(a):
    result = parse.unquote(a)
    return result


@app.route('/search/<name>') 
def returnResult(name):
    word = decode(name)
    result = run(word)
    return json.jsonify(result)

@app.route('/searchone/<id>') 
def returnOneResult(id): 
    result = runOne(id)
    return result


if __name__ == '__main__':
    app.run(debug=True)
