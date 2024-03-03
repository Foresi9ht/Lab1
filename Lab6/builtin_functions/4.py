import time
import math

def square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

number = 25100
milliseconds = 2123
print(f"Square root of {number} after {milliseconds} milliseconds is {square_root(number, milliseconds)}")
