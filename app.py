from flask import Flask, request, jsonify, abort, make_response, url_for
from flask_restful import Api, Resource, reqparse, fields, marshal
from datetime import datetime
import pyodbc
import json
import config

app = Flask(__name__)
api = Api(app)

class AzureSQLDatabase(object):
    connection = None
    cursor = None

    def __init__(self):
        self.connection = pyodbc.connect(config.CONN_STRING)
        self.cursor = self.connection.cursor()

    def query(self, query, params):
        return self.cursor.execute(query, params)

    def commit(self):
        return self.connection.commit()

    def __del__(self):
        self.connection.close()

deviceData_fields = {
    'device_id': fields.String,
    'pressure': fields.Integer,
    'temperature': fields.String,
    'humidity': fields.String,
    'timestamp': fields.DateTime,
    'uri': fields.Url('CapturedData')
}

def myconverter(o):
    return o.__str__()

class CapturedDataDevices(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('device_id', type=str, required=False)
        self.reqparse.add_argument('pressure', type=str, required=False)
        self.reqparse.add_argument('temperature', type=str, required=False)
        self.reqparse.add_argument('timestamp', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'), required=False)
        self.reqparse.add_argument('humidity', type=str, required=False)
        super(CapturedDataDevices, self).__init__()

    def get(self):
        try:
            conn = AzureSQLDatabase()
            args = self.reqparse.parse_args()
            if any(v is not None for v in args.values()):
                self.key = None
                for (key, value) in args.items():
                    if value:
                        self.key = key
                query = "SELECT * FROM CaptureData WHERE {0} = ?".format(self.key)
                cursor = conn.query(
                    query, args[self.key])
            elif all(v is None for v in args.values()):
                params = []
                cursor = conn.query(
                    "SELECT * FROM CaptureData", params)
            columns = [column[0] for column in cursor.description]
            deviceData = []
            for row in cursor.fetchall():
                deviceData.append(dict(zip(columns, row)))

            return {
                'message': 'Succes', 'Data' : marshal(deviceData, deviceData_fields)
            }


        except Exception as e:
            return {'error': str(e)}

    def post(self):
        try:
            args = self.reqparse.parse_args()
            #data = request.get_json(force=True)

            captureData = {
                'device_id': args['device_id'],
                'pressure': args['pressure'],
                'temperature': args['temperature'],
                'timestamp': myconverter(args['timestamp']),
                'humidity': args['humidity']
            }

            conn = AzureSQLDatabase()
            conn.query("insert into CaptureData (device_id, pressure, temperature, timestamp, humidity) values (?, ?, ?, ?, ?)", [captureData['device_id'], captureData['pressure'], captureData['temperature'], captureData['timestamp'], captureData['humidity']])
            conn.commit()

            return {
                'Message' : 'Succes', 'captureData': captureData
            }, 201

        except Exception as e:
            return {'error': str(e)}

api.add_resource(CapturedDataDevices, '/Api/V1/CapturedData', endpoint='CapturedData')


if __name__ == '__main__':
    app.run()
