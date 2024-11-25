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

## Scenario 1: Successful deletion

def test_delete_1(client):
    registration_helper(client)
    login_helper(client)
    deleteResponse = client.post('/delete')
    jsonResponse = deleteResponse.get_json()
    assert deleteResponse.status_code == 200
    assert jsonResponse["message"] == "Successfully deleted account!"


## Scenario 2: User registers, doesn't log in but tries to delete the account
## This scenario might not make sense in real-world because in functional websites,
## the "delete" button usually shows up in dashboard post-login. This is not the case in our project.

def test_delete_2(client):
    registration_helper(client)
    deleteResponse = client.post('/delete')
    jsonResponse = deleteResponse.get_json()

    # from the login_required decorator
    assert deleteResponse.status_code == 401
    assert jsonResponse["error"] == "Log in first!"


## Scenario 3: User tries to delete account that has already been deleted
## This scenario applies to when someone uses curl to post requests instead of using the GUI

def test_delete_3(client):
    registration_helper(client)

    # deleting the account
    client.post('/delete')

    # trying to delete again
    deleteResponse = client.post('/delete')

    # asserting against error msg doesn't make because our app isn't built well to report to the
    # user that they're trying to delete an already deleted account. The app would just respond as if
    # the user isn't authorized to delete the account once the session is cleared
    assert deleteResponse.status_code == 401

##############################################################################
# We haven't implemented the authentication bfr proceeding with              #
# account deletion, so the `register >> not logging in >> trying to delete`  #
# scenario has been ruled out                                                #                              
##############################################################################