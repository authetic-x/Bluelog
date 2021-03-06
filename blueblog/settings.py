import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig(object):

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 280

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)

    BLUEBLOG_EMAIL = os.getenv('BLUELOG_EMAIL')
    BLUEBLOG_POST_PER_PAGE = 10
    BLUEBLOG_MANAGE_POST_PER_PAGE = 15
    BLUEBLOG_COMMENT_PER_PAGE = 15
    BLUE_THEMES = {'perfect_blue':'Perfect Blue', 'black_swan':'Black Swan'}

class DevelopmentConfig(BaseConfig):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.db')

class TestingConfig(BaseConfig):

    TESTING = True
    WTF_CSRF_EABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memeory:'

class ProductionConfig(BaseConfig):

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' +
                                        os.path.join(basedir, 'data.db'))


config = {

    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig

}