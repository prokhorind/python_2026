# =========================

# ООП

# =========================

class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):

    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

print("ООП:")
for a in animals:
    a.speak()


# =========================

# ПРОЦЕДУРНИЙ ПІДХІД

# =========================

def dog_speak():
    print("Woof")


def cat_speak():
    print("Meow")

animals = ["dog", "cat"]

print("\nПроцедурно:")
for a in animals:
    if a == "dog":
        dog_speak()
    elif a == "cat":
        cat_speak()
