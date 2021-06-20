from flask import Blueprint
from app.models.admin import User


users_bp=Blueprint('users_bp',__name__, url_prefix='/users_page')


@users_bp.route("/")
def index():
    # adm=User.query.all()[0]
    adm="sadino PyProgrammer"
    return f'WELL COME TO USERS BLUEPRINT PAGE <b/>{adm}'
