"""Book Schema"""
from marshmallow import EXCLUDE, Schema, fields, validate

class BookSchema(Schema):
    """Book Schema"""
    id = fields.String(required=True)
    source = fields.String(required=True)
    title = fields.String(required=True, validate=validate.Length(min=1))
    subtitle = fields.String(required=False, validate=validate.Length(min=1))
    authors = fields.List(fields.String(), required=False, validate=validate.Length(min=1))
    categories = fields.List(fields.String(),required=False, validate=validate.Length(min=1))
    publishedDate = fields.String(required=False, validate=validate.Length(min=1))
    publisher = fields.String(required=False, validate=validate.Length(min=1))
    description = fields.String(required=False, validate=validate.Length(min=1))
    image = fields.String(allow_none=False)

    class Meta:
        unknown = EXCLUDE
