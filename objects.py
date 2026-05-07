''' OBJECTS
    (1) What is object
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

import array  # package/module
import math
from math import ceil
print("==== What is object ====")
# An object has state and method properties.
# Everything is object in Python!

print(type("Hello World!"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))


# Programming Language Paradigms => Functional Programming & Object Oriented Programming OOP (esasy ikisi)
# OOP 4 CONCEPTS => Abstraction | Encapsulation | Inheritence | Polimorphism

result1 = math.ceil(97.7)  # CALL
print(result1)

result2 = ceil(98.7)
print(result2)

print("==== Error handling system ====")
car_dict = dict(brand="Toyota", year=2026, electric=True)

# result = car_dict["origin"]
# print(result) # hata beradi

# error handling
try:
    print("passed here")
    #a = car_dict.speed # AttributeError
    result = car_dict["origin"]
    print(result)
except Exception as err:
    print("General Error:", err)
# except (KeyError, AttributeError) as err:
#     print("Error:", err)
# except KeyError as err:
#     print("No origin state property found:", err)
# except AttributeError as err:
#     print("No speed found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")

print("=====")

try:
    print("passed here")
    result = car_dict["year"]
    print(result)
except KeyError as err:
    print("No origin state property found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")