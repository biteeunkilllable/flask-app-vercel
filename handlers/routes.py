from flask import render_template
from modules import modules

def configure_routes(app):
    @app.route("/")
    def index():
        hello = modules.hello()
        content = modules.content()
        return content
