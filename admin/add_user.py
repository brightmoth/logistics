# Imports
from datetime import date

from admin.user_accounts import USER_FIELDS, hash_password, load_users, save_users

# Names Variables

# Code
def add_user():
    users = load_users()

    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if username == "admin":
        print("That username is reserved.")
        return
    existing_user = next(
        (user for user in users if user["username"] == username), None
    )
    if existing_user:
        if existing_user["password_hash"]:
            print("A user with that username already exists.")
            return

        password = input("Set a password for this existing user: ")
        if not password:
            print("Password cannot be empty.")
            return
        existing_user["password_hash"] = hash_password(password)
        save_users(users)
        print(f"Password set for user {username}.")
        return

    password = input("Enter password: ")
    if not password:
        print("Password cannot be empty.")
        return

    user = {field: "" for field in USER_FIELDS}
    user["username"] = username
    user["password_hash"] = hash_password(password)
    for field in USER_FIELDS[1:7]:
        user[field] = input(f"Enter {field.replace('_', ' ')}: ").strip()
    user["registration_date"] = date.today().isoformat()

    users.append(user)
    save_users(users)

    print(f"User {username} was added.")
