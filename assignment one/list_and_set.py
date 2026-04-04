


# Write a Python file for list & Set
print("\n=== SET EXAMPLES ===")
fruits = ["apple", "banana", "cherry"]
print("fruits", fruits)
print("first element: ", fruits[0])

fruits.append("orange")
print("after appending", fruits)

fruits.insert(1, "grape")
print("after inserting", fruits)

fruits.remove("orange")
print("after removing", fruits)

popped_item = fruits.pop()
print("Popped item:", popped_item)
print("after popping", fruits)
fruits[0] = "mango"
print("after changing", fruits)
#looping through list
print("loop through fruits")
for fruit in fruits:
    print(fruit)


print("\n=== SET EXAMPLES ===")
numbers = {1, 2,2,3, 3, 4, 5}
print("numbers", numbers)

#adding elements
numbers.add(10)
print("after add", numbers)

#removing elements
numbers.remove(2)
print("after remove", numbers)

numbers.discard(3)
print("after discarding", numbers)

set_a = {"a", "b", "c"}
print("set_a", set_a)
set_b = {"c", "e", "f"}
print("set_b", set_b)

#union
print("union", set_a | set_b)
#intersection
print("intersection", set_a & set_b)

#difference
print("difference", set_a - set_b)

print("length of set_a", len(set_a))

