# Приклад 2: Перевірка збалансованості дужок за допомогою стека

print("=== ПЕРЕВІРКА ЗБАЛАНСОВАНОСТІ ДУЖОК ===")

def check_brackets(expression):
    """
    Перевіряє, чи збалансовані дужки у виразі
    Повертає True, якщо збалансовані, False - якщо ні
    """
    stack = []
    
    # Відповідності відкриваючих та закриваючих дужок
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {
        "(": ")",
        "[": "]", 
        "{": "}"
    }
    
    print(f"Перевіряємо вираз: '{expression}'")
    
    for i, char in enumerate(expression):
        print(f"Символ {i+1}: '{char}'", end=" ")
        
        if char in opening_brackets:
            # Відкриваюча дужка - додаємо до стека
            stack.append(char)
            print(f"→ відкриваюча дужка, додаємо до стека: {stack}")
            
        elif char in closing_brackets:
            # Закриваюча дужка
            print(f"→ закриваюча дужка", end=" ")
            
            if not stack:
                # Стек порожній, але є закриваюча дужка
                print("→ ПОМИЛКА: немає відповідної відкриваючої дужки")
                return False
            
            # Забираємо останню відкриваючу дужку
            last_opening = stack.pop()
            expected_closing = bracket_pairs[last_opening]
            
            if char == expected_closing:
                print(f"→ відповідає '{last_opening}', стек: {stack}")
            else:
                print(f"→ ПОМИЛКА: очікувалась '{expected_closing}', а отримали '{char}'")
                return False
        else:
            # Інший символ - ігноруємо
            print("→ ігноруємо")
    
    # Перевіряємо, чи стек порожній
    if stack:
        print(f"ПОМИЛКА: залишились незакриті дужки: {stack}")
        return False
    else:
        print("✓ Всі дужки збалансовані!")
        return True

# Тестові вирази
test_expressions = [
    "()",                    # Прості круглі дужки
    "(())",                  # Вкладені круглі дужки
    "()[]{}", 	             # Різні типи дужок
    "((()))",                # Багато вкладених дужок
    "([{}])",                # Змішані вкладені дужки
    "(2 + 3) * [4 - 1]",     # Математичний вираз
    "(((",                   # Незакриті дужки
    ")))",                   # Зайві закриваючі дужки
    "([)]",                  # Неправильний порядок
    "{[}]",                  # Перехрещені дужки
    "",                      # Порожній рядок
    "abc",                   # Без дужок
]

print("Тестуємо різні вирази:\n")

for i, expr in enumerate(test_expressions, 1):
    print(f"--- ТЕСТ {i} ---")
    result = check_brackets(expr)
    status = "✓ ЗБАЛАНСОВАНО" if result else "✗ НЕ ЗБАЛАНСОВАНО"
    print(f"Результат: {status}\n")

# Спрощена версія функції
print("=== СПРОЩЕНА ВЕРСІЯ ===")

def simple_bracket_check(text):
    """Спрощена версія перевірки дужок"""
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or pairs.get(stack.pop()) != char:
                return False
    
    return len(stack) == 0

# Швидке тестування
quick_tests = ["(())", "([)]", "((()))", "()[]{}"]

print("Швидке тестування:")
for test in quick_tests:
    result = simple_bracket_check(test)
    print(f"'{test}' → {'збалансовано' if result else 'не збалансовано'}")

# Інтерактивна перевірка
print("\n=== ІНТЕРАКТИВНА ПЕРЕВІРКА ===")
print("Введіть вираз для перевірки дужок (або 'exit' для виходу):")

while True:
    user_input = input("Вираз: ").strip()
    
    if user_input.lower() == 'exit':
        print("До побачення!")
        break
    
    if user_input:
        is_balanced = simple_bracket_check(user_input)
        if is_balanced:
            print("✓ Дужки збалансовані!")
        else:
            print("✗ Дужки НЕ збалансовані!")
    else:
        print("Введіть непорожній вираз")
    
    print()

# Статистика по типах дужок
print("\n=== СТАТИСТИКА ДУЖОК ===")

def analyze_brackets(text):
    """Аналізує кількість різних типів дужок"""
    counts = {"(": 0, ")": 0, "[": 0, "]": 0, "{": 0, "}": 0}
    
    for char in text:
        if char in counts:
            counts[char] += 1
    
    print(f"Аналіз виразу: '{text}'")
    print(f"Круглі дужки: ( = {counts['(']}, ) = {counts[')']}")
    print(f"Квадратні дужки: [ = {counts['[']}, ] = {counts[']']}")
    print(f"Фігурні дужки: {{ = {counts['{']}, }} = {counts['}']}")
    
    # Перевірка балансу для кожного типу
    balanced_round = counts["("] == counts[")"]
    balanced_square = counts["["] == counts["]"]
    balanced_curly = counts["{"] == counts["}"]
    
    print(f"Баланс: круглі {'✓' if balanced_round else '✗'}, "
          f"квадратні {'✓' if balanced_square else '✗'}, "
          f"фігурні {'✓' if balanced_curly else '✗'}")

# Тестуємо аналіз
analyze_expressions = [
    "((()))",
    "([{}])",
    "(((",
    "([)]"
]

for expr in analyze_expressions:
    analyze_brackets(expr)
    print()