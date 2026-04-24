# 🔐 Amaliy topshiriq – 8  
## Xesh-jadval (Hash Table) va Hashing algoritmlari

---

## 📚 Fan: Dasturlash asoslari / Ma’lumotlar tuzilmasi  
## 👨‍💻 Talaba: Lazizbek Amonov  
## 👨‍🏫 O‘qituvchi: MUXIYATDINOV J.K  

---

## 📌 Loyihaning maqsadi
Ushbu amaliy topshiriqda xesh-jadval (hash table) va hashing algoritmlari o‘rganildi. Asosiy maqsad:

- Xesh-funksiya ishlashini tushunish  
- Kolliziya (collision) holatlarini aniqlash  
- Chaining va Linear Probing usullarini qo‘llash  
- Dictionary va Set bilan ishlashni mustahkamlash  
- Ma’lumotlarni tez qidirish va yangilash  

---

## 🧠 O‘rganilgan mavzular

- Hash Function
- Hash Table
- Collision (kolliziya)
- Chaining (zanjir usuli)
- Open Addressing (Linear Probing)
- Dictionary (`dict`)
- Set (unikal elementlar)

---

## 📂 Masalalar

---

### 🔹 1-masala: Xesh-funksiya asosida indekslash
index = key % 10

sonlar xesh-jadvalga joylashtiriladi.

---

### 🔹 2-masala: Ismlar jadvali
Ismlar birinchi harfi orqali indekslanadi:

index = ord(harf) % jadval_o‘lchami


---

### 🔹 3-masala: Kolliziya holati
Kalitlar:

15, 20, 25, 30

Xesh:

key % 5

Barcha elementlar bir indeksga tushadi → kolliziya chaining bilan hal qilinadi.

---

### 🔹 4-masala: Telefon raqamlarini saqlash
- Kalit: ism  
- Qiymat: telefon raqam  
- Ism orqali raqam qidiriladi  

---

### 🔹 5-masala: Belgilar chastotasi
Matndagi har bir belgining necha marta uchragani hisoblanadi:
- dictionary orqali frequency hisoblanadi  

---

### 🔹 6-masala: Login tizimi
- username → password saqlash  
- login orqali parolni topish funksiyasi yoziladi  

---

### 🔹 7-masala: Linear probing
Kalitlar:

10, 17, 24, 31

Xesh:

key % 7

Kolliziyalar ochiq adresatsiya bilan hal qilinadi.

---

### 🔹 8-masala: Balansni yangilash
- ID → balans  
- ID bo‘yicha qiymat yangilanadi  

---

### 🔹 9-masala: Satrlar uchun xesh-indeks

indeks = (ASCII yig‘indisi) % jadval_o‘lchami


---

### 🔹 10-masala: Unikal elementlar soni
Ro‘yxatdagi unikal elementlar:
- `set()` yoki `dict` orqali aniqlanadi  

---

## 🚀 Xulosa
Ushbu amaliy ish orqali hashing algoritmlari, xesh-jadval ishlash prinsipi, kolliziya muammolari va ularni hal qilish usullari amaliy tarzda o‘rganildi.

---

## 🛠 Texnologiyalar
- Python 🐍  
- Dictionary (Hash Map)  
- Set  
- List  

---

## 👨‍💻 Muallif
**Lazizbek Amonov**

---

## 👨‍🏫 O‘qituvchi
**MUXIYATDINOV J.K**
Berilgan butun sonlar uchun:

