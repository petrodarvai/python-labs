from app import db

class EquipmentSet(db.Model):
    __tablename__ = 'equipmentsets'
    SetID = db.Column(db.Integer, primary_key=True)
    SetName = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text)
    items = db.relationship('EquipmentItem', back_populates='set', lazy='select')

class EquipmentStatus(db.Model):
    __tablename__ = 'equipmentstatus'
    StatusID = db.Column(db.Integer, primary_key=True)
    StatusName = db.Column(db.String(50), nullable=False)
    items = db.relationship('EquipmentItem', back_populates='status', lazy='select')

class EquipmentType(db.Model):
    __tablename__ = 'equipmenttypes'
    TypeID = db.Column(db.Integer, primary_key=True)
    TypeName = db.Column(db.String(50), nullable=False)
    items = db.relationship('EquipmentItem', back_populates='type', lazy='select')

class EquipmentItem(db.Model):
    __tablename__ = 'equipmentitems'
    EquipmentID = db.Column(db.Integer, primary_key=True)
    InventoryNumber = db.Column(db.String(50), nullable=False, unique=True)
    TypeID = db.Column(db.Integer, db.ForeignKey('equipmenttypes.TypeID'), nullable=False)
    SetID = db.Column(db.Integer, db.ForeignKey('equipmentsets.SetID'))
    StatusID = db.Column(db.Integer, db.ForeignKey('equipmentstatus.StatusID'), nullable=False)

    type = db.relationship('EquipmentType', back_populates='items')
    set = db.relationship('EquipmentSet', back_populates='items')
    status = db.relationship('EquipmentStatus', back_populates='items')

class LabSession(db.Model):
    __tablename__ = 'labsessions'
    SessionID = db.Column(db.Integer, primary_key=True)
    SessionDate = db.Column(db.Date, nullable=False)
    CourseName = db.Column(db.String(100), nullable=False)
    Instructor = db.Column(db.String(100), nullable=False)
    students = db.relationship('Student', secondary='sessionstudents', back_populates='sessions')

class Project(db.Model):
    __tablename__ = 'projects'
    ProjectID = db.Column(db.Integer, primary_key=True)
    ProjectName = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text)
    StartDate = db.Column(db.Date)
    EndDate = db.Column(db.Date)
    students = db.relationship('Student', secondary='studentprojects', back_populates='projects')

class Student(db.Model):
    __tablename__ = 'students'
    StudentID = db.Column(db.Integer, primary_key=True)
    FullName = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), unique=True)
    GroupName = db.Column(db.String(50))
    Phone = db.Column(db.String(20))

    sessions = db.relationship('LabSession', secondary='sessionstudents', back_populates='students')
    projects = db.relationship('Project', secondary='studentprojects', back_populates='students')
    laser_logs = db.relationship('LaserCutterLog', back_populates='student')
    usage_logs = db.relationship('UsageLog', back_populates='student')

class LaserCutterLog(db.Model):
    __tablename__ = 'lasercutterlog'
    LaserLogID = db.Column(db.Integer, primary_key=True)
    StudentID = db.Column(db.Integer, db.ForeignKey('students.StudentID'), nullable=False)
    ProjectID = db.Column(db.Integer, db.ForeignKey('projects.ProjectID'))
    StartTime = db.Column(db.DateTime, nullable=False)
    EndTime = db.Column(db.DateTime, nullable=False)
    DurationMinutes = db.Column(db.Integer)

    student = db.relationship('Student', back_populates='laser_logs')
    project = db.relationship('Project')

class Staff(db.Model):
    __tablename__ = 'staff'
    StaffID = db.Column(db.Integer, primary_key=True)
    FullName = db.Column(db.String(100), nullable=False)
    Role = db.Column(db.String(50), nullable=False)
    maint_logs = db.relationship('MaintenanceLog', back_populates='staff')
    usage_logs = db.relationship('UsageLog', back_populates='staff')

class MaintenanceLog(db.Model):
    __tablename__ = 'maintenancelog'
    MaintenanceID = db.Column(db.Integer, primary_key=True)
    EquipmentID = db.Column(db.Integer, db.ForeignKey('equipmentitems.EquipmentID'), nullable=False)
    StaffID = db.Column(db.Integer, db.ForeignKey('staff.StaffID'), nullable=False)
    StartDate = db.Column(db.DateTime, nullable=False)
    EndDate = db.Column(db.DateTime)
    Description = db.Column(db.Text)

    equipment = db.relationship('EquipmentItem')
    staff = db.relationship('Staff', back_populates='maint_logs')

class SessionStudents(db.Model):
    __tablename__ = 'sessionstudents'
    SessionID = db.Column(db.Integer, db.ForeignKey('labsessions.SessionID'), primary_key=True)
    StudentID = db.Column(db.Integer, db.ForeignKey('students.StudentID'), primary_key=True)

class StudentProjects(db.Model):
    __tablename__ = 'studentprojects'
    StudentID = db.Column(db.Integer, db.ForeignKey('students.StudentID'), primary_key=True)
    ProjectID = db.Column(db.Integer, db.ForeignKey('projects.ProjectID'), primary_key=True)

class UsageLog(db.Model):
    __tablename__ = 'usagelog'
    UsageID = db.Column(db.Integer, primary_key=True)
    StudentID = db.Column(db.Integer, db.ForeignKey('students.StudentID'), nullable=False)
    EquipmentID = db.Column(db.Integer, db.ForeignKey('equipmentitems.EquipmentID'), nullable=False)
    ProjectID = db.Column(db.Integer, db.ForeignKey('projects.ProjectID'))
    StaffID = db.Column(db.Integer, db.ForeignKey('staff.StaffID'), nullable=False)
    CheckOutTime = db.Column(db.DateTime, nullable=False)
    ReturnTime = db.Column(db.DateTime)

    student = db.relationship('Student', back_populates='usage_logs')
    equipment = db.relationship('EquipmentItem')
    project = db.relationship('Project')
    staff = db.relationship('Staff', back_populates='usage_logs')
