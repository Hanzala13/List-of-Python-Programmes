def longest_word_length(sentence):
    words = sentence.split()
    max_length = max(len(word) for word in words)
    return max_length

# Example usage
sentence = input("Enter a sentence: ")
print("Length of the longest word:", longest_word_length(sentence))
