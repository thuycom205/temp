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

    SHOPIFY_API_KEY = '41cc66f3cc07c532af628efc01459a47'
    SHOPIFY_SHARED_SECRET = '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'