import json

import requests

# IP address to Track
ip_address = 'localhost'

request_url = 'https://geolocation-db.com/jsonp/' \
              + ip_address
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result = json.loads(result)
print("IP Address Location","\n", result)
