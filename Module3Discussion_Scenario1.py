# Scenario 1: Employee database
employees = [
    {
        "id": "E001",
        "name": "Alice",
        "hourly_rate": 25.5,
        "email": "alice@example.com",
        "phone": "123-456-7890",
        "address": "123 Elm St",
        "bank_info": {
            "account_number": "12345678",
            "routing_number": "87654321",
            "bank_name": "Bank of America",
            "account_type": "Checking"
        }
    },
    {
        "id": "E002",
        "name": "Bob",
        "hourly_rate": 30.0,
        "email": "bob@example.com",
        "phone": "234-567-8901",
        "address": "456 Oak St",
        "bank_info": {
            "account_number": "23456789",
            "routing_number": "98765432",
            "bank_name": "Chase Bank",
            "account_type": "Savings"
        }
    }
]

for employee in employees:
    print(f"ID: {employee['id']}, Name: {employee['name']}, Hourly Rate: ${employee['hourly_rate']}")
    print(f"Email: {employee['email']}, Phone: {employee['phone']}")
    print(f"Address: {employee['address']}")
    print(f"Bank Info - Account: {employee['bank_info']['account_number']}, Bank: {employee['bank_info']['bank_name']}")
    print("----")
