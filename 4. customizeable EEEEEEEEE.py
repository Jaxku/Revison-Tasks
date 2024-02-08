# EEEEEEE but custom mod swag right?
input_letter_counter = '0'

input_letter = input("Enter a letter: ")

# checking the stuff you feel me
sentence = input("write a sentence: ")
for char in sentence:
    if char == input_letter or char == input_letter.upper():
        input_letter_counter += '1'

# print
print(f"The number of {input_letter} in the sentence is:", input_letter_counter)
