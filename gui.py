import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import threading
from main import crack_passwords  # Import the password cracking logic

# Global variables to hold file paths
wordlist_path = ""
passwords_path = ""

def select_wordlist(output_area):
    """Open file dialog to select a wordlist file."""
    global wordlist_path
    file_path = filedialog.askopenfilename(title="Select Wordlist File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        wordlist_path = file_path  # Store the selected path
        output_area.insert(tk.END, f"Selected wordlist: {file_path}\n")

def select_passwords(output_area):
    """Open file dialog to select a passwords file."""
    global passwords_path
    file_path = filedialog.askopenfilename(title="Select Passwords File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        passwords_path = file_path  # Store the selected path
        output_area.insert(tk.END, f"Selected passwords: {file_path}\n")

def start_cracking(output_area):
    """Start the password cracking process in a separate thread."""
    if not wordlist_path or not passwords_path:
        messagebox.showwarning("Warning", "Please select both a wordlist and a passwords file.")
        return

    output_area.delete(1.0, tk.END)  # Clear previous output
    output_area.insert(tk.END, "Starting the password cracking process...\n")  # Indicate process start

    # Create and start a new thread for cracking passwords
    threading.Thread(target=crack_passwords, args=(wordlist_path, passwords_path, output_area), daemon=True).start()

# GUI Setup
def create_gui():
    root = tk.Tk()
    root.title("Password Cracker")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    # Create buttons for selecting wordlist and password files
    wordlist_button = tk.Button(frame, text="Select Wordlist", command=lambda: select_wordlist(output_area))
    wordlist_button.grid(row=0, column=0, padx=10)

    passwords_button = tk.Button(frame, text="Select Passwords", command=lambda: select_passwords(output_area))
    passwords_button.grid(row=0, column=1, padx=10)

    start_button = tk.Button(frame, text="Start Cracking", command=lambda: start_cracking(output_area))
    start_button.grid(row=0, column=2, padx=10)

    global output_area  # Declare output_area as global for access in other functions
    output_area = scrolledtext.ScrolledText(root, width=80, height=20)
    output_area.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
