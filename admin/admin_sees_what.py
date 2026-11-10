# Imports
from admin.add_user import add_user
from admin.delete_user import delete_user
from admin.edit_userinfo import edit_userinfo
from admin.view_all_users import view_all_users

# Names Variables


# Code

def admin_sees_choices():
    print("Admin can see the following choices:")
    print("1. View all users")
    print("2. Add a new user")
    print("3. Delete a user")
    print("4. Edit user information")
    print("5. Logout")
    print("Q! Quit program")

def admin_chooses_users():
    view_all_users()

def admin_chooses_add_user():
    add_user()

def admin_chooses_delete_user():
    delete_user()

def admin_chooses_logout():
    print("Admin has chosen to logout.")