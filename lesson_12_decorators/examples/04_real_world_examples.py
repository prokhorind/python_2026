# Приклад 4: Декоратори для школярів - практичні приклади

print("=== Декоратор для перевірки домашнього завдання ===")

def check_homework_done(func):
    """Декоратор, який перевіряє чи зроблено домашнє завдання"""
    def wrapper(student_name, homework_status, *args, **kwargs):
        if not homework_status:
            print(f"❌ {student_name}, спочатку зроби домашнє завдання!")
            return None
        
        print(f"✅ {student_name}, домашнє завдання зроблено. Можна продовжувати!")
        return func(student_name, *args, **kwargs)
    return wrapper

@check_homework_done
def play_game(student_name, game_name):
    """Грати в гру (тільки після домашнього завдання)"""
    message = f"🎮 {student_name} грає в {game_name}!"
    print(message)
    return message

@check_homework_done
def watch_movie(student_name, movie_name):
    """Дивитися фільм (тільки після домашнього завдання)"""
    message = f"🎬 {student_name} дивиться '{movie_name}'"
    print(message)
    return message

print("Тестування перевірки домашнього завдання:")
play_game("Іван", False, "Minecraft")      # Не зроблено ДЗ
play_game("Марія", True, "Among Us")       # ДЗ зроблено
watch_movie("Петро", True, "Людина-павук") # ДЗ зроблено

print("\n=== Декоратор для підрахунку балів ===")

total_points = 0

def add_points(points):
    """Декоратор, який додає бали за виконання завдань"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            global total_points
            result = func(*args, **kwargs)
            
            if result:  # Якщо завдання виконано успішно
                total_points += points
                print(f"🏆 +{points} балів! Загалом балів: {total_points}")
            else:
                print(f"❌ Завдання не виконано, балів не додано")
            
            return result
        return wrapper
    return decorator

@add_points(10)
def solve_math_problem(problem, answer):
    """Розв'язати математичну задачу"""
    correct_answers = {
        "2+2": 4,
        "5*3": 15,
        "10-7": 3,
        "8/2": 4
    }
    
    if problem in correct_answers and correct_answers[problem] == answer:
        print(f"✅ Правильно! {problem} = {answer}")
        return True
    else:
        print(f"❌ Неправильно! {problem} ≠ {answer}")
        return False

@add_points(15)
def complete_programming_task(task_name, is_completed):
    """Виконати завдання з програмування"""
    if is_completed:
        print(f"💻 Завдання '{task_name}' виконано!")
        return True
    else:
        print(f"❌ Завдання '{task_name}' не виконано")
        return False

print("Тестування системи балів:")
solve_math_problem("2+2", 4)        # +10 балів
solve_math_problem("5*3", 14)       # 0 балів (неправильно)
complete_programming_task("Цикли", True)   # +15 балів
solve_math_problem("10-7", 3)       # +10 балів

print(f"\n🎯 Фінальний результат: {total_points} балів")

print("\n=== Декоратор для контролю часу ===")

import time

def time_limit(max_seconds):
    """Декоратор, який обмежує час виконання завдання"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"⏰ У тебе є {max_seconds} секунд на виконання!")
            
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            
            elapsed = end_time - start_time
            
            if elapsed <= max_seconds:
                print(f"✅ Встиг! Витрачено {elapsed:.1f} секунд з {max_seconds}")
                return result
            else:
                print(f"⏰ Час вийшов! Витрачено {elapsed:.1f} секунд (ліміт: {max_seconds})")
                return None
        return wrapper
    return decorator

@time_limit(3)
def quick_math_quiz():
    """Швидкий математичний тест"""
    print("Швидко! Скільки буде 7 * 8?")
    time.sleep(2)  # Імітуємо час на роздуми
    answer = 56
    print(f"Відповідь: {answer}")
    return answer

@time_limit(1)
def super_quick_task():
    """Дуже швидке завдання"""
    print("Назви столицю України!")
    time.sleep(1.5)  # Занадто довго!
    print("Київ")
    return "Київ"

print("Тестування обмеження часу:")
quick_math_quiz()    # Встигне
super_quick_task()   # Не встигне

print("\n=== Декоратор для мотивації ===")

def motivate(func):
    """Декоратор, який мотивує студентів"""
    motivational_phrases = [
        "Ти молодець! 🌟",
        "Продовжуй в тому ж дусі! 💪",
        "Чудова робота! 🎉",
        "Ти на правильному шляху! 🚀",
        "Так тримати! ⭐"
    ]
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if result:
            import random
            phrase = random.choice(motivational_phrases)
            print(f"🎊 {phrase}")
        
        return result
    return wrapper

@motivate
def read_book(student_name, pages_read, target_pages):
    """Читання книги"""
    if pages_read >= target_pages:
        print(f"📚 {student_name} прочитав {pages_read} сторінок (ціль: {target_pages})")
        return True
    else:
        print(f"📖 {student_name} прочитав лише {pages_read} з {target_pages} сторінок")
        return False

@motivate
def exercise_completion(student_name, exercises_done, total_exercises):
    """Виконання вправ"""
    if exercises_done == total_exercises:
        print(f"✏️ {student_name} виконав всі {exercises_done} вправ!")
        return True
    else:
        print(f"✏️ {student_name} виконав {exercises_done} з {total_exercises} вправ")
        return False

print("Тестування мотиваційного декоратора:")
read_book("Анна", 25, 20)           # Перевиконала план
exercise_completion("Богдан", 10, 10)  # Виконав все
read_book("Віка", 5, 15)            # Не дочитала
exercise_completion("Григорій", 7, 10)  # Не доробив

print("\n=== Декоратор для нагадувань ===")

def remind_about(reminder_text):
    """Декоратор, який нагадує про щось важливе"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"💡 Нагадування: {reminder_text}")
            result = func(*args, **kwargs)
            print(f"💡 Не забудь: {reminder_text}")
            return result
        return wrapper
    return decorator

@remind_about("Зберегти файл після роботи!")
def write_essay(topic, word_count):
    """Написати есе"""
    print(f"✍️ Пишу есе на тему '{topic}' ({word_count} слів)")
    return f"Есе '{topic}' написано"

@remind_about("Перевірити правопис!")
def submit_homework(subject, assignment):
    """Здати домашнє завдання"""
    print(f"📤 Здаю домашнє завдання з {subject}: {assignment}")
    return True

print("Тестування нагадувань:")
write_essay("Моя майбутня професія", 200)
print()
submit_homework("Українська мова", "Твір про весну")