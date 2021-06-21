from flask import Flask, jsonify, request, url_for, render_template
from flask_migrate import Migrate
import time
import os
import random
from modulos import get_current_directory



appUrls = 'https://flaskchatbotmoz.herokuapp.com'


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(os.path.dirname(__file__), 'dados.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.db import init_db
    init_db(app)
    Migrate(app,app.db)

    from app.models.admin import User
    from app.views.users.bp_users import users_bp
    app.register_blueprint(users_bp, url_prefix='/users_page')

    @app.route("/", methods=['GET', 'POST'])
    def index():

        # clie = User(username='admin', email='admin@example.com')
        # db.session.add(admin)
        # db.session.commit()
        # print(algo)
        return render_template('index.html')

    routa2 = 'https://flaskchatbotmoz.herokuapp.com/bot'

    # @app.shell_context_processor
    # def make_shell_context():
    #     # com isto aki posso entrar no shell e fazer testes esporatico
    #     '''
        # db.create_all()  >> criare o banco
    #     '''
        # return dict(app=app, db=app.db, User=User)

    @app.route('/bot', methods=['POST', 'GET'])
    def response():
        print(request.method)
        if request.method == 'GET':
            return jsonify({'method': request.method, 'info': 'fizeste um GET por isso esta tendo esta resposta queira entao fazer um POST?'})
        # recebo o posto mandado por cliente
        # e devolvo para ele o result + a hora que este response foi feita
        query = dict(request.form)['query']
        result = 'comando nao reconhecido'
        if 'name' in query:
            result = 'my name is saidinoBot from python'
        elif 'image' in query.lower():
            result = 'thats is saidino image https://flaskchatbotmoz.herokuapp.com/static/image/hacking_tool.png'
        else:
            result = 'That command have not implemented yet'

        response = result+" \ntime is :"+time.ctime()
        return jsonify(response)

    return app


def main():
    app = create_app()
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
