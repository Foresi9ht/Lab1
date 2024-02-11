import math
num = int(input("sides: "))
length = float(input("length: "))
area = (num * length ** 2) / (4 * math.tan(math.pi / num))
print("area of polygon:", round(area))