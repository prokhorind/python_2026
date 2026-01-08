# Приклад 2: Функція для підрахунку

def count_positive_negative():
    """Підраховує кількість додатних та від'ємних чисел"""
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    print("Введи 8 чисел (можуть бути додатні, від'ємні або нулі):")
    
    for i in range(8):
        num = int(input(f"Число {i+1}: "))
        
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    return positive_count, negative_count, zero_count

# Виклик функції
positive, negative, zeros = count_positive_negative()

print(f"\n=== РЕЗУЛЬТАТИ ===")
print(f"Додатних чисел: {positive}")
print(f"Від'ємних чисел: {negative}")
print(f"Нулів: {zeros}")
print(f"Всього чисел: {positive + negative + zeros}")

# Статистика у відсотках
total = positive + negative + zeros
if total > 0:
    print(f"\nСтатистика:")
    print(f"Додатних: {round(positive/total*100, 1)}%")
    print(f"Від'ємних: {round(negative/total*100, 1)}%")
    print(f"Нулів: {round(zeros/total*100, 1)}%")