## 10 - What's my value? (Part 10)
b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# Will print [10, 2, 3]
# There is no local variable b initialized in my_function's definition.
# Thus b refers to the list in the outer scope. This list is mutated
# when it's first element is reassigned to the integer 10.
