import os

class DefaultConfig(object):

    PROJECT = "Hello Shopify"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = True
    TESTING = False

    SECRET_KEY = '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'

    SERVER_NAME = "localhost:8069"
    PREFERRED_URL_SCHEME = "https"

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/helloshopify.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    SHOPIFY_API_KEY = '2586b57d4e9aaf315e5a68c1cd81d006'
    SHOPIFY_SHARED_SECRET = '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'