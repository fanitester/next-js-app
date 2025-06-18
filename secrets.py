# leaky_module.py

# Simulated business logic
def charge_user():
    print("Charging user with Stripe...")
    # Dummy Stripe secret key (pattern matched by Gitleaks)
    stripe_key = "sk_live_51H8eQmCqZnKqP3EXAMPLEKEYABCDEFG"

# Apple Developer private key (fake)
apple_key = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BA...\n-----END PRIVATE KEY-----"

# Hardcoded JWT (test token, not real)
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0..."  # triggers Gitleaks

# AWS Access Key ID and Secret (fake)
aws_access_key = "AKIAIOSFODNN7EXAMPLE"
aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Fake RSA private key (will definitely trigger Gitleaks)
private_key = '''
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEArE7f1kR5H+F9x3F1pQhCwzMj7f2lP9D0rkB...
-----END RSA PRIVATE KEY-----
'''

def send_to_cloud():
    print("Sending data with AWS credentials...")
    print(f"Key: {aws_access_key}")
    print(f"Secret: {aws_secret_key}")

if __name__ == "__main__":
    charge_user()
    send_to_cloud()

