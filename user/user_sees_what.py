# Imports
from user.user import create_shipment, track_a_shipment, view_my_shipments

# Names Variables

# Code

def user_sees_choices():
    print("User can see the following choices:")
    print("1. View my shipments")
    print("2. Track a shipment")
    print("3. Create a shipment")
    print("4. Logout")
    print("Q! Quit program")


def user_chooses_shipments(username):
    view_my_shipments(username)


def user_chooses_tracking(username):
    track_a_shipment(username)


def user_creates_shipment(username):
    create_shipment(username)


def user_chooses_logout():
    print("User has chosen to logout.")