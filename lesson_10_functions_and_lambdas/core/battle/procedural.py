# ============================================
# ПРОЦЕДУРНИЙ ПІДХІД
# ============================================

# У цьому підході ми НЕ використовуємо класи
# Уся логіка — це змінні + функції

# Дані персонажів зберігаємо окремо
player1_name = "Knight"
player1_hp = 100
player1_attack = 20

player2_name = "Orc"
player2_hp = 120
player2_attack = 15


# Функція атаки
def attack(attacker_name, attacker_attack, defender_name, defender_hp):
    # Виводимо інформацію про атаку
    print(f"{attacker_name} атакує {defender_name} на {attacker_attack} шкоди")

    # Зменшуємо HP захисника
    defender_hp -= attacker_attack

    # Повертаємо нове значення HP
    return defender_hp


# Основний цикл гри
# Працює поки обидва персонажі живі
while player1_hp > 0 and player2_hp > 0:

    # Гравець 1 атакує
    player2_hp = attack(player1_name, player1_attack, player2_name, player2_hp)

    # Перевірка чи живий другий гравець
    if player2_hp <= 0:
        print(f"{player2_name} переможений!")
        break

    # Гравець 2 атакує
    player1_hp = attack(player2_name, player2_attack, player1_name, player1_hp)

    if player1_hp <= 0:
        print(f"{player1_name} переможений!")
        break


print("Гра завершена")