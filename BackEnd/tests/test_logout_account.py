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

## Scenario 1: Successful logout

def test_logout_1(client):
    registration_helper(client)
    login_helper(client)
    logoutResponse = client.post('/logout')
    jsonResponse = logoutResponse.get_json()
    assert logoutResponse.status_code == 200
    assert jsonResponse["message"] == "Successfully logged out!"


## Scenario 2: User registered and tried to logout w/o logging in

def test_logout_2(client):
    registration_helper(client)
    logoutResponse = client.post('/logout')
    jsonResponse = logoutResponse.get_json()

    # from the login_required decorator
    assert logoutResponse.status_code == 401
    assert jsonResponse["error"] == "Log in first!"


## Scenario 3: User tries to log out twice

def test_logout_3(client):
    registration_helper(client)
    login_helper(client)

    # logging out once
    client.post('/logout')

    # trying to log out for the 2nd time
    logoutResponse2 = client.post('/logout')
    jsonResponse = logoutResponse2.get_json()
    assert logoutResponse2.status_code == 401
    assert jsonResponse["error"] == "Log in first!"