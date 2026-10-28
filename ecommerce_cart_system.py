
"""E-commerce shopping cart and checkout utilities."""

import hashlib
import secrets

INITIAL_CART_ITEMS = {
    "ITEM1": {"name": "Wireless Mouse", "price": 25.0, "qty": 2},
    "ITEM2": {"name": "Mechanical Keyboard", "price": 80.0, "qty": 1},
    "ITEM3": {"name": "USB-C Hub", "price": 45.0, "qty": 3},
}

cart_items = INITIAL_CART_ITEMS.copy()
sales_summary = {"total_sales": 0.0}


def add_item_to_cart(item_id, name, price, qty=1, audit_log=None):
    """Add a new item to the cart and optionally record the action."""

    if item_id in cart_items or price < 0 or qty < 1:
        return False

    cart_items[item_id] = {
        "name": name,
        "price": price,
        "qty": qty,
    }
    sales_summary["total_sales"] += price * qty

    if audit_log is not None:
        audit_log.append(f"Added {item_id} with price {price:.2f}")

    return True


def remove_item_from_cart(item_id):
    """Remove an item from the cart if it exists."""
    if item_id not in cart_items:
        return False

    del cart_items[item_id]
    return True


def check_cart_status(item_id):
    """Return whether an item exists in the cart with positive quantity."""
    item = cart_items.get(item_id)
    return item is not None and item["qty"] > 0


def calculate_discounted_total(item_id, discount_rate):
    """Calculate an item's discounted total without evaluating code."""
    if item_id not in cart_items:
        raise KeyError(f"Item not found: {item_id}")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    item = cart_items[item_id]
    return item["price"] * (1 - discount_rate)


def generate_item_hash(item_id):
    """Generate a SHA-256 digest for an item identifier."""
    return hashlib.sha256(item_id.encode("utf-8")).hexdigest()


def generate_checkout_pin():
    """Generate a cryptographically secure four-digit checkout PIN."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_cart_receipt(filename="receipt.txt"):
    """Write the current cart contents to a UTF-8 receipt file."""
    with open(filename, "w", encoding="utf-8") as receipt:
        for item_id, details in cart_items.items():
            line_total = details["price"] * details["qty"]
            receipt.write(
                f"{item_id}: {details['name']} | "
                f"Quantity: {details['qty']} | "
                f"Line total: {line_total:.2f}\n"
            )

    print(f"Receipt saved to: {filename}")


def get_cart_summary(items):
    """Return the total quantity of items with positive quantities."""
    return sum(
        details["qty"]
        for details in items.values()
        if details["qty"] > 0
    )


def main():
    """Demonstrate the shopping cart operations."""
    add_item_to_cart("ITEM4", "Monitor Stand", 35.0, 1)
    remove_item_from_cart("ITEM2")

    print("Is ITEM1 in cart:", check_cart_status("ITEM1"))
    print(
        "Discounted Price:",
        calculate_discounted_total("ITEM1", 0.10),
    )
    print("Item Hash:", generate_item_hash("ITEM1"))
    print("Checkout PIN:", generate_checkout_pin())

    export_cart_receipt()
    print("Total items:", get_cart_summary(cart_items))


if __name__ == "__main__":
    main()
