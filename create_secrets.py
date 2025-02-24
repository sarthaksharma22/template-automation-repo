import os
from github import Github

# Fetch environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")  # Contains "owner/repo"

if not GITHUB_TOKEN or not GITHUB_REPOSITORY:
    raise ValueError("❌ Missing required environment variables: GITHUB_TOKEN or GITHUB_REPOSITORY.")

# Initialize GitHub API client
github_client = Github(GITHUB_TOKEN)

try:
    # Get the target repository
    repo = github_client.get_repo(GITHUB_REPOSITORY)  # No need to concatenate owner

    # Define secrets with empty values
    secrets = {f"SECRET_{i}": "" for i in range(1, 11)}

    # Create secrets in the repository
    for secret_name, secret_value in secrets.items():
        repo.create_secret(secret_name, secret_value)
        print(f"✅ Secret '{secret_name}' created successfully in {GITHUB_REPOSITORY}")

except Exception as e:
    print(f"❌ Failed to create secrets: {e}")
