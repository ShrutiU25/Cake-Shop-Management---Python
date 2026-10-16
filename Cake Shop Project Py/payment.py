class Payment:
    @staticmethod
    def process_payment():
        print("\nPayment Options")
        print("1. Cash on Delivery")
        print("2. UPI")

        choice = input("Choose option: ")

        if choice == "1":
            return "COD"

        elif choice == "2":
            upi = input("Enter UPI ID: ")
            if "@" not in upi:
                raise Exception("Invalid UPI ID")
            return "UPI"

        else:
            raise Exception("Invalid payment option")
