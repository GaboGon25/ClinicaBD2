from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from flask_session import Session
from flask import Flask
from models import db
# clase de Integrity Error
from sqlalchemy.exc import IntegrityError
# importaciones para login
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import requests

app= Flask(__name__)
app.config.from_object(Config)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

db.init_app(app)

#configuraciones para logearse
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

if __name__ == '__main__':
    app.run(debug=True) 
