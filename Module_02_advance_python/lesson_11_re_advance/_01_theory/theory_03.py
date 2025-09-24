import re

my_str_1 = "Мои номера телефонов: А1 +375(029)6234567; МТС +375(033)3334455"
my_reg_1 = re.compile(r'А1 \+\d{1,3}\((\d{1,3})\)(\d{7}); МТС \+\d{1,3}\((\d{1,3})\)(\d{7})')
match_obj = my_reg_1.match(my_str_1)
print(match_obj)


my_reg_2 = re.compile(r'Мои номера телефонов: А1 \+\d{1,3}\((\d{1,3})\)(\d{7});')
match_obj = my_reg_2.match(my_str_1)
print(match_obj)
print(match_obj.group())
print(match_obj.group(1))
print(match_obj.group(2))
