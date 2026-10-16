import pickle
import os
from password_utils import input_password
from order import Order

DATA_DIR = "data"
USER_FILE = os.path.join(DATA_DIR, "users.pkl")

class User:

    @staticmethod
    def register():
        os.makedirs(DATA_DIR, exist_ok=True)

        username = input("Username: ")
        password = input_password("Password: ")

        users = []

        if os.path.exists(USER_FILE):
            with open(USER_FILE, "rb") as f:
                users = pickle.load(f)

        # save as DICTIONARY
        users.append({
            "username": username,
            "password": password
        })

        with open(USER_FILE, "wb") as f:
            pickle.dump(users, f)

        print("Registration successful")

    @staticmethod
    def login():
        if not os.path.exists(USER_FILE):
            print("No users found")
            return

        username = input("Username: ")
        password = input_password("Password: ")

        with open(USER_FILE, "rb") as f:
            users = pickle.load(f)

        for u in users:
            # u is now a dictionary
            if u["username"] == username and u["password"] == password:
                print("Login successful")
                User.menu(username)
                return

        print("Invalid credentials")

    @staticmethod
    def menu(username):
        while True:
            print("\n1. Place Order")
            print("2. View My Orders")
            print("3. Logout")

            ch = input("Choice: ")

            if ch == "1":
                Order.place_order(username)
            elif ch == "2":
                Order.view_user_orders(username)
            elif ch == "3":
                break
            else:
                print("Invalid choice")
