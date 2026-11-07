# Imports

from admin.user_accounts import USER_FIELDS, load_users

# Names Variables

# Code
def view_all_users():
    users = load_users()
    if not users:
        print("There are no users to display.")
        return

    display_fields = [field for field in USER_FIELDS if field != "password_hash"]
    for user in users:
        print(", ".join(f"{field}: {user[field]}" for field in display_fields))