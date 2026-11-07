# Imports

from admin.user_accounts import load_users, save_users

# Names Variables

# Code
def delete_user():
    username = input("Enter the username to delete: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    users = load_users()

    remaining_users = [user for user in users if user["username"] != username]
    if len(remaining_users) == len(users):
        print(f"User {username} was not found.")
        return

    save_users(remaining_users)

    print(f"User {username} was deleted.")