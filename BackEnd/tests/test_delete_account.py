## Scenario 1: Successful deletion

def test_delete_1(client):
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

    deleteResponse = client.post('/delete')
    jsonResponse = deleteResponse.get_json()

    assert deleteResponse.status_code == 200
    assert "Successfully deleted account!" in jsonResponse["message"]


## Scenario 2: User registers, doesn't log in but tries to delete the account
## This scenario might not make sense in real-world because in functional websites,
## the "delete" button usually shows up in dashboard post-login. This is not the case in our project.

def test_delete_2(client):
    client.post('/register', json={
        "fullName": "Demo Account",
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
        "address": "Starkville",
        "usertype": "Admin"
    })

    deleteResponse = client.post('/delete')
    jsonResponse = deleteResponse.get_json()


    # from the login_required decorator
    assert deleteResponse.status_code == 401
    assert "Log in first!" in jsonResponse["error"]


## Scenario 3: User tries to delete account that has already been deleted
## This scenario applies to when someone uses curl to post requests instead of using the GUI

def test_delete_3(client):
    client.post('/register', json={
        "fullName": "Demo Account",
        "email": "demo@demo.edu",
        "plain_password": "Demo123!",
        "address": "Starkville",
        "usertype": "Admin"
    })



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