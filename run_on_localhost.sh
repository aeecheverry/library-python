export FLASK_DEBUG=True
export API_KEY="secret"
export PORT=3000
export GOOGLE_LIBRARY_URL="https://www.googleapis.com/books/v1/volumes"
export OPEN_LIBRARY_URL="http://openlibrary.org/search.json"
export DATABASE_IMPL="mongodb"
export MONGODB_URL="mongodb://localhost:27017"
export MONGODB_DATABASE="library"

docker-compose up -d
python main.py