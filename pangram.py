import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

# Example usage
sentence = "The quick brown fox jumps over the 1 lazy dog"
if is_pangram(sentence):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
