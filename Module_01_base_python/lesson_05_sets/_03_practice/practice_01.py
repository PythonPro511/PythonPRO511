event1_guests = ["Alice", "Bob", "Charlie", "David"]
event2_guests = ["Charlie", "Eve", "Alice", "Frank"]

event1_set = set(event1_guests)
event2_set = set(event2_guests)

both_events = event1_set.intersection(event2_set)
# both_events = event1_set & event2_set
only_event1 = event1_set.difference(event2_set)
# only_event1 = event1_set - event2_set
only_event2 = event2_set.difference(event1_set)
# only_event2 = event2_set - event1_set

print(f"Посетили оба: {both_events}")
print(f"Посетили только первое: {only_event1}")
print(f"Посетили только второе: {only_event2}")

print(f"Посетили оба: {', '.join(both_events)}")
print(f"Посетили только первое: {', '.join(only_event1)}")
print(f"Посетили только второе: {', '.join(only_event2)}")

# # для работы с множеством списков, целесообразно сначала все их преобразовать в множество циклом,
# # а потом действовать исходя из задачи
# all_events_guests = [event1_guests, event2_guests]
# all_events_guests_list_sets = []
#
# for event_guests in all_events_guests:
#     all_events_guests_list_sets.append(set(event_guests))
# print(all_events_guests_list_sets)

