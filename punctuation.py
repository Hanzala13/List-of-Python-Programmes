import string

def remove_punctuation(input_str):
    # Using str.translate to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    return input_str.translate(translator)

# Example usage
if __name__ == "__main__":
    sample_text = "Hello, World! Let's write some Python code..."
    cleaned_text = remove_punctuation(sample_text)
    print("Original Text: ", sample_text)
    print("Text without Punctuation: ", cleaned_text)