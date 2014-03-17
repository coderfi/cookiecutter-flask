# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
from flask import Flask, render_template, json
from flask_debugtoolbar import DebugToolbarExtension

from {{cookiecutter.app_name}}.settings import ProdConfig
from {{cookiecutter.app_name}}.assets import assets
from {{cookiecutter.app_name}}.extensions import (db, login_manager, migrate,
                                                  dbm, cache)
from {{cookiecutter.app_name}} import public, user, task

from bson import ObjectId

def create_app(config_object=ProdConfig):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_customjsonencoder(app)
    return app


def register_extensions(app):
    db.init_app(app)
    dbm.init_app(app)
    login_manager.init_app(app)
    assets.init_app(app)
    if app.config['DEBUG_TB_ENABLED']:
        DebugToolbarExtension(app)
    cache.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(task.views.blueprint)
    return None


def register_errorhandlers(app):
    def render_error(error):
        return render_template("{0}.html".format(error.code)), error.code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


class ObjectIdJSONEncoder(json.JSONEncoder):
    """ If a ``bson.ObjectId`` return it as the hex string equivalent """"
    def default(self, obj):
        try:
            if isinstance(obj, ObjectId):
                return str(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return json.JSONEncoder.default(self, obj)


def register_customjsonencoder(app):
    app.json_encoder = ObjectIdJSONEncoder
