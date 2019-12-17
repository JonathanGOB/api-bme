from flask_restful import Api, Resource
from flask import render_template, make_response, send_from_directory


class Graph(Resource):
    def __init__(self):
        pass

    def get(self):
        return send_from_directory('__vue__/dist', 'index.html')
