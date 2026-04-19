#!/usr/bin/env python3
# sales_aggregator.py - Aggregates sales data from a list of dictionaries.
# Handles duplicate product IDs by summing quantities and revenues.
# Output is sorted by total revenue in descending order.

# --- Sample Sales Data ---
# Each entry represents a sales transaction with a product_id, name, quantity, and unit price.

sales_data = [
    {"product_id": "P001", "product_name": "Laptop",     "quantity_sold": 5,  "price_per_unit": 999.99},
    {"product_id": "P002", "product_name": "Mouse",      "quantity_sold": 20, "price_per_unit": 25.00},
    {"product_id": "P003", "product_name": "Keyboard",   "quantity_sold": 15, "price_per_unit": 45.00},
    {"product_id": "P001", "product_name": "Laptop",     "quantity_sold": 3,  "price_per_unit": 999.99},  # duplicate P001
    {"product_id": "P004", "product_name": "Monitor",    "quantity_sold": 8,  "price_per_unit": 299.99},
    {"product_id": "P002", "product_name": "Mouse",      "quantity_sold": 10, "price_per_unit": 25.00},   # duplicate P002
    {"product_id": "P005", "product_name": "Webcam",     "quantity_sold": 12, "price_per_unit": 79.99},
    {"product_id": "P003", "product_name": "Keyboard",   "quantity_sold": 5,  "price_per_unit": 45.00},   # duplicate P003
]

# --- Aggregation ---

# Use a dict keyed by product_id to accumulate totals.
# Structure: { product_id: { "product_name": ..., "total_quantity": ..., "total_revenue": ... } }
aggregated = {}

for sale in sales_data:
    pid   = sale["product_id"]
    qty   = sale["quantity_sold"]
    price = sale["price_per_unit"]
    rev   = qty * price  # Revenue for this transaction

    if pid not in aggregated:
        # First time seeing this product — initialise its entry
        aggregated[pid] = {
            "product_name":    sale["product_name"],
            "total_quantity":  qty,
            "total_revenue":   rev,
        }
    else:
        # Duplicate product_id — add to existing totals
        aggregated[pid]["total_quantity"] += qty
        aggregated[pid]["total_revenue"]  += rev

# --- Sort by total revenue descending (bonus) ---
sorted_sales = sorted(aggregated.items(), key=lambda item: item[1]["total_revenue"], reverse=True)

# --- Print Results ---
print(f"{'ID':<8} {'Product':<12} {'Qty Sold':>10} {'Total Revenue':>15}")
print("-" * 50)

for pid, data in sorted_sales:
    print(f"{pid:<8} {data['product_name']:<12} {data['total_quantity']:>10} ${data['total_revenue']:>14,.2f}")

print("-" * 50)

# Grand total across all products
grand_total = sum(d["total_revenue"] for d in aggregated.values())
print(f"{'Grand Total':<22} ${grand_total:>14,.2f}")
