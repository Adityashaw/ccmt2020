"""
Flask main module,
Routes are defined in view.py.
"""

# import os
from flask import Flask
from sassutils.wsgi import SassMiddleware

app = Flask(__name__)

app.wsgi_app = SassMiddleware(
    app.wsgi_app, {"ccmt2020": ("static/sass", "static/css", "static/css")}
)  # noqa: E123

import ccmt2020.views  # noqa: E402, F401
