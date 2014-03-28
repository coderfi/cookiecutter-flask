# -*- coding: utf-8 -*-

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import DevConfig, ProdConfig

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
# from tornado import autoreload

import os
import sys

if os.environ.get("{{cookiecutter.app_name}}_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)


def main(argv=None):
    port = 5000

    print("Listening on 0.0.0.0:%d" % port)
    http_server = HTTPServer(WSGIContainer(app))
    http_server.bind(port)
    #Pre-forks N child process, where N is number of cpu cores
    http_server.start()
    IOLoop.instance().start()

    return 0

if __name__ == '__main__':
    sys.exit(main())
