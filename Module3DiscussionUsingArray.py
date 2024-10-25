from array import array

# Arrays to store product details as numbers
product_ids = array('i', [80, 81, 82])
prices = array('f', [10.99, 15.99, 8.99])
quantities = array('i', [100, 50, 200])


for i in range(len(product_ids)):
    print(f"Product ID (ASCII): {product_ids[i]}")
    print(f"Price: ${prices[i]:.2f}, Quantity: {quantities[i]}")
    print("----")
