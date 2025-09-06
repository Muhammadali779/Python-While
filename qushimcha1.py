# darsda ishlangan kodni uzgartirishlar va hech qanday kuchirishlarsiz ishlagan ko`rinishi
# asosan MENU o`zgartirildi

while True:
    print("""
|----------MENU----------|
| 1 - Calculator         |
| 2 - Sonlarni chiqarish |
| 3 - Dasturni yakunlash |
|________________________|
          
""")
    choise = input("> ")

    if choise == "1":
        print("Kalculator bo`limi yanlandi! ")

        a = int(input("1 - son: "))
        b = int(input("2 - son: "))
        amal = input("amalni tanlang: ")
        
        if amal == "+":
        
            print(f"Yig`indi: {a + b}")

        elif amal == "-":
        
            print(f"Yig`indi: {a - b}")

        elif amal == "+":
        
            print(f"Yig`indi: {a * b}")

        elif amal == "/" and b != 0:
        
            print(f"Yig`indi: {a / b}")
        else:
            print("Amal yoki sonlar kiritilmadi! ")

    elif choise == '2':
        print("Sonlar ketma ketligi tanlandi! ")

        num = int(input("Butun son kiritng: "))

        print("Sonlar ketma ketligi: ")

        for i in range(1, num + 1):
            print(i)
    
    elif choise == "3":
        print("Dastur yakunlanishi tanlandi! ")
        break

    else: 
        print("Menu da unday bo`lim mavjud emas! ")
        break
