# a = 147
# print("a:", a)

# message = "Hello World!"
# print(message)


print("Hello World!")
print("PYTHON: Everything is object!")
#hem qiymati hamda reference bor

message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("data type:", result)

# print,type => builtin functionlar

'''
dunder degan narosmi tushuncha bor
Dunder = __ = double underscore

Pythonni ihslayshi DUNDER VARIABLELAR yoki MAHSUS(magic) METOTLARGA asoslanadi.

__builtins__ => pythonni system variablelari hisoplanadi
__init__ => pythonni magic methodi
'''

''' In Python, there are builtin (ichki ornatilgan) tools:
(1) TYPES > int float str list dict
(2) FUNCTION > print(), len(), input(), type()
(3) CONSTANTS > True False None
'''

print(dir(__builtins__))


# python3 run.py   