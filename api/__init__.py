# Import flask and template operators
from flask import Flask, request, g, jsonify, send_from_directory
import json
import os
import logging

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import Basic Authentication modules
from flask_httpauth import HTTPBasicAuth

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask(__name__, template_folder=ASSETS_DIR, static_folder=ASSETS_DIR)

auth = HTTPBasicAuth()

# Configurations
cfg = os.environ.get("CFG", "config.Config")

app.config.from_object(cfg)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

@app.before_request
def before_request():
    """
    Converts request data to JSON
    If a request is a POST, PUT, or PATCH, then this method
    will convert the data from binary to JSON and set the
    json_data property on the request
    """
    if request.method in ['POST', 'PUT', 'PATCH']:
        data = request.get_data(as_text=True)
        request.json_data = json.loads(data)

@app.after_request
def add_header(response):
    response.headers['WWW-Authenticate'] = 'xBasic: api'
    return response

app.logger.debug("Registering url test")

def register_controller(controller, endpoint, url, methods=['GET', 'PUT', 'DELETE']):
    """
    Registers a controller with the application
    Args:
        controller (MethodView): The controller class to create
        endpoint (str): The name of the endpoint
        url (str): The url to map
        methods (list):  The HTTP method to map - Defaults to GET, PUT, and DELETE
    """
    app.logger.debug("Registering url %s" % url)
    view_func = controller.as_view(endpoint)
    app.add_url_rule("/api%s" % url, view_func=view_func, methods=methods)

# Import all the controllers so that they can register
from controllers import league

@app.route('/api/token/')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600, 'user': g.user.serialize()})
