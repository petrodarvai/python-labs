from ..domain.models import EquipmentStatus
from app import db

class EquipmentStatusService:
    @staticmethod
    def list_statuses():
        return EquipmentStatus.query.all()

    @staticmethod
    def get_status(status_id):
        return EquipmentStatus.query.get(status_id)

    @staticmethod
    def create_status(data):
        status = EquipmentStatus(**data)
        db.session.add(status)
        db.session.commit()
        return status

    @staticmethod
    def update_status(status_id, data):
        status = EquipmentStatus.query.get(status_id)
        if not status:
            return None
        for key, value in data.items():
            if hasattr(status, key):
                setattr(status, key, value)
        db.session.commit()
        return status

    @staticmethod
    def delete_status(status_id):
        status = EquipmentStatus.query.get(status_id)
        if not status:
            return False
        db.session.delete(status)
        db.session.commit()
        return True
