# import os
# from github import Github

# # ✅ Get environment variables
# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# GITHUB_OWNER = os.getenv("GITHUB_OWNER")  # Template repo owner
# SUB_REPO_NAME = os.getenv("GITHUB_REPOSITORY")  # Auto-detects the repo name

# if not GITHUB_TOKEN or not GITHUB_OWNER or not SUB_REPO_NAME:
#     raise ValueError("❌ Missing environment variables! Check GITHUB_TOKEN, GITHUB_OWNER, and GITHUB_REPOSITORY.")

# # ✅ Authenticate with GitHub API
# github_client = Github(GITHUB_TOKEN)

# try:
#     # 🔹 Get the repository object (sub-repo created from template)
#     repo = github_client.get_repo(f"{GITHUB_OWNER}/{SUB_REPO_NAME}")

#     # 🔹 Define 10 secrets with null values
#     secrets = {
#         "SECRET_1": "",
#         "SECRET_2": "",
#         "SECRET_3": "",
#         "SECRET_4": "",
#         "SECRET_5": "",
#         "SECRET_6": "",
#         "SECRET_7": "",
#         "SECRET_8": "",
#         "SECRET_9": "",
#         "SECRET_10": "",
#     }

#     # 🔹 Add secrets to GitHub
#     for secret_name, secret_value in secrets.items():
#         print(f"✅ Secret '{secret_name}' created successfully in {SUB_REPO_NAME}")
#         # repo.create_secret(secret_name, secret_value,"actions")

# except Exception as e:
#     print(f"❌ Failed to create secrets: {e}")




import os
from github import Github
from github import Auth

# Authentication using an access token
auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

# Instantiate the Github client with the access token
g = Github(auth=auth)

# Function to test authentication by listing repos
def test_authentication():
    try:
        # Get the authenticated user's repositories
        repos = g.get_user().get_repos()
        if repos:
            print("Authentication successful! Repositories:")
            for repo in repos:
                print(repo.name)  # Print the name of each repository
        else:
            print("No repositories found.")
    except Exception as e:
        print(f"Error: {e}")

# Run the test
test_authentication()

