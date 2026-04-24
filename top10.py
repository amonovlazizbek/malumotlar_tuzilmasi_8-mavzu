#1-usul

numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
count = len(set(numbers))
print("Unikal elementlar soni:", count)


#2-usul
numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique = {}

for num in numbers:
    unique[num] = True 

print("Unikal elementlar soni:", len(unique))
