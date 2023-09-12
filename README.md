This guide provides step-by-step instructions on setting up, running, and using the Flask API for your project. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on a database of persons.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Security Considerations](#security-considerations)

## Prerequisites

Before getting started, make sure you have the following prerequisites installed:

- Python (3.x recommended)
- MySQL or another supported database system
- Flask
- SQLAlchemy
- Other required libraries (install them using `pip`)

## Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/FestusMike/HNGX_RESTAPI_CRUD_TASK.git
   cd HNGX_RESTAPI_CRUD_TASK

2.  Install the required Python packages using pip:
    pip install -r requirements.txt

3.  Configure the database settings:
    Open main.py(or any python file you wish) and set the appropriate database URI, such as:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://username:password@host/database_name'

4.  Initialize the db:
    with app.app_context():
        db.create_all()

5.  Running The API:
        ```shell```
        'python main.py'
    The API should now be running locally at http://127.0.0.1:5000.

API Endpoints
The API exposes the following endpoints:

Create a Person (POST):

Endpoint: /api
Request Type: POST
Parameters: name (string, required)
Example: http://127.0.0.1:5000/api?name=John

Get a Person by ID (GET):

Endpoint: /api/<int:user_id>
Request Type: GET
Example: http://127.0.0.1:5000/api/1

Update a Person by ID (PUT):

Endpoint: /api/<int:user_id>
Request Type: PUT
Parameters: name (string, required)
Example: http://127.0.0.1:5000/api/1

Delete a Person by ID (DELETE):

Endpoint: /api/<int:user_id>
Request Type: DELETE
Example: http://127.0.0.1:5000/api/1

Testing
You can use tools like Postman or the provided Python script to test the API endpoints. Refer to the API documentation above for details on how to use each endpoint.

Security Considerations
SQL Injection: The API is designed to prevent SQL injection attacks by using SQLAlchemy's ORM and input validation. Avoid concatenating user input directly into SQL queries.

Authentication and Authorization: Implement user authentication and authorization to control access to the API's CRUD operations.

API's Source Code: 