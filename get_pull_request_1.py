import requests
respose=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(respose)
print(type(respose))

complete_details = respose.json()
print(type(complete_details))

#### Method 1.

# This code iterates over the complete_details list, where each element is a dictionary containing information about a GitHub pull request. 
# For every pull request in the list, the code prints several key details: the pull request's ID, title, state (such as open or closed), creation date, the username of the user who created the pull request, and the URL to view the pull request on GitHub. 
# Each of these values is accessed using the appropriate key in the dictionary.
# After printing the details for each pull request, a line of dashes is printed to visually separate the output for each entry, making the results easier to read. Finally, an empty print() statement is used to add a blank line after all pull requests have been listed, improving the readability of the output in the terminal or output pane. 
# This approach is clear and Pythonic, as it directly iterates over the list elements rather than using indices.

for pull_request in complete_details:
    print(f"Pull Request ID: {pull_request['id']}")
    print(f"Title: {pull_request['title']}")
    print(f"State: {pull_request['state']}")
    print(f"Created At: {pull_request['created_at']}")
    print(f"User: {pull_request['user']['login']}")
    print(f"URL: {pull_request['html_url']}")
    print("--------------------------------------------------")
print()

### Method 2.

# This code iterates over a list called complete_details, which contains information about GitHub pull requests. 
# The loop uses range(len(complete_details)) to generate indices for each element in the list, allowing access to each pull request dictionary by its index.
# Inside the loop,the code prints several details for each pull request. 
# It accesses and displays the pull request's ID, title, state (such as open or closed), creation date, the username of the user who created the pull request, and the URL to the pull request on GitHub.
# Each piece of information is retrieved from the corresponding dictionary using its key. After printing the details for one pull request, a line of dashes is printed to visually separate the output for each pull request.
# This approach is functionally similar to iterating directly over the list elements (using for pull_request in complete_details:), but uses indices instead.
# Using indices can be helpful if you need to know the position of each item or if you plan to modify the list during iteration, but for simple read-only access, direct iteration is usually more Pythonic and readable.
for i in range(len(complete_details)):
    print(f"Pull Request ID: {complete_details[i]['id']}")
    print(f"Title: {complete_details[i]['title']}")
    print(f"State: {complete_details[i]['state']}")
    print(f"Created At: {complete_details[i]['created_at']}")
    print(f"User: {complete_details[i]['user']['login']}")
    print(f"URL: {complete_details[i]['html_url']}")
    print("--------------------------------------------------")


################### PRACTICE ######################

# print(f"Printing the reponse using json function which will eventually convert output to dictionary.", respose.json())
# print("Printing the headers of pull request api call", respose.headers)
# print("Printing the response code of pull request i.e. ", respose.status_code)

# print(complete_details[0]) # This will print the first pull request details as a dictionary.
# print(complete_details[0]["title"])
# print(complete_details[0]["user"]["login"])

# for i in complete_details:
#     print(i["user"]["login"], i["title"], i["state"], i["created_at"], i["html_url"])

# for j in complete_details:
#     print(j["user"]["login"])

# print(f"Total length/number of pull requests per page: {len(complete_details)}")
# print(f"Total range of pull requests per page: {range(len(complete_details))}")
# print(f"Range of pull requests: {complete_details[0]['number']} to {complete_details[-1]['number']}")