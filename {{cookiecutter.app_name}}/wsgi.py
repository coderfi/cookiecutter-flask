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
    http_server = HTTPServer(WSGIContainer(app),
                             xheaders=app.config.get('SERVER_XHEADERS', False))
                             
    processes = app.config.get('SERVER_PROCESSES', 0)
    if processes is not None:
        # Pre-forks N child process, where N is number of cpu cores
        http_server.bind(port)
        http_server.start(processes)
    else:
        http_server.listen(port)
        
    IOLoop.instance().start()

    return 0

if __name__ == '__main__':
    sys.exit(main())
