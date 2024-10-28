# List to store visitor names with arrival times
visitors = [("Alice", "7:05 PM"), ("Bob", "7:10 PM")]

# Adding a new visitor
visitors.append(("Charlie", "7:15 PM"))

# Display visitor log
for name, time in visitors:
    print(f"Visitor: {name}, Arrived at: {time}")
