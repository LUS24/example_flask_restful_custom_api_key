from flask_restful import Resource, reqparse
# Reqparse se va a cambiar por marshmallow
from flask_jwt import jwt_required
from models.device import DeviceModel


class AddDevice(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'device_name',
        type=str,
        required=True
        )
    parser.add_argument(
        'user_id',
        type=int,
        required=True
        )

    @jwt_required()
    def post(self):
        
        data = AddDevice.parser.parse_args()

        if DeviceModel.find_by_name(data["device_name"]):
            return {'message': "A device with name '{}' already exists.".format(data["device_name"])}, 400

        new_device = DeviceModel(**data)
        new_device.save_to_db()

        # DeviceModel.find_by_name(data["device_name"]).json(), 201

        return  {"api_key": new_device.device_key}, 201