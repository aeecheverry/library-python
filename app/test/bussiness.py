"""Test business logic"""
from unittest.mock import patch
from business.library import Library

def test_create_book_with_mock():
    """Test create book with mock"""
    with patch.object(Library, "create_book") as mock_create_book:
        mock_create_book.return_value = True
        library = Library()
        book = {
            "title": "La isla del tesoro",
            "author": "Robert Louis Stevenson",
            "genre": "Novela de aventuras"
        }
        assert library.create_book(book) == book
        mock_create_book.assert_called_once_with("La isla del tesoro", "Robert Louis Stevenson", "Novela de aventuras")

def test_list_books_with_mock():
    """Test list books with mock"""
    with patch.object(Library, "list_books") as mock_list_books:
        mock_list_books.return_value = [
            {"id": 1, "title": "El Quijote", "author": "Miguel de Cervantes", "genre": "Novela de aventuras"},
            {"id": 2, "title": "Don Juan Tenorio", "author": "José Zorrilla", "genre": "Drama"},
            {"id": 3, "title": "La Regenta", "author": "Leopoldo Alas Clarín", "genre": "Novela realista"}
        ]
        library = Library()
        _input = {
            "from": 0,
            "size": 10
        }
        books = library.list_books(_input)
        assert len(books) == 3
        assert "La Regenta" in [book["title"] for book in books]
        mock_list_books.assert_called_once()

def test_get_book_with_mock():
    """Test get book with mock"""
    with patch.object(Library, "get_book") as mock_get_book:
        mock_get_book.return_value = {"id": 1, "title": "El Quijote", "author": "Miguel de Cervantes", "genre": "Novela de aventuras"}
        library = Library()
        book = library.get_book(1)
        assert book["title"] == "El Quijote"
        mock_get_book.assert_called_once_with(1)

def test_update_book_with_mock():
    """Test update book with mock"""
    with patch.object(Library, "update_book") as mock_update_book:
        mock_update_book.return_value = True
        library = Library()
        book_id = 2
        updated_book = {
            "title": "Cien años de soledad",
            "author": "Gabriel García Márquez",
            "genre": "Realismo mágico"
        }
        assert library.update_book(book_id, updated_book) == updated_book
        mock_update_book.assert_called_once_with(book_id, updated_book)

def test_delete_book_with_mock():
    """Test delete book with mock"""
    with patch.object(Library, "delete_book") as mock_delete_book:
        mock_delete_book.return_value = True
        library = Library()
        book_id = 3
        assert library.delete_book(book_id) == True
        mock_delete_book.assert_called_once_with(book_id)
