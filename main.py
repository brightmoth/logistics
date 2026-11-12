# Imports

from pathlib import Path



# Named Variables

continue_using = True
username_admin = "admin"
username_user = "user"
password_admin = "admin123"
password_user = "user123"

path_to_users_file = Path(__file__).resolve().parent / "users.csv"
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



# Need to add
    #Admin option for approve works by looking for user with status "pending" in the users_status.csv file. If found, it will prompt the admin to approve or reject the user. If approved, the user's status will be updated to "approved" in the users_status.csv file. If rejected, the user's status will be updated to "rejected".
    # User filles in info and writes to users.csv, then we automatically add the user to users_status.csv with status "pending". The admin can then approve or reject the user.
    # Admin would use something like:
        # with open("example.txt", "a", encoding="utf-8") as f:
        # f.write("Appended line\n")
    # User needs to following added somehow
        # with open("example.txt", "w", encoding="utf-8") as f:
        # f.write("First line\n")

# Laters problem
    # We will later have it write to a database instead of a csv file, but for now we will use csv files for simplicity.
    # Add cleaner CLI Interface with better formatting and colors for better user experience.(until we have web interface)
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

                if admin_choice == "1":
                    print("You selected: View Users")
                    # Add code to view users from users.csv
                elif admin_choice == "2":
                    print("You selected: Add User")
                    # Add code to add user to users.csv and users_status.csv with status "pending"
                elif admin_choice == "3":
                    print("You selected: Remove User")
                    # Add code to remove user from users.csv and users_status.csv
                elif admin_choice == "4":
                    print("You selected: Approve/Reject User")
                    # Add code to approve or reject user from users_status.csv
                elif admin_choice == "5":
                    continue_using = False
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

                if user_choice == "1":
                    print("You selected: Create Account")
                    username = input("Enter a username: ")
                    password = input("Enter a password: ")
                    email = input("Enter an email: ")
                    company_individual = input("Enter company or individual: ")
                    street_address = input("Enter street address: ")
                    city = input("Enter city: ")
                    province = input("Enter province: ")
                    postal_code = input("Enter postal code: ")

                    with path_to_users_file.open("a", encoding="utf-8") as users_file:
                        users_file.write(f"{username}, {password}, {email}, {company_individual}, {street_address}, {city}, {province}, {postal_code}\n")


                elif user_choice == "2":
                    print("You selected: View Profile")
                    # Add code to view profile from users.csv
                elif user_choice == "3":
                    print("You selected: Update Profile")
                    # Add code to update profile in users.csv
                elif user_choice == "4":
                    print("You selected: Change Password")
                    # Add code to change password in users.csv
                elif user_choice == "5":
                    continue_using = False
                else:
                    print("Invalid selection. Please try again.")
        else:
            print("Invalid username or password.")
            retry = input("Would you like to try again? (y/n): ").lower()
            if retry != "y":
                continue_using = False
    else:
        print("Invalid selection. Please try again.")
