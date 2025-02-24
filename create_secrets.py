import os
from github import Github

# ✅ Load environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")  # Corrected to fetch the repository name

if not GITHUB_TOKEN or not GITHUB_OWNER or not GITHUB_REPOSITORY:
    raise ValueError("❌ Missing required environment variables! Check GITHUB_TOKEN, GITHUB_OWNER, and GITHUB_REPOSITORY.")

# ✅ Authenticate with GitHub API
github_client = Github(GITHUB_TOKEN)

try:
    print(f"🔹 Fetching repository: {GITHUB_OWNER}/{GITHUB_REPOSITORY}")
    
    # 🔹 Get the repository object
    repo = github_client.get_repo(f"{GITHUB_OWNER}/{GITHUB_REPOSITORY}")

    # 🔹 Define 10 secrets with empty values
    secrets = {
        "SECRET_1": "",
        "SECRET_2": "",
        "SECRET_3": "",
        "SECRET_4": "",
        "SECRET_5": "",
        "SECRET_6": "",
        "SECRET_7": "",
        "SECRET_8": "",
        "SECRET_9": "",
        "SECRET_10": "",
    }

    # 🔹 Add secrets to the repository
    for secret_name, secret_value in secrets.items():
        repo.set_secret(secret_name, secret_value)  # Corrected secret creation method
        print(f"✅ Secret '{secret_name}' created successfully in {GITHUB_REPOSITORY}")

except Exception as e:
    print(f"❌ Failed to create secrets: {e}")
