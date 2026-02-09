# Arrays examples in Python

# 1. Dynamic array behavior
a = []
for i in range(5):
    a.append(i)
print("Dynamic array:", a)

# 2. Different types in one list
mixed = [1, "hello", 3.14]
print("Mixed types:", mixed)

# 3. References inside list
x = [1, 2, 3]
y = x
y.append(4)
print("x after y.append:", x)

# 4. Copy vs reference
original = [10, 20, 30]
copy_list = original.copy()
copy_list.append(40)
print("Original:", original)
print("Copy:", copy_list)

# 5. Index access O(1)
nums = [10, 20, 30, 40, 50]
print("Element at index 3:", nums[3])

# 6. Insert operation cost
nums.insert(0, 999)
print("After insert at beginning:", nums)

# 7. Size and id (memory reference)
print("ID of list:", id(nums))
print("Length:", len(nums))

# 8. Simulating static array idea
static_like = [0] * 5
print("Static-like array:", static_like)

a = [10, 20, 30, 40]
del a[1]
print("Dynamic array:", a)
