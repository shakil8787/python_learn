#simple if
temperature = -25
if temperature >= 20:
    print("its a warm day")
print("Simple if statement executed.")

#nested if
age = 20
if age >= 18:
    print("you are an adult")
    if age >= 65:
        print("you are a senior citizen")
    else:
        print("you are eligible to work")

print("nested if statement executed.")

#if else
marks = 90
if marks > 90 and marks <= 100:
    print("grade: A")
elif marks >= 80 and marks < 90:
    print("grade: B")
elif marks >= 70 and marks < 80:
    print("grade: C")
else:
    print("grade: F")
print("if elif else statement executed.")

#switch case using dictionary mapping

