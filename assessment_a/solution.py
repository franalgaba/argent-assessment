from collections import deque, Counter

# Linked list in Python
linked_list = deque(["a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c"])

# I wasn't sure if the desired solution was to remove all keys that are duplicated or just remove the duplicated keys so I implemented both.

# Solution 1: One liner
# Using set we can get an unordered, unindexed collection without duplicate members from any iterable.
# The complexity of set is O(1) / O(n) depending on the operation as it uses hash tables
result_1 = deque(list(set(linked_list)))
print(f"Solution 1: linked list without duplicated items is {result_1}")

linked_list = deque(["a", "b", "c", "d", "a", "a", "b", "b"])

# Solution 2: using list comprehensions
# O(n) complexity as will be needed to iterate through all the counted items in the linked list
result_2 = deque([item for item, amount in Counter(linked_list).items() if amount == 1])
print(f"Solution 2: linked list without duplicates is {result_2}")
