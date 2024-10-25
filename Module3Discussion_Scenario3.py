# Database in a Pharmacy
inventory = [
    {"product_id": "P001", "name": "Advil", "price": 10.99, "quantity": 100, "supplier": "Pfizer"},
    {"product_id": "P002", "name": "Tylenol", "price": 15.99, "quantity": 50, "supplier": "Moderna"},
    {"product_id": "P003", "name": "Probiotic", "price": 8.99, "quantity": 200, "supplier": "Novo Nordisk"}
]

for product in inventory:
    print(f"Product ID: {product['product_id']}, Name: {product['name']}")
    print(f"Price: ${product['price']}, Quantity: {product['quantity']}, Supplier: {product['supplier']}")
    print("----")
