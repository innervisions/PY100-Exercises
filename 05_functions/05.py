## 05 - Display Division

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three

# Will not print anything because multiples_of_three is never invoked on line 10.
