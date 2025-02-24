import os
from github import Github

# ✅ Get environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")  
SUB_REPO_NAME = os.getenv("GITHUB_REPOSITORY").split("/")[-1]  # Extract repo name

if not GITHUB_TOKEN or not GITHUB_OWNER or not SUB_REPO_NAME:
    raise ValueError("❌ Missing environment variables! Check GITHUB_TOKEN, GITHUB_OWNER, and GITHUB_REPOSITORY.")

# ✅ Authenticate with GitHub API
github_client = Github(GITHUB_TOKEN)

try:
    print(f"🔹 Fetching repository: {GITHUB_OWNER}/{SUB_REPO_NAME}")

    repo = github_client.get_repo(f"{GITHUB_OWNER}/{SUB_REPO_NAME}")
    print(f"✅ Repository found: {repo.full_name}")

    # 🔹 Define 10 secrets with `null` values
    secrets = {f"SECRET_{i}": "" for i in range(1, 11)}

    # 🔹 Add secrets to GitHub
    for secret_name, secret_value in secrets.items():
        repo.create_secret(secret_name, secret_value)
        print(f"✅ Secret '{secret_name}' created successfully in {SUB_REPO_NAME}")

except Exception as e:
    print(f"❌ Failed to create secrets: {e}")
