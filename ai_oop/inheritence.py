# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} খাচ্ছে...")

# Child Class (Inheriting from Animal)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} ঘেউ ঘেউ করছে!")

# অবজেক্ট তৈরি করা
my_dog = Dog("Buddy")

# Child Class এর অবজেক্ট Parent Class এর মেথড ব্যবহার করছে
my_dog.eat()   # Output: Buddy খাচ্ছে...
my_dog.bark()  # Output: Buddy ঘেউ ঘেউ করছে!