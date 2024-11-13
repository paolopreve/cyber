"""
original data: "El Psy Congroo"

encrypted data: "IFhiPhZNYi0KWiUcCls="

encrypted flag: "I3gDKVh1Lh4EVyMDBFo="

The flag is a composition of two names (two animals (?)).
"""
import base64

def base64_to_ascii(base64_string):
    # Step 1: Decode the Base64 string to bytes
    byte_data = base64.b64decode(base64_string)

    # Step 2: Convert bytes to ASCII string (if the bytes are valid ASCII)
    ascii_string = byte_data.decode('ascii', errors='ignore')  # Ignore non-ASCII characters

    return ascii_string

def xor_strings(str1, str2):
    # Ensure the strings are the same length
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")

    # Perform XOR operation between the characters of each string
    result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2))
    return result

data = "El Psy Congroo"
encryption = "IFhiPhZNYi0KWiUcCls="
base = base64_to_ascii(encryption)
key = xor_strings(data,base)
encryptioned = "I3gDKVh1Lh4EVyMDBFo="
based = base64_to_ascii(encryptioned)
print("--------------------------")
print(xor_strings(key,based))

#FLAG=Alpacaman
