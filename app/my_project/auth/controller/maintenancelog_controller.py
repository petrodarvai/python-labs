from flask import Blueprint, request, jsonify
from ..service.services import MaintenanceLogService


maintenancelog_bp = Blueprint('maintenancelog_bp', __name__)


@maintenancelog_bp.route('/', methods=['GET'])
def list_maint_logs():
    logs = MaintenanceLogService.list_logs()
    return jsonify([{'MaintenanceID': l.MaintenanceID, 'EquipmentID': l.EquipmentID, 'StaffID': l.StaffID, 'StartDate': l.StartDate.isoformat(), 'EndDate': l.EndDate.isoformat() if l.EndDate else None, 'Description': l.Description} for l in logs])


@maintenancelog_bp.route('/<int:id>', methods=['GET'])
def get_maint_log(id):
    l = MaintenanceLogService.get_log(id)
    if not l:
        return jsonify({'message': 'Log not found'}), 404
    return jsonify({'MaintenanceID': l.MaintenanceID, 'EquipmentID': l.EquipmentID, 'StaffID': l.StaffID, 'StartDate': l.StartDate.isoformat(), 'EndDate': l.EndDate.isoformat() if l.EndDate else None, 'Description': l.Description})


@maintenancelog_bp.route('/', methods=['POST'])
def create_maint_log():
    data = request.get_json()
    l = MaintenanceLogService.create_log(data)
    return jsonify({'message': 'Log created', 'MaintenanceID': l.MaintenanceID})


@maintenancelog_bp.route('/<int:id>', methods=['PUT'])
def update_maint_log(id):
    data = request.get_json()
    l = MaintenanceLogService.update_log(id, data)
    if not l:
        return jsonify({'message': 'Log not found'}), 404
    return jsonify({'message': 'Log updated'})


@maintenancelog_bp.route('/<int:id>', methods=['DELETE'])
def delete_maint_log(id):
    if not MaintenanceLogService.delete_log(id):
        return jsonify({'message': 'Log not found'}), 404
    return jsonify({'message': 'Log deleted'})