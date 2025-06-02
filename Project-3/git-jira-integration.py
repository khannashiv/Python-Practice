# Import necessary libraries
from flask import Flask, request         # Import 'request' to handle incoming data
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

    # Check if the request has content and if it contains the "/jira" command
    data = request.get_json()      # Get the JSON data from the incoming request (from git which is acting as client to flask server) and parse it to a Python dictionary
    print("Received data:", data)  # Print the received data for debugging purposes.
 
    if not data or 'comment' not in data or 'body' not in data['comment']:
        return "Invalid request data. No Jira ticket created."
    
    # Check if the message includes '/jira' (e.g., under the issue description or body)
    if '/jira' in data['comment']['body'].lower():
        # Construct the payload (data) for the new issue to be created
        payload = json.dumps({
            "fields": {
                "issuetype": {"id": "10007"},          # Issue type ID, e.g., 10009 corresponds to "Task" (verify in your Jira instance)
                "project": {"key": "SP1"},             # Project key, replace with your project's key (e.g., 'SP1')
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

        # Return the response from Jira API
        return f"Jira Issue Created: {json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(',', ': '))}"

    else:
        return "No /jira command found. No Jira ticket created."

# Run the Flask application
if __name__ == '__main__':
    app.run('0.0.0.0', port=9000, debug=True)  # Set debug=True for development; it will auto-reload on code changes
