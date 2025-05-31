# Calculating the pull request count for each user in the Kubernetes repository
# This script retrieves pull requests from the Kubernetes repository on GitHub and counts how many pull requests each user has made.
# The keys in the dictionary are the user's login names (e.g. 'Kevinz857', 'googs1025').
# The values are the counts of how many pull requests each user has made.

import requests

# Define the URL for GitHub API to get pull requests from the 'kubernetes/kubernetes' repository
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

# Send an HTTP GET request to the GitHub API to fetch pull requests data
response = requests.get(url)

# Print the response status code to check if the request was successful
print(response)

# Print the type of the response object (it should be <class 'requests.models.Response'>)
print(type(response))

# Parse the JSON response to get the list of pull requests
output = response.json()

# Print the type of the output (it should be a list of dictionaries)
print(type(output))

# Initialize a dictionary to store the count of pull requests made by each user
user_count = {}

# Loop through each pull request in the output (the list of pull requests)
for pr in output:
    # Extract the login name of the user who made the pull request
    user_login = pr['user']['login']

    # Check if the user already exists in the dictionary (i.e., if they've made a pull request before)
    if user_login in user_count:
        # If user exists, increment their pull request count by 1
        user_count[user_login] += 1
    else:
        # If user doesn't exist, add them to the dictionary with an initial pull request count of 1
        user_count[user_login] = 1

# Print the final count of pull requests made by each user
print("Pull request counts for all users:")

# Loop through the dictionary and print each user's login and the number of pull requests they've made
for user, count in user_count.items():
    print(f"{user}: {count}")


    