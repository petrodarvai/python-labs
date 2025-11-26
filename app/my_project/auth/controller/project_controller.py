from flask import Blueprint, request, jsonify
from ..service.services import ProjectService


project_bp = Blueprint('project_bp', __name__)


@project_bp.route('/', methods=['GET'])
def list_projects():
    projects = ProjectService.list_projects()
    return jsonify([{ 'ProjectID': p.ProjectID, 'ProjectName': p.ProjectName, 'Description': p.Description } for p in projects])


@project_bp.route('/<int:id>', methods=['GET'])
def get_project(id):
    p = ProjectService.get_project(id)
    if not p:
        return jsonify({'message': 'Project not found'}), 404
    return jsonify({ 'ProjectID': p.ProjectID, 'ProjectName': p.ProjectName, 'Description': p.Description })


@project_bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    p = ProjectService.create_project(data)
    return jsonify({'message': 'Project created', 'ProjectID': p.ProjectID})


@project_bp.route('/<int:id>', methods=['PUT'])
def update_project(id):
    data = request.get_json()
    p = ProjectService.update_project(id, data)
    if not p:
        return jsonify({'message': 'Project not found'}), 404
    return jsonify({'message': 'Project updated'})


@project_bp.route('/<int:id>', methods=['DELETE'])
def delete_project(id):
    if not ProjectService.delete_project(id):
        return jsonify({'message': 'Project not found'}), 404
    return jsonify({'message': 'Project deleted'})


@project_bp.route('/<int:id>/students', methods=['GET'])
def project_students(id):
    students = ProjectService.get_project_students(id)
    return jsonify([{'StudentID': s.StudentID, 'FullName': s.FullName} for s in students])