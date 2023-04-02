"""Routes factory module."""
from app.routes.library import LibraryRoutes

def create_routes(app):
    """Create routes."""
    LibraryRoutes().load_routes(app)
