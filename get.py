import requests
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json',params=query)
# print(response)
# print(response.content) 
# print(response.text)
# print(response.json() )
# print(response.url)
# print(response.status_code)
# print(response.headers)