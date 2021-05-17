from flask import Flask,jsonify, request, url_for, render_template
import time
import os

appUrls='https://flaskchatbotmoz.herokuapp.com'

def create_app(*args):
    app =Flask(__name__)
    @app.route("/")
    def index():
        return render_template('index.html')

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
        elif 'image' in query.lower():
            result='thats is saidino image https://flaskchatbotmoz.herokuapp.com/static/image/hacking_tool.png'
        else:
            result='That command have not implemented yet'

        response = result+" \ntime is :"+time.ctime()
        return jsonify(response);
        
    return app


def main():
    app=create_app()
    port=int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0',port=port)

if __name__ == '__main__':
    main()