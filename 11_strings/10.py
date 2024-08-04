## 10 - Count Substrings
# def count_substrings(string, substring):
#     sub_length = len(substring)
#     count = 0
#     index = 0
#     while index <= len(string) - sub_length:
#         if string[index: index + sub_length] == substring:
#             count += 1
#         index += 1
#     return count

def count_substrings(string, substring):
    return string.count(substring)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0
