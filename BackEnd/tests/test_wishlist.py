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

def adder_helper(client):
      return client.post('/addToWishlist', json={
            "ItemName": "Shoe name",
            "Price": "100",
            "Color": "Black",
            "Size": "8",
            "Gender": "Men",
            "Slug": "shoe_url"
      })
    

# Scenario 1: User trying to fetch empty wishlist and is successfully shown empty wishlist message

def test_wishlist_1(client):
      registration_helper(client)
      login_helper(client)

      wishlistResponse = client.get('/wishlist')
      jsonResponse = wishlistResponse.get_json()
      
      assert jsonResponse["message"] == "Wishlist is empty"


# Scenario 2: This has nested scenarios:
            # Successfully adds to wishlist and fetches
            # Then, tries to add duplicate items in wishlist and fails

def test_wishlist_2(client):
      registration_helper(client)
      login_helper(client)

      # Adding item for the first time
      addResponse = adder_helper(client)
      jsonResponse = addResponse.get_json()
      assert jsonResponse["message"] == "Successfully added to wishlist"

      # Fetching to see if really added or not
      wishlistResponse = client.get('/wishlist')
      jsonResponse = wishlistResponse.get_json()
      assert jsonResponse["message"] == "Wishlist fetched"

      # Trying to add the item again
      duplicateAddResponse = adder_helper(client)
      jsonResponse = duplicateAddResponse.get_json()
      assert jsonResponse["message"] == "Item already in wishlist"

        
# Scenario 3: User successfully adds and successfully removes too

def test_wishlist_3(client):
      registration_helper(client)
      login_helper(client)
      adder_helper(client)

      removeResponse = client.post('/removeFromWishlist', json={
            "ItemName": "Shoe name"
      })

      jsonResponse2 = removeResponse.get_json()
      assert jsonResponse2["message"] == "Successfully deleted Shoe name from wishlist!"

      # verifying that the wishlist is empty after removing the item
      wishlistResponse = client.get('/wishlist')
      jsonResponse3 = wishlistResponse.get_json()
      assert jsonResponse3["message"] == "Wishlist is empty"


######################################################################
# The user trying to remove items that weren't even in the wishlist  #
# is senseless, but this can be done via curl. This possibility has  #
# been ruled out though                                              #
######################################################################