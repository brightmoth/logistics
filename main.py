# Imports



# Named Variables

continue_using = True
username_admin = "admin"
username_user = "user"
password_admin = "admin123"
password_user = "user123"

path_to_users_file = "users.csv"
path_to_users_status_file = "users_status.csv"

options_for_admin = [
    "1. View Users",
    "2. Add User",
    "3. Remove User",
    "4. Approve/Reject User",
    "5. Exit"
]

options_for_user = [
    "1. Create Account",
    "2. View Profile",
    "3. Update Profile",
    "4. Change Password",
    "5. Exit"
]

# Code

while continue_using:
    print("welcome to the logistics app v0.1")
    print("Please select your role:")
    print("1. Admin")
    print("2. User")
    role_selection = input("Enter your choice (1 or 2): ")

    print(f"You have selected: {role_selection}")

    if role_selection == "1":
        print("Please enter the username and password before continuing.")
        username = input("Username: ")
        password = input("Password: ")

        if username == username_admin and password == password_admin:
            print("Login successful! Welcome, Admin.")
            while continue_using:
                print("Here are your options:")
                for option in options_for_admin:
                    print(option)
                admin_choice = input("Enter your choice: ")

                if admin_choice == "4":
                    continue_using = False
                elif admin_choice in {"1", "2", "3"}:
                    print(f"You selected: {options_for_admin[int(admin_choice) - 1]}")
                else:
                    print("Invalid selection. Please try again.")
        else:
            print("Invalid username or password.")
            retry = input("Would you like to try again? (y/n): ").lower()
            if retry != "y":
                continue_using = False
    elif role_selection == "2":
        print("Please enter the username and password before continuing.")
        username = input("Username: ")
        password = input("Password: ")

        if username == username_user and password == password_user:
            print("Login successful! Welcome, User.")
            while continue_using:
                print("Here are your options:")
                for option in options_for_user:
                    print(option)
                user_choice = input("Enter your choice: ")

                if user_choice == "4":
                    continue_using = False
                elif user_choice in {"1", "2", "3"}:
                    print(f"You selected: {options_for_user[int(user_choice) - 1]}")
                else:
                    print("Invalid selection. Please try again.")
        else:
            print("Invalid username or password.")
            retry = input("Would you like to try again? (y/n): ").lower()
            if retry != "y":
                continue_using = False
    else:
        print("Invalid selection. Please try again.")
