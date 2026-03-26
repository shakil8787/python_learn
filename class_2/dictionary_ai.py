# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "Physics"]
}
print(student)
print("=======================================")
# Accessing values
print(student["name"])       # Output: Alice
print(student.get("age"))    # Output: 22

# Adding a new key-value pair
student["grade"] = "A"

# Updating a value
student["age"] = 23

# Removing a key-value pair
del student["courses"]
print("------------------------------------------------")
# Iterating through dictionary
for key, value in student.items():
    print(key, ":", value)