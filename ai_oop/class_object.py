# Class তৈরি করা
class Car:
    # Constructor: যা দিয়ে বৈশিষ্ট্য সেট করা হয়
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # একটি Method (কাজ)
    def drive(self):
        print(f"{self.brand} গাড়িটি চলতে শুরু করেছে।")

# Object তৈরি করা
my_car = Car("Toyota", "Red")
friend_car = Car("BMW", "Blue")

# আউটপুট দেখা
print(my_car.brand)    # Output: Toyota
friend_car.drive()     # Output: BMW গাড়িটি চলতে শুরু করেছে।