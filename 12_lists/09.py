## 09 - Destinations
def contains(item, lst):
    for element in lst:
        if item == element:
            return True
    
    return False

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False
