import os
from github import Github, Auth

# ✅ Use Personal Access Token (PAT) for authentication
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Use PAT_TOKEN (not GITHUB_TOKEN)
GITHUB_OWNER = os.getenv("GITHUB_OWNER")  # GitHub username or org name
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY").split("/")[-1]  # Extract repo name

if not GITHUB_TOKEN or not GITHUB_OWNER or not GITHUB_REPOSITORY:
    raise ValueError("❌ Missing environment variables! Check GITHUB_TOKEN, GITHUB_OWNER, and GITHUB_REPOSITORY.")

# ✅ Authenticate with PAT
auth = Auth.Token(GITHUB_TOKEN)
github_client = Github(auth=auth)

try:
    # 🔹 Fetch correct repository (sub-repo created from template)
    repo = github_client.get_repo(f"{GITHUB_OWNER}/{GITHUB_REPOSITORY}")

    # 🔹 Define secrets
    secrets = {
        "SECRET_1": "value1",
        "SECRET_2": "value2",
        "SECRET_3": "value3",
    }

    # 🔹 Create secrets in the repository
    for secret_name, secret_value in secrets.items():
        repo.create_secret(secret_name, secret_value)
        print(f"✅ Secret '{secret_name}' created successfully in {GITHUB_REPOSITORY}")

except Exception as e:
    print(f"❌ Failed to create secrets: {e}")

finally:
    github_client.close()  # Close connection

# from github import Github

# # Authentication is defined via github.Auth
# from github import Auth

# # using an access token
# auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

# # First create a Github instance:

# # Public Web Github
# g = Github(auth=auth)

# # Github Enterprise with custom hostname
# # g = Github(base_url="https://{hostname}/api/v3", auth=auth)

# # Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)

# To close connections after use
# g.close()

# import os
# from github import Github, Auth

# # ✅ Get environment variables
# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# GITHUB_OWNER = os.getenv("GITHUB_OWNER")  # GitHub username or org name
# GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY").split("/")[-1]  # Extract only repo name

# # ✅ Ensure required environment variables are set
# if not GITHUB_TOKEN or not GITHUB_OWNER or not GITHUB_REPOSITORY:
#     raise ValueError("❌ Missing environment variables! Check GITHUB_TOKEN, GITHUB_OWNER, and GITHUB_REPOSITORY.")

# # ✅ Authenticate using Auth.Token()
# auth = Auth.Token(GITHUB_TOKEN)
# github_client = Github(auth=auth)

# try:
#     # 🔹 Print repo details for debugging
#     print(f"🔹 Fetching repository: {GITHUB_OWNER}/{GITHUB_REPOSITORY}")

#     # 🔹 Get the repository object
#     repo = github_client.get_repo(f"{GITHUB_OWNER}/{GITHUB_REPOSITORY}")

#     # 🔹 Define secrets with empty values
#     secrets = {
#         "SECRET_1": "value1",
#         "SECRET_2": "value2",
#         "SECRET_3": "value3",
#         "SECRET_4": "value4",
#         "SECRET_5": "value5",
#     }

#     # 🔹 Add secrets to GitHub
#     for secret_name, secret_value in secrets.items():
#         repo.create_secret(secret_name, secret_value)
#         print(f"✅ Secret '{secret_name}' created successfully in {GITHUB_REPOSITORY}")

# except Exception as e:
#     print(f"❌ Failed to create secrets: {e}")

# finally:
#     github_client.close()  # Close the connection




