# -*- coding: utf-8 -*-
import asyncio
import json
import logging
import os
import time
from datetime import datetime

from aiohttp import web

logging.basicConfig(level=logging.INFO)

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

async def init(loop):
    # define a webAPP:
    app = web.Application(loop=loop)
    # add get method:
    app.router.add_route('GET', '/', index)
    # create a web service using async coroutine:
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    #  set the log info:
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
    
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
