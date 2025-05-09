# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url =  "https://gyanvi-pandey.atlassian.net/rest/api/3/issue"


auth = HTTPBasicAuth("gyanvipandey1999@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": { 
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "E-Commerce Demo",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
     
      "issuetype": {
      "id": "10008"
    },
   
    "project": {
      "key": "ECD"
    },
    "summary": "My First Jira ticket through API",
  },
  "update": {}
} )


response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))




