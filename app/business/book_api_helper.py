"""Book API Helper"""
import requests
from app.schemas.book_schema import BookSchema

def dict_to_query(params):
    if "categories" in params:
        params["categories"] = "+".join(params["categories"])
    if "authors" in params:
        params["authors"] = "+".join(params["authors"])
    query = ""
    for key, value in params.items():
        if value is not None:
            if query == "":
                query += f"{value}"
            else:
                query += f"+{value}"
    return query

def google_book(self, query):
    """Google book"""
    if isinstance(query, dict):
        query = dict_to_query(query)
    query = {"q": query}
    response = requests.get(self.google_library_url, params=query, timeout=5000)
    if response.status_code == 200:
        result = response.json()
        if not result or result["totalItems"] == 0:
            return None
        else:
            results = result["items"]
            def fomating_book(result):
                book = result.get("volumeInfo")
                book["id"] = result["id"]
                if "imageLinks" in book:
                    book["image"] = book["imageLinks"]["thumbnail"]
                book["source"] = "google"
                return book
            return [fomating_book(book) for book in results]
    return None


def open_library(self, query):
    """Open library"""
    if isinstance(query, dict):
        query = dict_to_query(query)
    query = {"q": query}
    response = requests.get(self.open_library_url, params=query, timeout=5000)
    if response.status_code == 200:
        result = response.json()
        if not result or result["numFound"] == 0:
            return None
        else:
            result = result["docs"][0]
            def fomating_book(result):
                book = {}
                book["id"] = result["key"]
                book["source"] = "open_library"
                book["title"] = result["title"] if "title" in result else None
                book["authors"] = result["author_name"] if "author_name" in result else None
                book["categories"] = result["subject"] if "subject" in result else None
                book["publishedDate"] = str(result["first_publish_year"]) if "first_publish_year" in result else None
                book["description"] = result["description"] if "description" in result else None
                book["publisher"] = result["publisher"][0] if ("publisher" in result and result["publisher"]) else None
                book["image"] = result["cover_i"] if "cover_i" in result else None
                return book
            return [fomating_book(book) for book in result]
    return response
