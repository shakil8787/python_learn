#def function name()

def print_marks():
    for marks in range(1, 11):
        print(marks)

print_marks()

print("----------------------------")
def calculate(a, b):
    sum = a + b
    sub = a - b
    multi = a * b
    div = a / b
    return sum, sub, multi, div
print(calculate(10, 2))
print("================================")
def calculate_sub():
    a = 20
    b = 30
    return a - b
print(calculate_sub())