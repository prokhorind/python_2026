# Приклад 4: Пошук закономірностей у числах

def find_patterns(numbers):
    """Знаходить різні закономірності у списку чисел"""
    
    # Парні та непарні
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    # Числа, що діляться на 3
    divisible_by_3 = []
    for num in numbers:
        if num % 3 == 0:
            divisible_by_3.append(num)
    
    # Двозначні числа
    two_digit = []
    for num in numbers:
        if 10 <= num <= 99:
            two_digit.append(num)
    
    return {
        'парні': even_numbers,
        'непарні': odd_numbers,
        'діляться_на_3': divisible_by_3,
        'двозначні': two_digit
    }

# Тестові дані
test_numbers = [1, 12, 5, 18, 7, 24, 9, 15, 3, 100, 8, 6]

print(f"Вихідні числа: {test_numbers}")
print()

patterns = find_patterns(test_numbers)

for pattern_name, pattern_numbers in patterns.items():
    print(f"{pattern_name.replace('_', ' ').capitalize()}: {pattern_numbers}")
    print(f"  Кількість: {len(pattern_numbers)}")
    print()

# Статистика
total = len(test_numbers)
print(f"Загальна кількість чисел: {total}")
print(f"Парних: {len(patterns['парні'])}/{total}")
print(f"Непарних: {len(patterns['непарні'])}/{total}")