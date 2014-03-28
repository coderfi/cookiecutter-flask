# -*- coding: utf-8 -*-
import os


class Config(object):
    SECRET_KEY = 'shhhh'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LEVEL = 13
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.

    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_DATABASE = 'flask'
    MONGODB_SLAVE_OKAY = False
    MONGODB_USERNAME = None
    MONGODB_PASSWORD = None

    #see http://www.tornadoweb.org/en/branch2.2/_modules/tornado/httpserver.html
    SERVER_XHEADERS = True
    SERVER_PROCESSES = None #None: disable prefork, 0: auto


class ProdConfig(Config):
    '''Production configuration.'''
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    SERVER_PROCESSES = 0 #start up as many processes as CPU cores


class DevConfig(Config):
    '''Development configuration.'''
    ENV = 'dev'
    DEBUG = True
    DB_NAME = "dev.db"
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}".format(DB_PATH)
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
