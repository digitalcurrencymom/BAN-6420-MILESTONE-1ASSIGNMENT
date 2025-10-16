from policyholder import Policyholder
from product import Product
from payment import Payment

# -------------------------------
# Create Products
# -------------------------------
product1 = Product("P001", "Health Insurance", "Basic health coverage", 500)
product2 = Product("P002", "Life Insurance", "Term life insurance", 1000)

product1.create_product()
product2.create_product()

# -------------------------------
# Create Policyholders
# -------------------------------
holder1 = Policyholder("H001", "Alice Johnson")
holder2 = Policyholder("H002", "Bob Smith")

holder1.register()
holder2.register()

# -------------------------------
# Assign Products to Policyholders
# -------------------------------
holder1.add_product(product1)
holder2.add_product(product2)

# -------------------------------
# Process Payments
# -------------------------------
payment1 = Payment("PM001", holder1.holder_id, product1.product_id, product1.price, "2025-10-15")
payment2 = Payment("PM002", holder2.holder_id, product2.product_id, product2.price, "2025-10-16")

payment1.process_payment()
payment2.process_payment()

holder1.add_payment(payment1)
holder2.add_payment(payment2)

# -------------------------------
# Display Account Details
# -------------------------------
print("\n=== POLICYHOLDER ACCOUNT DETAILS ===")
holder1.display_account_details()
holder2.display_account_details()
