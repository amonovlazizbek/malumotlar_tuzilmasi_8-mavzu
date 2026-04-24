
users_balance = {
    101: 50000,
    102: 75000,
    103: 120000
}
def update_balance(user_id, new_balance):
    if user_id in users_balance:
        users_balance[user_id] = new_balance
        return "Balans yangilandi!"
    else:
        return "Foydalanuvchi topilmadi!"


uid = int(input("ID kiriting: "))
new_bal = int(input("Yangi balans: "))

print(update_balance(uid, new_bal))
print(users_balance)
