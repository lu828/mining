#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle

from .connection import connection_app
from .cube import cube_app
from .element import element_app
from .dashboard import dashboard_app
from .user import user_app
from .group import group_app
from .filter import filter_app


api_app = Bottle()
api_app.mount('/connection', connection_app)
api_app.mount('/cube', cube_app)
api_app.mount('/element', element_app)
api_app.mount('/dashboard', dashboard_app)
api_app.mount('/user', user_app)
api_app.mount('/group', group_app)
api_app.mount('/filter', filter_app)


@api_app.route('/')
def index():
    return 'OpenMining API!'
