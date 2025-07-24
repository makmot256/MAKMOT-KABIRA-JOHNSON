# Example 1: Message Sender and Payment System

class MessageSender:
    def send(self, recipient, message, attachment=None):
        if attachment:
            print(f"Sending '{message}' to {recipient} with attachment '{attachment}'")
        else:
            print(f"Sending '{message}' to {recipient}")

class WhatsAppSender(MessageSender):
    def send(self, recipient, message, attachment=None):
        print("WhatsApp:", end=" ")
        super().send(recipient, message, attachment)

class EmailSender(MessageSender):
    def send(self, recipient, message, attachment=None):
        print("Email:", end=" ")
        super().send(recipient, message, attachment)

class MultiSender(WhatsAppSender, EmailSender):
    pass

class PaymentProcessor:
    def process(self, amount, currency="USD"):
        print(f"Processing payment of {amount} {currency}")

class PayPalProcessor(PaymentProcessor):
    def process(self, amount, currency="USD"):
        print("PayPal:", end=" ")
        super().process(amount, currency)

class StripeProcessor(PaymentProcessor):
    def process(self, amount, currency="USD"):
        print("Stripe:", end=" ")
        super().process(amount, currency)

class CombinedProcessor(PayPalProcessor, StripeProcessor):
    pass

if __name__ == "__main__":
    # Messaging System
    print("Messaging System:")
    ms = MultiSender()
    ms.send("alice", "Hello!")  # Demonstrates overloading, overriding, and MRO
    ms.send("bob", "Report", "report.pdf")
    print("MRO:", [cls.__name__ for cls in MultiSender.mro()])

    # Payment System
    print("\nPayment System:")
    cp = CombinedProcessor()
    cp.process(100)  # Demonstrates overloading, overriding, and MRO
    cp.process(200, "EUR")
    print("MRO:", [cls.__name__ for cls in CombinedProcessor.mro()])