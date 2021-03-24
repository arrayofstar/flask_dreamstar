import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'      # 表单相关的
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.126.com')              # 发送邮件相关的
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'False').lower() in \
        ['true', 'on', '1']
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'True').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','mengfan_1993@126.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','EEIYDFVNQLMXVXWA')
    FLASKY_MAIL_SUBJECT_PREFIX = '[繁星之歌制作]'
    FLASKY_MAIL_SENDER = '繁星之歌 Admin <mengfan_1993@126.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN','574503706@qq.com')

    SQLALCHEMY_TRACK_MODIFICATIONS = False    #以便在不需要根据对象变化的时降低内存消耗

    @staticmethod
    def init_app(app):
        pass

#数据库相关的
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

#数据库相关的
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

#数据库相关的
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}