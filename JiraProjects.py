# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://gyanvi-pandey.atlassian.net/rest/api/3/project"

api_key = os.getenv("JIRA_TOKEN")
print(api_key)


auth = HTTPBasicAuth("gyanvipandey1999@gmail.com", api_key)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,

   headers=headers,
   auth=auth
)

output = json.loads(response.text)
name = output[1]["name"]
print(name)