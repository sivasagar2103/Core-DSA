'''

'''

from abc import abstractmethod, ABC

class PaymentGateway(ABC):

    @abstractmethod
    def initiate_payment(self, amt):
        pass


class StripePayementGateway(PaymentGateway):

    def initiate_payment(self, amt):
        print(f"{amt} from StripePayementGateway")

class PaypalPayementGateway(PaymentGateway):

    def initiate_payment(self, amt):
        print(f"{amt} from PaypalPayementGateway")

class CheckoutService:

    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def checkout(self, amount):
        self.payment_gateway.initiate_payment(amount)

if __name__ == '__main__':
    stripe_gateway = StripePayementGateway()
    checkout_service = CheckoutService(stripe_gateway)
    checkout_service.checkout(234)
