class Student:
    # এটি হলো class variable
    school_name = "Dhaka High School"

    def __init__(self, name, roll):
        # এগুলো হলো instance variable
        self.name = name
        self.roll = roll

# দুটি অবজেক্ট তৈরি করা হলো
s1 = Student("Rahim", 1)
s2 = Student("Karim", 2)

# আউটপুট দেখা যাক
print("Student 1:", s1.name, s1.roll, s1.school_name)
print("Student 2:", s2.name, s2.roll, s2.school_name)

# এখন class variable পরিবর্তন করলে
Student.school_name = "Chittagong High School"

print("After change:")
print("Student 1:", s1.name, s1.roll, s1.school_name)
print("Student 2:", s2.name, s2.roll, s2.school_name)