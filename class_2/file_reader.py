import os

# Get current working directory
current_directory = os.getcwd()

print("Current Directory:", current_directory)

filename = "C:\\Users\\User\\PycharmProjects\\python_learn\\number.txt"

with open(filename, "w") as file:
    file.write("\nhello world")

with open(filename, "a") as file2:
    file.write("\nhello world3")

file = open(filename, "r")
content = file.read()
print(content)
file.close()