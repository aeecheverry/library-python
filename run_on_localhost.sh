export FLASK_DEBUG=False
export API_KEY="secret"
export PORT=3000
export GOOGLE_LIBRARY_URL="https://www.googleapis.com/books/v1/volumes"
export DATABASE_IMPL="mongodb"
export MONGODB_URL="mongodb://localhost:27017"
export MONGODB_DATABASE="library"

python main.py