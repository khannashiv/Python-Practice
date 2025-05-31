import requests

respose=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# print(f"Printing the reponse using json function which will eventually convert output to dictionary.", respose.json())
# print("Printing the headers of pull request api call", respose.headers)
# print("Printing the response code of pull request i.e. ", respose.status_code)
complete_details = respose.json()
print(complete_details[0])
# print(f"Total number of pull requests per page: {len(complete_details)}")
#print(f"Range of pull requests: {complete_details[0]['number']} to {complete_details[-1]['number']}")
# for pull_request in complete_details:
#     print(f"Pull Request ID: {pull_request['id']}")
#     print(f"Title: {pull_request['title']}")
#     print(f"State: {pull_request['state']}")
#     print(f"Created At: {pull_request['created_at']}")
#     print(f"User: {pull_request['user']['login']}")
#     print(f"URL: {pull_request['html_url']}")
#     print("--------------------------------------------------")
# print()