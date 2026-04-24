
phone_book = {
    "Ali": "+998901234567",
    "Vali": "+998909876543",
    "Sami": "+998933334455",
    "Hasan": "+998977778899"
}

name = input("Ism kiriting: ")

if name in phone_book:
    print(f"{name} ning raqami: {phone_book[name]}")
else:
    print("Bunday foydalanuvchi topilmadi!")
