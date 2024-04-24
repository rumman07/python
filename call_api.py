from requests.auth import HTTPBasicAuth
import requests
import os 

api_key = os.environ.get("pat_token")
auth = HTTPBasicAuth('apikey', api_key)
req = requests.get("https://dev.azure.com/udemydevopscourse/testazuredevops/_apis/git/repositories?api-version=6.0",auth=auth)
print(req.json())