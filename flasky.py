import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role, Permission, Post


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission, Post=Post)


# @app.cli.command()
# @click.argument('test_names', nargs=-1)
# def test(test_names):
#     """Run the unit tests."""
#     import unittest
#     if test_names:
#         tests = unittest.TestLoader().loadTestsFromNames(test_names)
#     else:
#         tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    # app = create_app('development')
    # app_context = app.app_context()
    # app_context.push()
    # db.drop_all()  #删除数据库-如果有
    # db.create_all()     #创建数据库-如果没有
    # admin_role = Role(name='Admin')
    # mod_role = Role(name='Moderator')
    # user_role = Role(name='User')
    # user_john= User(username='test',role=admin_role)
    # db.session.add(admin_role)
    # db.session.add(mod_role)
    # db.session.add(user_role)
    # db.session.add(user_john)
    # #测试用户登陆
    # u = User(email='574503706@qq.com',username='mengfan',password='1234')
    # db.session.add(u)
    # db.session.commit()
    # admin_role.name = 'Administrator'
    # db.session.add(admin_role)
    # db.session.commit()
    # Role.insert_roles()
    # Role.query.all()
    # app.run(port=8000,debug=1)
    app.run(host='0.0.0.0', port=5000, debug=1)    #需要本地访问的话，就需要修改防火墙高级设置，在人站规则中添加端口号



