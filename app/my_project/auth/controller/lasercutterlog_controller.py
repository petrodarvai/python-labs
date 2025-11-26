from flask import Blueprint, request, jsonify
from ..service.services import LaserCutterLogService


lasercutterlog_bp = Blueprint('lasercutterlog_bp', __name__)


@lasercutterlog_bp.route('/', methods=['GET'])
def list_laser_logs():
    logs = LaserCutterLogService.list_logs()
    return jsonify([{'LaserLogID': l.LaserLogID, 'StudentID': l.StudentID, 'ProjectID': l.ProjectID, 'StartTime': l.StartTime.isoformat(), 'EndTime': l.EndTime.isoformat(), 'DurationMinutes': l.DurationMinutes} for l in logs])


@lasercutterlog_bp.route('/<int:id>', methods=['GET'])
def get_laser_log(id):
    l = LaserCutterLogService.get_log(id)
    if not l:
        return jsonify({'message': 'Log not found'}), 404
    return jsonify({'LaserLogID': l.LaserLogID, 'StudentID': l.StudentID, 'ProjectID': l.ProjectID, 'StartTime': l.StartTime.isoformat(), 'EndTime': l.EndTime.isoformat(), 'DurationMinutes': l.DurationMinutes})


@lasercutterlog_bp.route('/', methods=['POST'])
def create_laser_log():
    data = request.get_json()
    l = LaserCutterLogService.create_log(data)
    return jsonify({'message': 'Log created', 'LaserLogID': l.LaserLogID})


@lasercutterlog_bp.route('/<int:id>', methods=['PUT'])
def update_laser_log(id):
    data = request.get_json()
    l = LaserCutterLogService.update_log(id, data)
    if not l:
        return jsonify({'message': 'Log not found'}), 404
    return jsonify({'message': 'Log updated'})


@lasercutterlog_bp.route('/<int:id>', methods=['DELETE'])
def delete_laser_log(id):
    if not LaserCutterLogService.delete_log(id):
        return jsonify({'message': 'Log not found'}), 404
    return jsonify({'message': 'Log deleted'})
