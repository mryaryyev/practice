print("==== Iterable objects & RANGE ====")
# Iterable => takrorlash hususiyati
# Iterable object > string dict tuple list range map filter


range_obj = range(3)  # [0.3)
print(range_obj)

text = "MIT"
for letter in text:
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")


print("==== DICTIONARY ====")
# Dictionary is JSON object! dictionaryni json formatta hosil qilamiz
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

name = person_obj["name"]
print("name:", name)

#hobby = person_obj["hobby"]
#print(hobby) # ERROR beradi

# method: get()
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

del person_obj["single"]
for key in person_obj:
    print(f"the key: {key}")
    print(f"the key: {key} > value {person_obj.get(key)}")


