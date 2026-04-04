# if statement
x = 20

if x > 10:
    print("x is greater than 10")


#if else statement
print("=========================")
y = 3

if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")
# another if else statement
print("=========================")
print("mark and grade example")
if x > 10:
    print("x is greater than 10")
marks = 75

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

#nested if
print("=========================")

z = 15
if z > 10:
    print("z is greater than 10")
    if z % 2 == 0:
        print("z is even")
    else:
        print("z is odd")

#for loop
print("=========================")
print("LOOP EXAMPLE")
for i in range(5):
    print("i is ", i)

#function definition
print("=========================")
def greet(name):
    print("Hello ", name)
    if name == "shakil":
        print("welcome back, shakil")

greet("shakil")
greet("john")

#short hand if
print("=========================")
s = 5
t = 10

if s < t: print("s is less than t")

#short hand if-else
print("=========================")
result = "even" if y % 2 == 0 else "odd"
print("y is: ", result)

# another example short hand if-else
print("=========================")
age = 20
status = "adult" if age >= 18 else "teen"
print("you are an ", status)

# Multiple conditions (Logical operators)
print("=========================")
num = 15
if num >  10 and num < 20:
    print("num is greater than 10 and less than 20")
if num < 10 or num == 15:
    print("num is less than 10 or equal to 15")
if not (num < 10):
    print("num is not less than 10")