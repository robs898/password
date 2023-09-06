import secrets
import string

def generate_password(length=14):
    """https://docs.python.org/3/library/secrets.html"""
    alphabet = f"@#&*-_{string.ascii_letters}{string.digits}"
    while True:
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in "@#&*-_" for c in password)
        ):
            return password
