import requests

x=requests.post("http://saral.navgurukul.org/api/courses")
print(x.text)