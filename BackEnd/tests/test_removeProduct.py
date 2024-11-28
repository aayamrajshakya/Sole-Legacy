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


# Scenario 1: successfully views page
def test_get_request(client):
    registration_helper(client)
    login_helper(client)
    response = client.get('/admin_remove')
    assert response.status_code == 200


# Scenario 2: attempts to add an item, fails
def test_post_fail(client):
    registration_helper(client)
    login_helper(client)
    response = client.post('/admin_remove', json={'ItemId': '0'})
    assert response.status_code == 409