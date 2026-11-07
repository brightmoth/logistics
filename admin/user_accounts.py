# Imports
import csv
import hashlib
import hmac
import secrets
from pathlib import Path

# Names Variables
USERS_FILE = Path(__file__).resolve().parents[1] / "user" / "users.csv"
USER_FIELDS = [
    "username",
    "email",
    "phone_number",
    "address",
    "postalcode",
    "date_of_birth",
    "gender",
    "registration_date",
    "password_hash",
]
PASSWORD_HASH_ITERATIONS = 200_000

# Code
def load_users():
    with USERS_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        return [
            {
                field: (row.get(field) or "").strip()
                for field in USER_FIELDS
            }
            for row in reader
        ]


def save_users(users):
    with USERS_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=USER_FIELDS)
        writer.writeheader()
        writer.writerows(users)


def hash_password(password):
    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PASSWORD_HASH_ITERATIONS
    )
    return (
        f"pbkdf2_sha256${PASSWORD_HASH_ITERATIONS}"
        f"${salt.hex()}${password_hash.hex()}"
    )


def verify_password(password, stored_hash):
    try:
        algorithm, iterations, salt_hex, hash_hex = stored_hash.split("$")
        if algorithm != "pbkdf2_sha256":
            return False
        salt = bytes.fromhex(salt_hex)
        expected_hash = bytes.fromhex(hash_hex)
        actual_hash = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, int(iterations)
        )
    except (ValueError, TypeError):
        return False

    return hmac.compare_digest(actual_hash, expected_hash)


def authenticate_user(username, password):
    return any(
        user["username"] == username
        and user["password_hash"]
        and verify_password(password, user["password_hash"])
        for user in load_users()
    )
