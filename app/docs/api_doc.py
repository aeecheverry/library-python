"""Docs"""
from flask import send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/docs'
API_URL = '/docs/openapi.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Library"
    }
)

def generate_doc(app):
    """Generate docs"""

    @app.route("/docs/openapi.json")
    def send_openapi():
        """Send OpenAPI"""
        return send_from_directory('app/docs', 'openapi.json')

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

