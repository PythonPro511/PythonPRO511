from datetime import datetime

date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 9, 17)


delta = date2 - date1
print(delta)
print(delta.days)
print(type(delta))
