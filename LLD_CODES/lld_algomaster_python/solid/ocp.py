'''
'''
from abc import abstractmethod, ABC

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")
        # Complex logic for credit card processing

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
        # Logic for PayPal processing

class UPIPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount * 80}")  # Assuming conversion rate
        # Logic for UPI processing

class PaymentProcessor:
    def process(self, payment_method: PaymentMethod, amount):
        # No more if-else! The processor doesn't care about the specific type.
        # It just knows it can call processPayment.
        payment_method.process_payment(amount)

class CheckoutService:
    def process_payment(self, method: PaymentMethod, amount):
        processor = PaymentProcessor()
        processor.process(method, amount)

# Usage
checkout = CheckoutService()
checkout.process_payment(CreditCardPayment(), 100.00)
checkout.process_payment(PayPalPayment(), 100.00)
checkout.process_payment(UPIPayment(), 100.00)