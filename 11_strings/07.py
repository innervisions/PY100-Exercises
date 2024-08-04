## 07 - Is Empty or Blank?
# def is_empty_or_blank(string):
#     for char in string:
#         if char != ' ':
#             return False
#     return True
        
# def is_empty_or_blank(s):
#     return s.strip(' ') == ''

def is_empty_or_blank(s):
    return not s.strip(' ')

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
