# Project-3: Automating GitHub–Jira Integration

This project automates the integration between GitHub and Jira. Whenever a user comments `/jira` under a GitHub issue and selects a particular Jira issue, the integration triggers actions that connect GitHub issue activity to Jira seamlessly.

---

## 🛠️ Project Overview

- **Purpose:**  
  Automate the process of linking GitHub issues with Jira tickets using a webhook and a Python Flask server.

- **How it Works:**  
  1. A user comments `/jira` on a GitHub issue and selects a Jira issue.
  2. GitHub sends a webhook payload (type: "Issue comments") to an EC2 server.
  3. The EC2 server, running a Flask application, processes the payload and interacts with Jira as required.

---

## 📋 Prerequisites

- **AWS EC2 instance** (Ubuntu recommended)
- **Python 3.x** installed
- **GitHub repository** with webhook configured (event: "Issue comments")
- **Jira account** with API access
- **Jira API credentials** (for authentication)
- **Flask** (Python web framework)

---

## 🚀 Setup & Usage Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/khannashiv/Python-Practice.git
cd Python-Practice/Project-3
```

### 2. Create & Activate a Virtual Environment

```bash
python3 -m venv myenv         # Create a virtual environment named 'myenv'
source myenv/bin/activate     # Activate the virtual environment
```

### 3. Install Dependencies

```bash
pip install flask
# Add any other requirements here, e.g.:
# pip install requests python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file (if needed) to store sensitive data such as Jira API credentials.

### 5. Run the Flask Application

```bash
python3 <your_flask_script.py>
# Example:
# python3 one.py
```

### 6. Webhook Setup

- In your GitHub repository, add a webhook with:
  - **Payload URL:** The public URL of your EC2 server (ensure ports are open and server is accessible)
  - **Content Type:** `application/json`
  - **Event:** `Issue comments`

---

## 🔄 Integration Flow

```mermaid
sequenceDiagram
    participant User
    participant GitHub
    participant EC2_Server
    participant Jira

    User->>GitHub: Comments "/jira" on issue
    GitHub->>EC2_Server: Sends webhook payload (Issue comment event)
    EC2_Server->>Jira: Updates/Links issue via API
    Jira-->>EC2_Server: API Response
    EC2_Server-->>GitHub: (Optional) Comment/Update issue
```

---

## 📷 Outcomes & Screenshots

Below are example screenshots showing the integration in action:

- ![Git-jira-1](../Images/Git-jira-1.png)
- ![Git-jira-2](../Images/Git-jira-2.png)
- ![Git-jira-3](../Images/Git-jira-3.png)
- ![Git-jira-4](../Images/Git-jira-4.png)
- ![Git-jira-5](../Images/Git-jira-5.png)
- ![Git-jira-6](../Images/Git-jira-6.png)
- ![Git-jira-7](../Images/Git-jira-7.png)
- ![Git-jira-8](../Images/Git-jira-8.png)
- ![Git-jira-9](../Images/Git-jira-9.png)

---

## 📝 Notes

- To deactivate the virtual environment:
  ```bash
  deactivate
  ```
- Ensure your EC2 instance allows inbound traffic on the port used by Flask (default: 5000, whereas in our case app is running on 9000).
- For production, consider using a production-ready server (e.g., Gunicorn) and HTTPS.

---

## 📚 References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [GitHub Webhooks](https://docs.github.com/en/webhooks)
- [Jira REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)