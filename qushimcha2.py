# brinchi son mavjud bulishi kerak
first = True

while True:
    num = input("Son kiriting (to'xtash uchun 'stop'): ")

    if num == "stop":
        break 
    
    # agar input 'stop' dan farqli bo`lsa unda undagi sonlarni intga uzgartirib olamiz
    # va tekshirishni boshlaymiz
    num = int(num)

    if first: 
        _min = num
        first = False

    elif num < _min:       
        _min = num

print(f"Eng kichik son: {_min}")
