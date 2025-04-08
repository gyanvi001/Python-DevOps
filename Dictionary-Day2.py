# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

#Url to fetch pull req from github api
URL = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

#Get the pull req from github api
response = requests.get(URL)



#Only if the response is success 
if(response.status_code == 200):
    #Convert into json format
     pull_req = response.json()

     #Create empty dictionary 
     pr_creators={}

     #Iterate through the pull_requests
     for pull in pull_req:
          creator = pull['user']['login']
          if creator in pr_creators:
               pr_creators[creator] += 1
          else:
               pr_creators[creator] = 1

    
    # Display the dictionary of PR creators and their counts
     print("PR_Creators and the counts :")     
     for creator, count in pr_creators.items():
           print(f"{creator}: {count} PR(s)")
else:
     print(f"Failed to get the data. Status code: {response.status_code}")
     
 


            


               




