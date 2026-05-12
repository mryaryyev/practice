'''CLASS deep dive
    (1) ENCAPSULATION
    (2) INHERITENCE
    (3) POLIMORPHISM
'''

print("==== INHERITENCE ====")
# PARENT > CHILD # malum bir propertylarni (state & method) pass qiladi/meras beradi
# Parent only provides PUBLIC & PROTECTED properties (state + method) to children


class Animal:  # Parent
    # state
    description = "This class is PARENT for animals"

    # constructor
    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)  # SUPER degani PArentni CONSTRUCTOR degani

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)  # SUPER degani PARENTni CONSTRUCTOR degani

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)  # SUPER degani PARENTni CONSTRUCTOR degani

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myaw", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-----")
dog.make_voice()
cat.make_voice()
fish.make_voice()

print("-----")
print(Animal.description)
print(Dog.description)
print(dog.description)

print(dog.voice, cat.voice, fish.voice)
print("animal status:", dog._status)
