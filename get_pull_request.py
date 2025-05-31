import requests

respose=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(f"Printing the reponse using json function which will eventually convert output to dictionary.", respose.json())
print("Printing the headers of pull request api call", respose.headers)
print("Printing the response code of pull request api call", respose.status_code)