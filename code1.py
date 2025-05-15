# Unoptimized code example
import os

def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                duplicates.append(nums[i])
    return duplicates


def compute_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sum_large_numbers(nums):
    total = 0
    for num in nums:
        total += num
    return total


def get_first_n_fibonacci(n):
    fibonacci = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci


def find_max_value(nums):
    max_val = -float("inf")
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val


# Calling the functions
nums = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8]
n = 10
print(find_duplicates(nums))
print(compute_factorial(n))
print(sum_large_numbers(nums))
print(get_first_n_fibonacci(n))
print(find_max_value(nums))
