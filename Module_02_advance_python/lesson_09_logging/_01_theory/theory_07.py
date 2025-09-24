from datetime import datetime, timedelta

delta = timedelta(days=5)
print(delta)

today = datetime.today()
print(today)
future_day = today + timedelta(days=10, hours=2)
print(future_day)