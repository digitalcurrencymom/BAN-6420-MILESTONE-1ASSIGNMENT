class Product:
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.status = "Available"

    def create_product(self):
        print(f"Product '{self.name}' created.")

    def update_product(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price
        print(f"Product '{self.product_id}' updated.")

    def remove_product(self):
        self.status = "Removed"
        print(f"Product '{self.name}' removed.")

    def suspend_product(self):
        self.status = "Suspended"
        print(f"Product '{self.name}' suspended.")
