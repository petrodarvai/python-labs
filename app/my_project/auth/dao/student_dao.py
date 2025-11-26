from app import db
from ..domain.models import Student

class StudentDAO:
    @staticmethod
    def get_all():
        return Student.query.all()

    @staticmethod
    def get_by_id(student_id):
        return Student.query.get(student_id)

    @staticmethod
    def get_by_email(email):
        return Student.query.filter_by(Email=email).first()

    @staticmethod
    def create(student_obj):
        db.session.add(student_obj)
        db.session.commit()
        return student_obj

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(student_obj):
        db.session.delete(student_obj)
        db.session.commit()
