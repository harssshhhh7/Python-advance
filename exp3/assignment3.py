from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Strategy 1
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")


# Strategy 2
class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using PayPal.")


# Strategy 3
class BitcoinPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Bitcoin.")


# payment gateway Class
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
def main():

    amount = float(input("Enter payment amount: "))

    processor = PaymentProcessor(CreditCardPayment())

    while True:

        print("\n Payment Menu ")
        print("1. Credit Card")
        print("2. PayPal")
        print("3. Bitcoin")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            processor.set_strategy(CreditCardPayment())
            processor.process_payment(amount)

        elif choice == "2":
            processor.set_strategy(PayPalPayment())
            processor.process_payment(amount)

        elif choice == "3":
            processor.set_strategy(BitcoinPayment())
            processor.process_payment(amount)

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid Choice!")


main()