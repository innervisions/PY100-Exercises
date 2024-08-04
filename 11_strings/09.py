## 09 - Check Prefix
# def starts_with(string, prefix):
#     return prefix == string[0:len(prefix)]

def starts_with(string, prefix):
    return string.startswith(prefix)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
