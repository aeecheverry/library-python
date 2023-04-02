"""Create Book Schema"""
from marshmallow import Schema, fields, validate

class CreateBookSchema(Schema):
    """Create Book Schema"""
    id = fields.String(required=True)
    source = fields.String(required=True)
