"""Book Schemas"""
from marshmallow import Schema, fields, validate

class SearchBooksSchema(Schema):
    """Book Schema"""
    id = fields.String(required=False)
    title = fields.String(required=False, validate=validate.Length(min=1))
    subtitle = fields.String(required=False, validate=validate.Length(min=1))
    authors = fields.String(required=False, validate=validate.Length(min=1))
    categories = fields.String(required=False, validate=validate.Length(min=1))
    publishedDate = fields.Date(format="%Y-%m-%d", required=False)
    publisher = fields.String(required=False, validate=validate.Length(min=1))
    description = fields.String(required=False, validate=validate.Length(min=1))
    image = fields.String(allow_none=False)
