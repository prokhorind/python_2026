# Приклад 3: Аналіз тексту

def analyze_text(text):
    """Аналізує текст та повертає статистику"""
    # Підрахунок символів
    total_chars = len(text)
    letters = 0
    digits = 0
    spaces = 0
    
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char == ' ':
            spaces += 1
    
    # Підрахунок слів
    words = len(text.split())
    
    return {
        'символів': total_chars,
        'літер': letters,
        'цифр': digits,
        'пробілів': spaces,
        'слів': words
    }

# Тестування
sample_text = "Привіт! Мені 16 років і я вивчаю Python програмування."

stats = analyze_text(sample_text)

print(f"Текст: '{sample_text}'")
print("\nСтатистика:")
for key, value in stats.items():
    print(f"  {key.capitalize()}: {value}")

# Додаткова інформація
print(f"\nСередня довжина слова: {round(stats['літер'] / stats['слів'], 1)} літер")