# Random Password Generator

This is a simple Python program that generates random passwords of a desired length. The program utilizes a set of allowed characters, including uppercase and lowercase letters, digits, and a selection of special characters commonly permitted for use in passwords.

## Usage

1. Clone the repository or download the source code file `passwordGenerator.py`.
2. Navigate to the directory containing the source code.
3. Run the program using a Python interpreter.
4. You will be prompted to enter the desired length for the password.
5. If the entered length is valid (greater than 0), the program will generate a random password and display it.

## Features

- Generates passwords containing a mix of uppercase and lowercase letters, digits, and special characters.
- Allows users to specify the desired length of the password.
- Handles cases where an invalid length is entered (less than or equal to 0).

## Requirements

- Python 3.x

## How it Works

The program utilizes the `random` module to randomly select characters from a predefined set of allowed characters. The allowed character set consists of:

- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Digits (0-9)
- Special characters (!@#$%^&*)

The program then generates a password by concatenating randomly chosen characters from this set until the desired length is reached.

## Notes

- This program aims to provide a basic password generation mechanism and does not incorporate more advanced security features such as ensuring a certain level of randomness or avoiding easily guessable patterns.
- It's recommended to use a strong and secure password manager for generating and storing passwords for important accounts.

## Author

[@heythakur](https://www.github.com/heythakur)