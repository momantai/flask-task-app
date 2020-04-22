"""
    A traves de este archivo configuraremos nuestros modelos, nuestras base de datos, servidor de correos, etc.
"""
from decouple import config

class Config:
    SECRET_KEY = 'clavex'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:prueba@localhost/project_web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:prueba@localhost/project_web_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

config = {
    'development': DevelopmentConfig,
    'defualt': DevelopmentConfig,
    'test': TestConfig
}