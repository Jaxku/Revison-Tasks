"""
numbers and some random stuff to do with the numbers you feel me
"""

# define the list of numbers
numbers = [20, 36, 12, 24, 48, 74, 353, 23, 98]

# initialize a variable to store the sum of the numbers
max_value = numbers[0]

for number in numbers:
    if number > max_value:
        max_value = number

print("The largest element in the list is:", max_value)
