from flask import Blueprint, request, jsonify
from ..service.services import EquipmentItemService


equipmentitem_bp = Blueprint('equipmentitem_bp', __name__)


@equipmentitem_bp.route('/', methods=['GET'])
def list_items():
    items = EquipmentItemService.list_items()
    return jsonify([{'EquipmentID': i.EquipmentID, 'InventoryNumber': i.InventoryNumber, 'TypeID': i.TypeID, 'SetID': i.SetID, 'StatusID': i.StatusID} for i in items])


@equipmentitem_bp.route('/<int:id>', methods=['GET'])
def get_item(id):
    i = EquipmentItemService.get_item(id)
    if not i:
        return jsonify({'message': 'Item not found'}), 404
    return jsonify({'EquipmentID': i.EquipmentID, 'InventoryNumber': i.InventoryNumber, 'TypeID': i.TypeID, 'SetID': i.SetID, 'StatusID': i.StatusID})


@equipmentitem_bp.route('/', methods=['POST'])
def create_item():
    data = request.get_json()
    i = EquipmentItemService.create_item(data)
    return jsonify({'message': 'Item created', 'EquipmentID': i.EquipmentID})


@equipmentitem_bp.route('/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    i = EquipmentItemService.update_item(id, data)
    if not i:
        return jsonify({'message': 'Item not found'}), 404
    return jsonify({'message': 'Item updated'})


@equipmentitem_bp.route('/<int:id>', methods=['DELETE'])
def delete_item(id):
    if not EquipmentItemService.delete_item(id):
        return jsonify({'message': 'Item not found'}), 404
    return jsonify({'message': 'Item deleted'})