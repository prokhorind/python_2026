# Demonstration of main Python list methods

numbers = [10, 20, 30, 40, 50]

print("Initial list:", numbers)

# 1. append() - add element to the end
numbers.append(60)
print("After append(60):", numbers)

# 2. insert() - insert element at specific index
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

# 3. remove() - remove first occurrence of value
numbers.remove(40)
print("After remove(40):", numbers)

# 4. pop() - remove element by index (or last if no index)
last_element = numbers.pop()
print("After pop():", numbers)
print("Popped element:", last_element)

# 5. sort() - sort the list
numbers.sort()
print("After sort():", numbers)

# 6. reverse() - reverse the list
numbers.reverse()
print("After reverse():", numbers)

# 7. count() - count occurrences of value
count_20 = numbers.count(20)
print("Count of 20:", count_20)

# 8. index() - find index of first occurrence
index_30 = numbers.index(30)
print("Index of 30:", index_30)

print("Final list:", numbers)
