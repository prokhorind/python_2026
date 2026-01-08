# Приклад 2: Словники зі списками

print("=== СЛОВНИКИ ЗІ СПИСКАМИ ===")

# ============================================================================
# 1. БАЗА ДАНИХ ОЦІНОК УЧНІВ
# ============================================================================

print("1. База даних оцінок учнів")
print("-" * 40)

# Створюємо базу оцінок
grades_database = {
    "Анна Петренко": [12, 11, 10, 12, 11, 12],
    "Борис Іваненко": [9, 10, 11, 10, 9, 10],
    "Віра Сидоренко": [12, 12, 11, 12, 12, 11],
    "Григорій Коваленко": [8, 9, 10, 9, 8, 9],
    "Дарина Мельник": [11, 10, 12, 11, 10, 11],
    "Євген Шевченко": [10, 11, 9, 10, 11, 10]
}

print("База даних оцінок:")
for student, grades in grades_database.items():
    average = sum(grades) / len(grades)
    print(f"{student:<20}: {grades} (середній: {average:.2f})")

# Функції для роботи з базою оцінок
def add_grade(database, student_name, grade):
    """Додає оцінку учню"""
    if student_name in database:
        database[student_name].append(grade)
        print(f"✅ Додано оцінку {grade} для {student_name}")
        return True
    else:
        print(f"❌ Учень {student_name} не знайдений в базі")
        return False

def get_student_average(database, student_name):
    """Обчислює середній бал учня"""
    if student_name in database:
        grades = database[student_name]
        return sum(grades) / len(grades)
    return None

def get_top_students(database, min_average=10.0):
    """Знаходить учнів з високим середнім балом"""
    top_students = []
    
    for student, grades in database.items():
        average = sum(grades) / len(grades)
        if average >= min_average:
            top_students.append((student, average))
    
    # Сортуємо за середнім балом (від найвищого до найнижчого)
    top_students.sort(key=lambda x: x[1], reverse=True)
    return top_students

def get_subject_statistics(database):
    """Обчислює статистику по всіх оцінках"""
    all_grades = []
    
    for grades in database.values():
        all_grades.extend(grades)
    
    if not all_grades:
        return None
    
    return {
        "total_grades": len(all_grades),
        "average": sum(all_grades) / len(all_grades),
        "max_grade": max(all_grades),
        "min_grade": min(all_grades),
        "grade_12_count": all_grades.count(12),
        "grade_below_7": len([g for g in all_grades if g < 7])
    }

# Тестуємо функції
print("\n--- Тестування функцій ---")

# Додавання оцінок
add_grade(grades_database, "Анна Петренко", 12)
add_grade(grades_database, "Неіснуючий учень", 10)

# Середній бал
anna_avg = get_student_average(grades_database, "Анна Петренко")
print(f"Середній бал Анни Петренко: {anna_avg:.2f}")

# Топ учні
print(f"\nТоп учні (середній бал >= 10.5):")
top_students = get_top_students(grades_database, 10.5)
for i, (student, average) in enumerate(top_students, 1):
    print(f"  {i}. {student}: {average:.2f}")

# Загальна статистика
stats = get_subject_statistics(grades_database)
print(f"\nЗагальна статистика:")
print(f"  Всього оцінок: {stats['total_grades']}")
print(f"  Середній бал: {stats['average']:.2f}")
print(f"  Найвища оцінка: {stats['max_grade']}")
print(f"  Найнижча оцінка: {stats['min_grade']}")
print(f"  Кількість 12-ок: {stats['grade_12_count']}")
print(f"  Оцінок нижче 7: {stats['grade_below_7']}")

# ============================================================================
# 2. СИСТЕМА УПРАВЛІННЯ ЗАВДАННЯМИ
# ============================================================================

print("\n" + "=" * 50)
print("2. Система управління завданнями")
print("-" * 40)

# База завдань по категоріях
task_manager = {
    "навчання": [
        "Зробити домашнє завдання з математики",
        "Підготуватись до контрольної з фізики",
        "Прочитати розділ з біології",
        "Написати есе з літератури"
    ],
    "дім": [
        "Прибрати кімнату",
        "Допомогти з готуванням",
        "Винести сміття",
        "Полити квіти"
    ],
    "хобі": [
        "Намалювати картину",
        "Пограти на гітарі",
        "Прочитати книгу",
        "Подивитись фільм"
    ],
    "спорт": [
        "Піти в спортзал",
        "Пробігти 3 км",
        "Зробити ранкову зарядку"
    ]
}

print("Система завдань:")
for category, tasks in task_manager.items():
    print(f"\n📂 {category.upper()} ({len(tasks)} завдань):")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")

# Функції для управління завданнями
def add_task(manager, category, task):
    """Додає нове завдання до категорії"""
    if category in manager:
        manager[category].append(task)
        print(f"✅ Додано завдання '{task}' до категорії '{category}'")
    else:
        # Створюємо нову категорію
        manager[category] = [task]
        print(f"✅ Створено нову категорію '{category}' з завданням '{task}'")

def remove_task(manager, category, task_index):
    """Видаляє завдання за індексом"""
    if category in manager:
        if 0 <= task_index < len(manager[category]):
            removed_task = manager[category].pop(task_index)
            print(f"✅ Видалено завдання: '{removed_task}'")
            return removed_task
        else:
            print(f"❌ Неправильний індекс завдання: {task_index}")
    else:
        print(f"❌ Категорія '{category}' не існує")
    return None

def find_tasks_by_keyword(manager, keyword):
    """Знаходить завдання, що містять ключове слово"""
    found_tasks = []
    
    for category, tasks in manager.items():
        for i, task in enumerate(tasks):
            if keyword.lower() in task.lower():
                found_tasks.append((category, i, task))
    
    return found_tasks

def get_task_statistics(manager):
    """Повертає статистику завдань"""
    stats = {}
    total_tasks = 0
    
    for category, tasks in manager.items():
        task_count = len(tasks)
        stats[category] = task_count
        total_tasks += task_count
    
    stats["total"] = total_tasks
    return stats

# Тестуємо функції управління завданнями
print("\n--- Управління завданнями ---")

# Додавання завдань
add_task(task_manager, "навчання", "Підготуватись до іспиту з хімії")
add_task(task_manager, "робота", "Написати резюме")  # Нова категорія

# Пошук завдань
print(f"\nПошук завдань зі словом 'прочитати':")
found = find_tasks_by_keyword(task_manager, "прочитати")
for category, index, task in found:
    print(f"  {category}: {task}")

# Видалення завдання
print(f"\nВидалення завдання:")
remove_task(task_manager, "дім", 0)  # Видаляємо перше завдання з категорії "дім"

# Статистика
print(f"\nСтатистика завдань:")
stats = get_task_statistics(task_manager)
for category, count in stats.items():
    if category != "total":
        print(f"  {category}: {count} завдань")
print(f"  Всього: {stats['total']} завдань")

# ============================================================================
# 3. МУЗИЧНА БІБЛІОТЕКА
# ============================================================================

print("\n" + "=" * 50)
print("3. Музична бібліотека")
print("-" * 40)

# База музичних треків по виконавцях
music_library = {
    "The Beatles": [
        "Hey Jude",
        "Let It Be", 
        "Yesterday",
        "Come Together",
        "Here Comes the Sun"
    ],
    "Queen": [
        "Bohemian Rhapsody",
        "We Will Rock You",
        "Don't Stop Me Now",
        "Another One Bites the Dust"
    ],
    "Pink Floyd": [
        "Wish You Were Here",
        "Comfortably Numb",
        "Time",
        "Money"
    ],
    "Led Zeppelin": [
        "Stairway to Heaven",
        "Black Dog",
        "Kashmir"
    ]
}

print("Музична бібліотека:")
for artist, songs in music_library.items():
    print(f"\n🎵 {artist} ({len(songs)} пісень):")
    for i, song in enumerate(songs, 1):
        print(f"  {i}. {song}")

# Функції для роботи з музичною бібліотекою
def add_song(library, artist, song):
    """Додає пісню до бібліотеки"""
    if artist in library:
        if song not in library[artist]:
            library[artist].append(song)
            print(f"🎵 Додано '{song}' до {artist}")
        else:
            print(f"⚠️  Пісня '{song}' вже є у {artist}")
    else:
        library[artist] = [song]
        print(f"🎵 Додано нового виконавця {artist} з піснею '{song}'")

def find_song(library, song_title):
    """Знаходить пісню в бібліотеці"""
    results = []
    
    for artist, songs in library.items():
        for song in songs:
            if song_title.lower() in song.lower():
                results.append((artist, song))
    
    return results

def get_random_playlist(library, count=5):
    """Створює випадковий плейлист"""
    import random
    
    all_songs = []
    for artist, songs in library.items():
        for song in songs:
            all_songs.append((artist, song))
    
    if len(all_songs) < count:
        count = len(all_songs)
    
    return random.sample(all_songs, count)

def get_artist_with_most_songs(library):
    """Знаходить виконавця з найбільшою кількістю пісень"""
    max_songs = 0
    top_artist = None
    
    for artist, songs in library.items():
        if len(songs) > max_songs:
            max_songs = len(songs)
            top_artist = artist
    
    return top_artist, max_songs

# Тестуємо функції музичної бібліотеки
print("\n--- Робота з музичною бібліотекою ---")

# Додавання пісень
add_song(music_library, "The Beatles", "Help!")
add_song(music_library, "The Beatles", "Hey Jude")  # Дублікат
add_song(music_library, "Nirvana", "Smells Like Teen Spirit")  # Новий виконавець

# Пошук пісні
print(f"\nПошук пісень зі словом 'you':")
found_songs = find_song(music_library, "you")
for artist, song in found_songs:
    print(f"  {artist}: {song}")

# Випадковий плейлист
print(f"\nВипадковий плейлист (3 пісні):")
playlist = get_random_playlist(music_library, 3)
for i, (artist, song) in enumerate(playlist, 1):
    print(f"  {i}. {artist} - {song}")

# Топ виконавець
top_artist, song_count = get_artist_with_most_songs(music_library)
print(f"\nВиконавець з найбільшою кількістю пісень: {top_artist} ({song_count} пісень)")

# ============================================================================
# 4. СИСТЕМА КОНТАКТІВ
# ============================================================================

print("\n" + "=" * 50)
print("4. Система контактів")
print("-" * 40)

# База контактів з номерами телефонів
contacts_db = {
    "Анна Петренко": ["+380501234567", "+380671234567"],
    "Борис Іваненко": ["+380502345678"],
    "Віра Сидоренко": ["+380503456789", "+380673456789", "+380933456789"],
    "Григорій Коваленко": ["+380504567890"],
    "Дарина Мельник": ["+380505678901", "+380675678901"]
}

print("База контактів:")
for name, phones in contacts_db.items():
    print(f"{name}:")
    for i, phone in enumerate(phones, 1):
        phone_type = "основний" if i == 1 else f"додатковий {i-1}"
        print(f"  {phone} ({phone_type})")

# Функції для роботи з контактами
def add_phone(contacts, name, phone):
    """Додає номер телефону до контакту"""
    if name in contacts:
        if phone not in contacts[name]:
            contacts[name].append(phone)
            print(f"📞 Додано номер {phone} для {name}")
        else:
            print(f"⚠️  Номер {phone} вже є у {name}")
    else:
        contacts[name] = [phone]
        print(f"📞 Створено новий контакт {name} з номером {phone}")

def remove_phone(contacts, name, phone):
    """Видаляє номер телефону"""
    if name in contacts:
        if phone in contacts[name]:
            contacts[name].remove(phone)
            print(f"🗑️  Видалено номер {phone} у {name}")
            
            # Якщо номерів не залишилось, видаляємо контакт
            if not contacts[name]:
                del contacts[name]
                print(f"🗑️  Контакт {name} видалено (не залишилось номерів)")
        else:
            print(f"❌ Номер {phone} не знайдено у {name}")
    else:
        print(f"❌ Контакт {name} не існує")

def find_by_phone(contacts, phone_part):
    """Знаходить контакт за частиною номера"""
    results = []
    
    for name, phones in contacts.items():
        for phone in phones:
            if phone_part in phone:
                results.append((name, phone))
    
    return results

def get_contacts_statistics(contacts):
    """Повертає статистику контактів"""
    total_contacts = len(contacts)
    total_phones = sum(len(phones) for phones in contacts.values())
    
    contacts_with_multiple = 0
    for phones in contacts.values():
        if len(phones) > 1:
            contacts_with_multiple += 1
    
    return {
        "total_contacts": total_contacts,
        "total_phones": total_phones,
        "avg_phones_per_contact": total_phones / total_contacts if total_contacts > 0 else 0,
        "contacts_with_multiple_phones": contacts_with_multiple
    }

# Тестуємо функції контактів
print("\n--- Управління контактами ---")

# Додавання номерів
add_phone(contacts_db, "Анна Петренко", "+380991234567")
add_phone(contacts_db, "Євген Шевченко", "+380506789012")

# Пошук за номером
print(f"\nПошук контактів з номерами, що містять '050':")
found_contacts = find_by_phone(contacts_db, "050")
for name, phone in found_contacts:
    print(f"  {name}: {phone}")

# Видалення номера
remove_phone(contacts_db, "Віра Сидоренко", "+380933456789")

# Статистика
stats = get_contacts_statistics(contacts_db)
print(f"\nСтатистика контактів:")
print(f"  Всього контактів: {stats['total_contacts']}")
print(f"  Всього номерів: {stats['total_phones']}")
print(f"  Середня кількість номерів на контакт: {stats['avg_phones_per_contact']:.1f}")
print(f"  Контактів з кількома номерами: {stats['contacts_with_multiple_phones']}")

print("\n=== ВИСНОВКИ ===")
print("Словники зі списками ідеальні для:")
print("• Групування пов'язаних даних (оцінки учня, пісні виконавця)")
print("• Категоризації інформації (завдання по типах)")
print("• Зберігання множинних значень для одного ключа")
print("• Створення гнучких структур даних")
print("• Легкого пошуку та фільтрації даних")