# base_string = "  Hello, world! Hello, Guido!  "
# print(base_string)
# formatted_string = base_string.strip()
# print(formatted_string)
# new_string = formatted_string.replace('world', "Python")
# print(new_string)
# upper_string = new_string.upper()
# print(upper_string)
# lower_string = upper_string.lower()
# print(lower_string)
# capitalised_string = lower_string.capitalize()  # только 1й символ строки будет в верхнем регистре (если регистр есть)
# print(capitalised_string)
# titled_string = capitalised_string.title()
# print(titled_string)
# swapped_string = titled_string.swapcase()
# print(swapped_string)
# print()

# разделение строки
text = "Python is fun"
words = text.split()
print(words)
text = "Python::is::fun"
words = text.split("::")
print(words)
csv_line = 'one,two,three'
items = csv_line.split(',')
print(items)

joined_string = ' '.join(words)
print(joined_string)
joined_items = ','.join(items)
print(joined_items)


