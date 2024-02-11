import datetime
x = input("Date: ")
ndate = datetime.datetime.strptime(x, "%d.%m.%Y")
fx = ndate - datetime.timedelta(days=5)
print("Todays date:", ndate.strftime("%d.%m.%Y"))
print("Five days ago:", fx.strftime("%d.%m.%Y"))
