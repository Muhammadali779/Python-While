sum = 0 

while True:
    num = input("Son kiriting (to'xtash uchun 'stop'): ")

    if num == "stop":
        break

    num = int(num)

    if num % 2 == 0:   # juft son bo'lsa
        sum += num

print(f"Juft sonlarning yig'indisi: {sum}")
