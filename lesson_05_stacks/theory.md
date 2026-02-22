# Урок 5: Стеки

## Мета уроку
Вивчити концепцію стека як структури даних LIFO (Last In, First Out) та її практичне застосування.

## Теоретичний матеріал

### 1. Що таке стек?

Стек - це структура даних, яка працює за принципом **LIFO** (Last In, First Out) - "останній зайшов, перший вийшов".

```python
# Уявіть стопку тарілок:
# - Нову тарілку кладемо зверху (push)
# - Беремо тарілку також зверху (pop)
# - Не можемо взяти тарілку з середини стопки

stack_example = []
print("Порожній стек:", stack_example)

# Додаємо елементи (push)
stack_example.append("тарілка 1")
stack_example.append("тарілка 2") 
stack_example.append("тарілка 3")
print("Стек після додавання:", stack_example)

# Забираємо елементи (pop)
top_plate = stack_example.pop()
print(f"Взяли: {top_plate}")
print("Стек після взяття:", stack_example)
```

### 2. Основні операції стека

```python
class Stack:
    def __init__(self):
        """Створюємо порожній стек"""
        self.items = []
    
    def push(self, item):
        """Додаємо елемент на вершину стека"""
        self.items.append(item)
        print(f"Додано: {item}")
    
    def pop(self):
        """Забираємо елемент з вершини стека"""
        if self.is_empty():
            return None
        item = self.items.pop()
        print(f"Забрано: {item}")
        return item
    
    def peek(self):
        """Дивимось на верхній елемент, не забираючи його"""
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        """Перевіряємо, чи стек порожній"""
        return len(self.items) == 0
    
    def size(self):
        """Повертаємо розмір стека"""
        return len(self.items)
    
    def display(self):
        """Показуємо вміст стека"""
        if self.is_empty():
            print("Стек порожній")
        else:
            print("Стек (зверху вниз):", self.items[::-1])

# Приклад використання
my_stack = Stack()
my_stack.push("A")
my_stack.push("B") 
my_stack.push("C")
my_stack.display()

print(f"Верхній елемент: {my_stack.peek()}")
my_stack.pop()
my_stack.display()
```

### 3. Стек з використанням списку Python

```python
# Простий стек на основі списку
def create_stack():
    """Створює порожній стек"""
    return []

def push(stack, item):
    """Додає елемент до стека"""
    stack.append(item)
    print(f"Додано до стека: {item}")

def pop(stack):
    """Забирає елемент зі стека"""
    if is_empty(stack):
        print("Стек порожній!")
        return None
    item = stack.pop()
    print(f"Забрано зі стека: {item}")
    return item

def peek(stack):
    """Дивиться на верхній елемент"""
    if is_empty(stack):
        return None
    return stack[-1]

def is_empty(stack):
    """Перевіряє, чи стек порожній"""
    return len(stack) == 0

def display_stack(stack):
    """Показує стек"""
    if is_empty(stack):
        print("Стек: []")
    else:
        print(f"Стек: {stack} (← верх)")

# Демонстрація
book_stack = create_stack()
push(book_stack, "Математика")
push(book_stack, "Фізика")
push(book_stack, "Хімія")
display_stack(book_stack)

print(f"Верхня книга: {peek(book_stack)}")
pop(book_stack)
display_stack(book_stack)
```

### 4. Практичні застосування стеків


#### 4.1 Обернення рядка

```python
def reverse_string(text):
    """Обертає рядок за допомогою стека"""
    stack = []
    
    # Додаємо всі символи до стека
    for char in text:
        stack.append(char)
    
    # Забираємо символи зі стека (у зворотному порядку)
    reversed_text = ""
    while stack:
        reversed_text += stack.pop()
    
    return reversed_text

# Тестування
original = "Python"
reversed_str = reverse_string(original)
print(f"Оригінал: {original}")
print(f"Обернений: {reversed_str}")

# Обернення слів у реченні
def reverse_words(sentence):
    """Обертає кожне слово у реченні"""
    words = sentence.split()
    reversed_words = []
    
    for word in words:
        reversed_word = reverse_string(word)
        reversed_words.append(reversed_word)
    
    return " ".join(reversed_words)

sentence = "Привіт світ"
print(f"Оригінальне речення: {sentence}")
print(f"Обернені слова: {reverse_words(sentence)}")
```

#### 4.2 Калькулятор з постфіксним записом

```python
def evaluate_postfix(expression):
    """Обчислює вираз у постфіксному записі"""
    stack = []
    operators = {'+', '-', '*', '/'}
    
    tokens = expression.split()
    
    for token in tokens:
        if token not in operators:
            # Це число
            stack.append(float(token))
        else:
            # Це оператор
            if len(stack) < 2:
                return "Помилка: недостатньо операндів"
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    return "Помилка: ділення на нуль"
                result = a / b
            
            stack.append(result)
    
    if len(stack) == 1:
        return stack[0]
    else:
        return "Помилка: неправильний вираз"

# Тестування
# "3 4 + 2 *" означає (3 + 4) * 2 = 14
expressions = [
    "3 4 +",        # 3 + 4 = 7
    "3 4 + 2 *",    # (3 + 4) * 2 = 14
    "15 7 1 1 + - / 3 * 2 1 1 + + -"  # складніший вираз
]

for expr in expressions:
    result = evaluate_postfix(expr)
    print(f"'{expr}' = {result}")
```

### 5. Стек викликів функцій

```python
def function_a():
    """Демонстрація стека викликів"""
    print("Входимо в function_a")
    function_b()
    print("Виходимо з function_a")

def function_b():
    print("Входимо в function_b")
    function_c()
    print("Виходимо з function_b")

def function_c():
    print("Входимо в function_c")
    print("Виконуємо роботу в function_c")
    print("Виходимо з function_c")

# Виклик демонструє стек:
# function_a -> function_b -> function_c
# Потім повертаємось у зворотному порядку
print("=== ДЕМОНСТРАЦІЯ СТЕКА ВИКЛИКІВ ===")
function_a()

# Рекурсивна функція також використовує стек
def factorial(n):
    """Обчислює факторіал рекурсивно"""
    print(f"Викликаємо factorial({n})")
    
    if n <= 1:
        print(f"Базовий випадок: factorial({n}) = 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"Повертаємо: factorial({n}) = {result}")
        return result

print("\n=== РЕКУРСИВНИЙ ФАКТОРІАЛ ===")
result = factorial(4)
print(f"Результат: 4! = {result}")
```

## Ключові поняття
- **LIFO** - Last In, First Out (останній зайшов, перший вийшов)
- **Push** - додавання елемента на вершину стека
- **Pop** - забирання елемента з вершини стека
- **Peek/Top** - перегляд верхнього елемента без його забирання
- **Стек викликів** - механізм відстеження викликів функцій
- **Постфіксний запис** - математичний запис без дужок

## Практичні поради
1. Стеки ідеальні для обернення порядку елементів
2. Використовуйте стеки для перевірки збалансованості
3. Стек викликів допомагає зрозуміти рекурсію
4. У Python список може працювати як стек (append/pop)
5. Завжди перевіряйте, чи стек не порожній перед pop()
6. Стеки корисні в алгоритмах обходу графів та дерев