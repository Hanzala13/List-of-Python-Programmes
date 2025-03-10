def check_word_in_sentence(sentence, word):
    # Convert both sentence and word to lowercase for case-insensitive matching
    return word.lower() in sentence.lower().split()

# Example usage
sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if check_word_in_sentence(sentence, word):
    print(f"The word '{word}' is present in the sentence.")
else:
    print(f"The word '{word}' is NOT present in the sentence.")
