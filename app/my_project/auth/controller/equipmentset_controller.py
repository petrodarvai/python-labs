from flask import Blueprint, request, jsonify
from ..service.services import EquipmentSetService

equipmentset_bp = Blueprint('equipmentset_bp', __name__)

@equipmentset_bp.route('/', methods=['GET'])
def list_equipmentsets():
    items = EquipmentSetService.list_sets()
    return jsonify([{'SetID': i.SetID, 'SetName': i.SetName, 'Description': i.Description} for i in items])

@equipmentset_bp.route('/<int:id>', methods=['GET'])
def get_equipmentset(id):
    item = EquipmentSetService.get_set(id)
    if not item:
        return jsonify({'message': 'Not found'}), 404
    return jsonify({'SetID': item.SetID, 'SetName': item.SetName, 'Description': item.Description})

@equipmentset_bp.route('/', methods=['POST'])
def create_equipmentset():
    data = request.get_json()
    item = EquipmentSetService.create_set(data)
    return jsonify({'message': 'Created', 'SetID': item.SetID})

@equipmentset_bp.route('/<int:id>', methods=['PUT'])
def update_equipmentset(id):
    data = request.get_json()
    item = EquipmentSetService.update_set(id, data)
    if not item:
        return jsonify({'message': 'Not found'}), 404
    return jsonify({'message': 'Updated'})

@equipmentset_bp.route('/<int:id>', methods=['DELETE'])
def delete_equipmentset(id):
    if not EquipmentSetService.delete_set(id):
        return jsonify({'message': 'Not found'}), 404
    return jsonify({'message': 'Deleted'})
