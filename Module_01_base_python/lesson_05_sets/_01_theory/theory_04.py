set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}


# Подмножество (subset):
print(set_a.issubset(set_b))
print(set_a <= set_b)
print(set_b.issubset(set_a))
print()

# Надмножество (superset):
print(set_b.issuperset(set_a))
print(set_b >= set_a)
print(set_a.issuperset(set_b))
print()

# Равенство множеств:
set_c = {1, 2, 3}
print(set_a == set_c)
print(set_c == set_b)
print(set_a.issubset(set_c))
print(set_a.issuperset(set_c))
