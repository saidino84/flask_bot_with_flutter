from flask import Flask,jsonify, request
import time

appUrls='https://flaskchatbotmoz.herokuapp.com',
app =Flask(__name__)
@app.route("/")
def index():
    return 'Wellcome to saidino app'

routa2='https://flaskchatbotmoz.herokuapp.com/bot'
@app.route('/bot', methods=['POST','GET'])
def response():
    print(request.method)
    if request.method=='GET':
        return jsonify({'method':request.method,'info':'fizeste um GET por isso esta tendo esta resposta queira entao fazer um POST?'})
    # recebo o posto mandado por cliente
    # e devolvo para ele o result + a hora que este response foi feita
    query =dict(request.form)['query']
    result='comando nao reconhecido'
    if 'name' in query:
        result='my name is saidinoBot from python'

    result = result+" \ntime is :"+time.ctime()
    

    return jsonify(result);

app.run(debug=True)