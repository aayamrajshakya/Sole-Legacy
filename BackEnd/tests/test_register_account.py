## Scenario 1: Successful registration

def test_register_1(client):
    regResponse = client.post('/register', json={
        "fullName": "Aayam Raj Shakya",
        "email": "aayam@msu.edu",
        "plain_password": "Mississippi123!",
        "address": "Starkville",
        "usertype": "Admin"
    })
    jsonResponse = regResponse.get_json()

    assert regResponse.status_code == 201
    assert "Successfully registered!" in jsonResponse["message"]


## Scenario 2: Unsuccessful registration because of email address duplication

def test_register_2(client):
    # Creating genuine account first
    client.post('/register', json={
        "fullName": "Kevin McDonal",
        "email": "kevin@msu.edu",
        "plain_password": "Mississippi123!",
        "address": "Starkville",
        "usertype": "Admin"
    })

    # Creating account with already existing email address
    regResponse = client.post('/register', json={
        "fullName": "Charlie Virden",
        "email": "kevin@msu.edu",
        "plain_password": "Biloxi123!",
        "address": "Biloxi",
        "usertype": "Seller"
    })
    jsonResponse = regResponse.get_json()

    assert regResponse.status_code == 409
    assert "error" in jsonResponse


##########################################################################################
# https://testsigma.com/blog/test-cases-for-registration-page/                           #
# Scenarios like '@' in email address, checking "confirm passwords", password format,    #
# and so on are handled by HTML validation, so I didn't make test cases for them         #
##########################################################################################