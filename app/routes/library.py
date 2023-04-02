"""Library Routes."""
from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.business.library import Library
from app.routes.async_response import AsyncResponse
from app.security.authorizer import require_authorizer
from app.schemas.search_books_schema import SearchBooksSchema

class LibraryRoutes:
    """Library Routes."""

    def __init__(self):
        self.blue_print = Blueprint(
            "library", __name__, url_prefix='/library')
        self.library = Library()

    def load_routes(self, app):
        """Load the routes."""

        AsyncResponse(app)

        # @app.errorhandler(Exception)
        # def handle_error(error):
        #     """Handle error."""
        #     response = {"message": str(error)}
        #     return jsonify(response), 500

        @self.blue_print.route("/books", methods=["POST"])
        @require_authorizer
        def create():
            """
            Create book record
            """
            app.preprocess_request()
            _input = request.get_json()
            self.library.create_book(_input)
            
            response = {"message": "Accepted"}
            return jsonify(response), 202

        @self.blue_print.route("/books", methods=["GET"])
        @require_authorizer
        def search():
            """
            List books
            """
            try:
                book_schema = SearchBooksSchema()
                args = book_schema.load(request.args)
            except ValidationError as err:
                return jsonify({"error": err.messages}), 400

            result = self.library.search_books(args)
            print(result)
            response = {"message": result}
            return jsonify(response), 200

        @self.blue_print.route("/books/<id>", methods=["GET"])
        @require_authorizer
        def get(id):
            """
            Get book record
            """
            result, status = self.library.get_book(id)
            response = {"message": result}
            return jsonify(response), status

        @self.blue_print.route("/books/<id>", methods=["DELETE"])
        @require_authorizer
        def delete(id):
            """
            Delete book record
            """
            result, status = self.library.delete_book(id)
            response = {"message": result}
            return jsonify(response), status

        app.register_blueprint(self.blue_print)
