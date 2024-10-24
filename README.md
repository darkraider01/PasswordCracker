
# Password Cracker

## Introduction

This project is a Python-based password cracking tool designed to demonstrate techniques for cracking hashed passwords using bcrypt. The tool employs both a wordlist attack and brute-force methods to recover passwords.

## Features

- Supports bcrypt hashed password cracking.
- Uses a wordlist for faster password recovery.
- Implements brute-force techniques for unknown passwords.
- GUI option available for ease of use (separate module).

## Requirements

- Python 3.x
- bcrypt library
- tkinter (for GUI, optional)
- Other standard libraries (itertools, string, logging, etc.)

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/darkraider01/PasswordCracker.git
   cd PasswordCracker
   ```

2. **Install required packages**:
   You may need to install the bcrypt library if it's not already installed. You can do this using pip:
   ```bash
   pip install bcrypt
   ```

3. **Create a wordlist**:
   Prepare a text file named `wordlist.txt` in the project directory. This file should contain a list of potential passwords, one per line.

4. **Generate Passwords**:
   The script will generate a file named `passwords.txt` that contains bcrypt hashed passwords. The default includes a mix of complex, easy, and wordlist passwords. You can customize the passwords in the script.

## Usage

1. **Run the script**:
   For the command-line version, run the `main.py` script:
   ```bash
   python main.py
   ```

   For the GUI version, run the `gui.py` script:
   ```bash
   python gui.py
   ```

2. **Cracking passwords**:
   - For the command-line version, specify the path to the wordlist and passwords files as needed.
   - For the GUI version, use the file dialogs to select the wordlist and passwords files, then start the cracking process.

## How It Works

- **Wordlist Attack**: The tool checks each password from the wordlist against the hashed passwords.
- **Brute-force Attack**: If the password is not found in the wordlist, it attempts to brute-force passwords up to a specified length, using a combination of upper and lowercase letters, digits, and special characters.

## Security Notice

This project is intended for educational purposes only. Do not use this tool on any system or account without explicit permission.
```

