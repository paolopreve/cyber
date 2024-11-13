"""
Crack the cipher: vhixoieemksktorywzvhxzijqni

Your clue is:

"caesar is everything. But he took it to the next level."
"""
def generate_key(text, key):
    """Generate a repeating key that matches the length of the text."""
    key = list(key)
    if len(key) == len(text):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def vigenere_decrypt(ciphertext, keyword):
    """Decrypt the ciphertext using the Vigenère cipher with the given keyword."""
    key = generate_key(ciphertext, keyword)
    plaintext = []
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():  # Only decrypt alphabetic characters
            shift = ord(key[i].upper()) - ord('A')
            # Decrypt uppercase and lowercase separately to preserve case
            if ciphertext[i].isupper():
                decrypted_char = chr((ord(ciphertext[i]) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(ciphertext[i]) - ord('a') - shift + 26) % 26 + ord('a'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(ciphertext[i])  # Non-alphabet characters remain unchanged
    
    return "".join(plaintext)

string = "vhixoieemksktorywzvhxzijqni"
result = vigenere_decrypt(string, "caesar")
print(f"result: {result}")
