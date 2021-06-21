from flask import Blueprint,render_template,request
from app.models.admin import User


users_bp=Blueprint('users_bp',__name__, url_prefix='/users_page',static_folder='static',template_folder='templates')


@users_bp.route("/")
def index():
    users=User.query.all()
    # adm="sadino PyProgrammer"
    return render_template('home.html',users=users, users_size=len(users))

@users_bp.route('/add',methods=['POST','GET'])
def add():
    if request.method=='POST':
        print('added')
    else:
        return render_template('add.html'), 200
