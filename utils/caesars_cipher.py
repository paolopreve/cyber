import base64
"""
Julius,Q2Flc2FyCg==
-------------------
Caesar

World of Cryptography is like that Unsolved Rubik's Cube, given to a child that has no idea about it. A new combination at every turn.

Can you solve this one, with weird name?

ciphertext: fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ==
"""

def base64_to_ascii(base64_string):
    # Step 1: Decode the Base64 string to bytes
    byte_data = base64.b64decode(base64_string)

    # Step 2: Convert bytes to ASCII string (if the bytes are valid ASCII)
    ascii_string = byte_data.decode('ascii', errors='ignore')  # Ignore non-ASCII characters

    return ascii_string

def shift_ascii(s, shift):
    shifted_string = ""
    for char in s:
        # Get the ASCII value of the character
        ascii_value = ord(char)
        # Shift the value
        shifted_value = ascii_value - shift
        # Convert back to character
        shifted_char = chr(shifted_value)
        shifted_string += shifted_char
    return shifted_string

# Example usage
ciphertext = "fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=="
ascii_string = base64_to_ascii(ciphertext)
print(ascii_string)
for i in range(25):
    result = shift_ascii(ascii_string, i)
    print("Shifted: " + result)
