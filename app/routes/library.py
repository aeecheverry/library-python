"""Library Routes."""
from flask import Blueprint, jsonify, request, copy_current_request_context
from security.authorizer import require_api_key
from routes.async_response import AsyncResponse

class LibraryRoutes:
    """Library Routes."""

    def __init__(self):
        self.blue_print = Blueprint(
            "library", __name__, url_prefix='/library')

    def load_routes(self, app):
        """Load the routes."""

        AsyncResponse(app)

        @app.errorhandler(Exception)
        def handle_error(error):
            response = {"message": str(error)}
            return jsonify(response), 500

        @self.blue_print.route("/train", methods=["POST"])
        @require_api_key
        def list():
            """
            List books
            """
            
            @app.async_response
            @copy_current_request_context
            @require_api_key
            def train_async_response():
                app.preprocess_request()
                _input = request.get_json()
                #TODO 
            response = {"message": "Accepted"}
            return jsonify(response), 202

        @self.blue_print.route("/predict", methods=["POST"])
        @require_api_key
        def create():
            """
            Create book record
            """
            _input = request.get_json()
            #TODO
            response = {"message": result}
            return jsonify(response), 200

        app.register_blueprint(self.blue_print)
