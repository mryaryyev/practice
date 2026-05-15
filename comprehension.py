''' Comprehension
    (1) What is comprehension & list comp.
    (2) set and dictionary comp.
'''

print("===== What is comprehension & list comprehension =====")
# Comprehension acts like spread operator!

''' Comprehension general syntax:
    a) *iterable 
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''


# list comp.
# COMPREHENSION -> listning qiymatlaridan foydalangan holda butunlay yangi referencega ega bolgan listimizni hosil qilishka komek etadi
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version
# list_numbers = numbers  # degan bolsak IS TRUE bolardi, hem qiymat, hem reference almokda
print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("-----")
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # b version
list_people_age = [person[1] for person in people]  # b version
print("list_people:", list_people)
print("list_people:", list_people_age)

print("-----")

cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]
list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)


print("===== set and dictionary comprehension =====")
numbs = [1, 5, 4, 20, 4, 5]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)

people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
dict_people = {person[0]: person[1] for person in people} # b version
print("dict_people:", dict_people)

dict_people2 = {person[0]: person[1] 
                for person in people if person[1] > 20} # c version
print("dict_people:", dict_people2)