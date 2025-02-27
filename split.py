def count_words(sentence):
    words = sentence.split()
    return len(words)

# Taking user input
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"Number of words in the sentence: {word_count}")