class Payment:
    def __init__(self, payment_id, policyholder_id, product_id, amount, date):
        self.payment_id = payment_id
        self.policyholder_id = policyholder_id
        self.product_id = product_id
        self.amount = amount
        self.date = date
        self.status = "Paid"

    def process_payment(self):
        print(f"Payment of ${self.amount} processed for Policyholder {self.policyholder_id}.")

    def send_reminder(self):
        print(f"Reminder sent for payment ID {self.payment_id}.")

    def apply_penalty(self, penalty_amount):
        self.amount += penalty_amount
        self.status = "Late"
        print(f"Penalty applied. New amount: ${self.amount}")
