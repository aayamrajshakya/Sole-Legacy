## Scenario 1: Successful logout

def test_logout_1(client):
    client.post('/register', json={
        "fullName": "Demo Account",
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
        "address": "Starkville",
        "usertype": "Admin"
    })

    client.post('/login', json={
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
    })

    logoutResponse = client.post('/logout')
    jsonResponse = logoutResponse.get_json()

    assert logoutResponse.status_code == 200
    assert "Successfully logged out!" in jsonResponse["message"]



## Scenario 2: User registered and tried to logout w/o logging in

def test_logout_2(client):
    client.post('/register', json={
        "fullName": "Demo Account",
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
        "address": "Starkville",
        "usertype": "Admin"
    })

    logoutResponse = client.post('/logout')
    jsonResponse = logoutResponse.get_json()

    # from the login_required decorator
    assert logoutResponse.status_code == 401
    assert "Log in first!" in jsonResponse["error"]


## Scenario 3: User tries to log out twice

def test_logout_3(client):
    client.post('/register', json={
        "fullName": "Demo Account",
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
        "address": "Starkville",
        "usertype": "Admin"
    })

    client.post('/login', json={
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
    })

    # logging out once
    client.post('/logout')

    # trying to log out for the 2nd time
    logoutResponse2 = client.post('/logout')

    jsonResponse = logoutResponse2.get_json()

    assert logoutResponse2.status_code == 401
    assert "Log in first!" in jsonResponse["error"]