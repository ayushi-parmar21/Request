import requests
import json
response = requests.get('http://saral.navgurukul.org/api/courses')
print(response)