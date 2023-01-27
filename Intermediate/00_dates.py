### Dates ###

from datetime import datetime

now = datetime.now()

print_date(now)

timestamp = now.timestamp()

print(timestamp)

year_2023 = datetime(2023,1,1)

def print_date(date):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)