from flask_restful import Api, Resource, reqparse, fields, marshal
import AzureSQLDatabase

deviceData_fields = {
    'device_id': fields.String
}

class Devices(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('device_id', type=str, required=False)
        super(Devices, self).__init__()

    def get(self):
        try:
            conn = AzureSQLDatabase.AzureSQLDatabase()
            args = self.reqparse.parse_args()
            params = []
            if args['device_id'] != None:
                query = "SELECT device_id FROM CaptureData GROUP BY device_id WHERE {0}".format(args['device_id'])
            else:
                query = "SELECT device_id FROM CaptureData GROUP BY device_id"
            cursor = conn.query(
                query, params)

            columns = [column[0] for column in cursor.description]
            deviceData = []
            for row in cursor.fetchall():
                deviceData.append(dict(zip(columns, row)))

            return {
                'message': 'Succes', 'Data': marshal(deviceData, deviceData_fields)
            }, 201

        except Exception as e:
           return {'error': str(e)}