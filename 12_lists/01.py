## 01 - First Element
# def first(list):
#     if len(list) == 0:
#         return None
#     return list[0]

def first(lst):
    if lst:
        return lst[0]
    else:
       return None

print(first(['Earth', 'Moon', 'Mars']))  # Earth
