
from . import models
from .server.ws_server import ChatHandler
import asyncio
import tornado.ioloop
import tornado.web
import tornado.httpserver

import threading

asyncio.set_event_loop(asyncio.new_event_loop())
app = tornado.web.Application([
        (r"/chat", ChatHandler),
    ])
http_server = tornado.httpserver.HTTPServer(app)
app.listen(2222)
threading._start_new_thread(tornado.ioloop.IOLoop.instance().start, ())


