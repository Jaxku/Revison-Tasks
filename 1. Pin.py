"""
Simple pin program man so secure so much encryption, most def not stored in
plaintext. 100% secure, no need to worry about your pin being stolen.
"""

pin = ''

while not pin:
    pin = input('Enter your pin: ')
    if pin == "0456":
        print("Correct")
        break
    else:
        print("Incorrect")
        pin = ''
