#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description: This shift cipher encryption scheme encrypts English text, and decrypts as English text. The main method of the code sets up the main functioning body of what we're doing.
We set the variables to intialized values at first and then describe the code to the user of the script. We then prompt the user to enter any text they'd like while checking to ensure that it is valid english text.
Afterwards, we confirm with them the desired shift of the scheme they would like to implement and the shortly repeat it to the user. Future versions would expand it to allow multiple uses. The cleartext is then displayed with the ciphertext to display it's correct implementation.
Special characters are also denied.
"""

# Import statements
import os
import string
import sys

# Global variables
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = string.ascii_lowercase

def main(args):
    cleartext = ""
    shift = None

    print(f"This script encrypts your plaintext using the Caesar/Shift cipher and also allows you to decrypt it as well. The supported characters are: {letters}.")
    
    cleartext = input("\nEnter your cleartext here: ").lower()
    if cleartext.isalpha() == True:
        print(f"Confirming input: {cleartext}")
    else:
        print("Invalid input. Ending.")
        sys.exit()

    shift = input("\nEnter your desired shift here: ")
    if shift.isdigit() == True:
        shift = int(shift)
        print(f"Confirming shift: {shift}")
    else:
        print("You didn't pick a shift. Ending.")
        sys.exit()
    
    print(f"\nRunning encryption scheme based on this text '{cleartext}' and a '{shift}' shift.")

    e_message = encrypt(cleartext, shift)
    print(f"\nYour encrypted data: {e_message}")

    d_message = decrypt(e_message, shift)
    print(f"Your decrypted data: {d_message}")

def encrypt (cleartext, shift):
    ciphertext = ""

    for char in cleartext:
        if char.isalpha():
            index = letters.index(char)
            shifted = (index + shift) % 26
            ciphertext += letters[shifted]
        else:
            ciphertext += char

    return ciphertext

def decrypt (ciphertext, shift):
    return encrypt(ciphertext, -shift)

if __name__ == '__main__':
    main(sys.argv[1:])