# ============================================
# MULTIPARADIGM BATTLE (SIMPLE PRODUCTION STYLE)
# ============================================

import random


# ---------------------------------
# CONFIG (налаштування гри)
# ---------------------------------

GAME_CONFIG = {
    "max_rounds": 20,
    "crit_chance": 0.25
}


# ---------------------------------
# OOP: МОДЕЛІ
# ---------------------------------

class Character:
    def __init__(self, name, hp, attack):
        # Дані персонажа
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        # Перевірка чи живий персонаж
        return self.hp > 0


class BattleEvent:
    def __init__(self, attacker, defender, damage):
        # Подія бою (хто кого вдарив і на скільки)
        self.attacker = attacker
        self.defender = defender
        self.damage = damage


# ---------------------------------
# FUNCTIONAL: ЛОГІКА
# ---------------------------------

# lambda: базова шкода
base_damage = lambda attack: attack

# lambda: критичний удар
critical_damage = lambda attack: attack * 2

# lambda: застосування шкоди
apply_damage = lambda hp, dmg: max(hp - dmg, 0)


def calculate_damage(attack):
    """
    Вибір типу атаки (звичайна або критична)
    """
    if random.random() < GAME_CONFIG["crit_chance"]:
        return critical_damage(attack)
    return base_damage(attack)


def perform_attack(attacker, defender):
    """
    Одна дія в бою
    """
    damage = calculate_damage(attacker.attack)

    # змінюємо стан об'єкта (OOP)
    defender.hp = apply_damage(defender.hp, damage)

    print(f"{attacker.name} атакує {defender.name} на {damage}")

    # повертаємо подію (для аналітики)
    return BattleEvent(attacker.name, defender.name, damage)


def get_alive_characters(characters):
    """
    filter + lambda
    """
    return list(filter(lambda c: c.is_alive(), characters))


def calculate_total_damage(events):
    """
    reduce (але через цикл — простіше для учнів)
    """
    total = 0
    for e in events:
        total += e.damage
    return total


# ---------------------------------
# PROCEDURAL: ОРКЕСТРАЦІЯ
# ---------------------------------

def run_battle(player1, player2):
    events = []
    round_counter = 0

    while player1.is_alive() and player2.is_alive():
        round_counter += 1

        if round_counter > GAME_CONFIG["max_rounds"]:
            print("Досягнуто ліміт раундів!")
            break

        # Хід 1
        events.append(perform_attack(player1, player2))

        if not player2.is_alive():
            print(f"{player2.name} переможений!")
            break

        # Хід 2
        events.append(perform_attack(player2, player1))

        if not player1.is_alive():
            print(f"{player1.name} переможений!")
            break

    return events


def show_statistics(events):
    """
    Аналіз бою
    """
    total_damage = calculate_total_damage(events)

    print("\n--- СТАТИСТИКА ---")
    print("Всього ударів:", len(events))
    print("Загальна шкода:", total_damage)


def main_menu():
    """
    Просте меню (procedural стиль)
    """
    print("\n=== BATTLE GAME ===")
    print("1. Почати бій")
    print("2. Вийти")

    return input("Ваш вибір: ")


def main():
    """
    Головна функція програми
    """
    while True:
        choice = main_menu()

        if choice == "1":
            # створення об'єктів (OOP)
            player1 = Character("Knight", 100, 20)
            player2 = Character("Orc", 120, 15)

            # запуск бою (procedural)
            events = run_battle(player1, player2)

            # аналітика (functional)
            show_statistics(events)

        elif choice == "2":
            print("Вихід...")
            break

        else:
            print("Невірний вибір!")


if __name__ == "__main__":
    main()