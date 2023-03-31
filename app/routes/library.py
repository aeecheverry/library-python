"""Library Routes."""
from flask import Blueprint, jsonify, request, copy_current_request_context
from security import require_authorizer
from routes.async_response import AsyncResponse
from business.library import Library

class LibraryRoutes:
    """Library Routes."""

    def __init__(self):
        self.blue_print = Blueprint(
            "library", __name__, url_prefix='/library')
        self.library = Library()

    def load_routes(self, app):
        """Load the routes."""

        AsyncResponse(app)

        @app.errorhandler(Exception)
        def handle_error(error):
            response = {"message": str(error)}
            return jsonify(response), 500

        @self.blue_print.route("/books", methods=["POST"])
        @require_authorizer
        def create():
            """
            Create book record
            """
 
            @app.async_response
            @copy_current_request_context
            @require_authorizer
            def create_async_response():
                app.preprocess_request()
                _input = request.get_json()
                self.library.create_book(_input)
            response = {"message": "Accepted"}
            return jsonify(response), 202

        @self.blue_print.route("/books", methods=["GET"])
        @require_authorizer
        def lista():
            """
            List books
            """
            _input = request.get_json()
            result = self.library.list_books(_input)
            response = {"message": result}
            return jsonify(response), 200
        
        @self.blue_print.route("/books/:id", methods=["GET"])
        @require_authorizer
        def get():
            """
            Get book record
            """
            #Get book id from request
            book_id = request.args.get('id')
            result = self.library.get_book(book_id)
            response = {"message": result}
            return jsonify(response), 200
        
        @self.blue_print.route("/books/:id", methods=["PUT"])
        @require_authorizer
        def update():
            """
            Update book record
            """
            book_id = request.args.get('id')
            _input = request.get_json()
            result = self.library.update_book(book_id, _input)
            response = {"message": result}
            return jsonify(response), 200
        
        @self.blue_print.route("/books/:id", methods=["DELETE"])
        @require_authorizer
        def delete():
            """
            Delete book record
            """
            book_id = request.args.get('id')
            result = self.library.delete_book(book_id)
            response = {"message": result}
            return jsonify(response), 200

        app.register_blueprint(self.blue_print)
