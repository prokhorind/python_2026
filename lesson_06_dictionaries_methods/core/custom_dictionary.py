class MyDictionary:
    """
    Власна спрощена реалізація dictionary
    на основі хеш-таблиці з open addressing.
    """

    def __init__(self, size=10):
        """
        Конструктор.

        size — розмір внутрішнього масиву.
        table — список фіксованого розміру,
        в якому зберігатимуться пари (key, value).
        """
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """
        Приватний метод хешування.

        1. Викликає вбудовану функцію hash()
        2. Обмежує індекс розміром таблиці через %
        3. Повертає індекс комірки
        """
        return hash(key) % self.size

    def put(self, key, value):
        """
        Додавання або оновлення елемента.

        Алгоритм:
        1. Обчислюємо індекс через _hash()
        2. Якщо комірка порожня — вставляємо
        3. Якщо ключ співпадає — оновлюємо значення
        4. Якщо зайнята іншим ключем — рухаємось далі
           (лінійне пробування)
        """
        index = self._hash(key)

        while self.table[index] is not None:
            # Якщо ключ вже існує — оновлюємо
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

            # Колізія — переходимо до наступної комірки
            index = (index + 1) % self.size

        # Якщо знайшли порожню комірку
        self.table[index] = (key, value)

    def get(self, key):
        """
        Пошук значення за ключем.

        Алгоритм:
        1. Обчислюємо індекс
        2. Перевіряємо комірку
        3. Якщо ключ співпадає — повертаємо значення
        4. Якщо ні — рухаємось далі
        5. Якщо зустріли None — ключа немає
        """
        index = self._hash(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]

            index = (index + 1) % self.size

        return None

    def remove(self, key):
        """
        Видалення елемента.

        1. Знаходимо ключ
        2. Якщо знайшли — ставимо None
        (Увага: це спрощена версія.
        У реальних хеш-таблицях використовують
        спеціальні маркери видалених елементів.)
        """
        index = self._hash(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return

            index = (index + 1) % self.size

    def display(self):
        """
        Допоміжний метод для виведення таблиці.
        Показує внутрішню структуру.
        """
        for i, item in enumerate(self.table):
            print(i, "->", item)