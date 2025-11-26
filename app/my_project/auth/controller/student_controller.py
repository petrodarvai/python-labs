# ================================================
# Контролери для всіх таблиць, по окремих файлах
# ================================================

# student_controller.py
from flask import Blueprint, request, jsonify
from ..service.services import StudentService

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/', methods=['GET'])
def list_students():
    students = StudentService.list_students()
    return jsonify([{
        'StudentID': s.StudentID,
        'FullName': s.FullName,
        'Email': s.Email,
        'GroupName': s.GroupName,
        'Phone': s.Phone
    } for s in students])

@student_bp.route('/<int:id>', methods=['GET'])
def get_student(id):
    s = StudentService.get_student(id)
    if not s:
        return jsonify({'message': 'Student not found'}), 404
    return jsonify({
        'StudentID': s.StudentID,
        'FullName': s.FullName,
        'Email': s.Email,
        'GroupName': s.GroupName,
        'Phone': s.Phone
    })

@student_bp.route('/', methods=['POST'])
def create_student():
    data = request.get_json()
    s = StudentService.create_student(data)
    return jsonify({'message': 'Student created', 'StudentID': s.StudentID})

@student_bp.route('/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    s = StudentService.update_student(id, data)
    if not s:
        return jsonify({'message': 'Student not found'}), 404
    return jsonify({'message': 'Student updated'})

@student_bp.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    if not StudentService.delete_student(id):
        return jsonify({'message': 'Student not found'}), 404
    return jsonify({'message': 'Student deleted'})

@student_bp.route('/<int:id>/projects', methods=['GET'])
def student_projects(id):
    projects = StudentService.get_student_projects(id)
    return jsonify([{'ProjectID': p.ProjectID, 'ProjectName': p.ProjectName} for p in projects])

@student_bp.route('/<int:id>/sessions', methods=['GET'])
def student_sessions(id):
    sessions = StudentService.get_student_sessions(id)
    return jsonify([{'SessionID': s.SessionID, 'CourseName': s.CourseName} for s in sessions])


# project_controller.py
from flask import Blueprint, request, jsonify
from ..service.services import ProjectService

project_bp = Blueprint('project_bp', __name__)

@project_bp.route('/', methods=['GET'])
def list_projects():
    projects = ProjectService.list_projects()
    return jsonify([{
        'ProjectID': p.ProjectID,
        'ProjectName': p.ProjectName,
        'Description': p.Description
    } for p in projects])

@project_bp.route('/<int:id>', methods=['GET'])
def get_project(id):
    p = ProjectService.get_project(id)
    if not p:
        return jsonify({'message': 'Project not found'}), 404
    return jsonify({
        'ProjectID': p.ProjectID,
        'ProjectName': p.ProjectName,
        'Description': p.Description
    })

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


