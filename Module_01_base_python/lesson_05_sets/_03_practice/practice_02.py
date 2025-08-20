text_1 = input("Введите первый текст: ")
text_2 = input("Введите второй текст: ")

text_1_set = set(text_1.split())
text_2_set = set(text_2.split())


all_words = text_1_set.union(text_2_set)
common_words = text_1_set.intersection(text_2_set)
unique_to_text1 = text_1_set.difference(text_2_set)
unique_to_text2 = text_2_set.difference(text_1_set)
both_text_unique = text_1_set.symmetric_difference(text_2_set)
print(all_words)
print(common_words)
print(unique_to_text1)
print(unique_to_text2)
print(both_text_unique)

