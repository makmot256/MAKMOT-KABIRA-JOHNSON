
# Scenario: Payment Processing Systemclass Payment:
class Payment:
    def process(self):
        print("Processing payment...")

class MobileMoney(Payment):
    def process(self):
        print("Processing payment via Mobile Money...")

# Usage
pay = MobileMoney()
pay.process()  # Output: Processing payment via Mobile Money...
