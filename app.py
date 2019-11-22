from flask import Flask
from flask_restful import Resource, Api
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


api.add_resource(AllCapturedDataDevices, '/AllCapturedData')


if __name__ == '__main__':
    app.run()
