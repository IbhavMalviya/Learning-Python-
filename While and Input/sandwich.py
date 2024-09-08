sanwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'beef', 'pastrami']
finished_sandwiches = []
while sanwich_orders:
    current_sandwich = sanwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches are made:")
print(sanwich_orders)