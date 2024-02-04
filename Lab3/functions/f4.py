def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def filter_prime(nums):
    return [num for num in nums if is_prime(num)]