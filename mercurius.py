import requests

# Function to check if the house matches criteria
def matches_criteria(house, bedrooms, baths, max_price):
    print("House:", house)  # Debug print statement
    bedrooms_match = house.get('bedrooms') is not None and house['bedrooms'] == bedrooms
    baths_match = house.get('bathrooms') is not None and house['bathrooms'] == baths
    price_valid = house.get('price') is not None and house['price'] <= max_price
    
    return all([bedrooms_match, baths_match, price_valid])

# Your specified criteria
bedrooms_required = 4
bathrooms_required = 3.5
price_limit = 1200000

# The API endpoint and headers
url = "https://zillow-working-api.p.rapidapi.com/pro/byzpid"
headers = {
    "X-RapidAPI-Key": "2848bc9cf6msh4d9bb54a6d9ae63p1b936ajsn1ad1e12ba683",
    "X-RapidAPI-Host": "zillow-working-api.p.rapidapi.com"
}

# Example parameter, you should use the one that applies to your situation
querystring = {"area": "Rochester"}

response = requests.get(url, headers=headers, params=querystring)

# Response checking
print("Response status code:", response.status_code)  # Debug print statement
if response.status_code == 200:
    response_data = response.json()
    print("Response data:", response_data)  # Debug print statement
    
    # Replace 'propertyDetails' with the correct key from your response
    data = response_data.get('propertyDetails', [])
    print("Number of properties:", len(data))  # Debug print statement
    
    matching_houses = [house for house in data if matches_criteria(house, bedrooms_required, bathrooms_required, price_limit)]
    print("Number of matching houses:", len(matching_houses))  # Debug print statement
    
    # Print or do something with the matching_houses
    for house in matching_houses:
        print(house)
else:
    print(f"Failed to retrieve data: {response.status_code}")
