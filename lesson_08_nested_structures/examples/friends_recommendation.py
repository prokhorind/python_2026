"""
ЗАДАЧА: Рекомендація друзів у соціальній мережі.

У нас є граф друзів.

Ключ словника — це користувач.
Список — це його друзі.

Завдання:
знайти "друзів друзів", яких користувач ще не має у списку друзів.

Це простий приклад того, як графи використовуються
у соціальних мережах (Facebook, LinkedIn).
"""

graph = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "Eve"],
    "David": ["Bob"],
    "Eve": ["Charlie"]
}


def recommend_friends(user):
    """
    Повертає список рекомендованих друзів.

    Алгоритм:
    1. беремо друзів користувача
    2. дивимось їхніх друзів
    3. якщо цей друг не є самим користувачем
       і його ще немає у списку друзів — рекомендуємо
    """

    friends = graph[user]
    recommendations = set()

    for friend in friends:

        # беремо друзів друга
        for friend_of_friend in graph[friend]:

            if friend_of_friend != user and friend_of_friend not in friends:
                recommendations.add(friend_of_friend)

    return recommendations


print("Friend recommendations for Alice:")
print(recommend_friends("Alice"))