import json

orders_json = '''
[
    {"order_id": "O1001", "product": "T-Shirt", "quantity": 2, "price": 19.99, "status": "fulfilled"},
    {"order_id": "O1002", "product": "Sneakers", "quantity": 1, "price": 59.99, "status": "pending"},
    {"order_id": "O1003", "product": "T-Shirt", "quantity": 3, "price": 19.99, "status": "fulfilled"},
    {"order_id": "O1004", "product": "Backpack", "quantity": 1, "price": 39.99, "status": "cancelled"}
]
'''
inventory_json = '''
[
    {"product": "T-Shirt", "stock": 50},
    {"product": "Sneakers", "stock": 8},
    {"product": "Backpack", "stock": 0}
]
'''

orders = json.loads(orders_json)
inventory = json.loads(inventory_json)

# Print all orders
for order in orders:
    print(f"Order {order['order_id']}: {order['quantity']}x {order['product']} - ${order['price']} ({order['status']})")

# Total revenue from fulfilled orders
total_revenue = 0
for order in orders:
    if order['status'] == 'fulfilled':
        total_revenue += order['quantity'] * order['price']
print(f"\nTotal revenue from fulfilled orders: ${total_revenue:.2f}")

# Low stock alerts
print("\nInventory check:")
low_stock_threshold = 10
for item in inventory:
    if item['stock'] <= low_stock_threshold:
        print(f"⚠️ Low stock alert: {item['product']} has only {item['stock']} left")

# Check if pending orders can be fulfilled
print("\nFulfillment check:")
stock_lookup = {item['product']: item['stock'] for item in inventory}

for order in orders:
    if order['status'] == 'pending':
        product = order['product']
        quantity_needed = order['quantity']
        available_stock = stock_lookup.get(product, 0)
        
        if available_stock >= quantity_needed:
            print(f"✅ Order {order['order_id']} can be fulfilled ({available_stock} in stock)")
        else:
            print(f"❌ Order {order['order_id']} CANNOT be fulfilled - only {available_stock} in stock, needs {quantity_needed}")