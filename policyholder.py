class Policyholder:
    def __init__(self, holder_id, name):
        self.holder_id = holder_id
        self.name = name
        self.status = "Active"
        self.products = []
        self.payment_history = []

    def register(self):
        self.status = "Active"
        print(f"{self.name} registered successfully.")

    def suspend(self):
        self.status = "Suspended"
        print(f"{self.name} has been suspended.")

    def reactivate(self):
        self.status = "Active"
        print(f"{self.name} has been reactivated.")

    def add_product(self, product):
        self.products.append(product)

    def add_payment(self, payment):
        self.payment_history.append(payment)

    def display_account_details(self):
        print(f"\nPolicyholder ID: {self.holder_id}")
        print(f"Name: {self.name}")
        print(f"Status: {self.status}")
        print("Products:")
        for product in self.products:
            print(f" - {product.name} (${product.price})")
        print("Payments:")
        for payment in self.payment_history:
            print(f" - ${payment.amount} on {payment.date} [{payment.status}]")
