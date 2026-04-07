# ============================================
# OOP ПІДХІД
# ============================================

# Тут ми описуємо персонажа як ОБ'ЄКТ

class Character:
    def __init__(self, name, hp, attack):
        # Конструктор — створює персонажа
        self.name = name
        self.hp = hp
        self.attack_power = attack

    def attack(self, other):
        # Метод — поведінка об'єкта
        print(f"{self.name} атакує {other.name} на {self.attack_power} шкоди")

        # Ми змінюємо стан іншого об'єкта
        other.hp -= self.attack_power

    def is_alive(self):
        # Метод для перевірки стану
        return self.hp > 0


# Створюємо об'єкти (екземпляри класу)
player1 = Character("Knight", 100, 20)
player2 = Character("Orc", 120, 15)


# Ігровий цикл
while player1.is_alive() and player2.is_alive():

    player1.attack(player2)

    if not player2.is_alive():
        print(f"{player2.name} переможений!")
        break

    player2.attack(player1)

    if not player1.is_alive():
        print(f"{player1.name} переможений!")
        break


print("Гра завершена")