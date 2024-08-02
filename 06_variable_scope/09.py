## 09 - What's my value? (Part 9)
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# Will print 7.
# When my_function is invoked, the local variable b is assigned
# the integer values assigned to a. This does not reassign the global
# variable a.

# Later b is reassigned to it's previous value + 7. The global variable a
# remains unaffected.
