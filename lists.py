''' List
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enumerate, map and filter
'''

print("===== Working with Lists =====")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Ryan", "age": 33}  # Dictionary
people = ("Andrew", "John", "Michael")  # Tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # List

for team in groups:
    print(f"the team: {team}")


# constructor => CLASSlar orqali hosil qilish
result = list("Hello World!")
print(f"the letters: {result} and size: {len(result)}")


print("-----")

fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("===== List methods =====")
# methods >
# - mutable => append() insert() pop() remove() clear() sort()
# - immutable => index() method & sorted function

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append result: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop results2: {result2} and letters: {letters}")

print("-----")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)


exist1 = animals.index("cat")
print(f"the exist: {exist1}")


try:
    exist2 = animals.index("fish")
    print(exist2)
except Exception as err:
    print(f"the is no element in list and error: {err}")


animals.clear()
print("animal clear:", animals)


if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")


print("-----")

numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable sorted
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)  # RETURN FUNCTION
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


print("===== Lambda function =====")
# lambda is small ANONYMOUS function


def calculate(x, y): return x * y


result = calculate(3, 5)
print("result", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Josepp", 25),
    ("Michael", 30),
    ("Ali", 40)
]
people.sort()  # isimlere gore sort yapiyor
print("people(1):", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people(2)", people)


print("===== enumerate, map and filter =====")
# enumerate for index & value

animals = ["dog", "cat", "fish"] # list
for element in enumerate(animals):
    print("element:", element)

for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")

# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2025) # dict
result = car_obj.get("brand")
print(result)

result = car_obj.items()
print("result:", result)
for (key,value) in result:
    print(f"the key: {key} and value: {value}")


print("-----")
# map

cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_cars(1):", new_cars)

result_map = map(lambda car: car[0], cars)
print("result1", result_map) # => cikarmaydi, list'ga olish kerak
print(f"the result_map: {result_map} and type: {type(result_map)}")
new_cars = list(result_map)
print("new_cars(2):", new_cars)


print("-----")
# filter

result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))


