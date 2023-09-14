# Contact Book

A simple Contact Book application that allows users to manage their contacts, including adding, viewing, searching, updating, and deleting contacts. The contacts are stored in an Excel file for easy persistence between runs.

## Features

- Add new contacts with their name, phone number, email, and address.
- View a list of all saved contacts, including names and phone numbers.
- Search for contacts by name or phone number.
- Update contact details (phone, email, address).
- Delete a contact from the list.
- Contacts are saved to an Excel file for easy access between program runs. (optional)

## Getting Started

### Prerequisites

- Python 3.x
- `openpyxl` library (install using `pip install openpyxl`)

### Usage

#### NOTE:
There are two modes to run this program:
-  **Online-mode**: In this mode, you have to add the contacts again every time you will run the program as it doesn't get saved in any file.

-  **Local-mode**: Here, you don't have to add the contacts again and again doesn't matter how many times you restart the program. It will automatically create and save the contact into a local excel file, "contacts.xlsx" everytime you add a contact. And it will the contacts everytime the program is being run.

The program will be the in Online-mode by default.

#### Online-mode Use
- Copy the code from the contactBook.py and paste it in any Online Compiler (Interpreter), e.g., Replit, Collab, Programiz.
- Make sure to Uncomment the lines with #LocalUseComment (line no: 5), must be commented by default.
- And, to Comment the lines with #OnlineUseComment (line no: 4,6,8,12)
- And you are good to go.

#### Local-mode Use
- Download the `contactBook.py` and run it in your local IDE (e.g., VSCode).
- Comment the lines with #LocalUseComment (line no: 5), must be commented by default.
- And, to Uncomment the lines with #OnlineUseComment (line no: 4,6,8,12), if commented.
- And the program is ready to be used in Local-mode Use.


## Author

[@heythakur](https://www.github.com/heythakur)