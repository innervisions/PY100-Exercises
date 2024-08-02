## 02 - What's my value? (Part 2)
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# Will raise an error. x defined in my_function is a local
# variable that shadows the x defined globally. The assignment
# on line 5 is self referential but x had not been initialized prior
# to that point.
