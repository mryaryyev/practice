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