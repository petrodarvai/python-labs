# app/my_project/auth/route/routes.py
from flask import Blueprint

from ..controller.student_controller import student_bp
from ..controller.project_controller import project_bp
from ..controller.labsession_controller import labsession_bp
from ..controller.equipmentset_controller import equipmentset_bp
from ..controller.equipmentstatus_controller import equipmentstatus_bp
from ..controller.equipmenttype_controller import equipmenttype_bp
from ..controller.equipmentitem_controller import equipmentitem_bp
from ..controller.lasercutterlog_controller import lasercutterlog_bp
from ..controller.usagelog_controller import usagelog_bp
from ..controller.staff_controller import staff_bp
from ..controller.maintenancelog_controller import maintenancelog_bp
from ..controller.sessionstudents_controller import sessionstudents_bp
from ..controller.studentprojects_controller import studentprojects_bp

auth_bp = Blueprint('auth_bp', __name__)

# Регістрація всіх Blueprints
auth_bp.register_blueprint(student_bp, url_prefix='/students')
auth_bp.register_blueprint(project_bp, url_prefix='/projects')
auth_bp.register_blueprint(labsession_bp, url_prefix='/labsessions')
auth_bp.register_blueprint(equipmentset_bp, url_prefix='/equipmentsets')
auth_bp.register_blueprint(equipmentstatus_bp, url_prefix='/equipmentstatus')
auth_bp.register_blueprint(equipmenttype_bp, url_prefix='/equipmenttypes')
auth_bp.register_blueprint(equipmentitem_bp, url_prefix='/equipmentitems')
auth_bp.register_blueprint(lasercutterlog_bp, url_prefix='/lasercutterlog')
auth_bp.register_blueprint(usagelog_bp, url_prefix='/usagelog')
auth_bp.register_blueprint(staff_bp, url_prefix='/staff')
auth_bp.register_blueprint(maintenancelog_bp, url_prefix='/maintenancelog')
auth_bp.register_blueprint(sessionstudents_bp, url_prefix='/sessionstudents')
auth_bp.register_blueprint(studentprojects_bp, url_prefix='/studentprojects')
