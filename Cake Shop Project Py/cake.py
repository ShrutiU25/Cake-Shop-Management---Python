import pickle
import os    

DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "cakes.pkl")

class Cake:

    @staticmethod
    def add_cake():
        os.makedirs(DATA_DIR, exist_ok=True)

        cake = {
            "id": input("Cake ID: "),
            "name": input("Cake Name: "),
            "price": float(input("Price: "))
        }

        cakes = []

        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "rb") as f:
                cakes = pickle.load(f)

        cakes.append(cake)

        with open(FILE_PATH, "wb") as f:
            pickle.dump(cakes, f)

        print("Cake added successfully")

    @staticmethod
    def view_cakes():
        if not os.path.exists(FILE_PATH):
            print("No cakes available")
            return

        with open(FILE_PATH, "rb") as f:
            cakes = pickle.load(f)

        print("\nAvailable Cakes:")
        for c in cakes:
            print(f"{c['id']} - {c['name']} : Rs.{c['price']}")

    @staticmethod
    def get_cake_by_id(cid):
        if not os.path.exists(FILE_PATH):
            return None

        with open(FILE_PATH, "rb") as f:
            cakes = pickle.load(f)

        for c in cakes:
            if c["id"] == cid:
                return c
        return None
