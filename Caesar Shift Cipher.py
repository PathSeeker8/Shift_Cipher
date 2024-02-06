#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import statements
import os
import string
import sys

# Global variables
letters = string.ascii_lowercase

def main(args):
    cleartext = ""
    shift = None

    print(f"This script encrypts your plaintext using the Caesar/Shift cipher and also allows you to decrypt it as well. The supported characters are: {letters}.")
    
    cleartext = input("\nEnter your cleartext here: ").lower()
    if all(char.isalpha() or char.isspace() for char in cleartext):
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
        elif char.isspace():
            ciphertext += char
        else:
            ciphertext += char

    return ciphertext

def decrypt (ciphertext, shift):
    return encrypt(ciphertext, -shift)

if __name__ == '__main__':
    main(sys.argv[1:])