# imports
import csv
from pathlib import Path

# names variable
SHIPMENTS_FILE = Path(__file__).resolve().parent / "track_shipment.csv"
SHIPMENT_FIELDS = [
    "shipment_number",
    "status",
    "creation_date",
    "destination",
    "estimated_delivery_date",
    "current_location",
    "last_updated",
]

# code
def _load_shipments():
    with SHIPMENTS_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        return reader.fieldnames or [], list(reader)


def _user_shipments(username, fields, shipments):
    if "username" not in fields:
        return shipments if username == "user" else []

    return [
        shipment
        for shipment in shipments
        if shipment.get("username", "").strip() == username
    ]


def _display_shipment(shipment, fields):
    display_fields = [field for field in SHIPMENT_FIELDS if field in fields]
    print(
        ", ".join(
            f"{field.replace('_', ' ')}: {(shipment.get(field) or '').strip()}"
            for field in display_fields
        )
    )


def view_my_shipments(username):
    fields, shipments = _load_shipments()
    user_shipments = _user_shipments(username, fields, shipments)
    if not user_shipments:
        print("You have no shipments.")
        return

    for shipment in user_shipments:
        _display_shipment(shipment, fields)


def track_a_shipment(username):
    fields, shipments = _load_shipments()
    shipment_number = input("Enter your shipment number: ").strip()
    for shipment in _user_shipments(username, fields, shipments):
        if shipment.get("shipment_number", "").strip() == shipment_number:
            _display_shipment(shipment, fields)
            return

    print("Shipment not found for your account.")
