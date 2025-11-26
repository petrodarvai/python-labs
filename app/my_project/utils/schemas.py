from marshmallow import Schema, fields

class StudentSchema(Schema):
    StudentID = fields.Int(dump_only=True)
    FullName = fields.Str(required=True)
    Email = fields.Email(allow_none=True)
    GroupName = fields.Str(allow_none=True)
    Phone = fields.Str(allow_none=True)

class EquipmentItemSchema(Schema):
    EquipmentID = fields.Int(dump_only=True)
    InventoryNumber = fields.Str(required=True)
    TypeID = fields.Int(required=True)
    SetID = fields.Int(allow_none=True)
    StatusID = fields.Int(required=True)
