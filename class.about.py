''' CLASS
    (1) What is class 
    (2) ordinary vs static properties
    (3) special methods
'''

print("==== What is class ====")
# class - blueprint for object creation! => object yasash uchun hizmat qiladigan shablon
# class structrure => state | constructor | method


class Person():
    # state
    message = "Class: static state property"

    # constructor
    def __init__(self, name, age):  # self => objectga karatilgan
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")
    
    @classmethod # decorator yordamga keladi
    def explain(cls):
        print("Class: static method property executed!")


person1 = Person("Ryan", 33)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ordinary state
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print("==== ordinary vs static properties ====")
# static property => object bilan emas togridan togri class bilan keladi

# static state
new_message = Person.message
print(new_message)

# static method
Person.explain()