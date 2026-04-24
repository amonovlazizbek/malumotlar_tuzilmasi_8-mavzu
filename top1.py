
numbers = [23, 45, 12, 67, 34, 89]

hash_table = [None] * 10

for key in numbers:
    index = key % 10
    hash_table[index] = key

for i, value in enumerate(hash_table):
    print(f"Index {i}: {value}")
