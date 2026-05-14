''' LOOP operators
    (1) for 
    (2) break/else 
    (3) while  
'''

print("===== for operator =====")
# iterable objects > string dict tuple list range map filter
text = "MIT"
nums = [10, 7, 3, 4] # list
car_obj = dict(brand = "ferrari", year = 2025)
range_obj = range(5) # [0, 5)

for letter in text:
    print(f"the letter {letter}")

print("-----")

for number in nums:
    print(f"the number: {number}")

print("-----")

for x in range_obj:
    print(f"the element: {x}")

print("-----")

for key in car_obj:
    print(f"the key: {key} => {car_obj.get(key)}")


print("===== break/else =====")

for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10: #x>100 bolsa else=> ishlayar
        print("Reached break")
        break
else:
    print("Looped successfully")


print("===== while =====") # takrorlanish miqtori na aniq bolganida WHILE'dan foydalanamiz
numb = 40
while numb > 0:
    numb -= 10
    print(f"the num equals {numb}")


print("-----")

count = 0
while True:
    count += 1
    x = int(input("find number "))

    if x == 41:
        print(f"you found number in {count} steps")
        break
    else:
        print("wrong, please find again")


