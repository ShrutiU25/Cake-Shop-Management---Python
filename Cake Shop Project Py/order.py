import pickle
import os
from cake import Cake

DATA_DIR = "data"
ORDER_FILE = os.path.join(DATA_DIR, "orders.pkl")

class Order:

    @staticmethod
    def place_order(username):
        os.makedirs(DATA_DIR, exist_ok=True)

        cart = []
        total = 0

        while True:
            Cake.view_cakes()

            cid = input("Enter Cake ID to add (or 'done'): ")
            if cid.lower() == "done":
                break

            cake = Cake.get_cake_by_id(cid)
            if cake:
                qty = int(input("Quantity: "))
                cart.append({
                    "name": cake["name"],
                    "qty": qty,
                    "price": cake["price"]
                })
                total += cake["price"] * qty
            else:
                print("Invalid cake ID")

        if not cart:
            print("No items ordered")
            return

        order = {
            "user": username,
            "items": cart,
            "total": total,
            "status": "Pending"
        }

        orders = []
        if os.path.exists(ORDER_FILE):
            with open(ORDER_FILE, "rb") as f:
                orders = pickle.load(f)

        orders.append(order)

        with open(ORDER_FILE, "wb") as f:
            pickle.dump(orders, f)

        print("Order placed successfully")

    @staticmethod
    def view_user_orders(username):
        if not os.path.exists(ORDER_FILE):
            print("No orders found")
            return

        with open(ORDER_FILE, "rb") as f:
            orders = pickle.load(f)

        found = False
        for o in orders:
            if o["user"] == username:
                found = True
                print("\nItems:")
                for item in o["items"]:
                    print(f"{item['name']} x {item['qty']}")

                print("Total:", o["total"])
                print("Status:", o["status"])

        if not found:
            print("No orders for this user")
    
    @staticmethod
    def view_all_orders():
        if not os.path.exists(ORDER_FILE):
            print("No orders found")
            return

        with open(ORDER_FILE, "rb") as f:
            orders = pickle.load(f)

        if not orders:
            print("No orders available")
            return

        print("\n--- ALL ORDERS ---")
        for i, o in enumerate(orders, start=1):
            print(f"\nOrder {i}")
            print("User:", o["user"])

            print("Items:")
            for item in o["items"]:
                print(f"  {item['name']} x {item['qty']}")

            print("Total:", o["total"])
            print("Status:", o["status"])
