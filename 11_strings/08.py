##08 - Capitalize Words
# def capitalize_words(string):
#     words = my_string.split(' ')
#     capitalized_words = [word.capitalize() for word in words]
#     return ' '.join(capitalized_words)

def capitalize_words(string):
    return string.title()

my_string = 'launch school tech & talk'
print(capitalize_words(my_string))
