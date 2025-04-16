#!/usr/bin/env python3
"""
Email Hasher Script

This script takes an email address as a command line argument,
hashes it using the SHA-256 algorithm, and writes the hash to stdout and to a file.

Usage:
    python email_hasher.py <email_address>

Example:
    python email_hasher.py example@email.com
"""

import sys
import hashlib
import re

def hash_email(email):
    """
    Hash an email address using SHA-256 and return the hexadecimal digest.
    
    Args:
        email (str): The email address to hash
        
    Returns:
        str: The SHA-256 hash of the email in hexadecimal format
    """
    # 1. Convert the email string to bytes
    byte_email = email.encode()
    # 2. Create a SHA-256 hash of the email
    hash_256 = hashlib.sha256(byte_email)
    # 3. Return the hash in hexadecimal format
    return hash_256.hexdigest()

def write_hash_to_file(hash_value, filename="hash.email"):
    """
    Write a hash value to a file.
    
    Args:
        hash_value (str): The hash value to write
        filename (str): The name of the file to write to (default: "hash.email")
    """
    # 1. Open the file in write mode
    with open(filename, "w") as file:
        # 2. Write the hash value to the file
        file.write(hash_value)

def main():
    """
    Main function to process command line arguments and execute the script.
    """
    # 1. Check if an email address was provided as a command line argument
    if len(sys.argv) <= 1:
        print("Error: No email entered.")
        sys.exit(1)

    # 2. Validate that the input is a proper email format
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    email_argument = sys.argv[1]

    if not re.match(pattern, email_argument):
        print("Error: What was entered wasn't detected as an email.")
        sys.exit(1)
        
    # 3. Hash the email address
    hashed = hash_email(email_argument)
    
    # 4. Print the hash to stdout
    print(hashed)
    
    # 5. Write the hash to a file named "hash.email"
    write_hash_to_file(hashed)

if __name__ == "__main__":
    main()
