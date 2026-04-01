class person:
    def __init__(self, age, height):
        self.age = age
        self.height = height
    def print_age(self):
        print(self.age)
    def print_height(self):
        print(self.height)

p2 = person(age=23, height=45)
p2.print_age()
p2.print_height()
