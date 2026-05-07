''' FUNCTIONS
    (1) DEFINE vs CALL
    (2) Parametr vs Argument
    (3) Keyword & default arguments
    (4) Scope
'''

print("==== DEFINE (parametr) vs CALL (argument) ====")
# build in function > print() type()
# Function => reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - build / parametr
def greet(a): # VOID Function
    print(f"How do you do, {a}") 


def greeting(b): # RETURN Function
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute / argument
greet("Ryan")


# Return function -> return qiladi
# Void function -> None(pythonda) -> undefined(java)
result1 = greet("Ryan")
print("result1: ", result1)

result2 = greeting("Justin")
print("result2: ", result2)
