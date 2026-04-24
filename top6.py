
users = {
    "ali123": "pass123",
    "vali007": "qwerty",
    "sami_dev": "python",
    "hasan99": "abcd"
}

def get_password(username):
    return users.get(username, "Foydalanuvchi topilmadi!")


login = input("Login kiriting: ")
print(get_password(login))
