# Import the requests library for making HTTP requests
import requests

# Import HTTPBasicAuth to handle basic authentication (email + API token)
from requests.auth import HTTPBasicAuth

# Import json for parsing and pretty-printing JSON responses
import json

# Import os to access environment variables
import os

# Import dotenv to load variables from a .env file
from dotenv import load_dotenv

# -------------------------------------
# Load environment variables from a `.env` file located in the same directory
# This allows you to keep sensitive info (like API tokens) out of your code
# -------------------------------------
load_dotenv()

# -------------------------------------
# Set up the Jira API URL
# This is the endpoint to list all projects
# You can replace this with another endpoint (e.g., /project/search) for more options
# -------------------------------------
url = "https://shiventerprise.atlassian.net/rest/api/3/project"

# Your Atlassian (Jira) account email address
email = "shiv.khanna29@gmail.com"

# Read the Jira API token from the loaded environment variables
api_token = os.getenv("JIRA_API_TOKEN")

# -------------------------------------
# Set up HTTP Basic Auth using email and token
# Jira requires email + API token for authentication
# -------------------------------------
auth = HTTPBasicAuth(email, api_token)

# -------------------------------------
# Set HTTP headers
# Accept: application/json tells the server we want the response in JSON format
# -------------------------------------
headers = {
    "Accept": "application/json"
}

# -------------------------------------
# Make the GET request to the Jira API
# Pass in the URL, headers, and authentication
# -------------------------------------
response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)

#--------------------------------------
# The response object returned by requests.get(), requests.post(), etc. is an instance of requests.models.Response.
# You can use dir() to see all the attributes and methods available in the response object.
# print(type(response))  # Print the type of the response object, for example, it should be <class 'requests.models.Response'>
# print(dir(response)) # Uncomment this line to see all attributes and methods of the response object
#--------------------------------------

# -------------------------------------
# Optionally, you can print the token for debugging (but avoid in production)
# print(os.getenv("JIRA_API_TOKEN"))
# -------------------------------------

# -------------------------------------
# Convert the response text (which is a JSON string) into a Python object,
# then pretty-print it as formatted JSON with indentation.
# This makes the output human-readable.
# -------------------------------------
print(json.dumps(
    json.loads(response.text),  # Convert raw JSON string to Python dict
    sort_keys=True,             # Sort keys alphabetically
    indent=4,                   # Indent output for readability
    separators=(",", ": ")      # Use custom separators (comma, colon with space)
))
# -------------------------------------

output_1 = json.loads(response.text) # This will convert the JSON response into a Python list of dictionaries
# print(f'Name of my first project is  - ', output_1[0]["name"]) # This will print the name of the first project
# print(f'Name of my second project is - ', output_1[1]["name"]) # This will print the name of the second project

# Loop through the list of projects and print the name of each project

# Method 1: Using a for loop with range
for i in range(len(output_1)):
    # print(type(i))    # This will print the type of i, which is an integer
    # print(i)          # This will print the index of the project
    print(f'Project {i+1} name is - ', output_1[i]["name"])

# Method 2: Using a for loop to iterate through the list directly
for i in output_1:
    # print(type(i)) # This will print the type of i, which is a dictionary
    print(i["name"])  # This will print the name of each project in the list
