login = "admin"

while True:
    _login = input("Login kiriting: ")

    if _login == login:
        print(f"Xush kelibsiz, {login}!")
        break
    else:
        print("Login xato! Qayta urinib ko‘ring.")
