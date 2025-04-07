#Get the pull request info form the git hub repo using python

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_details = response.json()

for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"]);

