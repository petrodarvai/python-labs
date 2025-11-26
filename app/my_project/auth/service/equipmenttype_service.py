from ..domain.models import EquipmentType
from app import db

class EquipmentTypeService:
    @staticmethod
    def list_types():
        return EquipmentType.query.all()

    @staticmethod
    def get_type(type_id):
        return EquipmentType.query.get(type_id)

    @staticmethod
    def create_type(data):
        t = EquipmentType(**data)
        db.session.add(t)
        db.session.commit()
        return t

    @staticmethod
    def update_type(type_id, data):
        t = EquipmentType.query.get(type_id)
        if not t:
            return None
        for k, v in data.items():
            if hasattr(t, k):
                setattr(t, k, v)
        db.session.commit()
        return t

    @staticmethod
    def delete_type(type_id):
        t = EquipmentType.query.get(type_id)
        if not t:
            return False
        db.session.delete(t)
        db.session.commit()
        return True
