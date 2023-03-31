"""Routes factory module."""
from routes.library import LibraryRoutes

def create_routes(app):
    """Create routes."""
    LibraryRoutes().load_routes(app)
