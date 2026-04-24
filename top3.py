keys = [15, 20, 25, 30]
table_size = 5


hash_table = [[] for _ in range(table_size)]

for key in keys:
    index = key % table_size
    hash_table[index].append(key)

for i, values in enumerate(hash_table):
    print(f"Index {i}: {values}")
