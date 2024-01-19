import requests


url="https://api.pole-emploi.io/partenaire/offresdemploi/v2/offres/search"




def api_attributes():
    
    
    url = 'https://api.pole-emploi.io/partenaire/offresdemploi/v2/offres/search'
    headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer da2659323720b71602f8eb00ac1d2182138014d76bcb0969151170d7ce82d19c',
    'Range': 'items=0-149'  # Adjust the range based on your needs
}

    response = requests.get(url, headers=headers)
    # Check if the request was successful (status code 200)
    if response.status_code in [200, 206]:
    # Parse the JSON content
        data = response.json()

    # Extract and print attributes only from the first item
        first_offer = data.get('resultats', [])[0]
    
        if first_offer:
        # Print or use the attributes of the first item
            for key, value in first_offer.items():
             print(f'{key}')
    else: 
        print(response.headers)
        print(f'Error: {response.status_code}')

# Print the response status code and content
    # print(f'Status Code: {response.status_code}')
    # print('Response Content:')
    # print(response.json())

api_attributes()    