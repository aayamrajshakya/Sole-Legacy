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



# Scenario 1: Attempts to POST with incorrect data causing a TypeError
def test_for_get(client):
    registration_helper(client)
    login_helper(client)
    data = {}
    response = client.post('/admin_add', json=data)
    assert response.status_code == 500
    assert response.json == {'message': 'Invalid Data'}


# Scenario 2: attempts to view page without logging in
def test_for_fail(client):
    response = client.get('/admin_add')
    assert response.status_code == 500