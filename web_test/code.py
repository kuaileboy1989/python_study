#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

render = web.template.render('temp/')

urls = (
        '/(.*)','index'
        )

class index:
    def GET(self, name):
        print render.index(name)
        return render.index(name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

