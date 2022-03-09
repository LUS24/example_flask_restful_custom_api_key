from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.device import DeviceModel


class AddDevice(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'device_name',
        type=str,
        required=True
        )

    @jwt_required()
    def post(self):
        data = AddDevice.parser.parse_args()
        name = data["device_name"]

        if DeviceModel.find_by_name(data["device_name"]):
            return {'message': f"A device with name '{name}' already exists."}, 400

        new_device = DeviceModel(
            device_name=name,
            user_id=current_identity.id
        )
        new_device.save_to_db()

        return  {"api_key": new_device.device_key}, 201