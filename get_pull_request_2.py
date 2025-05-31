# Calculating the pull request count for each user in the Kubernetes repository
# This script retrieves pull requests from the Kubernetes repository on GitHub and counts how many pull requests each user has made.
# The keys in the dictionary are the user's login names (e.g. 'Kevinz857', 'googs1025').
# The values are the counts of how many pull requests each user has made.
import requests
url="https://api.github.com/repos/kubernetes/kubernetes/pulls"
response=requests.get(url)

print(response)
print(type(response))

output = response.json()
print(type(output))

# Initialize a dictionary to track pull request counts for each user
user_count = {}

for pr in output:
    #print(f"User who made pull request: {pr['user']['login']}")
    user_login = pr['user']['login']

    # If user is already in dictionary, increment their count
    if user_login in user_count:
        user_count[user_login] += 1
    else:
        # Otherwise, add the user to the dictionary with an initial count of 1
        user_count[user_login] = 1

# Print the count of pull requests made by each user
print("\nPull request counts for all users:")
for user, count in user_count.items():
    print(f"{user}: {count}")

    