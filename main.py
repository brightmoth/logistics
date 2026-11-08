# Imports
from admin.user_accounts import authenticate_user
from admin.admin_sees_what import (
    admin_chooses_add_user,
    admin_chooses_delete_user,
    admin_chooses_logout,
    admin_chooses_users,
    admin_sees_choices,
)
from user.user_sees_what import (
    user_chooses_logout,
    user_creates_shipment,
    user_chooses_shipments,
    user_chooses_tracking,
    user_sees_choices,
)

# Names Variables
quit_program = False

# Code
print("Current account types include: Admin and User")
while not quit_program:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "admin123":
        print("Welcome Admin!")
        while not quit_program:
            admin_sees_choices()
            admin_choice = input("Choose an option: ")

            if admin_choice.strip().upper() == "Q!":
                quit_program = True
                break
            elif admin_choice == "1":
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
    elif (username == "user" and password == "user123") or authenticate_user(
        username, password
    ):
        print("Welcome User!")
        while not quit_program:
            user_sees_choices()
            user_choice = input("Choose an option: ")

            if user_choice.strip().upper() == "Q!":
                quit_program = True
                break
            elif user_choice == "1":
                user_chooses_shipments(username)
            elif user_choice == "2":
                user_chooses_tracking(username)
            elif user_choice == "3":
                user_creates_shipment(username)
            elif user_choice == "4":
                user_chooses_logout()
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password. Please try again.")