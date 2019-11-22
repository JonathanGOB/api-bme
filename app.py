from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import json
import pyodbc

app = Flask(__name__)
api = Api(app)

server = 'tcp:dc6-iotdb-server.database.windows.net,1433'
database = 'device-website'
username = 'dc6admin'
password = 'Sy4c0Fqz'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()



class AllCapturedDataDevices(Resource):
    def get(self):
        returndata = []
        cursor.execute(
            "SELECT * FROM CapturedData")
        if(cursor.fetchall):
            for row in cursor.fetchall():
                returndata.append(row)
            return {'message': 'Succes', 'Data' : returndata}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('device_id', required = True)
        parser.add_argument('pressure', required=True)
        parser.add_argument('temperature', required=True)
        parser.add_argument('humidity', required=True)
        parser.add_argument('timestamp', required=True)

        args = parser.parse_args()
        return {'Message' : 'Succes', 'Data' : args}
        cursor.execute("insert into CaptureData values (?)", (json.dump(args),))
        cursor.commit

api.add_resource(AllCapturedDataDevices, '/AllCapturedData')


if __name__ == '__main__':
    app.run()
