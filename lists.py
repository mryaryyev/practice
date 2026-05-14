''' List
    (1) Working with lists
    (2) List methods
    (3) Lambda function
    (4) enumarate, map and filter
'''

print("===== Working with Lists =====")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Ryan", "age": 33} # Dictionary
people = ("Andrew", "John", "Michael") # Tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"] # List

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

letters.append("c") # add behind
print(f"the append result: {letters}")

letters.insert(0, "z") # add front
print(f"the insert result: {letters}")

size = len(letters) -1 
result1 = letters.pop(size) # pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0) # pop front
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
new_numbs = sorted(numbs) # RETURN FUNCTION
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")