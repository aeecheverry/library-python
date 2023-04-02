"""Book Schema"""
from marshmallow import Schema, fields, validate

class BookSchema(Schema):
    """Book Schema"""
    id = fields.String(required=True)
    source = fields.String(required=True)
    title = fields.String(required=True, validate=validate.Length(min=1))
    subtitle = fields.String(required=True, validate=validate.Length(min=1))
    authors = fields.List(fields.String(), required=True, validate=validate.Length(min=1))
    categories = fields.List(fields.String(),required=True, validate=validate.Length(min=1))
    publication_date = fields.Date(format="%Y-%m-%d", required=True)
    publisher = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))
    image = fields.String(allow_none=False)
