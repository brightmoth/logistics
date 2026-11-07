# Imports
from admin.admin_sees_what import (
    admin_chooses_add_user,
    admin_chooses_delete_user,
    admin_chooses_logout,
    admin_chooses_users,
    admin_sees_choices,
)

# Names Variables
continue_program = True
account_type = []
username = []
password = []

# Code
print("current accounts include \n1. Admin\n2. User")
print("To login as admin use username: admin and password: admin123")
print("To login as user use username: user and password: user123")
while continue_program == True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "admin123":
        print("Welcome Admin!")
        while True:
            admin_sees_choices()
            admin_choice = input("Choose an option: ")

            if admin_choice == "1":
                admin_chooses_users()
            elif admin_choice == "2":
                admin_chooses_add_user()
            elif admin_choice == "3":
                admin_chooses_delete_user()
            elif admin_choice == "4":
                admin_chooses_logout()
                break
            else:
                print("Invalid choice. Please try again.")
    elif username == "user" and password == "user123":
        print("Welcome User!")
        continue_program = True
    else:
        print("Invalid username or password. Please try again.")
        continue_program = True