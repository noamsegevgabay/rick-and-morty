# Rick and Morty Flask App

## This project is a Flask application that queries the Rick and Morty API for characters who are human, alive, and originated from Earth. It provides REST API endpoints to fetch this data and a health check endpoint.

```bash
docker build -t noamsegevgabay/rickandmorty-flask-app .
docker run -d -p 5000:5000 --name rickandmorty-flask-app rickandmorty-flask-app
```

 ## REST API Endpoints
 
### 1. `/characters`
- **Method**: `GET`
- **Description**: Fetches a list of human characters who are alive and originated from Earth.
- **Response**: Returns a JSON array of characters, each with `Name`, `Location`, and `Image`.
## Example Request:
```bash
curl http://localhost:5000/characters
```
### 2. /healthcheck
# Method: GET
### Description: Returns the health status of the application.
### Response: Returns a JSON object indicating the status of the application.
## Example Request:
```bash
curl http://localhost:5000/healthcheck
```
# Test the Endpoints
```bash
curl http://localhost:5000/healthcheck
curl http://localhost:5000/characters
```
