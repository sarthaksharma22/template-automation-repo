import os
from github import Github

# Use GitHub Actions' default token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")

if not GITHUB_TOKEN or not GITHUB_REPO or not GITHUB_OWNER:
    raise ValueError("Missing environment variables! Check GITHUB_TOKEN, GITHUB_REPO, and GITHUB_OWNER.")

# Initialize GitHub API client
github_client = Github(GITHUB_TOKEN)

try:
    # Get the repository object
    repo = github_client.get_repo(f"{GITHUB_OWNER}/{GITHUB_REPO}")

    # Define secrets and values
    secrets = {
        "SECRET_1": "",
        "SECRET_2": "",
        "SECRET_3": "",
        "SECRET_4": "",
        "SECRET_5": "",
    }

    # Add secrets
    for secret_name, secret_value in secrets.items():
        repo.create_secret(secret_name, secret_value)
        print(f"✅ Secret '{secret_name}' created successfully in {GITHUB_REPO}")

except Exception as e:
    print(f"❌ Failed to create secrets: {e}")
