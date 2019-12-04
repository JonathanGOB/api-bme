from flask import Flask, request, jsonify, abort, make_response, url_for
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_cors import CORS
import CapturedDataDevices
import Devices

app = Flask(__name__)
cors = CORS(app, resources={r"/api/V1/*": {"origins": "*"}})
api = Api(app)

api.add_resource(CapturedDataDevices.CapturedDataDevices, '/Api/V1/CapturedData', endpoint='CapturedData')
api.add_resource(Devices.Devices, '/Api/V1/Devices', endpoint='Devices')

if __name__ == '__main__':
    app.run()
