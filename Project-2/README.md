# Project-2
<!--
Project 2 Documentation .

This file provides an overview of Project 2, detailing the objectives, features, and progress made. Under Project 2, we have implemented and documented various Python programming exercises and mini-projects to enhance practical coding skills. The project includes problem statements, solutions, and explanations for each task undertaken, serving as a comprehensive reference for learning and revision.
-->
## 📝 Overview
This project provides Python scripts and step-by-step instructions for automating interactions with Jira via its REST API. We have done the following tasks:

- **Retrieve all Jira projects:** Fetch a list of all projects from your Jira instance for reporting or management purposes.
- **Create Jira issues programmatically:** Automate the creation of issues (tasks, bugs, etc.) in specific projects, saving time and reducing manual effort.

The guide below explains how to set up your environment, securely manage API credentials, install required dependencies, and execute each script independently. Whether you're new to Jira automation or looking to streamline your workflow, this documentation will help you get started quickly and safely.

---

## 📁 Directory Structure

```
Project-2/
│
├── get_jira_projects.py
├── .env
└── .gitignore
|__ create_jira_issues.py
|__ README.md
|__ sample_jira_project.py

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
   Execute the following script one by one since they are independent of each other:
   ```
   python get_jira_projects.py
   python create_jira_issues.py
   python sample_jira_project.py
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