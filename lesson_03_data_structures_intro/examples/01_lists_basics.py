# Приклад 1: Основи роботи зі списками

# Створення списку улюблених фільмів
movies = ["Гаррі Поттер", "Месники", "Зоряні війни", "Титанік"]

print("Мої улюблені фільми:")
for i, movie in enumerate(movies, 1):
    print(f"{i}. {movie}")

# Додавання нового фільму
new_movie = "Людина-павук"
movies.append(new_movie)
print(f"\nДодав новий фільм: {new_movie}")

# Вставка фільму на певну позицію
movies.insert(2, "Форсаж")
print("Вставив 'Форсаж' на 3-тю позицію")

# Видалення фільму
removed_movie = movies.pop(0)  # Видаляє перший елемент
print(f"Видалив фільм: {removed_movie}")

# Поточний список
print(f"\nОновлений список ({len(movies)} фільмів):")
for i, movie in enumerate(movies, 1):
    print(f"{i}. {movie}")

# Пошук фільму
search_movie = "Месники"
if search_movie in movies:
    position = movies.index(search_movie) + 1
    print(f"\n'{search_movie}' знаходиться на {position} позиції")
else:
    print(f"\n'{search_movie}' не знайдено у списку")

# Сортування списку
movies_sorted = sorted(movies)
print(f"\nСписок за алфавітом: {movies_sorted}")

# Оригінальний список не змінився
print(f"Оригінальний список: {movies}")