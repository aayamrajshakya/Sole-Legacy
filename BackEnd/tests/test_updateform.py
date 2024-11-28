
def registration_helper(client):
    return client.post('/register', json={
        "fullName": "John Doe",
        "email": "johndoe@msu.edu",
        "plain_password": "Mississippi123!",
        "address": "Starkville",
        "usertype": "Admin"
    })

def login_helper(client):
        return client.post('/login', json={
              "email": "johndoe@msu.edu",
              "plain_password": "Mississippi123!"
        })



# Scenario 1: User attempts to change the name on their account
def test_update_form_name(client):
    registration_helper(client)
    login_helper(client)
    data = {"FullName": "NewName"}
    response = client.post("/update_form", json=data)

    assert response.status_code == 200
    assert response.json == {"message": "successful"}


# Scenario 2: User attempts to change the Email on their account
def test_update_form_email(client):
    registration_helper(client)
    login_helper(client)
    data = {"Email": "NewEmail"}
    response = client.post("/update_form", json=data)

    assert response.status_code == 200
    assert response.json == {"message": "successful"}


# Scenario 3: User attempts to change the Address on their account
def test_update_form_address(client):
    registration_helper(client)
    login_helper(client)
    data = {"Address": "NewAddress"}
    response = client.post("/update_form", json=data)

    assert response.status_code == 200
    assert response.json == {"message": "successful"}


# Scenario 4: User attempts to change the Password on their account
def test_update_form_password(client):
    registration_helper(client)
    login_helper(client)
    data = {"Password": "NewPassword"}
    response = client.post("/update_form", json=data)

    assert response.status_code == 200
    assert response.json == {"message": "successful"}


# Scenario 5: tests for proper GET requests
def test_update_form_get_request(client):
    registration_helper(client)
    login_helper(client)
    response = client.get('/update_form')
    assert response.status_code == 200

