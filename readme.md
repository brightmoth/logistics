# Logistics Management Platform

A logistics management platform that aims to connect shipment administration,
dispatch, tracking, drivers, customers, and billing in one place. This repository
is an early command-line prototype: it currently demonstrates basic account
management and shipment lookup using CSV files. The larger platform described
below is the intended direction, not functionality that is already implemented.

## What works today

- Sign in as an administrator or user.
- Add users, list user details, and delete users from `user/users.csv` through
  the administrator menu.
- Set a password for a user already in the CSV or create a new account. New
  account passwords are stored as salted PBKDF2 hashes.
- Sign in with accounts that have a password hash in the CSV.
- View shipment details and look up a shipment by its shipment number.
- Create shipments by entering a destination and estimated delivery date;
  shipments are saved to the CSV and associated with the signed-in user.
- Enter `Q!` in either role's menu to quit, or choose `4` to log out.

The initial shipment data is in `user/track_shipment.csv`. That sample file does
not yet have an owner column, so its shipment is available only to the built-in
`user` account. Creating the first shipment adds a `username` column and
preserves the sample shipment's built-in user ownership. Users can then see and
track only rows matching their signed-in username.

## Running the prototype

Run from the repository root with Python:

```bash
python main.py
```

The current demonstration logins are:

| Account | Username | Password |
|---|---|---|
| Administrator | `admin` | `admin123` |
| Built-in user | `user` | `user123` |

These credentials are hard-coded for demonstration purposes and are not suitable
for a deployed or publicly accessible system. Users in `user/users.csv` need a
password hash to sign in. For an existing CSV row without one, sign in as the
administrator and use **Add a new user** with that username to set its password.

## Current limitations

- This is a command-line prototype, not a web portal or mobile application.
- The administrator account and its password are hard-coded; account roles and
  permissions are not managed in the CSV.
- User and shipment records use local CSV files, without a database, concurrent
  access controls, or an audit log.
- Shipment data is sample data. There is no live GPS integration, shipment
  status update workflow, or notification system.
- Users can create bookings, but there is no administrator or dispatcher
  workflow for assigning shipments or managing their operational status.
- There is no password reset, account recovery, or production-ready sign-in
  protection.

## Intended platform

The long-term goal is a single logistics platform for operations from booking
through final delivery and billing. The planned capabilities include:

### Shipments, dispatch, and tracking

- Create bookings with pickup and delivery details, cargo, service levels, and
  handling requirements.
- Assign loads to drivers, vehicles, or carriers and support dispatch changes.
- Track shipment status, vehicle progress, and estimated arrival times.
- Notify staff and customers about status changes, delays, and exceptions.
- Capture delivery confirmation, including proof of delivery (POD).

### Fleet, drivers, and warehouses

- Manage drivers, vehicles, availability, capacity, servicing, inspections, and
  fuel records.
- Give drivers a mobile workflow for assigned jobs, status updates, navigation,
  POD capture, and work-hour logging.
- Manage warehouse receiving, storage, picking, packing, loading, and inventory.
- Support barcode or QR scanning and shipment-linked inventory records.

### Billing, documents, and reporting

- Calculate freight charges and prepare invoices while tracking payment status.
- Store shipment documents such as bills of lading (BOLs), permits, customs
  paperwork, receipts, and PODs.
- Keep an audit trail for important record changes.
- Report on on-time delivery (OTD), costs, vehicle utilization, carrier
  performance, and shipment profitability.

### Portals and integrations

- Provide role-appropriate tools for dispatchers, drivers, customers, carriers,
  finance staff, and administrators.
- Add customer booking, tracking, document uploads, invoice viewing, and support.
- Support mobile and offline driver workflows.
- Integrate with mapping, messaging, accounting, customer-management, and
  carrier systems as the platform develops.

## Suggested next steps

1. Add shipment creation and assignment so each shipment has an owning username.
2. Replace CSV storage with a database and validate records consistently.
3. Move administrator credentials into a secure account and role system.
4. Add shipment status updates and delivery confirmation.
5. Build dispatcher, driver, and customer interfaces around the shared shipment
   records.
6. Add integrations, notifications, billing, and reporting incrementally.

## Abbreviations

- **POD:** Proof of delivery.
- **BOL:** Bill of lading.
- **OTD:** On-time delivery.
