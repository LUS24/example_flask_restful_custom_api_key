from db import db
import uuid

class DeviceModel(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key = True)
    device_name = db.Column(db.String(80))
    device_key = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel', back_populates="devices")

    def __init__(self, device_name, user_id):
        self.device_name = device_name
        self.user_id = user_id
        self.create_key()
    
    def create_key(self):
        self.device_key = str(uuid.uuid4())

    def json(self):
        return {'device_name': self.device_name, 'device_key': self.device_key, 'user_id': self.user_id}

    @classmethod
    def find_by_name(cls, device_name):
        return cls.query.filter_by(device_name=device_name).first()

    @classmethod
    def find_by_device_key(cls, device_key):
        return cls.query.filter_by(device_key=device_key).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()