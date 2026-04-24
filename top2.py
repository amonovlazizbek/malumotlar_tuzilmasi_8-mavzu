
names = ["Ali", "Vali", "Sami", "Hasan", "Husan", "Karim", "Salim"]

table_size = 10

hash_table = [[] for _ in range(table_size)]

for name in names:
    first_char = name[0]             
    index = ord(first_char) % table_size
    hash_table[index].append(name)

for i, values in enumerate(hash_table):
    print(f"Index {i}: {values}")
