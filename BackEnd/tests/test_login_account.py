## Scenario 1: Successful login

def test_login_1(client):
    client.post('/register', json={
        "fullName": "Demo Account",
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
        "address": "Starkville",
        "usertype": "Admin"
    })

    loginResponse = client.post('/login', json={
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
    })
    jsonResponse = loginResponse.get_json()

    assert loginResponse.status_code == 200
    assert "Successfully logged in" in jsonResponse["message"]


## Scenario 2: Wrong password

def test_login_2(client):
    client.post('/register', json={
        "fullName": "Demo Account",
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
        "address": "Starkville",
        "usertype": "Admin"
    })

    loginResponse = client.post('/login', json={
        "email": "demo@demo.edu",
        "plain_password": "wrongpassword",
    })
    jsonResponse = loginResponse.get_json()

    assert loginResponse.status_code == 401
    assert "error" in jsonResponse


#############################################################
# Wrong user-type scenario is handled by flask-react        #                              
#############################################################