# 📄 2. `oop_vs_procedural_examples.py`

# 🔷 ООП приклад

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def change_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password


# використання
user = User("admin", "123456")

print(user.check_password("123456"))
user.change_password("newpass")
print(user.check_password("newpass"))


# 🔷 Процедурний варіант

username = "admin"
password = "123456"

def check_password(input_password):
    return password == input_password

def change_password(new_password):
    global password
    if len(new_password) >= 6:
        password = new_password


print(check_password("123456"))
change_password("newpass")
print(check_password("newpass"))


# 🔷 Closure варіант

def create_user(username, password):

    def check_password(input_password):
        return password == input_password

    def change_password(new_password):
        nonlocal password
        if len(new_password) >= 6:
            password = new_password

    return check_password, change_password


check, change = create_user("admin", "123456")

print(check("123456"))
change("newpass")
print(check("newpass"))