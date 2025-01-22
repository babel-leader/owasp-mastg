import requests
import os

GITHUB_REPO = "OWASP/owasp-mastg"

# GitHub API Token for Authentication
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set")

# GitHub API headers
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

def get_latest_successful_run(workflow_file):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/workflows/{workflow_file}/runs"
    params = {"status": "success", "per_page": 1}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    runs = response.json()["workflow_runs"]
    if runs:
        return f"{runs[0]["html_url"]}#artifacts"
    else:
        return None