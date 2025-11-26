from flask import Blueprint, request, jsonify
from ..service.services import LabSessionService


labsession_bp = Blueprint('labsession_bp', __name__)


@labsession_bp.route('/', methods=['GET'])
def list_sessions():
    sessions = LabSessionService.list_sessions()
    return jsonify([{ 'SessionID': s.SessionID, 'SessionDate': s.SessionDate.isoformat(), 'CourseName': s.CourseName, 'Instructor': s.Instructor } for s in sessions])


@labsession_bp.route('/<int:id>', methods=['GET'])
def get_session(id):
    s = LabSessionService.get_session(id)
    if not s:
        return jsonify({'message': 'Session not found'}), 404
    return jsonify({ 'SessionID': s.SessionID, 'SessionDate': s.SessionDate.isoformat(), 'CourseName': s.CourseName, 'Instructor': s.Instructor })


@labsession_bp.route('/', methods=['POST'])
def create_session():
    data = request.get_json()
    s = LabSessionService.create_session(data)
    return jsonify({'message': 'Session created', 'SessionID': s.SessionID})


@labsession_bp.route('/<int:id>', methods=['PUT'])
def update_session(id):
    data = request.get_json()
    s = LabSessionService.update_session(id, data)
    if not s:
        return jsonify({'message': 'Session not found'}), 404
    return jsonify({'message': 'Session updated'})


@labsession_bp.route('/<int:id>', methods=['DELETE'])
def delete_session(id):
    if not LabSessionService.delete_session(id):
        return jsonify({'message': 'Session not found'}), 404
    return jsonify({'message': 'Session deleted'})


@labsession_bp.route('/<int:id>/students', methods=['GET'])
def session_students(id):
    students = LabSessionService.get_session_students(id)
    return jsonify([{'StudentID': s.StudentID, 'FullName': s.FullName} for s in students])