from flask import Blueprint, request, jsonify
from ..service.services import SessionStudentsService


sessionstudents_bp = Blueprint('sessionstudents_bp', __name__)


@sessionstudents_bp.route('/', methods=['GET'])
def list_session_students():
    records = SessionStudentsService.list_records()
    return jsonify([{'SessionID': r.SessionID, 'StudentID': r.StudentID} for r in records])


@sessionstudents_bp.route('/', methods=['POST'])
def create_session_student():
    data = request.get_json()
    r = SessionStudentsService.create_record(data)
    return jsonify({'message': 'Record created', 'SessionID': r.SessionID, 'StudentID': r.StudentID})


@sessionstudents_bp.route('/<int:session_id>/<int:student_id>', methods=['DELETE'])
def delete_session_student(session_id, student_id):
    if not SessionStudentsService.delete_record(session_id, student_id):
        return jsonify({'message': 'Record not found'}), 404
    return jsonify({'message': 'Record deleted'})