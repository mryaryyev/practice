''' Tuple
    (1) What is tuple: tuple vs list
    (2) Unpacking argument
    (3) zip
'''

print("===== What is tuple: tuple vs list =====")
# Java/PHP/NodeJS array => Python list

# LITERAL orqali kurush
numbs = [3, 5, 1, 2]
# car_dict = {"brand": "ferrari", "year": 1995}
print(numbs)

# CONSTRUCTOR orqali kurush
letters = list("Hello World!")
# person_dic = dict(name="Ryan", age="33")
print(letters)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)


# TUPLE => we can not mutate tuple = qiymatini ozgartirolmaymiz
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird" =>> hato beradi