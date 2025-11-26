from flask import Blueprint, request, jsonify
from ..service.services import StaffService


staff_bp = Blueprint('staff_bp', __name__)


@staff_bp.route('/', methods=['GET'])
def list_staff():
    staff_list = StaffService.list_staff()
    return jsonify([{'StaffID': s.StaffID, 'FullName': s.FullName, 'Role': s.Role} for s in staff_list])


@staff_bp.route('/<int:id>', methods=['GET'])
def get_staff(id):
    s = StaffService.get_staff(id)
    if not s:
        return jsonify({'message': 'Staff not found'}), 404
    return jsonify({'StaffID': s.StaffID, 'FullName': s.FullName, 'Role': s.Role})


@staff_bp.route('/', methods=['POST'])
def create_staff():
    data = request.get_json()
    s = StaffService.create_staff(data)
    return jsonify({'message': 'Staff created', 'StaffID': s.StaffID})


@staff_bp.route('/<int:id>', methods=['PUT'])
def update_staff(id):
    data = request.get_json()
    s = StaffService.update_staff(id, data)
    if not s:
        return jsonify({'message': 'Staff not found'}), 404
    return jsonify({'message': 'Staff updated'})


@staff_bp.route('/<int:id>', methods=['DELETE'])
def delete_staff(id):
    if not StaffService.delete_staff(id):
        return jsonify({'message': 'Staff not found'}), 404
    return jsonify({'message': 'Staff deleted'})