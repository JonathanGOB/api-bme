from flask import Flask
from flask import request


app = Flask(__name__)


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
