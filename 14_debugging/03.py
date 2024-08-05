## 10 - Multiply By Five
def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")

# The value being retuned by the invocation of input on line 6
# is a string. When multiply_by_five is called, the operation on line 3
# is actually string multiplication.

# We can fix this bug by typecasting the input on line 6 as an int.
