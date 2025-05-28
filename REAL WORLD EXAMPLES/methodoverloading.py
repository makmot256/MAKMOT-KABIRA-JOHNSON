# Scenario: Print Invoice Function
class Invoice:
    def print_invoice(self, customer=None, amount=None):
        if customer and amount:
            print(f"Invoice for {customer}: UGX {amount}")
        elif customer:
            print(f"Invoice for {customer}")
        else:
            print("Generic Invoice")

# Usage
inv = Invoice()
inv.print_invoice("John", 50000)
inv.print_invoice("Sarah")
inv.print_invoice()
