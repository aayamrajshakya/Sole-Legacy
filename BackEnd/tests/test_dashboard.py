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

# Scenario 1: User visits dashboard after logging in

def test_dashboard_1(client):
      registration_helper(client)
      login_helper(client)

      dashboardResponse = client.get('/dashboard')
      jsonResponse = dashboardResponse.get_json()

      # I had set dashboard in such a way that it returns user info when logged in and
      # error msg when not. The below checks if "AccountID" is in the data or not
      # For more explanation, run print(jsonResponse)
      assert "AccountID" in jsonResponse


# Scenario 2: User registers but doesn't log in and tries to view dashboard

def test_dashboard_2(client):
      registration_helper(client)
      dashboardResponse = client.get('/dashboard')
      jsonResponse = dashboardResponse.get_json()

      # error msg from the login_required wrapper
      assert jsonResponse["error"] == "Log in first!"