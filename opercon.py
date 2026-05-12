''' OPERATORS & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''

print(" ===== Operators =====")
# + - > >= < <= == is * /     // % += **

a = 19
b = 5

print("a * b", a * b)
print("a > b", a > b)
print("a / b", a / b)

result = a // b # 
left = a % b # koldiq
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("b*b:", b**2)
print("b*b*b:", b**3)

print("="*5)

c = dict(name="Ryan", age=33)
d = dict(name="Ryan", age=33)
e = c

print("c==d", c==d) # True ==> only value compare
print(id(c), id(d))


print("c is d", c is d) # False ==> different reference
print("c is e", c is e) # True ==> same reference and value