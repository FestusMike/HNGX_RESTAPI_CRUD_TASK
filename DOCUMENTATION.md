# Flask API Documentation

## Table of Contents

- [Introduction](#introduction)
- [Endpoints](#endpoints)
  - [Create a Person](#create-a-person)
  - [Get a Person by ID](#get-a-person-by-id)
  - [Update a Person by ID](#update-a-person-by-id)
  - [Delete a Person by ID](#delete-a-person-by-id)
- [Sample Usage](#sample-usage)
  - [Create a Person](#create-a-person-sample-usage)
  - [Get a Person by ID](#get-a-person-by-id-sample-usage)
  - [Update a Person by ID](#update-a-person-by-id-sample-usage)
  - [Delete a Person by ID](#delete-a-person-by-id-sample-usage)
- [Known Limitations](#known-limitations)
- [Setup and Deployment](#setup-and-deployment)
  - [Local Setup](#local-setup)
  - [Server Deployment](#server-deployment)

## Introduction

This documentation provides details on how to use the Flask API for managing a database of persons. The API supports CRUD (Create, Read, Update, Delete) operations on person records. Below are the API endpoints and usage instructions.

## Endpoints

### Create a Person

- **Endpoint:** `/api`
- **Request Type:** POST
- **Parameters:**
  - `name` (string, required) - The name of the person to be created.
- **Response:**
  - Success (HTTP 201):
    ```json
    {
      "message": "Person created successfully"
    }
    ```
  - Error (HTTP 400 or 500):
    ```json
    {
      "error": "Error message"
    }
    ```

### Get a Person by ID

- **Endpoint:** `/api/<int:user_id>`
- **Request Type:** GET
- **Response:**
  - Success (HTTP 200):
    ```json
    {
      "id": 1,
      "name": "John"
    }
    ```
  - Error (HTTP 404):
    ```json
    {
      "error": "Person not found"
    }
    ```

### Update a Person by ID

- **Endpoint:** `/api/<int:user_id>`
- **Request Type:** PUT
- **Parameters:**
  - `name` (string, required) - The updated name for the person.
- **Response:**
  - Success (HTTP 200):
    ```json
    {
      "message": "Person updated successfully"
    }
    ```
  - Error (HTTP 400 or 404):
    ```json
    {
      "error": "Error message"
    }
    ```

### Delete a Person by ID

- **Endpoint:** `/api/<int:user_id>`
- **Request Type:** DELETE
- **Response:**
  - Success (HTTP 200):
    ```json
    {
      "message": "Person deleted successfully"
    }
    ```
  - Error (HTTP 404):
    ```json
    {
      "error": "Person not found"
    }
    ```

## Sample Usage

### Create a Person (Sample Usage)

**Request:**
```http
POST /api?name=John
Response (HTTP 201):

json
{
  "message": "Person created successfully"
}
Get a Person by ID (Sample Usage)
Request:
http
GET /api/1
Response (HTTP 200):

json
{
  "id": 1,
  "name": "John"
}
Update a Person by ID (Sample Usage)
Request:
http
PUT /api/1
Content-Type: application/json

{
  "name": "Updated John"
}
Response (HTTP 200):

json
{
  "message": "Person updated successfully"
}
Delete a Person by ID (Sample Usage)

Request:
http
DELETE /api/1
Response (HTTP 200):
json
{
  "message": "Person deleted successfully"
}

Known Limitations
The API assumes that person names are unique.
Error responses may provide limited details for security reasons.

Setup and Deployment
Local Setup
Clone the repository:

```shell

git clone https://github.com/FestusMike/HNGX_RESTAPI_CRUD_TASK.git
cd HNGX_RESTAPI_CRUD_TASK

Install the required Python packages using pip:
```shell
pip install -r requirements.txt

Configure the database settings in main.py.

Initialize the database:
    with app.app_context():
        db.create_all

Run the API:
```shell
python main.py
The API should now be accessible locally at http://127.0.0.1:5000.

Server Deployment
For deploying the API on a server, refer to your hosting provider's documentation or consider using a platform like Heroku, AWS, or Google Cloud Platform.

Ensure that your database is accessible from the server.
Set environment variables for sensitive configuration data.
Deploy the code to the server.
Configure any necessary web server (e.g., Nginx, Apache) or WSGI server (e.g., Gunicorn) to serve the Flask application.
Consult your server hosting provider's documentation for specific deployment instructions.


