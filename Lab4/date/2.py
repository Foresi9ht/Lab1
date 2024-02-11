import datetime
today = input("date: ")
x = datetime.datetime.strptime(today, "%d.%m.%Y").date()
yesterday = x - datetime.timedelta(days=1)
tomorrow = x + datetime.timedelta(days=1)
print("yesterday:", yesterday.strftime("%d.%m.%Y"))
print("today:", x.strftime("%d.%m.%Y"))
print("tomorrow:", tomorrow.strftime("%d.%m.%Y"))
