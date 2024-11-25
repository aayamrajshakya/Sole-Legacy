# Helper functions to shorten the codebase

def registration_helper(client):
    return client.post('/register', json={
        "fullName": "Aayam Raj Shakya",
        "email": "aayam@msu.edu",
        "plain_password": "Mississippi123!",
        "address": "Starkville",
        "usertype": "Admin"
    })

def login_helper(client):
        return client.post('/login', json={
              "email": "aayam@msu.edu",
              "plain_password": "Mississippi123!"
        })

## Scenario 1: Successful login

def test_login_1(client):
    registration_helper(client)
    loginResponse = login_helper(client)
    jsonResponse = loginResponse.get_json()
    assert loginResponse.status_code == 200
    assert jsonResponse["message"] == "Successfully logged in"


## Scenario 2: Wrong password

def test_login_2(client):
    registration_helper(client)
    loginResponse = client.post('/login', json={
        "email": "aayam@msu.edu",
        "plain_password": "wrongpassword",
    })
    jsonResponse = loginResponse.get_json()
    assert loginResponse.status_code == 401
    assert jsonResponse["error"] == "Login credentials don't match"


#############################################################
# Wrong user-type scenario is handled by flask-react        #                              
#############################################################