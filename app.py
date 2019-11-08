from flask import Flask
from flask import request
import pyodbc

app = Flask(__name__)

server = 'tcp:coreiot.database.windows.net'
database = 'esp-data'
username = 'system'
password = 'g9vbqvZjBwU^!9C'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


@app.route('/api/v1/sensors',  methods = ['GET'])
def sensor():
    if request.method == 'GET':
        sensor = request.args.get('sensorname')
        return sensor

@app.route('/')
def hello():
    return 'hello world'

if __name__ == '__main__':
    app.run()
