import os, sys, math  # Unused imports

def add_numbers(x, y):
    result = x + y
    return result  # Inefficient return statement

def find_max(numbers):
    max_num = -float("inf")
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num  # Can use built-in max()

print(add_numbers(10, 20)) 
print(find_max([1, 2, 3, 4, 5]))

def unused_function():
    pass  # This function does nothing
