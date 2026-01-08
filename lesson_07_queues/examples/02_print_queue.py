# Приклад 2: Черга друку документів

print("=== ЧЕРГА ДРУКУ ДОКУМЕНТІВ ===")

from collections import deque
import time

class PrintQueue:
    def __init__(self, printer_name="HP LaserJet"):
        """Ініціалізує чергу друку"""
        self.queue = deque()
        self.printer_name = printer_name
        self.total_printed = 0
        self.is_printing = False
    
    def add_document(self, document_name, pages=1, priority="normal"):
        """Додає документ до черги друку"""
        document = {
            "name": document_name,
            "pages": pages,
            "priority": priority,
            "time_added": time.strftime("%H:%M:%S")
        }
        
        self.queue.append(document)
        position = len(self.queue)
        
        print(f"📄 Документ додано до черги:")
        print(f"   Назва: {document_name}")
        print(f"   Сторінок: {pages}")
        print(f"   Час: {document['time_added']}")
        print(f"   Позиція в черзі: {position}")
        
        return position
    
    def print_next_document(self):
        """Друкує наступний документ з черги"""
        if not self.queue:
            print("❌ Черга друку порожня")
            return False
        
        if self.is_printing:
            print("⏳ Принтер зайнятий, зачекайте...")
            return False
        
        # Забираємо документ з черги
        document = self.queue.popleft()
        self.is_printing = True
        
        print(f"\n🖨️  Починаємо друк:")
        print(f"   Документ: {document['name']}")
        print(f"   Сторінок: {document['pages']}")
        print(f"   Додано: {document['time_added']}")
        
        # Імітація процесу друку
        print("   Статус: Підготовка...")
        time.sleep(0.5)
        
        for page in range(1, document['pages'] + 1):
            print(f"   Друкуємо сторінку {page}/{document['pages']}...")
            time.sleep(0.3)  # Імітація часу друку сторінки
        
        print(f"✅ Документ '{document['name']}' надруковано успішно!")
        
        self.total_printed += 1
        self.is_printing = False
        
        # Показуємо наступний документ в черзі
        if self.queue:
            next_doc = self.queue[0]
            print(f"📋 Наступний в черзі: {next_doc['name']} ({next_doc['pages']} стор.)")
        else:
            print("📭 Черга друку порожня")
        
        return True
    
    def show_queue(self):
        """Показує поточну чергу друку"""
        print(f"\n📊 Черга принтера {self.printer_name}:")
        
        if not self.queue:
            print("   Черга порожня")
        else:
            print(f"   Документів в черзі: {len(self.queue)}")
            
            total_pages = 0
            for i, doc in enumerate(self.queue, 1):
                total_pages += doc['pages']
                print(f"   {i}. {doc['name']} ({doc['pages']} стор.) - {doc['time_added']}")
            
            print(f"   Всього сторінок: {total_pages}")
            
            # Приблизний час очікування (1 сторінка = 10 секунд)
            estimated_time = total_pages * 10
            minutes = estimated_time // 60
            seconds = estimated_time % 60
            
            if minutes > 0:
                print(f"   Приблизний час друку: {minutes} хв {seconds} сек")
            else:
                print(f"   Приблизний час друку: {seconds} сек")
    
    def cancel_document(self, position):
        """Скасовує документ за позицією в черзі"""
        if position < 1 or position > len(self.queue):
            print(f"❌ Неправильна позиція: {position}")
            return False
        
        # Перетворюємо позицію в індекс
        index = position - 1
        cancelled_doc = list(self.queue)[index]
        
        # Видаляємо документ (створюємо нову чергу без цього документа)
        new_queue = deque()
        for i, doc in enumerate(self.queue):
            if i != index:
                new_queue.append(doc)
        
        self.queue = new_queue
        
        print(f"🗑️  Документ '{cancelled_doc['name']}' скасовано")
        return True
    
    def get_statistics(self):
        """Показує статистику принтера"""
        print(f"\n📈 Статистика принтера {self.printer_name}:")
        print(f"   Надруковано документів: {self.total_printed}")
        print(f"   В черзі зараз: {len(self.queue)}")
        print(f"   Статус: {'Друкує' if self.is_printing else 'Готовий'}")

# Демонстрація роботи черги друку
print("Створюємо чергу друку для шкільного принтера")
school_printer = PrintQueue("Шкільний принтер HP")

# Додаємо документи від різних учнів
print("\n=== ДОДАВАННЯ ДОКУМЕНТІВ ===")
school_printer.add_document("Реферат з історії - Анна", pages=5)
school_printer.add_document("Домашнє завдання - Борис", pages=2)
school_printer.add_document("Презентація - Віра", pages=10)
school_printer.add_document("Контрольна робота - Григорій", pages=3)

# Показуємо чергу
school_printer.show_queue()

# Друкуємо кілька документів
print("\n=== ПРОЦЕС ДРУКУ ===")
school_printer.print_next_document()

print("\n" + "="*50)
school_printer.print_next_document()

# Додаємо терміновий документ
print("\n=== ДОДАВАННЯ ТЕРМІНОВОГО ДОКУМЕНТА ===")
school_printer.add_document("ТЕРМІНОВО: Довідка - Дарина", pages=1)

# Показуємо оновлену чергу
school_printer.show_queue()

# Скасовуємо один документ
print("\n=== СКАСУВАННЯ ДОКУМЕНТА ===")
school_printer.cancel_document(2)  # Скасовуємо другий документ
school_printer.show_queue()

# Друкуємо решту документів
print("\n=== ЗАВЕРШЕННЯ ДРУКУ ===")
while school_printer.queue:
    school_printer.print_next_document()
    print()

# Показуємо фінальну статистику
school_printer.get_statistics()

# Демонстрація пріоритетної черги друку
print("\n" + "="*60)
print("=== ПРІОРИТЕТНА ЧЕРГА ДРУКУ ===")

class PriorityPrintQueue:
    def __init__(self):
        self.high_priority = deque()    # Високий пріоритет
        self.normal_priority = deque()  # Звичайний пріоритет
    
    def add_document(self, name, pages=1, priority="normal"):
        """Додає документ з пріоритетом"""
        document = {"name": name, "pages": pages, "priority": priority}
        
        if priority == "high":
            self.high_priority.append(document)
            print(f"🔥 ВИСОКИЙ ПРІОРИТЕТ: {name} ({pages} стор.)")
        else:
            self.normal_priority.append(document)
            print(f"📄 Звичайний: {name} ({pages} стор.)")
    
    def print_next(self):
        """Друкує наступний документ (спочатку високий пріоритет)"""
        if self.high_priority:
            doc = self.high_priority.popleft()
            print(f"🖨️  Друкуємо ПРІОРИТЕТНИЙ: {doc['name']}")
        elif self.normal_priority:
            doc = self.normal_priority.popleft()
            print(f"🖨️  Друкуємо звичайний: {doc['name']}")
        else:
            print("❌ Черга порожня")
    
    def show_queue(self):
        """Показує чергу з пріоритетами"""
        print("\n📋 Черга з пріоритетами:")
        
        if self.high_priority:
            print("   🔥 Високий пріоритет:")
            for i, doc in enumerate(self.high_priority, 1):
                print(f"      {i}. {doc['name']} ({doc['pages']} стор.)")
        
        if self.normal_priority:
            print("   📄 Звичайний пріоритет:")
            for i, doc in enumerate(self.normal_priority, 1):
                print(f"      {i}. {doc['name']} ({doc['pages']} стор.)")
        
        if not self.high_priority and not self.normal_priority:
            print("   Черга порожня")

# Тестуємо пріоритетну чергу
priority_printer = PriorityPrintQueue()

priority_printer.add_document("Звичайний реферат", 5, "normal")
priority_printer.add_document("ТЕРМІНОВО: Атестат", 1, "high")
priority_printer.add_document("Домашка", 2, "normal")
priority_printer.add_document("КРИТИЧНО: Документи", 3, "high")

priority_printer.show_queue()

print("\nДрукуємо документи за пріоритетом:")
while priority_printer.high_priority or priority_printer.normal_priority:
    priority_printer.print_next()

print("\n=== ВИСНОВКИ ===")
print("Черги друку демонструють:")
print("• FIFO принцип - перший додав, перший надрукував")
print("• Управління ресурсами - один принтер, багато користувачів")
print("• Пріоритетність - важливі документи друкуються першими")
print("• Планування завдань - оптимізація використання принтера")