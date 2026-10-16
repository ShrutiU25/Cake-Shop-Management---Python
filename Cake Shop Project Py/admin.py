from cake import Cake
from order import Order
from password_utils import input_password

class Admin:
    @staticmethod
    def login():
        u = input("Admin Username: ")
        p = input_password("Password: ")


        if u == "admin" and p == "admin123":
            Admin.menu()
        else:
            print("Invalid admin login")

    @staticmethod
    def menu():
        while True:
            print("\n1.Add Cake")
            print("2.View Cakes")
            print("3.View Orders")
            print("4.Mark Delivered")
            print("5.Logout")

            ch = input("Choice: ")

            if ch == "1":
                Cake.add_cake()
            elif ch == "2":
                Cake.view_cakes()
            elif ch == "3":
                Order.view_all_orders()
            elif ch == "4":
                Order.mark_delivered()
            elif ch == "5":
                break
            else:
                print("Invalid choice")
