import requests

# API base url
base_url = 'http://127.0.0.1:5000/api'

# Function to send a GET request to retrieve a person by ID
def get_person(user_id):
    url = f'{base_url}/{user_id}'
    response = requests.get(url)
    return response

# Function to send a POST request to create a new person
def create_person(name):
    data = {'name': name}
    response = requests.post(base_url, params=data)
    return response

# Function to send a PUT request to update a person's name by ID
def update_person(user_id, new_name):
    url = f'{base_url}/{user_id}'
    data = {'name': new_name}
    response = requests.put(url, json=data)
    return response

# Function to send a DELETE request to delete a person by ID
def delete_person(user_id):
    url = f'{base_url}/{user_id}'
    response = requests.delete(url)
    return response

if __name__ == '__main__':
    # Test the CRUD operations
    try:
        # Create a new person
        create_response = create_person("Micheal")
        print("Create Response:", create_response.json())

        # Get the ID of the newly created person
        person_id = create_response.json().get('message').split()[-1]

        # Update the person's name
        update_response = update_person(person_id, "Updated Micheal")
        print("Update Response:", update_response.json())

        # Get the updated person by ID
        get_response = get_person(person_id)
        print("Get Response:", get_response.json())

        # Delete the person
        delete_response = delete_person(person_id)
        print("Delete Response:", delete_response.json())

        # Attempt to get the deleted person (will return return a 404 error)
        get_response_after_delete = get_person(person_id)
        print("Get Response After Delete:", get_response_after_delete.json())

    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)
