
# EXAMPLES.py

# --- OOP + DTO ---

class UserDTO:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserService:
    def print_user(self, user: UserDTO):
        print(f"User: {user.username}, Email: {user.email}")

user = UserDTO("denys", "[denys@gmail.com](mailto:denys@gmail.com)")
service = UserService()
service.print_user(user)

# --- Procedural approach ---

def create_user(username, email):
    return {
    "username": username,
    "email": email
}

def print_user(user):
    print(f"User: {user['username']}, Email: {user['email']}")

user = create_user("denys", "[denys@gmail.com](mailto:denys@gmail.com)")
print_user(user)