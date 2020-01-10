# -*- coding: utf-8 -*-
import datetime
import os
import logging
# from odoo import models,api
import urllib.parse
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.websocket import WebSocketHandler
from tornado.options import define, options
define("port", default=2222, type=int)


class ChatHandler(WebSocketHandler):

    # users = set()  # 用来存放在线用户的容器
    users_dict = {}  # 用来存放在线用户的容器

    def get_uid(self):
        urlparse = urllib.parse.urlparse(self.request.uri)
        qs = urllib.parse.parse_qs(urlparse.query)
        uid = qs.get('uid')[0]
        return uid

    def open(self):
        # self.users.add(self)  # 建立连接后添加用户到容器中
        uid = self.get_uid()
        self.users_dict[uid] = self  # 建立连接后添加用户到容器中
        print('当前所有用户字典==》》》》', self.users_dict)
        for k, v in self.users_dict.items():
            v.write_message(
                u"[%s号小妖精]-[%s]-进入聊天室" % (uid, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def on_message(self, message):
        uid = self.get_uid()
        for k, v in self.users_dict.items():  # 向在线用户广播消息
            v.write_message(u"[%s号小妖精]-[%s]-说：%s" % (uid, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

    def on_close(self):
        # self.users.remove(self) # 用户关闭连接后从容器中移除用户
        uid = self.get_uid()
        self.users_dict.pop(uid)
        for k, v in self.users_dict.items():
            v.write_message(
                u"[%s号小妖精]-[%s]-离开聊天室" % (uid, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
            (r"/chat", ChatHandler),
        ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

