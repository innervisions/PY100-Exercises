## 06 - Check the Weather, Part 2
weather = 'sunny'

match weather:
    case 'sunny':
        print("Let's go outside!")
    case 'rainy':
        print('Grab your umbrella!')
    case _:
        print("Let's stay inside.")
