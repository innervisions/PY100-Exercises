## 06 - What's my value? (Part 6)
a = 1

def my_function():
    a = 2

my_function()
print(a)

# Will print 1.
# The a on line 8 is the global variable initialized on line 1.
# The a on line 5 is a local variable that is never printed.
