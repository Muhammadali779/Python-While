## 📝 Uyga vazifalar – `while` loop

---

### 🔹 1. Raqam topish o‘yini

**Izoh:**

* Kompyuter 1 dan 20 gacha tasodifiy son tanlaydi (`random` modulidan foydalanish mumkin).
* O‘quvchi `while` loop orqali doim taxmin qiladi.
* Agar foydalanuvchi **kichikroq son kiritsa**, kompyuter “Katta son” deydi.
* Agar foydalanuvchi **katta son kiritsa**, “Kichik son” deydi.
* To‘g‘ri topilganda esa loop tugashi kerak.

👉 Bu yerda asosiy g‘oya: **loop faqat to‘g‘ri son topilganda to‘xtaydi**.

---

### 🔹 2. Parol tekshirish dasturi

**Izoh:**

* Biror **maxfiy parol** oldindan belgilanadi, masalan `"python123"`.
* Foydalanuvchi **while loop** orqali parol kiritadi.
* To‘g‘ri bo‘lmasa: `"Xato! Qayta urinib ko‘ring."` chiqadi.
* To‘g‘ri kiritganda: `"Xush kelibsiz!"` chiqadi va loop tugaydi.

👉 Bu vazifada o‘quvchilar:

* **Cheksiz loop**ga tushmaslik uchun shartni to‘g‘ri qo‘yish,
* Foydalanuvchidan **doimiy input olish**,
* `if` bilan tekshirishni mashq qilishadi.

---

### 🔹 3. To‘plangan ball o‘yini

**Izoh:**

* Boshlanishida ball = 0.
* Foydalanuvchi input kiritadi:

  * Agar `+` yozsa → ball **10 ga oshadi**.
  * Agar `stop` yozsa → loop tugaydi va umumiy ball chiqariladi.
* Noto‘g‘ri belgi kiritilsa → “Faqat `+` yoki `stop` yozing!” deb ogohlantirish mumkin.

👉 Bu vazifa orqali o‘quvchilar:

* `while True:` (cheksiz loop) yozishni,
* `break` orqali loopni to‘xtatishni,
* O‘zgaruvchini (`ball`) **har safar yangilash**ni o‘rganishadi.

---

### 🔹 4. Kalkulyator (oddiy versiya)

**Izoh:**

* Foydalanuvchidan **ikki son** so‘raladi.
* Keyin amal (`+`, `-`, `*`, `/`) tanlanadi.
* Dastur hisoblab, natijani chiqaradi.
* So‘ng: `"Davom etasizmi? (ha/yo‘q)"` deb so‘raladi.
* Agar `ha` deb yozsa → loop davom etadi,
* Agar `yo‘q` deb yozsa → loop tugaydi.

👉 Bu vazifada o‘quvchilar:

* **loopni foydalanuvchi xohishiga qarab to‘xtatish**,
* if-else orqali amallarni boshqarish,
* input → int/float ga o‘tkazishni mashq qilishadi.

---

### 🔹 5. Matn sanash dasturi

**Izoh:**

* Foydalanuvchidan so‘z/matn kiritish so‘raladi.
* Agar foydalanuvchi `"stop"` yozsa → loop tugaydi.
* Aks holda kiritilgan matnlar sanab boriladi.
* Oxirida necha marta matn kiritilgani chiqariladi.

👉 Bu yerda o‘quvchilar:

* **loop orqali ma’lumot yig‘ish**,
* **hisoblagich (`count`) ishlatish**,
* `while`ni shart bilan tugatishni o‘rganishadi.
|
|
|

QOSHIMCHA SAVOLLAR:  
|
|
|
|
|



### 🔹 qushimcha 2. Minimal son topish

**Izoh:**

* Foydalanuvchi ketma-ket sonlar kiritadi.
* Agar `"stop"` deb yozsa → loop tugaydi.
* Oxirida eng kichik son ekranga chiqariladi.

👉 Bu vazifa orqali o‘quvchilar:

* `while` orqali **doimiy input olish**,
* **shartli solishtirish** bilan eng kichik qiymatni saqlash,
* `"stop"` so‘zi kiritilganda loopni tugatishni o‘rganadi.

---

### 🔹 qushimcha 3. Juft son yig‘uvchi dastur

**Izoh:**

* Foydalanuvchi son kiritadi.
* Agar son **juft** bo‘lsa, u yig‘indiga qo‘shiladi.
* Agar `"stop"` kiritilsa → loop tugaydi.
* Oxirida juft sonlarning yig‘indisi chiqariladi.

👉 Bu orqali:

* `while` bilan **cheksiz input olish**,
* **modul (%) operatoridan foydalanish**,
* natijani **yig‘ish (sum)** mashq qilinadi.

---

### 🔹 qushimcha 4. Foydalanuvchi loginini tekshirish

**Izoh:**

* Oldindan `"admin"` login belgilab qo‘yiladi.
* Foydalanuvchi `while` orqali login kiritadi.
* Agar to‘g‘ri bo‘lsa: `"Xush kelibsiz, admin!"`.
* Agar noto‘g‘ri bo‘lsa: `"Login xato! Qayta urinib ko‘ring."`.
* To‘g‘ri login yozilganda loop tugaydi.

👉 Bu orqali:

* `while` bilan **takroriy input olish**,
* **if-else tekshirish**,
* login-parol kabi amaliy mashqlarni o‘rganishadi.

---

### 🔹 qushimcha 5. Kvadrat chiqarish dasturi

**Izoh:**

* Foydalanuvchi son kiritadi.
* Dastur uning kvadratini chiqaradi.
* Agar foydalanuvchi `"stop"` yozsa → loop tugaydi.

👉 Bu orqali:

* `while True:` yozish,
* **int() ga o‘tkazish va matematik amal bajarish**,
* `"stop"` bilan loopni boshqarish mashq qilinadi.

---

❓ Xohlaysizmi, men bu 4 ta vazifaga ham **tayyor Python kodini** yozib beray?
