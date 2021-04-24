from flask import Flask,jsonify, request
import time

app =Flask(__name__)
@app.route("/")
def index():
    return 'Wellcome to saidino app'

@app.route('/bot', methods=['POST','GET'])
def response():
    # recebo o posto mandado por cliente
    # e devolvo para ele o result ai
    query =dict(request.form)['query']
    result = query+" "+time.ctime()
    if request.method=='GET':
        return "SO FAZ POST PARA TER A RESPOSTA"

    return jsonify(result);

# app.run()