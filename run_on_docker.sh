export FLASK_DEBUG=False
export API_KEY="secret"
export PORT=3000
export GOOGLE_LIBRARY_URL="https://www.googleapis.com/books/v1/volumes"
export DATABASE_IMPL="mongodb"
export MONGODB_URL="mongodb://localhost:27017"
export MONGODB_DATABASE="library"

# Build the Docker image

docker build -t library .

# Run the Docker image with environment variables

docker run -it --rm \
-p $PORT:$PORT \
-e API_KEY=$API_KEY \
-e GOOGLE_LIBRARY_URL=$GOOGLE_LIBRARY_URL \
-e DATABASE_IMPL=$DATABASE_IMPL \
-e MONGODB_URL=$MONGODB_URL \
-e MONGODB_DATABASE=$MONGODB_DATABASE \
-e FLASK_DEBUG=$FLASK_DEBUG \
library


