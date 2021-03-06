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

    # use the LB/proxy's X-REAL-IP and X-SCHEME and X-FORWARDED-PROTO
    # and X-FORWARDED-FOR
    SERVER_XHEADERS = True

    # number of pre fork processes
    # None: disable prefork
    # 0: auto (number of cpu cores)
    # Note: if running behind a proxy like NGINX or APACHE
    # it is probably better to disable prefork
    # i.e. explicitly run N separate Tornado instances
    # behind the proxy
    SERVER_PROCESSES = None
    

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
