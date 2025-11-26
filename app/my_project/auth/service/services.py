from app import db
from ..domain.models import *

# ---------------- Student Service ----------------
class StudentService:
    @staticmethod
    def list_students():
        return Student.query.all()

    @staticmethod
    def get_student(student_id):
        return Student.query.get(student_id)

    @staticmethod
    def create_student(data):
        s = Student(**data)
        db.session.add(s)
        db.session.commit()
        return s

    @staticmethod
    def update_student(student_id, data):
        s = Student.query.get(student_id)
        if not s:
            return None
        for key, value in data.items():
            if hasattr(s, key):
                setattr(s, key, value)
        db.session.commit()
        return s

    @staticmethod
    def delete_student(student_id):
        s = Student.query.get(student_id)
        if not s:
            return False
        db.session.delete(s)
        db.session.commit()
        return True

    @staticmethod
    def get_student_projects(student_id):
        s = Student.query.get(student_id)
        if s:
            return s.projects
        return []

    @staticmethod
    def get_student_sessions(student_id):
        s = Student.query.get(student_id)
        if s:
            return s.sessions
        return []


# ---------------- Project Service ----------------
class ProjectService:
    @staticmethod
    def list_projects():
        return Project.query.all()

    @staticmethod
    def get_project(project_id):
        return Project.query.get(project_id)

    @staticmethod
    def create_project(data):
        p = Project(**data)
        db.session.add(p)
        db.session.commit()
        return p

    @staticmethod
    def update_project(project_id, data):
        p = Project.query.get(project_id)
        if not p:
            return None
        for key, value in data.items():
            if hasattr(p, key):
                setattr(p, key, value)
        db.session.commit()
        return p

    @staticmethod
    def delete_project(project_id):
        p = Project.query.get(project_id)
        if not p:
            return False
        db.session.delete(p)
        db.session.commit()
        return True

    @staticmethod
    def get_project_students(project_id):
        p = Project.query.get(project_id)
        if p:
            return p.students
        return []

# ---------------- LabSession Service ----------------
class LabSessionService:
    @staticmethod
    def list_sessions():
        return LabSession.query.all()

    @staticmethod
    def get_session(session_id):
        return LabSession.query.get(session_id)

    @staticmethod
    def create_session(data):
        s = LabSession(**data)
        db.session.add(s)
        db.session.commit()
        return s

    @staticmethod
    def update_session(session_id, data):
        s = LabSession.query.get(session_id)
        if not s:
            return None
        for key, value in data.items():
            if hasattr(s, key):
                setattr(s, key, value)
        db.session.commit()
        return s

    @staticmethod
    def delete_session(session_id):
        s = LabSession.query.get(session_id)
        if not s:
            return False
        db.session.delete(s)
        db.session.commit()
        return True

    @staticmethod
    def get_session_students(session_id):
        s = LabSession.query.get(session_id)
        if s:
            return s.students
        return []

# ---------------- Equipment Services ----------------
class EquipmentItemService:
    @staticmethod
    def list_items():
        return EquipmentItem.query.all()

    @staticmethod
    def get_item(item_id):
        return EquipmentItem.query.get(item_id)

    @staticmethod
    def create_item(data):
        e = EquipmentItem(**data)
        db.session.add(e)
        db.session.commit()
        return e

    @staticmethod
    def update_item(item_id, data):
        e = EquipmentItem.query.get(item_id)
        if not e:
            return None
        for key, value in data.items():
            if hasattr(e, key):
                setattr(e, key, value)
        db.session.commit()
        return e

    @staticmethod
    def delete_item(item_id):
        e = EquipmentItem.query.get(item_id)
        if not e:
            return False
        db.session.delete(e)
        db.session.commit()
        return True

# ---------------- EquipmentSet Service ----------------
class EquipmentSetService:
    @staticmethod
    def list_sets():
        return EquipmentSet.query.all()

# ---------------- EquipmentStatus Service ----------------
class EquipmentStatusService:
    @staticmethod
    def list_status():
        return EquipmentStatus.query.all()

# ---------------- EquipmentType Service ----------------
class EquipmentTypeService:
    @staticmethod
    def list_types():
        return EquipmentType.query.all()

# ---------------- Staff Service ----------------
class StaffService:
    @staticmethod
    def list_staff():
        return Staff.query.all()

    @staticmethod
    def get_staff(staff_id):
        return Staff.query.get(staff_id)

    @staticmethod
    def delete_staff(staff_id):
        s = Staff.query.get(staff_id)
        if not s:
            return False
        db.session.delete(s)
        db.session.commit()
        return True

# ---------------- MaintenanceLog Service ----------------
class MaintenanceLogService:
    @staticmethod
    def list_logs():
        return MaintenanceLog.query.all()

# ---------------- LaserCutterLog Service ----------------
class LaserCutterLogService:
    @staticmethod
    def list_logs():
        return LaserCutterLog.query.all()

# ---------------- UsageLog Service ----------------
class UsageLogService:
    @staticmethod
    def list_logs():
        return UsageLog.query.all()

# ---------------- SessionStudents Service ----------------
class SessionStudentsService:
    @staticmethod
    def list_entries():
        return SessionStudents.query.all()

# ---------------- StudentProjects Service ----------------
class StudentProjectsService:
    @staticmethod
    def list_entries():
        return StudentProjects.query.all()
