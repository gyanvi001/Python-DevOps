# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import os

from requests.auth import HTTPBasicAuth
import json

url = "https://gyanvi-pandey.atlassian.net/rest/api/3/project"

API_Token = os.getenv("JIRA_API_TOKEN")
auth = HTTPBasicAuth("gyanvipandey1999@gmail.com", API_Token)


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