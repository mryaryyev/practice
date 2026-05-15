''' Array & Set
    (1) Array
    (2) Set
    (3) Specific operators with set
'''

# ARRAY -> strict type (sonlar bilan string aralashtirish MUMKUN EMAS)
from array import array
print("===== Array =====")

# i f
# juda katta hajimdagi malumotlar bolsa ARRAY bn ishlaymiz
numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1):", numbers)


numbers.append(100)
numbers.insert(0, 14)
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)


print("===== Set =====")

# { } takrorlamaydigan kolleksiya
# Set of unique collection without keeping order!

new_numbers = array("i", [1, 4, 7, 5, 4, 5, 7, 8, 41])
numbs_set = set(new_numbers)

print(f"numbs_set: {numbs_set} and type: {type(numbs_set)}")

numbs_set.add(200)
print("numbs_set(1):", numbs_set)

numbs_set.add(7)
print("numbs_set(2):", numbs_set)


print("===== Specific operators =====")

# | & - ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b # union
print("result1:", result1)

result2 = a & b # intersection
print("result2:", result2)

result3 = a - b # difference
print("result3:", result3)

result4 = a ^ b # symmetric difference
print("result4:", result4)