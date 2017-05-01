# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import http.client

connection = http.client.HTTPSConnection("www.google.com")
connection.request("GET", "/")
response = connection.getresponse()
print(response.status, response.reason)
