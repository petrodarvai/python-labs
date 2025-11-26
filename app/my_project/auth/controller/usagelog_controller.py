from flask import Blueprint, request, jsonify


usagelog_bp = Blueprint('usagelog_bp', __name__)


@usagelog_bp.route('/', methods=['GET'])
def list_usage_logs():
    logs = UsageLogService.list_logs()
    return jsonify([{'UsageID': l.UsageID, 'StudentID': l.StudentID, 'EquipmentID': l.EquipmentID, 'ProjectID': l.ProjectID, 'StaffID': l.StaffID, 'CheckOutTime': l.CheckOutTime.isoformat(), 'ReturnTime': l.ReturnTime.isoformat() if l.ReturnTime else None} for l in logs])


@usagelog_bp.route('/<int:id>', methods=['GET'])
def get_usage_log(id):
    l = UsageLogService.get_log(id)
    if not l:
        return jsonify({'message': 'Log not found'}), 404
    return jsonify({'UsageID': l.UsageID, 'StudentID': l.StudentID, 'EquipmentID': l.EquipmentID, 'ProjectID': l.ProjectID, 'StaffID': l.StaffID, 'CheckOutTime': l.CheckOutTime.isoformat(), 'ReturnTime': l.ReturnTime.isoformat() if l.ReturnTime else None})


@usagelog_bp.route('/', methods=['POST'])
def create_usage_log():
    data = request.get_json()
    l = UsageLogService.create_log(data)
    return jsonify({'message': 'Log created', 'UsageID': l.UsageID})


@usagelog_bp.route('/<int:id>', methods=['PUT'])
def update_usage_log(id):
    data = request.get_json()
    l = UsageLogService.update_log(id, data)
    if not l:
        return jsonify({'message': 'Log not found'}), 404
    return jsonify({'message': 'Log updated'})


@usagelog_bp.route('/<int:id>', methods=['DELETE'])
def delete_usage_log(id):
    if not UsageLogService.delete_log(id):
        return jsonify({'message': 'Log not found'}), 404
    return jsonify({'message': 'Log deleted'})