import requests
import json

# Name of API key: stockdb_usage
# The API key has a rate limit of 3 per second and
# has monthly limit of 3000 per month


api_key = ''
header = {"X-API-KEY":api_key}

while(True):
    print("1. Get current list\n2. Add entry\n3. Remove entry\n4. Exit\n")
    option = int(input("Enter choice: "))
    print()

    if (option == 1):
        url = 'https://votpumzhh8.execute-api.ap-south-1.amazonaws.com/live/getall'

        response = dict(requests.get(url = url, headers = header).json())

        for key in response:
            print(key,end = ' : ')
            print('minPrice:',response[key]['minPrice'], ', maxPrice:',response[key]['maxPrice'],'\n')
    
    if (option == 2):
        symbol = str(input("Enter symbol (eg. INFY.NS): "))
        minPrice = int(input("Enter minPrice: "))
        maxPrice = int(input("Enter maxPrice: "))
        url = 'https://votpumzhh8.execute-api.ap-south-1.amazonaws.com/live/add'
        payload = {'symbol':symbol, 'minPrice':minPrice, 'maxPrice':maxPrice}
        response = requests.get(url = url, params = payload,headers = header)
        
        if (response.ok):
            print("Entry added\n")
        else:
            print(response)
    
    if (option == 3):
        symbol = str(input("Enter symbol (eg. INFY.NS): "))
        url = 'https://votpumzhh8.execute-api.ap-south-1.amazonaws.com/live/remove'
        payload = {'symbol':symbol}
        response = requests.get(url = url, params = payload, headers = header)

        if(response.ok):
            print("Entry removed\n")
        else:
            print(response)

    if (option == 4):
        break
        
        
