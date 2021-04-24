from flask import Flask,jsonify, request
import time

app =Flask(__name__)

@app.route('/bot', methods=['POST'])
def response():
    # recebo o posto mandado por cliente
    # e devolvo para ele o result ai
    query =dict(request.form)['query']
    result = query+" "+time.ctime()

    return jsonify(result);