from flask import Blueprint, request, jsonify
from ..service.equipmenttype_service import EquipmentTypeService

equipmenttype_bp = Blueprint('equipmenttype_bp', __name__)

@equipmenttype_bp.route('/', methods=['GET'])
def list_types():
    items = EquipmentTypeService.list_types()
    return jsonify([{'TypeID': i.TypeID, 'TypeName': i.TypeName} for i in items])

@equipmenttype_bp.route('/<int:id>', methods=['GET'])
def get_type(id):
    item = EquipmentTypeService.get_type(id)
    if not item:
        return jsonify({'message': 'Not found'}), 404
    return jsonify({'TypeID': item.TypeID, 'TypeName': item.TypeName})

@equipmenttype_bp.route('/', methods=['POST'])
def create_type():
    data = request.get_json()
    item = EquipmentTypeService.create_type(data)
    return jsonify({'message': 'Created', 'TypeID': item.TypeID})

@equipmenttype_bp.route('/<int:id>', methods=['PUT'])
def update_type(id):
    data = request.get_json()
    item = EquipmentTypeService.update_type(id, data)
    if not item:
        return jsonify({'message': 'Not found'}), 404
    return jsonify({'message': 'Updated'})

@equipmenttype_bp.route('/<int:id>', methods=['DELETE'])
def delete_type(id):
    if not EquipmentTypeService.delete_type(id):
        return jsonify({'message': 'Not found'}), 404
    return jsonify({'message': 'Deleted'})
