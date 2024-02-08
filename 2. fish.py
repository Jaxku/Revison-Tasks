"""
fish
"""

fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]

# a. print the first letter of each fish on a new line
print("a. First letter of each fish name:")
for name in fish:
    # Access the first letter of each fish name
    print(name[0])

# b. Print the first 3 letters of each fish on a new line
print("\nb. First 3 letters of each fish name:")
for name in fish:
    # Access the first 3 letters of each fish name
    print(name[:3])

# c. print the longest fish name
print("\nc. Longest fish name:", max(fish, key=len))

# d. print out any fish name which is more than one word
print("\nd. Fish name with more than one word:")
for name in fish:
    if " " in name:
        print(name)

# e. print out any fish name which contains the word cod
print("\ne. Fish name containing the word 'cod':")
for name in fish:
    if "cod" in name:
        print(name)
