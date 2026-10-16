from admin import Admin
from user import User

while True:
    print("\n=== CAKE SHOP SYSTEM ===")
    print("1.Admin Login\n2.User Login\n3.Register\n4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        Admin.login()
    elif ch == "2":
        User.login()
    elif ch == "3":
        User.register()
    elif ch == "4":
        break
