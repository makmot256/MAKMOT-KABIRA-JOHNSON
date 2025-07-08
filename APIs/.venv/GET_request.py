#GET MEANS # GET means to retrieve data from a server
# GET is used to request data from a specified resource.

#example of api request
import requests
# Define the URL for the GET request
url = 'https://jsonplaceholder.typicode.com/posts/1'
# Send the GET request
response = requests.get(url)    
# Check if the request was successful
if response.status_code == 200:
    print('GET request was successful.')
    print('Response JSON:', response.json())
else:
    print('GET request failed with status code:', response.status_code)
    print('Response:', response.text)   
# This code sends a GET request to a placeholder API and prints the response.
# GET requests are typically used to retrieve data from a server without modifying it.
# GET requests are idempotent, meaning that multiple identical requests should have the same effect as a single request.
# GET requests can include query parameters in the URL to filter or modify the data being retrieved.