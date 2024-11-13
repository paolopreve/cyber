def replace_chars(input_string, replacements):
    """
    Replace characters in input_string based on the replacements dictionary.

    Parameters:
    - input_string (str): The original string to modify.
    - replacements (dict): A dictionary with characters as keys and their replacements as values.

    Returns:
    - str: The modified string with characters replaced.
    """
    # Create a list to store the modified characters for efficiency
    modified_chars = []
    
    # Iterate over each character in the input string
    for char in input_string:
        # Replace the character if it's in the dictionary, otherwise keep it as is
        modified_chars.append(replacements.get(char, char))
    
    # Join the list into a single string and return
    return ''.join(modified_chars)

# Example usage
replacements = {
    "A": "l",
    "B": "s",
    "C": "r",
    "D": "o",
    "E": "E",
    "F": "a",
    "G": "d",
    "H": "b",
    "I": "g",
    "J": "p",
    "K": "i",
    "L": "h",
    "M": "n",
    "N": "t",
    "O": "O",
    "P": "y",
    "Q": "m",
    "R": "R",
    "S": "v",
    "T": "u",
    "U": "e",
    "V": "w",
    "W": "f",
    "X": "c",
    "Y": "Y",
    "Z": "Z"
}

string = "MKXU IDKMI DM BDASKMI NLU XCPJNDICFQ! K VDMGUC KW PDT GKG NLKB HP LFMG DC TBUG PDTC CUBDTCXUB. K'Q BTCU MDV PDT VFMN F WAFI BD LUCU KN KB WAFI GDKMINLKBHPLFMGKBQDCUWTMNLFMFMDMAKMUNDDA"

output_string = replace_chars(string, replacements)
print("Result:", output_string)
