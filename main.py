import bcrypt
import itertools
import string
import logging
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
from tkinter import messagebox

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_wordlist(wordlist_path):
    """Load the wordlist into memory for faster access."""
    try:
        with open(wordlist_path, 'r') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        logging.error(f"Wordlist file not found: {wordlist_path}")
        raise

def test_pass(hashed_password, wordlist):
    """Attempt to match a hashed password with words from the wordlist."""
    for word in wordlist:
        if bcrypt.checkpw(word.encode('utf-8'), hashed_password.encode('utf-8')):
            logging.info(f"[+] Found Password: {word}")
            return word
    return None

def brute_force_password(hashed_password, max_length=8):
    """Attempt to brute-force a password up to max_length using uppercase, lowercase, digits, and special characters."""
    chars = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            password = ''.join(attempt)
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                logging.info(f"[+] Found Password: {password}")
                return password
    logging.warning("[-] Password not found.")
    return None

def process_user(line, wordlist, output_area):
    """Process each user entry to attempt password cracking."""
    if ":" in line:
        user, hashed_password = line.split(":")
        output_area.insert(tk.END, f"[*] Cracking Password for {user.strip()}\n")
        
        # First, try the wordlist method
        found_password = test_pass(hashed_password.strip(), wordlist)
        if not found_password:
            # If not found, fall back to brute-force
            output_area.insert(tk.END, f"[*] Attempting brute-force for {user.strip()}\n")
            found_password = brute_force_password(hashed_password.strip(), max_length=12)  # Adjust max_length as needed

        if found_password:
            output_area.insert(tk.END, f"[+] Found Password for {user.strip()}: {found_password}\n")
        else:
            output_area.insert(tk.END, f"[-] Password Not Found for {user.strip()}\n")

def crack_passwords(wordlist_path, passwords_path, output_area):
    """The main function to crack passwords."""
    try:
        wordlist = load_wordlist(wordlist_path)
        
        with open(passwords_path, 'r') as passFile:
            users = passFile.readlines()

        with ThreadPoolExecutor() as executor:
            for line in users:
                executor.submit(process_user, line, wordlist, output_area)

    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {passwords_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# No need to run anything here as this will be executed from gui.py

