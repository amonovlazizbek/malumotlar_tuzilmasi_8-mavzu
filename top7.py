keys = [10, 17, 24, 31]
table_size = 7

hash_table = [None] * table_size

for key in keys:
    index = key % table_size

    
    while hash_table[index] is not None:
        index = (index + 1) % table_size

    hash_table[index] = key

for i, value in enumerate(hash_table):
    print(f"Index {i}: {value}")
