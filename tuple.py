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


# try avoid this
people = "Andrew", "John"
animals = "dog",

print("===== Unpacking argument =====")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, z, a) = groups
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)  # list =>> ["DEVEX", "MG"]


# *args > tuple
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
print("-----")
calculate(0, 2, 300)
print("-----")
calculate(5, 7)

print("-----")
# **kwargs > DICTIONARY'ga yoyip beradi


def introduce(**kwargs): # keyword argument
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old")
    pass

# CALL
introduce(name="Ryan", age=33)
introduce(name="Shawn", age=32, single = True)


print("-----")

def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)

# CALL
greeting("hi", True, 10, name="John", age=22)

