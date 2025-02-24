import os
from github import Github

# Use GITHUB_TOKEN provided by GitHub Actions
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")  # Sub-repo where secrets will be added
GITHUB_OWNER = os.getenv("GITHUB_OWNER")  # Repo owner

if not GITHUB_TOKEN or not GITHUB_REPO or not GITHUB_OWNER:
    raise ValueError("Missing environment variables! Check GITHUB_TOKEN, GITHUB_REPO, and GITHUB_OWNER.")

# Initialize GitHub SDK with the automatically generated token
github_client = Github(GITHUB_TOKEN)

# Get repository object
repo = github_client.get_repo(f"{GITHUB_OWNER}/{GITHUB_REPO}")

# List of secrets to create
SECRETS = [
    "SECRET_1", "SECRET_2", "SECRET_3", "SECRET_4", "SECRET_5",
    "SECRET_6", "SECRET_7", "SECRET_8", "SECRET_9", "SECRET_10"
]

# Create secrets with null values
for secret_name in SECRETS:
    try:
        repo.create_secret(secret_name, "")
        print(f"✅ Secret '{secret_name}' created successfully in {GITHUB_REPO}")
    except Exception as e:
        print(f"❌ Failed to create secret '{secret_name}': {e}")
