# Have to populate inventory for the Scenario 1 test instance
import sqlite3
def populateTable():
    connection = sqlite3.connect('StoreDatabase.db')
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Inventory (ItemName, Description, Image, Url, Quantity, Price, Gender) 
        VALUES ('Nike Zoom Vomero 5', '(Description was too long)', 'showcase_1.png', 'Nike_Zoom_Vomero_5', 20, 109.97, 'Men')
    """)

    connection.commit()
    cursor.close()
    connection.close()

#Scenario 1: User gets item in inventory

def test_search_1(client):
    # Adding item to the database
    populateTable() 
    searchResponse = client.post('/search', json={
        "searchKeyword": "nike"
    })
    jsonResponse = searchResponse.get_json()
    assert jsonResponse["message"] == "Search results posted"    


# Scenario 2: User gets error msg when nonexistent item is searched

def test_search_2(client):
    searchResponse = client.post('/search', json={
        "searchKeyword": "gucci"
    })
    jsonResponse = searchResponse.get_json()
    assert jsonResponse["error"] == "No such item"