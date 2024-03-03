from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers_str = input()
numbers = [int(x) for x in numbers_str.split()]

print("Product of all numbers:", multiply_list(numbers))
