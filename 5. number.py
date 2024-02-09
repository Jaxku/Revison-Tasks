"""
numbers and some random stuff to do with the numbers you feel me
"""

# define the list of numbers
numbers = [20, 36, 12, 24, 48, 74, 353, 23, 98]

# initialize a variable to store the sum of the numbers
index_to_replace = None

# loop through the list of numbers
for i in range(len(numbers)):
    if numbers[i] == 353:
        index_to_replace = i
        break


print("Index to replace :", index_to_replace)

if index_to_replace is not None:
    numbers[index_to_replace] = 53

print("\nUpdated list of numbers: ", numbers)

if index_to_replace is not None:
    print("\nThe number 353 was found at index", index_to_replace, "and replaced with 53")
else:
    print("\nThe number 353 was not found in the list")

print("\nfirst number in the list is", numbers)
