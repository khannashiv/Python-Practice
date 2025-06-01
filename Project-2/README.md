# Project-2

This project provides scripts and instructions to retrieve all Jira projects using Python. The guide below covers environment setup, dependency installation, and script execution.

---

## 📁 Directory Structure

```
Project-2/
│
├── get_jira_projects.py
├── .env
└── .gitignore
|__ create_jira_issues.py

```

---

## 🚀 Setup & Usage Instructions

1. **Create a `.env` file:**  
   Add the necessary environment variables (e.g., API credentials) required by the script.

2. **Ignore `.env` in version control:**  
   Add `.env` to your `.gitignore` file to keep sensitive data out of your repository.

3. **Install dependencies:**  
   Run the following command to install the required package:
   ```
   pip install python-dotenv
   ```

4. **Run the script:**  
   Execute the script with:
   ```
   python get_all_projects.py
   ```

---

## 📚 References

- [Jira REST API (Projects)](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-get)
- [Jira REST API (Create Issue)](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Requests Quickstart: Make a Request](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request)
- [How to Get the ID of a Jira Project from a Web Browser](https://support.atlassian.com/jira/kb/how-to-get-the-id-of-a-jira-project-from-a-web-browser/)
- [Sample Jira Project API Response (SP1)](https://shiventerprise.atlassian.net/rest/api/latest/project/SP1)

---

> Refer to this guide whenever setting up or running Project-2.