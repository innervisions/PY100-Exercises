## 04 - What's my value? (Part 4)
a = 1

def my_function():
    print(a)

my_function()

# Will print the value of a, which is 1.
# The global variable a is accessible in the inner scope of my_function
# Because there is no assignment of a inside the function, shadowing is not implied.
