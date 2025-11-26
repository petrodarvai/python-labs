from flask import Blueprint, request, jsonify
from ..service.services import StudentProjectsService


studentprojects_bp = Blueprint('studentprojects_bp', __name__)


@studentprojects_bp.route('/', methods=['GET'])
def list_student_projects():
    records = StudentProjectsService.list_records()
    return jsonify([{'StudentID': r.StudentID, 'ProjectID': r.ProjectID} for r in records])


@studentprojects_bp.route('/', methods=['POST'])
def create_student_project():
    data = request.get_json()
    r = StudentProjectsService.create_record(data)
    return jsonify({'message': 'Record created', 'StudentID': r.StudentID, 'ProjectID': r.ProjectID})


@studentprojects_bp.route('/<int:student_id>/<int:project_id>', methods=['DELETE'])
def delete_student_project(student_id, project_id):
    if not StudentProjectsService.delete_record(student_id, project_id):
        return jsonify({'message': 'Record not found'}), 404
    return jsonify({'message': 'Record deleted'})