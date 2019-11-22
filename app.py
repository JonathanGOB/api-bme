from flask import Flask
from flask_restful import Resource, Api
import pyodbc

app = Flask(__name__)
api = Api(app)

server = 'tcp:coreiot.database.windows.net'
database = 'esp-data'
username = 'system'
password = 'g9vbqvZjBwU^!9C'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()



class AllCapturedDataDevices(Rescource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(AllCapturedDataDevices, '/AllCapturedData')


if __name__ == '__main__':
    app.run()
