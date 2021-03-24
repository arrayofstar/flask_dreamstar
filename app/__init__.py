from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()      #使用flask-login验证用户登陆
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)    # 用户登陆

    from .main import main as main_blueprint     #这里引用了main文件下的init中的蓝本，并进行注册
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

