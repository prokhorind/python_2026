# ============================================
# ФУНКЦІОНАЛЬНИЙ ПІДХІД (з lambda)
# ============================================

# У функціональному підході:
# ❗ ми НЕ змінюємо дані
# ❗ створюємо нові значення
# ❗ використовуємо функції як значення

# Персонажі як словники
player1 = {"name": "Knight", "hp": 100, "attack": 20}
player2 = {"name": "Orc", "hp": 120, "attack": 15}


# ---------------------------------
# lambda функції
# ---------------------------------

# Перевірка чи персонаж живий
is_alive = lambda character: character["hp"] > 0

# Розрахунок нового HP (чиста функція)
apply_damage = lambda hp, damage: hp - damage

# Формування нового стану персонажа
create_updated_character = lambda defender, damage: {
    "name": defender["name"],
    "hp": apply_damage(defender["hp"], damage),
    "attack": defender["attack"]
}


# ---------------------------------
# Основна функція атаки
# ---------------------------------

def attack(attacker, defender):
    print(f"{attacker['name']} атакує {defender['name']} на {attacker['attack']} шкоди")

    # Використовуємо lambda для створення нового об'єкта
    return create_updated_character(defender, attacker["attack"])


# ---------------------------------
# Додатково: використання map/filter
# ---------------------------------

# Список персонажів (для демонстрації)
characters = [player1, player2]

# filter — залишає тільки живих персонажів
alive_characters = list(filter(is_alive, characters))

# map — отримуємо імена персонажів
names = list(map(lambda c: c["name"], alive_characters))

print("Живі персонажі:", names)


# ---------------------------------
# Ігровий цикл
# ---------------------------------

while is_alive(player1) and is_alive(player2):

    player2 = attack(player1, player2)

    if not is_alive(player2):
        print(f"{player2['name']} переможений!")
        break

    player1 = attack(player2, player1)

    if not is_alive(player1):
        print(f"{player1['name']} переможений!")
        break


print("Гра завершена")