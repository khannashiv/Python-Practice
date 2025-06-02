# Import necessary libraries
from flask import Flask
import requests                          # Library to make HTTP requests
from requests.auth import HTTPBasicAuth  # For HTTP Basic Authentication
import json                              # To handle JSON data
import os                                # For interacting with the operating system (e.g., to load environment variables)
from dotenv import load_dotenv           # For loading environment variables from a .env file


# Create a Flask application instance
app = Flask(__name__) 

# Define a route for the root URL ("/")
@app.route('/CreateJIRA', methods=['POST'])  # This route will handle POST requests to /CreateJIRA

# Define the function that will be called when this route is accessed
def Create_Jira():
    
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

    return f"Response Body: {json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(',', ': '))}"


# Run the Flask application
if __name__ == '__main__':
    app.run('0.0.0.0', port=9000, debug=True)  # Set debug=True for development; it will auto-reload on code changes