import bcrypt
import random

# Define a set of more complex passwords with a mix of characters
new_plaintext_passwords = {
    "user1": "D3fault!@2023",
    "user2": "C0mpl3x#Password",
    "user3": "Str0ng*Passw0rd!",
    "user4": "Qwerty123#%",
    "user5": "P@ssword!IsStrong",
    "user6": "N3wP@ss*2024",
    "user7": "Secret!#4567",
    "user8": "MyNewPass#123",
    "user9": "Best!Passw0rd$",
    "user10": "Unique#Pass!2024"
}

# Define a list of easy passwords
easy_passwords = [
    "123456",
    "password",
    "qwerty",
    "letmein",
    "welcome",
    "abc123",
    "admin",
    "iloveyou",
    "sunshine",
    "12345678"
]

# Function to load passwords from a wordlist
def load_wordlist(file_path):
    """Load a wordlist into memory."""
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Wordlist file not found: {file_path}")
        return []

# Load passwords from a wordlist (if available)
wordlist_file = 'wordlist.txt'  # Path to your wordlist file
wordlist_passwords = load_wordlist(wordlist_file)

# Combine all passwords into one dictionary
combined_passwords = {
    **new_plaintext_passwords,
    **{f"user_easy{i+11}": pw for i, pw in enumerate(easy_passwords)},
    **{f"user_wordlist{i+21}": pw for i, pw in enumerate(wordlist_passwords)}
}

# Write bcrypt hashes to passwords.txt
with open('passwords.txt', 'w') as f:
    for user, password in combined_passwords.items():
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))
        f.write(f"{user}:{hashed.decode()}\n")

print("Generated passwords.txt with new bcrypt hashes, including easy passwords and those from the wordlist.")
