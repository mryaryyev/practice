print("===== number =====")
# in JAVA, variable is a name storage location => malumot manzilining nomlanishi
# in Python, variable is named reference! => referensning nomlanishi

count = 100
count_type = type(count)
print("count:", count, count_type)
print(f"the count: {count}, and type: {count_type}") # format string

result1 = count.bit_count() # method [cube]()// OBJECTLAR => uzining hir hator propertylarga (method hamda  statelar) ega bolgan mahsus data type.
result2 = count.numerator # state [wrench-achor]
print(result1, result2)

print("==== string ====")
 # METHODS: uppper() lower() title() find() replace()

course = "AI Python Fullstack"
result = type(course)
print(f"the result (1): {result}")

result = course.title()
print(f"the result (2): {result}")

result = course.upper()
print(f"the result (3): {result}")

result = course.replace("Fullstack", "MasterClass")
print(f"the result (4): {result}")

print(course) # AI Python Fullstack => ozgarmaydi