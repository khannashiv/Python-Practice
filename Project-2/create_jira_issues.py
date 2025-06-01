import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url = "https://shiventerprise.atlassian.net/rest/api/3/issue"
email = "shiv.khanna29@gmail.com"
api_token = os.getenv("JIRA_API_TOKEN")
auth = HTTPBasicAuth(email, api_token)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Updated payload with formatted description
payload = json.dumps({
    "fields": {
        "issuetype": {"id": "10009"},
        "project": {"key": "SP1"},
        #"project": {"id": "10001"},
        "summary": "Dummy issue for testing"
    }
})

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)


print("Response Body:", json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
