password = "python123"

while True:
    enter_password = input("Parolni kiriting: ")

    if enter_password != password:
        print("Xato! Qayta urinib ko‘ring.")
    
    else:
        print("Xush kelibsiz!")
        break

