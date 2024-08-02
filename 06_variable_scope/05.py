## 05 - What's my value? (Part 5)
a = 1

def my_function():
    print(a)
    a = 2

my_function()

# Raises an error.
# Because a is initialized in my_function, it is treated as a
# local variable that shadows the global variable a.
# This local variable is accessed before it is assigned.
