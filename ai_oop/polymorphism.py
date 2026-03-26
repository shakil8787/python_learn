class Animal:
    def speak(self):
        pass

class Dog(Animal):   # বড় হাতের অক্ষরে ক্লাস নাম
    def speak(self):
        return "ভউ ভউ!"

class Cat(Animal):
    def speak(self):
        return "মিউ মিউ!"

animals = [Cat(), Dog()]   # লিস্টের নাম বহুবচন করা ভালো

for animal in animals:
    print(animal.speak())