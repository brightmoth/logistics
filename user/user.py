# imports
import csv
from datetime import date, datetime
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


def create_shipment(username):
    destination = input("Enter the shipment destination: ").strip()
    while not destination:
        print("Destination cannot be empty.")
        destination = input("Enter the shipment destination: ").strip()

    estimated_delivery_date = input(
        "Enter the estimated delivery date (YYYY-MM-DD): "
    ).strip()
    while True:
        try:
            parsed_date = datetime.strptime(estimated_delivery_date, "%Y-%m-%d")
            if parsed_date.strftime("%Y-%m-%d") != estimated_delivery_date:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format.")
            estimated_delivery_date = input(
                "Enter the estimated delivery date (YYYY-MM-DD): "
            ).strip()

    fields, shipments = _load_shipments()
    if not fields:
        fields = SHIPMENT_FIELDS.copy() + ["username"]
    else:
        fields = list(fields)
        if "username" not in fields:
            for shipment in shipments:
                shipment["username"] = "user"
        for field in SHIPMENT_FIELDS:
            if field not in fields:
                fields.append(field)
        if "username" not in fields:
            fields.append("username")

    existing_numbers = {
        shipment.get("shipment_number", "").strip() for shipment in shipments
    }
    shipment_number = 1
    while f"SP-{shipment_number:06d}" in existing_numbers:
        shipment_number += 1

    today = date.today().isoformat()
    shipment = {
        "shipment_number": f"SP-{shipment_number:06d}",
        "status": "Booked",
        "creation_date": today,
        "destination": destination,
        "estimated_delivery_date": estimated_delivery_date,
        "current_location": "Pending pickup",
        "last_updated": today,
        "username": username,
    }
    shipments.append(shipment)

    with SHIPMENTS_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(shipments)

    print(f"Shipment {shipment['shipment_number']} created successfully.")
