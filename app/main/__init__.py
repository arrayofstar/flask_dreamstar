from flask import Blueprint

main = Blueprint('main', __name__)    #main指蓝本所在的包（文件夹）


from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)