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


# Scenario 1: Admin is logged in and views account database
def test_for_get(client):
    registration_helper(client)
    login_helper(client)
    response = client.get('/admin_view')
    assert response.status_code == 200
