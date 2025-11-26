# app/my_project/auth/controller/equipmentstatus_controller.py
from flask import Blueprint, request, jsonify
from ..service.equipmentstatus_service import EquipmentStatusService

equipmentstatus_bp = Blueprint('equipmentstatus_bp', __name__)

@equipmentstatus_bp.route('/', methods=['GET'])
def list_statuses():
    items = EquipmentStatusService.list_statuses()
    return jsonify([{'StatusID': i.StatusID, 'StatusName': i.StatusName} for i in items])

@equipmentstatus_bp.route('/<int:id>', methods=['GET'])
def get_status(id):
    item = EquipmentStatusService.get_status(id)
    if not item:
        return jsonify({'message': 'Not found'}), 404
    return jsonify({'StatusID': item.StatusID, 'StatusName': item.StatusName})

@equipmentstatus_bp.route('/', methods=['POST'])
def create_status():
    data = request.get_json()
    item = EquipmentStatusService.create_status(data)
    return jsonify({'message': 'Created', 'StatusID': item.StatusID})

@equipmentstatus_bp.route('/<int:id>', methods=['PUT'])
def update_status(id):
    data = request.get_json()
    item = EquipmentStatusService.update_status(id, data)
    if not item:
        return jsonify({'message': 'Not found'}), 404
    return jsonify({'message': 'Updated'})

@equipmentstatus_bp.route('/<int:id>', methods=['DELETE'])
def delete_status(id):
    if not EquipmentStatusService.delete_status(id):
        return jsonify({'message': 'Not found'}), 404
    return jsonify({'message': 'Deleted'})
