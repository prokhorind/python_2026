# ОБЕРІТЬ ОДНЕ ЗАВДАННЯ ДЛЯ ВИКОНАННЯ:

# ============================================
# ЗАВДАННЯ 1: ЕЛЕКТРОННИЙ ЩОДЕННИК 📚
# ============================================

print("=== ЕЛЕКТРОННИЙ ЩОДЕННИК ===")

# Крок 1: Створи словник з предметами та оцінками
diary = {
    "математика": [10, 8, 9],
    "фізика": [9, 7, 8, 10],
    "англійська": [11, 9, 10]
}

# Покажи поточні оцінки
print("\nПоточні оцінки:")
for subject, grades in diary.items():
    print(f"{subject}: {grades}")

# Крок 2: Додай нову оцінку до існуючого предмету
subject = input("\nДо якого предмету додати оцінку? ")
if subject in diary:
    new_grade = int(input("Нова оцінка: "))
    # TODO: Додай нову оцінку до списку оцінок предмету
    diary[subject].append(new_grade)
    print(f"{subject}: {diary[subject]}")
else:
    print("Такого предмету немає")

# Крок 3: Додай новий предмет
new_subject = input("\nНазва нового предмету: ")
grades_input = input("Оцінки через пробіл: ")
# TODO: Перетвори рядок оцінок у список чисел
grades_list = [int(grade) for grade in grades_input.split()]
# TODO: Додай новий предмет до словника
diary[new_subject] = grades_list

print(f"{new_subject}: {diary[new_subject]}")

# Крок 4: Обчисли середні оцінки
print("\n=== СТАТИСТИКА ===")
subject_averages = {}

for subject, grades in diary.items():
    # TODO: Обчисли середню оцінку для кожного предмету
    average = sum(grades) / len(grades)
    subject_averages[subject] = average
    print(f"{subject}: середня {average:.1f} ({len(grades)} оцінок)")

# Крок 5: Знайди найкращий та найгірший предмети
# TODO: Знайди предмет з найвищою середньою оцінкою
best_subject = max(subject_averages.items(), key=lambda x: x[1])
# TODO: Знайди предмет з найнижчою середньою оцінкою
worst_subject = min(subject_averages.items(), key=lambda x: x[1])

print(f"\nНайкращий предмет: {best_subject[0]} ({best_subject[1]:.1f})")
print(f"Найгірший предмет: {worst_subject[0]} ({worst_subject[1]:.1f})")

# Крок 6: Загальна статистика
# TODO: Обчисли загальну середню оцінку
all_grades = []
for grades in diary.values():
    all_grades.extend(grades)

overall_average = sum(all_grades) / len(all_grades)
print(f"Загальна середня: {overall_average:.1f}")

# ============================================
# ЗАВДАННЯ 2: АНАЛІЗАТОР ТЕКСТУ 🔍
# ============================================

# Розкоментуй цей блок, якщо обираєш завдання 2:

"""
print("=== АНАЛІЗАТОР ТЕКСТУ ===")

# Крок 1: Введи текст для аналізу
text = input("\\nВведіть текст: ").lower()

# Крок 2: Аналіз слів
words = text.split()
word_count = {}

# TODO: Підрахуй частоту кожного слова
for word in words:
    # Очищаємо слово від розділових знаків
    clean_word = ''.join(char for char in word if char.isalpha())
    if clean_word:
        word_count[clean_word] = word_count.get(clean_word, 0) + 1

print(f"\\n=== АНАЛІЗ СЛІВ ===")
print(f"Всього слів: {len(words)}")
print(f"Унікальних слів: {len(word_count)}")

print("\\nЧастота слів:")
# TODO: Покажи частоту кожного слова
for word, count in word_count.items():
    print(f"{word}: {count}")

# TODO: Знайди найчастіше слово
most_frequent_word = max(word_count.items(), key=lambda x: x[1])
print(f"\\nНайчастіше слово: {most_frequent_word[0]} ({most_frequent_word[1]} рази)")

# TODO: Знайди рідкісні слова (що зустрічаються 1 раз)
rare_words = [word for word, count in word_count.items() if count == 1]
print(f"Рідкісні слова (1 раз): {', '.join(rare_words)}")

# Крок 3: Аналіз літер
letter_count = {}
total_letters = 0

# TODO: Підрахуй частоту кожної літери
for char in text:
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1
        total_letters += 1

print(f"\\n=== АНАЛІЗ ЛІТЕР ===")
print(f"Всього літер: {total_letters}")
print(f"Унікальних літер: {len(letter_count)}")

# TODO: Покажи топ-5 найчастіших літер
top_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)[:5]
print("\\nТоп-5 літер:")
for letter, count in top_letters:
    print(f"{letter}: {count}", end=", ")
print()

# TODO: Знайди найрідкісніші літери
min_count = min(letter_count.values())
rarest_letters = [letter for letter, count in letter_count.items() if count == min_count]
print(f"\\nНайрідкісніші літери: {', '.join(rarest_letters)} (по {min_count} разу)")
"""

# ============================================
# ЗАВДАННЯ 3: МЕНЕДЖЕР КОНТАКТІВ 📞
# ============================================

# Розкоментуй цей блок, якщо обираєш завдання 3:

"""
print("=== МЕНЕДЖЕР КОНТАКТІВ ===")

# Крок 1: Створи базу контактів
contacts = {
    "Мама": {"phone": "+380501234567", "group": "сім'я"},
    "Тато": {"phone": "+380507654321", "group": "сім'я"},
    "Олексій": {"phone": "+380631112233", "group": "друзі"}
}

print("\\nДодаю контакти:")
for name, info in contacts.items():
    print(f"✓ {name} ({info['phone']}, {info['group']})")

# Крок 2: Додай новий контакт
new_name = input("\\nІм'я нового контакту: ")
new_phone = input("Телефон: ")
new_group = input("Група (сім'я/друзі/робота): ")

# TODO: Додай новий контакт до словника
contacts[new_name] = {"phone": new_phone, "group": new_group}
print(f"✓ {new_name} ({new_phone}, {new_group})")

# Крок 3: Пошук контактів
search_term = input("\\nПошук контакту (ім'я або частина телефону): ").lower()
found_contacts = []

# TODO: Знайди контакти за пошуковим терміном
for name, info in contacts.items():
    if search_term in name.lower() or search_term in info['phone']:
        found_contacts.append((name, info))

print(f"\\nПошук '{search_term}': знайдено {len(found_contacts)} контактів")
for name, info in found_contacts:
    print(f"  {name}: {info['phone']} ({info['group']})")

# Крок 4: Групування контактів
print("\\n=== ГРУПИ КОНТАКТІВ ===")
groups = {}

# TODO: Згрупуй контакти за групами
for name, info in contacts.items():
    group = info['group']
    groups.setdefault(group, []).append(name)

for group, names in groups.items():
    print(f"{group} ({len(names)}): {', '.join(names)}")

# Крок 5: Оновлення контакту
update_name = input("\\nІм'я контакту для оновлення: ")
if update_name in contacts:
    new_phone = input("Новий телефон: ")
    # TODO: Оновити телефон контакту
    contacts[update_name]["phone"] = new_phone
    print("✓ Контакт оновлено")
else:
    print("Контакт не знайдено")

# Крок 6: Статистика
print("\\n=== СТАТИСТИКА ===")
print(f"Всього контактів: {len(contacts)}")

# TODO: Знайди найбільшу групу
largest_group = max(groups.items(), key=lambda x: len(x[1]))
print(f"Найбільша група: {largest_group[0]} ({len(largest_group[1])} контакти)")
print(f"Груп: {len(groups)}")
"""