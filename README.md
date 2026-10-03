# E-commerce Order Processor

A Python script that processes order and inventory data to calculate revenue, flag low stock, and check whether pending orders can actually be fulfilled.

## How it works
- Parses orders and inventory from JSON data
- Prints a summary of all orders
- Calculates total revenue from fulfilled orders only
- Flags any inventory item at or below a low-stock threshold
- Cross-references pending orders against current stock to determine if each one can be fulfilled

## How to run
```bash
python order_processor.py
```

## What I learned
- Parsing multiple related JSON datasets and connecting them by a shared field (`product`)
- Using a dictionary comprehension (`{item['product']: item['stock'] for item in inventory}`) to build a fast lookup table
- Filtering and aggregating based on a status field (`fulfilled`, `pending`, `cancelled`)
- Comparing requested quantity against available stock to make a real fulfillment decision
