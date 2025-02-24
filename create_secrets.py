import os
import base64
import requests
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from dotenv import load_dotenv

# Load GitHub token from environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GIT_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")  # Repo where secrets will be added
GITHUB_OWNER = os.getenv("GITHUB_OWNER")  # Owner (org/user) of the repo

GITHUB_API = "https://api.github.com"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Function to get the repository's public key
def get_public_key():
    url = f"{GITHUB_API}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/actions/secrets/public-key"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch public key: {response.text}")

# Function to encrypt a secret value
def encrypt_secret(public_key, secret_value):
    public_key_bytes = base64.b64decode(public_key["key"])
    
    # Generate RSA key from the public key
    rsa_key = rsa.RSAPublicNumbers(
        e=int.from_bytes(public_key_bytes[:3], byteorder="big"),
        n=int.from_bytes(public_key_bytes[3:], byteorder="big")
    ).public_key()

    encrypted = rsa_key.encrypt(
        secret_value.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

    return base64.b64encode(encrypted).decode()

# Function to create a secret
def create_secret(secret_name, secret_value):
    public_key = get_public_key()
    encrypted_value = encrypt_secret(public_key, secret_value)

    url = f"{GITHUB_API}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/actions/secrets/{secret_name}"
    data = {
        "encrypted_value": encrypted_value,
        "key_id": public_key["key_id"]
    }

    response = requests.put(url, headers=HEADERS, json=data)

    if response.status_code == 201 or response.status_code == 204:
        print(f"✅ Secret '{secret_name}' created successfully!")
    else:
        print(f"❌ Failed to create secret '{secret_name}': {response.text}")

# List of secrets to create
SECRETS = [
    "SECRET_1", "SECRET_2", "SECRET_3", "SECRET_4", "SECRET_5",
    "SECRET_6", "SECRET_7", "SECRET_8", "SECRET_9", "SECRET_10"
]

# Create all secrets with empty values (null for now)
for secret in SECRETS:
    create_secret(secret, "")
