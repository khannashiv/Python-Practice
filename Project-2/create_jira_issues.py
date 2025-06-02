"""
===============================================================================
create_jira_issues.py
-------------------------------------------------------------------------------
This script creates a new issue in a Jira project using Jira's REST API v3.
Features:
- Loads Jira credentials (email and API token) from a .env file for security.
- Constructs and sends a POST request to create an issue in the specified Jira project.
- Prints the API response, which contains details about the created issue or error messages.
Requirements:
- requests
- python-dotenv
Environment Variables (to be set in .env file):
- JIRA_EMAIL:     Pull from .env file, your Jira account email.
- JIRA_API_TOKEN: Pull from .env file, your Jira API token.
Usage:
- Update the project key and issue type ID as per your Jira instance.
- Run the script to create a dummy issue in the specified Jira project.
Author: Shiv Kumar Khanna
===============================================================================
"""
# Import necessary libraries
import requests                          # Library to make HTTP requests
from requests.auth import HTTPBasicAuth  # For HTTP Basic Authentication
import json                              # To handle JSON data
import os                    # For interacting with the operating system (e.g., to load environment variables)
from dotenv import load_dotenv           # For loading environment variables from a .env file

# Load environment variables from a .env file (ensure that JIRA_API_TOKEN & JIRA_EMAIL are set in this file)
load_dotenv()

# Jira API endpoint for creating an issue
url = "https://shiventerprise.atlassian.net/rest/api/3/issue"

# Jira login credentials
email = os.getenv("JIRA_EMAIL")          # Your Jira account email
api_token = os.getenv("JIRA_API_TOKEN")  # Jira API token loaded from the .env file (ensure this is set)

# Authentication for Jira using the email and API token
auth = HTTPBasicAuth(email, api_token)

# Headers to specify the content type and what kind of response we expect
headers = {
    "Accept": "application/json",       # Accept JSON responses from Jira
    "Content-Type": "application/json"  # Send the request body in JSON format
}

# Construct the payload (data) for the new issue to be created
payload = json.dumps({
    "fields": {
        "issuetype": {"id": "10007"},          # Issue type ID, e.g., 10009 corresponds to "Task" (verify in your Jira instance)
        "project": {"key": "SP1"},             # Project key, replace with your project's key (e.g., 'SP1')
        #"project": {"id": "10001"},           # Alternatively, you could use project ID (this line is commented out)
        "summary": "Dummy issue for testing"   # Summary of the issue (title)
        # We can add other fields like 'description', 'priority', 'labels' here ...
    }
})

# Make the POST request to Jira's API to create the issue
response = requests.request(
    "POST",           # HTTP method (POST means creating a new issue)
    url,              # URL for Jira API endpoint
    data=payload,     # JSON data to send in the body of the request
    headers=headers,  # Request headers
    auth=auth         # Authentication credentials
)

# Print the response from Jira API (this will include details about the created issue or error messages)
print("Response Body:", json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

