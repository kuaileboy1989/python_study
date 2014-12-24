#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

urls = (
        '/(.*)','hello'
        )

app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello,'+name+'!'

application = app.wsgifunc()
