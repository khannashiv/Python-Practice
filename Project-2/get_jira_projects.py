# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

url   = "https://shiventerprise.atlassian.net/rest/api/3/project"
email = "shiv.khanna29@gmail.com"

# Load environment variables from .env file
load_dotenv()

auth = HTTPBasicAuth(email, os.getenv("JIRA_API_TOKEN"))

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(os.getenv("JIRA_API_TOKEN")) --- > For debugging purposes, you can uncomment this line to see the token
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))