# Приклад 3: Обернення рядків за допомогою стека

print("=== ОБЕРНЕННЯ РЯДКІВ ЗА ДОПОМОГОЮ СТЕКА ===")

def reverse_string_with_stack(text):
    """Обертає рядок за допомогою стека"""
    stack = []
    
    print(f"Оригінальний рядок: '{text}'")
    print("Процес обернення:")
    
    # Крок 1: Додаємо всі символи до стека
    print("\n1. Додаємо символи до стека:")
    for i, char in enumerate(text):
        stack.append(char)
        print(f"   Додали '{char}' → стек: {stack}")
    
    # Крок 2: Забираємо символи зі стека
    print("\n2. Забираємо символи зі стека:")
    reversed_text = ""
    step = 1
    
    while stack:
        char = stack.pop()
        reversed_text += char
        print(f"   Крок {step}: забрали '{char}' → результат: '{reversed_text}'")
        step += 1
    
    print(f"\nОбернений рядок: '{reversed_text}'")
    return reversed_text

# Тестуємо обернення
test_words = ["Python", "Привіт", "12345", "abc"]

for word in test_words:
    print("=" * 50)
    reverse_string_with_stack(word)
    print()

# Порівняння з вбудованим методом
print("=== ПОРІВНЯННЯ З ВБУДОВАНИМ МЕТОДОМ ===")

def compare_reverse_methods(text):
    """Порівнює різні способи обернення"""
    
    # Метод 1: За допомогою стека
    stack = []
    for char in text:
        stack.append(char)
    
    stack_result = ""
    while stack:
        stack_result += stack.pop()
    
    # Метод 2: Вбудований метод Python
    builtin_result = text[::-1]
    
    # Метод 3: Через цикл
    loop_result = ""
    for i in range(len(text) - 1, -1, -1):
        loop_result += text[i]
    
    print(f"Оригінал: '{text}'")
    print(f"Стек:     '{stack_result}'")
    print(f"[::-1]:   '{builtin_result}'")
    print(f"Цикл:     '{loop_result}'")
    print(f"Всі методи дають однаковий результат: {stack_result == builtin_result == loop_result}")

compare_words = ["Hello", "Світ", "123"]
for word in compare_words:
    compare_reverse_methods(word)
    print()

# Обернення слів у реченні
print("=== ОБЕРНЕННЯ СЛІВ У РЕЧЕННІ ===")

def reverse_words_in_sentence(sentence):
    """Обертає кожне слово у реченні окремо"""
    words = sentence.split()
    reversed_words = []
    
    print(f"Оригінальне речення: '{sentence}'")
    print("Обертаємо кожне слово:")
    
    for word in words:
        # Обертаємо слово за допомогою стека
        stack = []
        for char in word:
            stack.append(char)
        
        reversed_word = ""
        while stack:
            reversed_word += stack.pop()
        
        reversed_words.append(reversed_word)
        print(f"  '{word}' → '{reversed_word}'")
    
    result = " ".join(reversed_words)
    print(f"Результат: '{result}'")
    return result

# Тестуємо обернення слів
sentences = [
    "Привіт світ",
    "Python програмування",
    "Один два три чотири",
    "Стек це круто"
]

for sentence in sentences:
    reverse_words_in_sentence(sentence)
    print()

# Перевірка паліндромів за допомогою стека
print("=== ПЕРЕВІРКА ПАЛІНДРОМІВ ===")

def is_palindrome_with_stack(text):
    """Перевіряє, чи є рядок паліндромом, використовуючи стек"""
    # Очищаємо рядок від пробілів та приводимо до нижнього регістру
    clean_text = text.replace(" ", "").lower()
    
    stack = []
    
    # Додаємо всі символи до стека
    for char in clean_text:
        stack.append(char)
    
    # Порівнюємо оригінал з оберненим
    reversed_text = ""
    while stack:
        reversed_text += stack.pop()
    
    is_palindrome = clean_text == reversed_text
    
    print(f"Текст: '{text}'")
    print(f"Очищений: '{clean_text}'")
    print(f"Обернений: '{reversed_text}'")
    print(f"Паліндром: {'Так' if is_palindrome else 'Ні'}")
    
    return is_palindrome

# Тестуємо паліндроми
palindrome_tests = [
    "шалаш",
    "А роза упала на лапу Азора",
    "мадам",
    "Python",
    "12321",
    "Козак",
]

for test in palindrome_tests:
    is_palindrome_with_stack(test)
    print()

# Обернення числа
print("=== ОБЕРНЕННЯ ЧИСЛА ===")

def reverse_number(num):
    """Обертає цифри числа за допомогою стека"""
    # Перетворюємо число в рядок
    num_str = str(abs(num))  # Беремо модуль для обробки від'ємних чисел
    
    stack = []
    
    print(f"Оригінальне число: {num}")
    print("Додаємо цифри до стека:")
    
    # Додаємо цифри до стека
    for digit in num_str:
        stack.append(digit)
        print(f"  Додали {digit} → стек: {stack}")
    
    # Забираємо цифри зі стека
    reversed_str = ""
    print("Забираємо цифри зі стека:")
    
    while stack:
        digit = stack.pop()
        reversed_str += digit
        print(f"  Забрали {digit} → результат: {reversed_str}")
    
    # Перетворюємо назад у число
    reversed_num = int(reversed_str)
    
    # Враховуємо знак оригінального числа
    if num < 0:
        reversed_num = -reversed_num
    
    print(f"Обернене число: {reversed_num}")
    return reversed_num

# Тестуємо обернення чисел
numbers = [12345, -6789, 100, 7]

for number in numbers:
    reverse_number(number)
    print()

print("=== ВИСНОВКИ ===")
print("Стек ідеально підходить для обернення порядку елементів:")
print("• Рядки → обернені рядки")
print("• Числа → обернені числа") 
print("• Перевірка паліндромів")
print("• Обернення слів у реченні")
print("Принцип LIFO природно обертає порядок!")