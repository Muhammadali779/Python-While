import random


num = random.randint(1, 20)
print("Kompyuter (1 dan 20 gacha bo`lgan oraliqda son o`yladi.Topa olasizmi ?)")

while True:
    checked_num = int(input("Son tanlang: "))
    
    if checked_num < num:
        print("Kompyuter tanlagan son Kattaroq! ")

    elif checked_num > num:
        print("Kompyuter tanlagan son Kichikroq! ")

    else:
        print("Siz tanlangan raqamni topdingiz! ")
        print(f"Tanlangan raqam: {num} edi")
        break