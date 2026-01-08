# Приклад 4: Стек викликів функцій та рекурсія

print("=== СТЕК ВИКЛИКІВ ФУНКЦІЙ ===")

# Глобальна змінна для відстеження глибини викликів
call_depth = 0

def show_call_stack(func_name, action="enter"):
    """Показує поточний стан стека викликів"""
    global call_depth
    
    if action == "enter":
        print("  " * call_depth + f"→ Входимо в {func_name}()")
        call_depth += 1
    else:  # exit
        call_depth -= 1
        print("  " * call_depth + f"← Виходимо з {func_name}()")

def function_a():
    """Перша функція в ланцюжку викликів"""
    show_call_stack("function_a", "enter")
    print("  " * call_depth + "Виконуємо роботу в function_a")
    
    function_b()  # Викликаємо наступну функцію
    
    print("  " * call_depth + "Повернулись в function_a")
    show_call_stack("function_a", "exit")

def function_b():
    """Друга функція в ланцюжку викликів"""
    show_call_stack("function_b", "enter")
    print("  " * call_depth + "Виконуємо роботу в function_b")
    
    function_c()  # Викликаємо наступну функцію
    
    print("  " * call_depth + "Повернулись в function_b")
    show_call_stack("function_b", "exit")

def function_c():
    """Третя функція в ланцюжку викликів"""
    show_call_stack("function_c", "enter")
    print("  " * call_depth + "Виконуємо роботу в function_c")
    print("  " * call_depth + "Це найглибша функція - тут зупиняємось")
    show_call_stack("function_c", "exit")

print("Демонстрація стека викликів:")
print("main() → function_a() → function_b() → function_c()")
print()

# Скидаємо глибину
call_depth = 0
function_a()

print("\n" + "="*50)
print("=== РЕКУРСИВНІ ФУНКЦІЇ ===")

def factorial_with_trace(n, depth=0):
    """Обчислює факторіал з трасуванням стека"""
    indent = "  " * depth
    print(f"{indent}→ factorial({n})")
    
    if n <= 1:
        print(f"{indent}  Базовий випадок: {n}! = 1")
        print(f"{indent}← Повертаємо 1")
        return 1
    else:
        print(f"{indent}  Рекурсивний випадок: {n}! = {n} * {n-1}!")
        result = n * factorial_with_trace(n - 1, depth + 1)
        print(f"{indent}← Повертаємо {n} * {result//n} = {result}")
        return result

print("Обчислення факторіалу 4! з трасуванням стека:")
result = factorial_with_trace(4)
print(f"\nРезультат: 4! = {result}")

print("\n" + "="*50)
print("=== ЧИСЛА ФІБОНАЧЧІ З ТРАСУВАННЯМ ===")

# Лічильник викликів для демонстрації
fib_calls = 0

def fibonacci_with_trace(n, depth=0):
    """Обчислює числа Фібоначчі з трасуванням"""
    global fib_calls
    fib_calls += 1
    
    indent = "  " * depth
    print(f"{indent}→ fib({n}) [виклик #{fib_calls}]")
    
    if n <= 1:
        print(f"{indent}  Базовий випадок: fib({n}) = {n}")
        print(f"{indent}← Повертаємо {n}")
        return n
    else:
        print(f"{indent}  Рекурсивний випадок: fib({n}) = fib({n-1}) + fib({n-2})")
        
        left = fibonacci_with_trace(n - 1, depth + 1)
        right = fibonacci_with_trace(n - 2, depth + 1)
        
        result = left + right
        print(f"{indent}← Повертаємо {left} + {right} = {result}")
        return result

print("Обчислення fib(5) з трасуванням стека:")
fib_calls = 0
result = fibonacci_with_trace(5)
print(f"\nРезультат: fib(5) = {result}")
print(f"Загальна кількість викликів: {fib_calls}")

print("\n" + "="*50)
print("=== СИМУЛЯЦІЯ СТЕКА ВИКЛИКІВ ===")

class CallStack:
    """Клас для симуляції стека викликів"""
    
    def __init__(self):
        self.stack = []
    
    def push(self, function_name, parameters=None):
        """Додає виклик функції до стека"""
        call_info = {
            'function': function_name,
            'parameters': parameters or {},
            'local_vars': {}
        }
        self.stack.append(call_info)
        self.show_stack(f"Викликаємо {function_name}")
    
    def pop(self, return_value=None):
        """Забирає виклик функції зі стека"""
        if self.stack:
            call_info = self.stack.pop()
            func_name = call_info['function']
            self.show_stack(f"Повертаємось з {func_name} (результат: {return_value})")
            return call_info
        return None
    
    def set_local_var(self, var_name, value):
        """Встановлює локальну змінну в поточній функції"""
        if self.stack:
            self.stack[-1]['local_vars'][var_name] = value
    
    def show_stack(self, action=""):
        """Показує поточний стан стека"""
        print(f"\n{action}")
        print("Стек викликів:")
        
        if not self.stack:
            print("  [порожній]")
        else:
            for i, call in enumerate(self.stack):
                indent = "  " * (i + 1)
                func_name = call['function']
                params = call['parameters']
                locals_vars = call['local_vars']
                
                print(f"{indent}{func_name}({params})")
                if locals_vars:
                    print(f"{indent}  локальні: {locals_vars}")

# Демонстрація симуляції
print("Симулюємо обчислення factorial(3):")

call_stack = CallStack()

# Симулюємо factorial(3)
call_stack.push("factorial", {"n": 3})
call_stack.set_local_var("n", 3)

# factorial(3) викликає factorial(2)
call_stack.push("factorial", {"n": 2})
call_stack.set_local_var("n", 2)

# factorial(2) викликає factorial(1)
call_stack.push("factorial", {"n": 1})
call_stack.set_local_var("n", 1)

# factorial(1) повертає 1
call_stack.pop(1)

# factorial(2) повертає 2 * 1 = 2
call_stack.pop(2)

# factorial(3) повертає 3 * 2 = 6
call_stack.pop(6)

print("\n" + "="*50)
print("=== ПЕРЕПОВНЕННЯ СТЕКА ===")

def infinite_recursion(n):
    """Демонстрація переповнення стека (обережно!)"""
    print(f"Рекурсивний виклик #{n}")
    
    # Обмежуємо кількість викликів для безпеки
    if n > 10:
        print("Зупиняємо рекурсію для безпеки!")
        return
    
    return infinite_recursion(n + 1)

print("Демонстрація потенційного переповнення стека:")
print("(обмежено 10 викликами для безпеки)")

try:
    infinite_recursion(1)
except RecursionError as e:
    print(f"Помилка переповнення стека: {e}")

print("\n=== ВИСНОВКИ ===")
print("Стек викликів функцій:")
print("• Відстежує порядок викликів функцій")
print("• Зберігає локальні змінні кожної функції")
print("• Забезпечує правильне повернення з функцій")
print("• Може переповнитись при надто глибокій рекурсії")
print("• Працює за принципом LIFO")
print("• Критично важливий для роботи програм!")