while True:
    num = input("Son kiriting (to'xtash uchun 'stop'): ")

    if num == "stop":
        print("Dastur tugatildi!")
        break

    num = int(num)
    print(f"{num} sonining kvadrati: {pow(num, 2)}")
