##07 - What's my value? (Part 7)

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# Will print 2.
# The statement on line 6 declares that a should refer to the global a.
