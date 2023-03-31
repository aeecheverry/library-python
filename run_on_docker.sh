export API_KEY="secret"
export PORT=3000

# Build the Docker image

docker build -t library .

# Run the Docker image with environment variables

docker run -it --rm \
-p $PORT:$PORT \
-e API_KEY=$API_KEY \
library


